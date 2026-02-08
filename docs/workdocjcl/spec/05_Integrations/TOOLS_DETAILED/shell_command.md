# Tool: `shell_command` (function)

## 0. 目的（Purpose）
为模型提供“给定一段 shell script 字符串，在用户默认 shell 中执行并返回输出”的能力。
与 `shell` 的关键差异：
- `shell_command.command` 是 **字符串**（而不是 argv 数组）
- 运行时会根据 session 的用户 shell 把字符串转换成 argv（例如 `["/bin/zsh", "-lc", "..."]`）

## 1. 暴露/启用条件（Exposed when）
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

`shell_command` tool spec 会在以下情况下被暴露给模型：
- `ToolsConfig.shell_type == ShellCommand` → `builder.push_spec(create_shell_command_tool(request_rule_enabled))`

并且当 `ToolsConfig.shell_type != Disabled` 时，handler 名称始终注册：
- `builder.register_handler("shell_command", ShellCommandHandler)`

## 2. 输入（Input arguments）
来源（权威类型）：`codex-rs/protocol/src/models.rs::ShellCommandToolCallParams`

字段：
- `command`（必填，`String`）：要执行的脚本字符串
- `workdir`（可选）：工作目录（最终 `turn.resolve_path`）
- `login`（可选）：是否以 login shell 语义运行（缺省 `true`）
- `timeout_ms`（可选）：超时（缺省同 exec 默认 10s）
- `sandbox_permissions` / `justification` / `prefix_rule`：语义与 `shell` 相同
  - `prefix_rule` 仅在 feature `RequestRule` 启用时生效

> 结构化 schema 参考：`workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.json`（条目：`name=shell_command kind=function`）

## 3. 运行时语义（Runtime semantics）
处理器：`codex-rs/core/src/tools/handlers/shell.rs::ShellCommandHandler`

### 3.1 参数解析与 argv 生成
1) `arguments` JSON → `ShellCommandToolCallParams`
2) 选择 shell：
   - 使用 `session.user_shell()`
3) 由 `ShellCommandHandler::base_command(shell, command, login)` 生成 argv
4) 组装 `ExecParams`（cwd/env/sandbox/justification 同 `shell`）

### 3.2 审批、apply_patch 拦截、执行编排
后续流程复用 `ShellHandler::run_exec_like(...)`：
- 审批策略硬门槛（`require_escalated` 只能在 `OnRequest`）
- apply_patch 拦截（防止间接调用）
- exec_policy 计算审批要求
- ToolOrchestrator + ShellRuntime 执行

## 4. 输出（Output）
与 `shell` 相同：返回 `ToolOutput::Function` 的 `content` 文本。

## 5. 代码映射（Code ↔ Spec）
- tool schema：`codex-rs/core/src/tools/spec.rs::create_shell_command_tool`
- handler：`codex-rs/core/src/tools/handlers/shell.rs::ShellCommandHandler`
- 参数类型：`codex-rs/protocol/src/models.rs::ShellCommandToolCallParams`
- 公共输出封装：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/_COMMON_OUTPUT_ENVELOPE.md`

