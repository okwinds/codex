# Tool: `container.exec` (legacy alias)

## 0. 目的（Purpose）
`container.exec` 是历史兼容别名：旧 prompt/旧模型可能会发起名为 `container.exec` 的 function call。
本仓库运行时会把它当作 `shell` 同构处理。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

当 `ToolsConfig.shell_type != Disabled` 时：
- 总会 `register_handler("container.exec", ShellHandler)`

注意：
- `container.exec` **通常不会被 push_spec 暴露给模型**（即 tool list 里不一定出现它）
- 但如果模型返回 tool call 名称是 `container.exec`，仍会被执行（兼容性）

## 2. 输入（Input arguments）
与 `shell` 完全一致：
- 权威类型：`codex-rs/protocol/src/models.rs::ShellToolCallParams`
- 文档：`workdocjcl/spec/05_Integrations/TOOLS_DETAILED/shell.md`

## 3. 运行时语义（Runtime semantics）
处理器与逻辑与 `shell` 相同：
- handler：`codex-rs/core/src/tools/handlers/shell.rs::ShellHandler`
- `tool_name` 在事件与日志中会保持为 `"container.exec"`（用于溯源）

