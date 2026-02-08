# Tool: `list_mcp_resource_templates` (function)

## 0. 目的
列出 MCP servers 的 resource templates。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

无条件 push_spec，且支持并行：
- `builder.push_spec_with_parallel_support(create_list_mcp_resource_templates_tool(), true)`
- `builder.register_handler("list_mcp_resource_templates", McpResourceHandler)`

## 2. 输入
解析类型：`codex-rs/core/src/tools/handlers/mcp_resource.rs::ListResourceTemplatesArgs`

字段：
- `server`（可选）：不填则聚合列出所有 server 的 templates（此时不支持 cursor）
- `cursor`（可选）：仅当 server 指定时可用

## 3. 运行时语义
实现与 `list_mcp_resources` 同构：
- `server=Some` → `session.list_resource_templates(server, params)`
- `server=None` → `mcp_connection_manager.list_all_resource_templates()`
- cursor 仅 server=Some 时允许
- 输出 payload 类型：`ListResourceTemplatesPayload`
- begin/end 事件：`McpToolCallBeginEvent` / `McpToolCallEndEvent`

## 4. 输出
`ToolOutput::Function { content: <JSON string>, success: Some(true) }`

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_list_mcp_resource_templates_tool`
- handler：`codex-rs/core/src/tools/handlers/mcp_resource.rs`

