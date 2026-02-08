# Tool: `list_mcp_resources` (function)

## 0. 目的
列出 MCP（Model Context Protocol）servers 的 resources。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

该 tool 会被无条件加入（push_spec），并标记支持并行：
- `builder.push_spec_with_parallel_support(create_list_mcp_resources_tool(), true)`
- `builder.register_handler("list_mcp_resources", McpResourceHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_list_mcp_resources_tool`
解析类型：`codex-rs/core/src/tools/handlers/mcp_resource.rs::ListResourcesArgs`

字段：
- `server`（可选）：不填则“聚合列出所有 server 的资源”（此时 **不支持 cursor**）
- `cursor`（可选）：仅当指定 `server` 时可用（分页）

## 3. 运行时语义
handler：`codex-rs/core/src/tools/handlers/mcp_resource.rs::McpResourceHandler`

核心分支（payload_result）：
1) `server=Some(server_name)`：
   - `params = cursor.map(|c| PaginatedRequestParam{ cursor:Some(c) })`
   - 调用 `session.list_resources(server_name, params).await`
   - 输出 `ListResourcesPayload::from_single_server(server_name, result)`：
     - `server: Some(server_name)`
     - `resources: [{ server, ...resource_fields }]`
     - `nextCursor`（若 MCP 返回）
2) `server=None`：
   - 若 `cursor.is_some()` → 错误 `"cursor can only be used when a server is specified"`
   - 调用 `session.services.mcp_connection_manager.list_all_resources().await`
   - 输出 `ListResourcesPayload::from_all_servers(...)`：
     - `server: None`
     - `resources` 为跨 server 展平后的列表（按 server 名排序）

事件：
- begin：`McpToolCallBeginEvent`
- end：`McpToolCallEndEvent`（包含 duration、result 或 error）

输出序列化：
- payload 会被 `serialize_function_output(payload)` 序列化为 JSON 文本，并作为 tool output content 返回。

## 4. 输出
`ToolOutput::Function { content: <JSON string>, success: Some(true) }`

## 5. 错误
典型错误：
- MCP 调用失败（`resources/list failed: ...`）
- cursor 在 server=None 时被使用
- 序列化失败（Fatal）

## 6. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_list_mcp_resources_tool`
- handler：`codex-rs/core/src/tools/handlers/mcp_resource.rs`

