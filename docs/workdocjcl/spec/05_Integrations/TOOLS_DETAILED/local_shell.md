# Tool: `local_shell` (tool type: `local_shell`)

## 0. 目的（Purpose）
`local_shell` 不是标准的 function tool；它对应 OpenAI Responses API 的 `type="local_shell"` item。
本仓库会把 provider 返回的 `ResponseItem::LocalShellCall` 转换为本地可执行的 `ToolPayload::LocalShell`，并复用 `ShellHandler` 完成执行。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

当 `ToolsConfig.shell_type == Local`：
- `builder.push_spec(ToolSpec::LocalShell {})`（向 provider 声明支持 local_shell tool）

并且当 `ToolsConfig.shell_type != Disabled`：
- 总会 `register_handler("local_shell", ShellHandler)`（供 `ToolPayload::LocalShell` dispatch）

## 2. 输入（Input）
来源：`codex_protocol::models::ResponseItem::LocalShellCall`

关键字段：
- `call_id` / `id`：用于回注输出与事件关联
- `action`：目前只支持 `LocalShellAction::Exec`

在 `ToolRouter::build_tool_call` 中，会把 `LocalShellAction::Exec` 转成：
- `tool_name = "local_shell"`
- `ToolPayload::LocalShell { params: ShellToolCallParams { command, workdir, timeout_ms, sandbox_permissions=UseDefault, prefix_rule=None, justification=None } }`

## 3. 运行时语义
- handler：`codex-rs/core/src/tools/handlers/shell.rs::ShellHandler`
- payload：`ToolPayload::LocalShell` 分支
  - 仍会走审批/沙箱/exec_policy 等统一路径

## 4. 输出与错误
见公共封装：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/_COMMON_OUTPUT_ENVELOPE.md`

## 5. 代码映射
- tool call 转换：`codex-rs/core/src/tools/router.rs::ToolRouter::build_tool_call`
- schema push_spec：`codex-rs/core/src/tools/spec.rs::build_specs`
- handler：`codex-rs/core/src/tools/handlers/shell.rs::ShellHandler`

