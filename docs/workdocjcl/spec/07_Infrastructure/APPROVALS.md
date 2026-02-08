# Approvals（用户审批体系）复刻级规格

本章目标：完整复刻 Codex CLI 的“用户审批”系统，使复刻实现满足：
- **同样的审批触发条件**（按 `AskForApproval`、execpolicy、sandbox deny、工具类型）
- **同样的审批缓存语义**（ApprovedForSession）
- **同样的事件与协议**（`ExecApprovalRequestEvent`、`ApplyPatchApprovalRequestEvent`、`ReviewDecision`）
- **同样的重试策略**（sandbox deny → 可选无沙箱重试）
- **同样的 execpolicy amendment 应用路径**（ApprovedExecpolicyAmendment）

本章覆盖“通用审批骨架”，而 execpolicy 本身的规则语言/匹配/落盘细节见：
- `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md`

---

## 0. 关键类型（协议层）

### 0.1 ReviewDecision（用户最终决策）
协议枚举：`codex-rs/protocol/src/protocol.rs:ReviewDecision`

- `Approved`：批准本次执行
- `ApprovedExecpolicyAmendment { proposed_execpolicy_amendment }`：批准本次执行 + 申请将提案前缀写入 execpolicy（见 §6）
- `ApprovedForSession`：批准本次执行 + 在本 session 内缓存“同 key 的后续请求”无需再次询问
- `Denied`：拒绝，但会话继续（模型应换方案）
- `Abort`：拒绝并中断当前任务（等待用户下一条输入）

> 复刻注意：`ApprovedForSession` 的缓存粒度不是“任意同类命令”，而是由工具定义的 **ApprovalKey** 精确决定（见 §3.2）。

### 0.2 ExecApprovalRequestEvent（命令执行审批事件）
结构：`codex-rs/protocol/src/approvals.rs:ExecApprovalRequestEvent`

字段要点：
- `call_id`：对应工具调用（Responses API call id 或本地工具 call id）
- `turn_id`：所属 turn（sub_id）
- `command: Vec<String>`：待执行命令 token
- `cwd: PathBuf`：工作目录
- `reason: Option<String>`：人类可读原因（可能来自 execpolicy justification、tool justification、或 sandbox deny 重试提示）
- `proposed_execpolicy_amendment: Option<ExecPolicyAmendment>`：可选的“保存前缀”提案（用户可选择以 ApprovedExecpolicyAmendment 接受）
- `parsed_cmd: Vec<ParsedCommand>`：解析后的命令结构（UI 可用来高亮/展示；解析逻辑见 core）

### 0.3 ApplyPatchApprovalRequestEvent（写文件审批事件）
结构：`codex-rs/protocol/src/approvals.rs:ApplyPatchApprovalRequestEvent`

字段要点：
- `changes: HashMap<PathBuf, FileChange>`：每个文件的变更
- `grant_root: Option<PathBuf>`：当需要扩大写权限时，工具可请求“本 session 内允许写该 root”

---

## 1. 核心组件（core 实现）

### 1.1 ApprovalStore：session 级缓存
实现：`codex-rs/core/src/tools/sandboxing.rs:ApprovalStore`

语义：
- key 是“ApprovalKey 的 JSON 序列化字符串”
- value 是 `ReviewDecision`
- 目前只会缓存 `ApprovedForSession`（其它决策不会写入缓存）

### 1.2 with_cached_approval：统一缓存包装
实现：`codex-rs/core/src/tools/sandboxing.rs:with_cached_approval`

输入：
- `keys: Vec<K>`：工具定义的一组 approval keys（通常只有 1 个；apply_patch 可能多个）
- `fetch: async fn() -> ReviewDecision`：真正触发 UI 审批的函数

算法：
1. 若 `keys` 为空：直接 `fetch()`
2. 若所有 key 在 `ApprovalStore` 中均为 `ApprovedForSession`：返回 `ApprovedForSession`（跳过 UI）
3. 否则触发 `fetch()`
4. 若返回 `ApprovedForSession`：将所有 key 单独缓存为 `ApprovedForSession`（未来子集也能命中）

> 复刻注意：对多 key 的处理是“全通过才算已批准”，但缓存写入是“逐 key 写入”。

---

## 2. ExecApprovalRequirement：工具级“是否需要审批”的策略接口

### 2.1 ExecApprovalRequirement 枚举
实现：`codex-rs/core/src/tools/sandboxing.rs:ExecApprovalRequirement`

- `Skip { bypass_sandbox, proposed_execpolicy_amendment }`
  - `bypass_sandbox`：提示 runtime 可在 **第一次尝试** 直接无沙箱执行
  - `proposed_execpolicy_amendment`：仅在特定条件下用于“未来跳过审批/跳过沙箱”（详见 execpolicy 章节）
- `NeedsApproval { reason, proposed_execpolicy_amendment }`
  - `reason`：可选说明（用于 UI）
- `Forbidden { reason }`

辅助方法：
- `proposed_execpolicy_amendment(&self) -> Option<&ExecPolicyAmendment>`
  - 仅在 `Skip/NeedsApproval` 中且字段为 Some 时返回

### 2.2 默认审批策略（无自定义 requirement 的工具）
实现：`codex-rs/core/src/tools/sandboxing.rs:default_exec_approval_requirement`

输入：`AskForApproval` + `SandboxPolicy`

规则（复刻用）：
- `AskForApproval::Never` / `OnFailure` → 默认 `Skip`
- `AskForApproval::UnlessTrusted` → 默认 `NeedsApproval`
- `AskForApproval::OnRequest`：
  - 若 `SandboxPolicy` 是 `DangerFullAccess` 或 `ExternalSandbox{...}` → 默认 `Skip`
  - 否则（ReadOnly/WorkspaceWrite）→ 默认 `NeedsApproval`

> execpolicy（若启用）会覆盖默认策略：shell/unified exec 会把 `exec_approval_requirement` 显式设为 execpolicy 结果。

---

## 3. ToolOrchestrator：审批 + 沙箱选择 + 重试的统一编排

实现：`codex-rs/core/src/tools/orchestrator.rs`

### 3.1 总体执行序列（伪代码）
对任意 tool runtime：
1. **Approval 阶段**
   - 取 `requirement = tool.exec_approval_requirement(req) ?? default_exec_approval_requirement(...)`
   - 若 `Forbidden`：立刻拒绝
   - 若 `NeedsApproval`：调用 `tool.start_approval_async(...)` 获取 `ReviewDecision`
   - 若 `Skip`：跳过 UI
2. **第一次执行（带沙箱或无沙箱）**
   - `initial_sandbox = SandboxManager::select_initial(...)`，除非 `tool.sandbox_mode_for_first_attempt(...)` 要求 bypass
   - `tool.run(req, initial_attempt)`
3. 若第一次执行成功：返回
4. 若第一次执行返回 “Sandbox denied”（`SandboxErr::Denied`）：
   - 若 `tool.escalate_on_failure()==false`：直接返回该错误
   - 若 `tool.wants_no_sandbox_approval(approval_policy)==false`（即 policy 为 Never/OnRequest）：直接返回该错误（不提示无沙箱重试）
   - 否则：
     - 若还未 approved（且 policy != Never）：再发一次审批（reason 固定为 `"command failed; retry without sandbox?"`）
     - 用户拒绝则终止
     - 用户同意则进行 **第二次执行：无沙箱**（`sandbox=None`）

### 3.2 审批缓存与 ApprovalKey
ToolRuntime 通过实现 `Approvable<Req>` 指定：
- `approval_keys(req) -> Vec<ApprovalKey>`

常见 key 组成（复刻为同等粒度）：
- shell：`{command, cwd, sandbox_permissions}`
  - 实现：`codex-rs/core/src/tools/runtimes/shell.rs:ApprovalKey`
- unified exec：`{command, cwd, tty, sandbox_permissions}`
  - 实现：`codex-rs/core/src/tools/runtimes/unified_exec.rs:UnifiedExecApprovalKey`

缓存语义：
- 只有 `ApprovedForSession` 会写入缓存（通过 `with_cached_approval`）
- 一旦缓存命中：tool orchestrator 的 `should_bypass_approval` 会直接跳过再次询问

---

## 4. `start_approval_async`：如何把 “requirement/justification” 变成 UI reason

shell/unified exec 的 reason 选择逻辑（两者一致）：
- `reason = ctx.retry_reason.or_else(|| req.justification.clone())`
  - `ctx.retry_reason` 可能来自：
    - execpolicy prompt/forbidden 的 justification（由 execpolicy 生成的 `ExecApprovalRequirement::NeedsApproval.reason`）
    - 或 sandbox deny 的固定提示 `"command failed; retry without sandbox?"`
  - `req.justification` 来自工具输入参数（模型请求提供）

然后会调用 `Session::request_command_approval(...)` 发出 `ExecApprovalRequestEvent`。

来源：
- `codex-rs/core/src/tools/runtimes/shell.rs:start_approval_async`
- `codex-rs/core/src/tools/runtimes/unified_exec.rs:start_approval_async`
- `codex-rs/core/src/codex.rs:request_command_approval`

---

## 5. 用户响应如何回到 session（exec_approval / patch_approval）

### 5.1 Exec approval 的处理入口
`codex-rs/core/src/codex.rs:exec_approval(sess, id, decision)`

规则：
1. 若 `decision` 是 `ApprovedExecpolicyAmendment { proposed_execpolicy_amendment }`：
   - 先调用 `persist_execpolicy_amendment(...)`（可能失败并发出 WarningEvent）
   - 成功后记录一条 developer message：`Approved command prefix saved:\n...`
2. 若 `decision == Abort`：中断当前任务（`interrupt_task`）
3. 否则：把决策传递给等待中的 in-flight tool（`notify_approval`）

### 5.2 Patch approval 的处理入口
`codex-rs/core/src/codex.rs:patch_approval(sess, id, decision)`

规则：
- 若 `Abort`：中断任务
- 否则：`notify_approval`

---

## 6. execpolicy amendment：ApprovedExecpolicyAmendment 的副作用（与 execpolicy 章节闭环）

当用户选择 `ApprovedExecpolicyAmendment`：
- 必须把 `ExecPolicyAmendment` 写入 `<CODEX_HOME>/rules/default.rules`
- 并更新内存中的 policy（使当前 session 立即生效）

写入格式与去重、文件锁等 **必须复刻**，详见：
- `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md` §6.3.1

---

## 7. Source Map（本章关键源码）
- 编排器：`codex-rs/core/src/tools/orchestrator.rs`
- 通用审批/缓存：`codex-rs/core/src/tools/sandboxing.rs`
- exec 审批事件发出：`codex-rs/core/src/codex.rs:request_command_approval`
- exec 审批决策处理：`codex-rs/core/src/codex.rs:exec_approval`
- 协议定义：`codex-rs/protocol/src/protocol.rs`、`codex-rs/protocol/src/approvals.rs`

## 来源（Source）
- `codex-rs/core/src/tools/orchestrator.rs`
- `codex-rs/core/src/tools/sandboxing.rs`
- `codex-rs/core/src/codex.rs#request_command_approval`
- `codex-rs/core/src/codex.rs#exec_approval`
- `codex-rs/core/src/codex.rs#patch_approval`
- `codex-rs/protocol/src/approvals.rs`
- `codex-rs/protocol/src/protocol.rs`
