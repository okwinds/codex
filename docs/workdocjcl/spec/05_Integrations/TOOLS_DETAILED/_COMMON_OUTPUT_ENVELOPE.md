# Tool Output Envelope（统一输出封装）

本文件描述 **所有 tool handler** 共同遵守的“调用→执行→回注模型”的封装协议。逐工具文档只描述各自的输入/行为差异；公共的封装逻辑以此为准。

## 1. Tool call 来源（模型输出 item → ToolCall）

### 1.1 Function tool call
- 输入：`codex_protocol::models::ResponseItem::FunctionCall { name, arguments, call_id, ... }`
- 解析位置：`codex-rs/core/src/tools/router.rs::ToolRouter::build_tool_call`
- 行为：
  1) 如果 `name` 能被解析为 MCP tool（`session.parse_mcp_tool_name(&name)`），则创建：
     - `ToolPayload::Mcp { server, tool, raw_arguments }`
  2) 否则创建：
     - `ToolPayload::Function { arguments }`

### 1.2 Custom tool call（freeform）
- 输入：`ResponseItem::CustomToolCall { name, input, call_id, ... }`
- 行为：创建 `ToolPayload::Custom { input }`

### 1.3 Local shell call（非 function schema）
- 输入：`ResponseItem::LocalShellCall { id, call_id, action, ... }`
- 行为：
  - 生成 `tool_name = "local_shell"`
  - 生成 `ToolPayload::LocalShell { params: ShellToolCallParams { ... } }`
  - 注意：这里会为 `sandbox_permissions/prefix_rule/justification` 等字段注入默认值（见源码）。

## 2. Dispatch（ToolCall → handler）
- 位置：`codex-rs/core/src/tools/router.rs::ToolRouter::dispatch_tool_call`
- 输入：`ToolInvocation { session, turn, tracker, call_id, tool_name, payload }`
- 行为：调用 `ToolRegistry::dispatch(invocation).await`

## 3. 错误处理（handler error → 回注模型）

### 3.1 错误分类
所有 tool handler 返回 `Result<ResponseInputItem, FunctionCallError>`，其中：
- `FunctionCallError::Fatal(message)`：向上抛出，中止（由上层 turn loop 处理）
- 其他错误：被包装成 “失败的 tool output”，回注给模型继续生成

### 3.2 失败 output 的形状（注意：wire 形状与内部字段不同）
位置：`ToolRouter::failure_response`
- 若原 tool payload 是 `ToolPayload::Custom`（即 custom tool），则回注：
  - `ResponseInputItem::CustomToolCallOutput { call_id, output: message }`
- 否则回注 function output：
  - `ResponseInputItem::FunctionCallOutput { call_id, output: { content: message, success: Some(false), ... } }`

重要：`codex_protocol::models::FunctionCallOutputPayload` 的 `Serialize` 实现会把 **没有 `content_items` 的 output 一律序列化成 plain string**（忽略 `success` 字段）。因此：
- 内部结构里可能携带 `success: Some(false)`（用于日志/未来扩展）
- 但 **回注到模型 provider 的 wire 形状** 通常仍是 `"output": "<string>"`（除非 `content_items` 非空）

> 结论：除 `Fatal` 外，工具失败不会直接中断 turn；而是以“失败文本”回注模型继续生成；是否携带可见的 `success=false` 取决于 provider/wire shape（本仓库当前实现通常不携带）。

## 4. 成功 output 的形状（handler 成功路径）
多数 function tools 会返回：
- `ToolOutput::Function { content: String, content_items: Option<...>, success: Some(true) }`

custom tools（freeform）会返回：
- `ToolOutput::Custom { ... }`（具体以 handler 实现为准）

最终由 ToolRegistry/Router 转成对应的 `ResponseInputItem::*CallOutput` 回注模型；wire 形状由 `FunctionCallOutputPayload` 的 `Serialize` 决定（string vs items）。

## 5. 并行调用能力（parallel_tool_calls）
- 位置：`codex-rs/core/src/tools/spec.rs::build_specs` 使用 `builder.push_spec_with_parallel_support(tool_spec, true/false)`
- 查询 API：`ToolRouter::tool_supports_parallel(tool_name)`
- 复刻要求：
  - 并行支持必须与原实现一致，否则模型可能在并行 tool calls 下产生不可复现的竞态/资源冲突。
