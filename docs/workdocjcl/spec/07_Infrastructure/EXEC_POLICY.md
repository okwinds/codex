# Execpolicy（命令执行策略）复刻级规格

本章目标：以“**仅凭本文即可复刻出与本仓库一致的 execpolicy 行为**”为标准，完整描述 Codex CLI 对“命令执行（shell / unified exec）”的**规则语言、加载合并、匹配与决策、审批联动、以及规则持久化（amendment）**。

> 重要：execpolicy 不是“是否启用沙箱”的策略；它是更细粒度的“命令级策略层”，与 `approval_policy`、`sandbox_policy`、`sandbox_permissions` 共同决定：
> - 是否允许直接执行
> - 是否必须走审批
> - 是否完全禁止
> - 是否允许**绕过沙箱**（bypass sandbox）

---

## 0. 核心对象与术语

### 0.1 Decision（策略决策）
决策枚举（从宽到严，严度可比较）：`allow < prompt < forbidden`。

- `allow`：无需进一步批准即可执行
- `prompt`：需要用户批准（但若 `AskForApproval::Never` 则会升级为 `forbidden`）
- `forbidden`：禁止执行

来源：
- `codex-rs/execpolicy/src/decision.rs`

### 0.2 RuleMatch（匹配结果项）
一次评估会产出 `matched_rules: Vec<RuleMatch>`，每个元素是：
- `PrefixRuleMatch { matched_prefix, decision, justification? }`：由 `.rules` 文件里的 `prefix_rule(...)` 命中
- `HeuristicsRuleMatch { command, decision }`：当无任何 prefix 规则命中时，调用“启发式 fallback”产生（详见 §3）

来源：
- `codex-rs/execpolicy/src/rule.rs`（结构定义）

### 0.3 Evaluation（评估结果）
`Evaluation { decision, matched_rules }` 的 `decision` 规则：
- **严格按严度取最大值**（`max()`）：`forbidden > prompt > allow`
- `matched_rules` 可能包含多个 prefix 规则命中（同一 program 下多个规则都可命中）

来源：
- `codex-rs/execpolicy/src/policy.rs`（`Evaluation::from_matches`）

---

## 1. 规则语言（`.rules` 文件）——可复刻的语法与语义

### 1.1 文件形式与加载入口
- 规则文件扩展名：`.rules`
- 每个文件是 **Starlark**（Bazel Starlark）脚本；加载时启用 `Dialect::Extended` 且 `enable_f_strings = true`
- 目前仅实现内建函数（builtin）：`prefix_rule(...)`

来源：
- `codex-rs/core/src/exec_policy.rs`（加载/解析）
- `codex-rs/execpolicy/src/parser.rs`（Starlark parser + builtin）

### 1.2 `prefix_rule(...)` builtin

#### 1.2.1 参数
```starlark
prefix_rule(
  pattern = [...],          # 必填：token 序列；每个位置是 string 或 [string,...]（表示 alternatives）
  decision = "...",         # 可选：allow | prompt | forbidden；缺省为 allow
  justification = "...",    # 可选：人类可读原因（prompt/forbidden 时常展示给用户）
  match = [...],            # 可选：必须命中该规则的例子（作为 load-time 校验）
  not_match = [...],        # 可选：必须不命中该规则的例子（作为 load-time 校验）
)
```

#### 1.2.2 pattern token 规则
- `pattern` 是 **有序 token 序列**
- 每个元素允许：
  - `"token"`：精确匹配
  - `["alt1","alt2",...]`：该位置可匹配任一备选 token（alternatives）
- 约束：
  - `pattern` **不能为空**
  - alternatives 列表 **不能为空**；且所有 alternatives 必须是 string

匹配算法（Prefix semantics）：
- 令 `pattern_length = len(pattern)`
- 当且仅当 `cmd[0..pattern_length]` 逐 token 匹配 pattern 时命中
- 命中后输出 `matched_prefix = cmd[0..pattern_length]`

来源：
- `codex-rs/execpolicy/src/parser.rs`（pattern 解析）
- `codex-rs/execpolicy/src/rule.rs`（`PrefixPattern::matches_prefix`）

#### 1.2.3 `match` / `not_match`（例子校验）
- `match`、`not_match` 是 load-time 校验：
  - `match` 中每个例子必须至少命中一次当前 program 下的规则集合
  - `not_match` 中每个例子不得命中任何规则
- 例子支持两种表示：
  - token array：`["git","status"]`
  - string：`"git status"`（用 `shlex` 进行 tokenization；语法非法则报错）

注意：这是一种“规则单元测试”，用于防止配置写错。

来源：
- `codex-rs/execpolicy/src/parser.rs`（example 解析）
- `codex-rs/execpolicy/src/rule.rs`（`validate_match_examples` / `validate_not_match_examples`）

---

## 2. 规则加载与合并（多层 config + requirements）

### 2.1 ConfigLayerStack 与 precedence
`ConfigLayerStack.layers` 存储顺序：**最低优先级 → 最高优先级**（后者覆盖前者的 config key）。但注意：execpolicy 的决策聚合是“取最严格”，因此“覆盖”更多体现为**增量叠加**而非 allow 覆盖 forbidden（详见 §2.4）。

来源：
- `codex-rs/core/src/config_loader/state.rs`（`ConfigLayerStack`、`get_layers`、layer ordering）

### 2.2 `.rules` 文件发现规则（每个 layer）
加载入口：`codex-rs/core/src/exec_policy.rs:load_exec_policy(...)`。

遍历顺序：
1. 取 `config_stack.get_layers(LowestPrecedenceFirst, include_disabled=true)`
2. 对每个 layer：
   - 若 `layer.config_folder()` 存在，则进入 `<config_folder>/rules/`
   - 收集该目录下的所有 `*.rules` 文件

关键点：
- `include_disabled=true`：**即使 project layer 因 “trust disabled” 被标为 disabled，也仍然加载其 `.codex/rules/*.rules`**（确保项目规则仍生效）
- 只扫描 `rules/` 子目录；不扫描 `config_folder` 根目录下的 `*.rules`
- `collect_policy_files` 会对路径排序（字典序），保证稳定加载顺序
- 目录不存在：视为无规则（返回空列表）

来源：
- `codex-rs/core/src/exec_policy.rs:load_exec_policy`、`collect_policy_files`
- `codex-rs/core/src/config_loader/state.rs:ConfigLayerEntry::config_folder`

### 2.3 解析与构建
- 对每个规则文件：
  - `identifier = policy_path.to_string_lossy().to_string()`（用作 starlark parse 的 “文件名/标识”，用于报错定位）
  - 读取内容并 `parser.parse(identifier, contents)`
- 所有文件 parse 完后：`policy = parser.build()`

错误处理：
- 若 feature `ExecPolicy` 关闭：整体 policy 为空（`Policy::empty()`）
- 若 parse 任一文件失败：
  - `check_execpolicy_for_warnings`/`load_exec_policy_for_features_with_warning` 会把 parse error 降级为 warning（返回 empty policy + warning）
  - 其他 I/O 错误（read_dir / read_file）通常会作为 hard error 返回

来源：
- `codex-rs/core/src/exec_policy.rs:ExecPolicyManager::load`

### 2.4 requirements.toml 中的 execpolicy（强约束层）
如果 `config_stack.requirements().exec_policy` 存在，则加载完 `.rules` 后会做一次合并：
- `combined_rules = policy.rules().clone()`
- 对 requirements policy 中的每个 rule：`combined_rules.insert(program, rule)`
- 最终返回 `Policy::new(combined_rules)`

requirements policy 的来源与限制：
- 来源文件：`codex-rs/core/src/config_loader/requirements_exec_policy.rs`
- TOML 结构：`[rules].prefix_rules = [...]`
- 限制：requirements 的 decision **不允许 allow**（只允许 prompt / forbidden），否则报错
- 规则 head token 支持 alternatives（`token` 或 `any_of`），会展开为多个 program（每个 head 一个 rule）

为什么 requirements 不允许 allow：
- 因为 execpolicy 的合并是取最严格（max）；requirements 作为约束层，应该只“收紧”而不是“放宽”

---

## 3. 未命中规则时的启发式决策（fallback）

### 3.1 启发式入口与触发条件
当某个命令 `cmd` 在 policy 中 **没有任何 prefix 规则命中** 时：
- `Policy::matches_for_command(..., heuristics_fallback=Some(...))` 会产生一个 `HeuristicsRuleMatch { command: cmd, decision: heuristics_fallback(cmd) }`
- 在 core 中，fallback 函数实现为：`render_decision_for_unmatched_command(...)`

来源：
- `codex-rs/execpolicy/src/policy.rs:matches_for_command`
- `codex-rs/core/src/exec_policy.rs:render_decision_for_unmatched_command`

### 3.2 安全/危险启发式
`render_decision_for_unmatched_command` 的判断顺序（必须按顺序复刻）：

1. **已知安全命令**：如果 `is_known_safe_command(command)` 返回 true，则 `Decision::Allow`。
2. 否则计算：
   - `runtime_sandbox_provides_safety = cfg!(windows) && matches!(sandbox_policy, SandboxPolicy::ReadOnly)`
3. 如果 `command_might_be_dangerous(command) == true` **或** `runtime_sandbox_provides_safety == true`：
   - 若 `approval_policy == Never`：`Decision::Forbidden`
   - 否则：`Decision::Prompt`
4. 否则按 `AskForApproval` 分支：
   - `Never` / `OnFailure`：`Allow`
   - `UnlessTrusted`：`Prompt`
   - `OnRequest`：
     - `SandboxPolicy::DangerFullAccess` 或 `ExternalSandbox{...}`：`Allow`
     - `SandboxPolicy::ReadOnly` 或 `WorkspaceWrite{...}`：
       - 若 `sandbox_permissions.requires_escalated_permissions()`：`Prompt`
       - 否则：`Allow`

来源：
- `codex-rs/core/src/exec_policy.rs:render_decision_for_unmatched_command`
- `docs/workdocjcl/spec/07_Infrastructure/COMMAND_SAFETY.md`（`is_known_safe_command` / `command_might_be_dangerous` 的完整复刻级定义）

#### 3.2.1 决策矩阵（复刻用）
| 条件 | 输出 Decision |
|---|---|
| `is_known_safe_command(cmd)==true` | `allow` |
| `command_might_be_dangerous(cmd)==true` 且 `AskForApproval!=never` | `prompt` |
| `command_might_be_dangerous(cmd)==true` 且 `AskForApproval==never` | `forbidden` |
| `cfg!(windows)` 且 `SandboxPolicy==ReadOnly` 且 `AskForApproval!=never` | `prompt` |
| `cfg!(windows)` 且 `SandboxPolicy==ReadOnly` 且 `AskForApproval==never` | `forbidden` |
| 否则且 `AskForApproval in {never,on_failure}` | `allow` |
| 否则且 `AskForApproval==unless_trusted` | `prompt` |
| 否则且 `AskForApproval==on_request` 且 `SandboxPolicy in {danger_full_access,external_sandbox}` | `allow` |
| 否则且 `AskForApproval==on_request` 且 `SandboxPolicy in {read_only,workspace_write}` 且 `sandbox_permissions==RequireEscalated` | `prompt` |
| 否则 | `allow` |

---

## 4. shell `-lc` 脚本拆解（execpolicy 与安全/危险启发式共享）

为了避免 `bash -lc "..."` 把危险命令藏在脚本里，core 会尽量把 `-lc` 脚本拆成多个“plain commands”分别评估。

### 4.1 支持的外层形式
`parse_shell_lc_plain_commands(command: &[String]) -> Option<Vec<Vec<String>>>`：
- 仅当 `command` 精确是 3 个参数：`[shell, flag, script]`
- 且 `flag` 为 `-lc` 或 `-c`
- 且 `shell` 解析为 `{bash,zsh,sh}`（通过 `detect_shell_type`）

来源：
- `codex-rs/core/src/bash.rs:extract_bash_command`、`parse_shell_lc_plain_commands`

### 4.2 允许的脚本子集（word-only command sequence）
脚本必须能被 tree-sitter-bash 解析，且满足严格白名单：
- **允许的 named node kinds**（出现其它 named node 直接拒绝）：`program` / `list` / `pipeline` / `command` / `command_name` / `word` / `string` / `string_content` / `raw_string` / `number` / `concatenation`
- **允许的 operator tokens**：`&&`、`||`、`;`、`|`，以及引号 token（`"`、`'`）
- 明确拒绝（任一出现即返回 None）：
  - 重定向（`>` 等）
  - subshell / parentheses
  - command substitution（`$(...)`、反引号）
  - 变量展开（`$HOME`、`${VAR}`，包括在双引号/拼接中）
  - 变量赋值前缀（`FOO=bar ls`）
  - 背景执行 `&` 等非白名单操作符

拆解输出：
- 返回 `Vec<Vec<String>>`，每个 inner `Vec<String>` 是一个命令的 token 序列（含解析后的引号内容）
- 若脚本为空或解析失败/包含不支持结构：返回 `None`

来源：
- `codex-rs/core/src/bash.rs:try_parse_word_only_commands_sequence` + tests

### 4.3 execpolicy 对 `-lc` 的实际评估方式
在 core 的 execpolicy 入口中（见 §5.1），会执行：
- `commands = parse_shell_lc_plain_commands(command).unwrap_or_else(|| vec![command.to_vec()])`
- 然后 `policy.check_multiple(commands.iter(), fallback)`

这意味着：
- 如果 `bash -lc` 可拆解：对每条内命令分别匹配 prefix rules / heuristics，再聚合严度
- 如果不可拆解：把整个外层命令当作一个普通命令评估（可能导致更宽/更严取决于规则与 heuristics）

---

## 5. 从“策略评估”到“是否需要审批”的转换（ExecApprovalRequirement）

### 5.1 核心入口
`ExecPolicyManager::create_exec_approval_requirement_for_command`（对 shell/unified exec 共用）：

输入：
- `command: &[String]`：待执行命令（tokens）
- `approval_policy: AskForApproval`：本 turn 的审批策略
- `sandbox_policy: &SandboxPolicy`：本 turn 的沙箱策略
- `sandbox_permissions: SandboxPermissions`：是否要求 escalated（绕过 sandbox）
- `features: &Features`：feature gates（至少 `ExecPolicy`、`RequestRule`）
- `prefix_rule: Option<Vec<String>>`：模型可选提供的“请求保存的 prefix”（仅在 `Feature::RequestRule` 开启时才会被上层透传）

输出：`ExecApprovalRequirement`

来源：
- `codex-rs/core/src/exec_policy.rs:ExecPolicyManager::create_exec_approval_requirement_for_command`
- 透传点：`codex-rs/core/src/tools/handlers/shell.rs`、`codex-rs/core/src/unified_exec/process_manager.rs`

### 5.2 Decision → ExecApprovalRequirement 映射
设 `evaluation = policy.check_multiple(parsed_commands, fallback)`：

#### A) `evaluation.decision == forbidden`
输出：
- `ExecApprovalRequirement::Forbidden { reason }`
- `reason` 由 `derive_forbidden_reason(original_command, &evaluation)` 产生：
  - 选取 **matched_prefix 最长** 的 `PrefixRuleMatch(decision=forbidden)`，若有 justification 则拼入
  - 若没有任何 prefix-rule forbidden（理论上不会发生，因为 decision forbidden 可能来自 heuristics，但 core 仍会输出兜底 reason）

#### B) `evaluation.decision == prompt`
输出分两种：

1) 若 `approval_policy == AskForApproval::Never`：
   - 直接返回 `Forbidden { reason = "approval required by policy, but AskForApproval is set to Never" }`
2) 否则：
   - 返回 `NeedsApproval { reason, proposed_execpolicy_amendment }`
   - `reason`：仅当“policy prompt”驱动时才返回（`derive_prompt_reason`）；若是 heuristics prompt，则为 `None`
   - `proposed_execpolicy_amendment`：见 §6（提案规则）

#### C) `evaluation.decision == allow`
输出：
- `Skip { bypass_sandbox, proposed_execpolicy_amendment }`
- `bypass_sandbox` 为 true 当且仅当：
  - `evaluation.matched_rules` 中存在 `PrefixRuleMatch`（不是 heuristics）且其 decision == allow
  - 含义：**明确被 execpolicy allow 的命令，允许第一尝试直接绕过 sandbox**
- `proposed_execpolicy_amendment`：见 §6（仅在某些“heuristics allow”场景提出）

来源：
- `codex-rs/core/src/exec_policy.rs:create_exec_approval_requirement_for_command`

---

## 6. 提案规则（proposed_execpolicy_amendment）与落盘（amendment）

### 6.1 ExecPolicyAmendment 结构
- 类型：`ExecPolicyAmendment { command: Vec<String> }`
- 语义：若应用该 amendment，则将其写入 `default.rules` 为一条 `decision="allow"` 的 prefix_rule，使未来以该 token 前缀开头的命令可跳过审批/（部分场景）跳过 sandbox。

来源：
- `codex-rs/protocol/src/approvals.rs:ExecPolicyAmendment`

### 6.2 何时提出 amendment（core 规则）
`ExecApprovalRequirement` 内可携带 `proposed_execpolicy_amendment`，最终会进入 `ExecApprovalRequestEvent.proposed_execpolicy_amendment`（UI 可展示给用户）。

提案来源一共有三类（按优先级）：

#### 6.2.1 用户/模型显式请求的 prefix_rule（RequestRule）
`derive_requested_execpolicy_amendment(features, prefix_rule, matched_rules)`：
- 条件：
  - `Feature::ExecPolicy` 必须开启
  - `prefix_rule` 必须存在且非空
  - 若 `matched_rules` 中存在任何 `PrefixRuleMatch(decision=prompt)`：返回 None（因为即便加 allow 前缀，policy prompt 仍会命中）
- 否则返回 `Some(ExecPolicyAmendment::new(prefix_rule.clone()))`

注意：`prefix_rule` 是否可被透传取决于上层 tool handler 是否开启 `Feature::RequestRule`（shell handler 会强制 gate，详见 §6.4）。

来源：
- `codex-rs/core/src/exec_policy.rs:derive_requested_execpolicy_amendment`

#### 6.2.2 prompt 场景的 heuristics 提案（仅当没有 policy prompt）
`try_derive_execpolicy_amendment_for_prompt_rules(matched_rules)`：
- 若存在任何 `PrefixRuleMatch(decision=prompt)`：返回 None
- 否则返回首个 `HeuristicsRuleMatch(decision=prompt)` 的 `command` 作为 amendment（注意：只取第一个）

用途：
- 当因为 heuristics 触发审批（例如 `AskForApproval::UnlessTrusted`），允许用户“一键保存前缀”以减少后续审批。

来源：
- `codex-rs/core/src/exec_policy.rs:try_derive_execpolicy_amendment_for_prompt_rules`

#### 6.2.3 allow 场景的 heuristics 提案（用于“下次直接绕过 sandbox”）
`try_derive_execpolicy_amendment_for_allow_rules(matched_rules)`：
- 若存在任何 policy match（任一 `PrefixRuleMatch`）：返回 None
- 否则返回首个 `HeuristicsRuleMatch(decision=allow)` 的 `command` 作为 amendment

用途：
- 该提案只在“命令在 sandbox 内失败 → 询问用户是否无 sandbox 重试”时真正产生价值：用户可选择把“这类命令”加入 allow 前缀，使未来第一尝试就 bypass sandbox（见 §5.2C 与 tools runtime 的 `SandboxOverride`）。

来源：
- `codex-rs/core/src/exec_policy.rs:try_derive_execpolicy_amendment_for_allow_rules`

### 6.3 应用 amendment（持久化 + 内存更新）
用户若在 UI 选择 `ReviewDecision::ApprovedExecpolicyAmendment { proposed_execpolicy_amendment }`：
1. `codex-rs/core/src/codex.rs:exec_approval(...)` 调用 `persist_execpolicy_amendment(...)`
2. `persist_execpolicy_amendment` 会：
   - 校验 `Feature::ExecPolicy` 已开启，否则返回 `FeatureDisabled`
   - 调用 `ExecPolicyManager::append_amendment_and_update(codex_home, amendment)`
3. `append_amendment_and_update` 做两件事：
   - **落盘**：将 allow 前缀追加到 `<CODEX_HOME>/rules/default.rules`
   - **内存更新**：复制当前 policy，调用 `policy.add_prefix_rule(prefix, allow)`，再写回 `ArcSwap`

来源：
- `codex-rs/core/src/codex.rs:persist_execpolicy_amendment`
- `codex-rs/core/src/exec_policy.rs:append_amendment_and_update`

### 6.3.1 `<CODEX_HOME>/rules/default.rules` 写入格式（必须复刻）
写入函数：`codex-rs/execpolicy/src/amend.rs:blocking_append_allow_prefix_rule`。

规则行格式（单行）：
- `prefix_rule(pattern=[<json string token>, ...], decision="allow")`

其中每个 token 的序列化使用 `serde_json::to_string(token)`，保证包含空格/引号时仍可被正确编码。

追加语义：
- 若文件目录不存在：创建 `<CODEX_HOME>/rules/`（仅创建一层 `rules` 目录）
- 文件锁：使用 advisory lock（`file.lock()`）
- 若文件中已存在完全相同的行（逐行字符串相等）：不重复写入
- 若文件不为空但不以 `\n` 结尾：先补一个换行再追加
- 追加后必然以 `\n` 结尾

来源：
- `codex-rs/execpolicy/src/amend.rs`

### 6.4 `prefix_rule` 输入的安全门（RequestRule feature gate）
以 shell tool 为例（unified exec 由其 request 构造层负责）：
- `ShellHandler` 会读取 `features.enabled(Feature::RequestRule)`：
  - 若未开启：强制 `prefix_rule = None`（忽略模型输入的 prefix_rule）
  - 若开启：允许 `prefix_rule` 透传进 execpolicy

此外，shell handler 还会限制模型“直接要求无 sandbox 执行”的能力：
- 若 `sandbox_permissions == RequireEscalated` 且 `approval_policy != OnRequest`：直接拒绝该 tool call（要求模型不要这么做）

来源：
- `codex-rs/core/src/tools/handlers/shell.rs`（prefix_rule gate + approval policy guard）

---

## 7. 与审批/沙箱运行时的联动（最低闭包）

execpolicy 的输出不会直接执行命令；它通过 `ExecApprovalRequirement` 影响 `ToolOrchestrator`：

1. 若 `Forbidden`：tool 直接被拒绝（不执行）
2. 若 `NeedsApproval`：发出 `ExecApprovalRequestEvent`，等待 `ReviewDecision`
3. 若 `Skip`：不需要审批，进入执行

额外关键点：bypass sandbox
- shell/unified exec runtime 会在以下任一条件满足时，将“第一次尝试”强制设为无 sandbox：
  - `sandbox_permissions == RequireEscalated`
  - 或 `ExecApprovalRequirement::Skip { bypass_sandbox: true }`

来源：
- `codex-rs/core/src/tools/orchestrator.rs`（审批→尝试→失败重试）
- `codex-rs/core/src/tools/runtimes/shell.rs`、`codex-rs/core/src/tools/runtimes/unified_exec.rs`（`SandboxOverride::BypassSandboxFirstAttempt`）
- `codex-rs/protocol/src/protocol.rs:ReviewDecision`（含 `ApprovedExecpolicyAmendment`）

> 注：更完整的“审批缓存、sandbox deny 重试、ApprovedForSession 语义”等，请参见 `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`（本仓库规格文档体系内的审批总章）。

## 来源（Source）
- `codex-rs/core/src/exec_policy.rs`
- `codex-rs/core/src/codex.rs#persist_execpolicy_amendment`
- `codex-rs/execpolicy/src/amend.rs`
- `codex-rs/core/src/tools/handlers/shell.rs`
- `codex-rs/core/src/tools/orchestrator.rs`
- `codex-rs/core/src/tools/runtimes/shell.rs`
- `codex-rs/core/src/tools/runtimes/unified_exec.rs`
- `codex-rs/protocol/src/protocol.rs#ReviewDecision`
