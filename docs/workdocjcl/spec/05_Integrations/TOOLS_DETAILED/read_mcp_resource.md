# Tool: `read_mcp_resource` (function)

## 0. 目的
从指定 MCP server 读取某个 resource（按 uri）。

## 1. 暴露/启用条件
入口：`codex-rs/core/src/tools/spec.rs::build_specs`

无条件 push_spec，且支持并行：
- `builder.push_spec_with_parallel_support(create_read_mcp_resource_tool(), true)`
- `builder.register_handler("read_mcp_resource", McpResourceHandler)`

## 2. 输入
解析类型：`codex-rs/core/src/tools/handlers/mcp_resource.rs::ReadResourceArgs`

字段：
- `server`（必填）：server name（normalize_required_string，不允许空字符串）
- `uri`（必填）：resource uri（normalize_required_string，不允许空字符串）

## 3. 运行时语义
1) 发送 begin 事件（含 `McpInvocation { server, tool:"read_mcp_resource", arguments }`）
2) 调用 `session.read_resource(&server, ReadResourceRequestParam { uri })`
3) 组装输出 `ReadResourcePayload { server, uri, result: ReadResourceResult }`
4) JSON 序列化后作为 tool output content 返回
5) 发送 end 事件（成功/失败）

## 4. 输出
JSON 字符串（包含 server/uri 与 MCP 返回的 read result 字段）。

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_read_mcp_resource_tool`
- handler：`codex-rs/core/src/tools/handlers/mcp_resource.rs`

