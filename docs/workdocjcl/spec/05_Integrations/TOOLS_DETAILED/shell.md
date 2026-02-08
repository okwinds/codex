# Tool: `shell` (function)

## 0. 目的（Purpose）
为模型提供“执行一条 shell 命令并返回输出”的能力；执行受 **审批策略** 与 **沙箱策略** 约束。

## 1. 暴露/启用条件（Exposed when）
代码入口：`codex-rs/core/src/tools/spec.rs::build_specs`

`shell` tool spec 仅在以下情况下被 **push_spec（暴露给模型）**：
- `ToolsConfig.shell_type == Default` → `builder.push_spec(create_shell_tool(request_rule_enabled))`

但当 `ToolsConfig.shell_type != Disabled` 时，运行时始终会注册 handler 名称（兼容旧 prompt）：
- `builder.register_handler("shell", ShellHandler)`
- `builder.register_handler("container.exec", ShellHandler)`（legacy alias）
- `builder.register_handler("local_shell", ShellHandler)`（本地 shell tool type 的输出会路由到同一 handler）

## 2. 输入（Input arguments）
来源（权威类型）：`codex-rs/protocol/src/models.rs::ShellToolCallParams`

字段：
- `command`（必填，`Vec<String>`）：要执行的命令参数数组
  - 非 Windows 的推荐形态：`["bash", "-lc", "<cmd>"]`（来自 `codex-rs/core/src/tools/spec.rs::create_shell_tool` 描述）
  - Windows 的推荐形态：`["powershell.exe", "-Command", "<cmd>"]`
- `workdir`（可选，`Option<String>`）：工作目录（相对 turn cwd 的路径；最终会被 resolve）
- `timeout_ms`（可选，`Option<u64>`）：超时（毫秒）
  - 若缺省：使用 `DEFAULT_EXEC_COMMAND_TIMEOUT_MS = 10000`（见 `codex-rs/core/src/exec.rs`）
- `sandbox_permissions`（可选，`Option<SandboxPermissions>`）：`use_default` 或 `require_escalated`
- `justification`（可选）：当请求 `require_escalated` 时用于向用户解释的审批问题
- `prefix_rule`（可选）：请求持久化的 command 前缀白名单（**仅当** feature `RequestRule` 启用时生效；否则会被丢弃）

> 结构化 schema 参考：`workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`（条目：`name=shell kind=function`）

## 3. 运行时语义（Runtime semantics）
处理器：`codex-rs/core/src/tools/handlers/shell.rs::ShellHandler`

### 3.1 解析与 ExecParams 构造
1) `arguments` JSON → 反序列化为 `ShellToolCallParams`
2) 构造 `ExecParams`（`ShellHandler::to_exec_params`）：
   - `command` 그대로（不再二次拼接）
   - `cwd = turn.resolve_path(workdir)`（`None` → turn.cwd）
   - `expiration = ExecExpiration::from(timeout_ms)`（`None` → DefaultTimeout）
   - `env = create_env(turn.shell_environment_policy)`，并额外 merge `session.dependency_env()`（如果非空）
   - `sandbox_permissions = params.sandbox_permissions.unwrap_or_default()`
   - `justification = params.justification`

### 3.2 审批策略硬门槛（显式 escalated 限制）
若 `sandbox_permissions == RequireEscalated` 且 `turn.approval_policy != AskForApproval::OnRequest`：
- 直接返回 `FunctionCallError::RespondToModel(...)`（拒绝执行）

### 3.3 apply_patch 拦截（防止模型用 shell 间接调用 apply_patch）
在真正执行前，会调用：
- `intercept_apply_patch(&exec_params.command, &exec_params.cwd, timeout, ...)`

若检测到命令中包含可解析的 apply_patch 输入：
- **不会执行 shell**
- 改为走 apply_patch 的处理与审批路径，并返回对应 `ToolOutput`

### 3.4 事件与执行编排
1) 构造 `ToolEmitter::shell(...)` 并发出 begin/end 事件（用于 UI/日志/diff 跟踪）
2) 通过 `session.services.exec_policy.create_exec_approval_requirement_for_command(...)` 计算审批要求
3) 组装 `ShellRequest` 并用 `ToolOrchestrator` 驱动 `ShellRuntime` 执行
4) 执行结果由 `ToolEmitter` 格式化为 `content: String`

## 4. 输出（Output）
- 成功：`ToolOutput::Function { content: <shell 输出/格式化文本>, success: Some(true) }`
- 失败：抛出 `FunctionCallError`，由 ToolRouter 以“失败文本”回注（见 `_COMMON_OUTPUT_ENVELOPE.md`）

## 5. 错误与边界（Errors / edge cases）
典型 `RespondToModel` 错误：
- 参数 JSON 解析失败
- 请求 `require_escalated` 但审批策略不是 `OnRequest`
- shell runtime 执行失败/超时/沙箱错误（会被格式化为可回注文本）

## 6. 安全与副作用（Security / side effects）
- 可能产生：进程执行、文件系统读写、网络访问（取决于命令 + sandbox_policy）
- `is_mutating` 用 `is_known_safe_command` 判定（用于审批/并行调度策略）

## 7. 代码映射（Code ↔ Spec）
- tool schema：`codex-rs/core/src/tools/spec.rs::create_shell_tool`
- handler：`codex-rs/core/src/tools/handlers/shell.rs::ShellHandler`
- 参数类型：`codex-rs/protocol/src/models.rs::ShellToolCallParams`
- 输出封装：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/_COMMON_OUTPUT_ENVELOPE.md`

