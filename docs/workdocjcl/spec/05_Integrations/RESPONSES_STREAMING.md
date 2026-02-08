# 集成：Responses API 流式事件与传输（SSE / WebSocket）复刻级规格

本章目标：复刻 Codex 在 `WireApi::Responses` 下的“流式请求 + 事件解析 + 断线重试 + WebSocket→HTTP 回退”语义，使实现者可以在不同 provider/feature 组合下得到一致的：
- 传输选择（SSE vs WebSocket）
- 请求头/turn_state 行为（x-codex-turn-state、x-reasoning-included 等）
- 事件解析规则（哪些 SSE/WS event type 会产出内部 `ResponseEvent`，哪些会被忽略）
- 错误分类（fatal vs retryable）与重试/回退策略

本章不覆盖：
- Prompt 组装（见 `workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`）
- Provider registry/auth 注入（见 `workdocjcl/spec/05_Integrations/MODEL_PROVIDERS.md`）
- Tool execution 与 approvals（见 `workdocjcl/spec/05_Integrations/TOOLS_DETAILED/*`、`workdocjcl/spec/07_Infrastructure/APPROVALS.md`）

---

## 1. 传输选择矩阵（Responses：SSE vs WebSocket）

当 provider 配置 `wire_api = responses` 时，每个 turn 的 streaming 由 core `ModelClientSession::stream(prompt)` 决定：

### 1.1 WebSocket 启用条件（同时满足）
仅当以下都为 true 才会尝试 WebSocket：
- provider 声明支持：`provider.supports_websockets == true`
- feature 开启：`Feature::ResponsesWebsockets` enabled（config key：`responses_websockets`）
- 当前 session 未禁用 websockets：`TransportManager.disable_websockets() == false`

否则使用 HTTP SSE（`/v1/responses` streaming）。

### 1.2 一次性回退开关（TransportManager）
`TransportManager` 内部只有一个原子布尔开关：
- 初始：`disable_websockets = false`
- 一旦触发 HTTP fallback：置为 true，并在该 session 生命周期内保持（不会自动恢复）。

复刻要求：
- 回退必须是“最多一次激活”的幂等行为：只有从 false→true 的第一次切换算作激活。

---

## 2. 请求与 options（Responses）

core 在 Responses API 下会构造：
- `ApiPrompt`：`instructions` + `input` + `tools` + `parallel_tool_calls` + `output_schema`
- `ApiResponsesOptions`：reasoning/include、prompt_cache_key、text controls、conversation_id、extra_headers、compression、turn_state 等

关键点：

### 2.1 `prompt_cache_key` 与 `conversation_id`
- `prompt_cache_key = conversation_id`（字符串化 thread id）
- `conversation_id` 同时：
  - 写入 options（用于 HTTP 请求 / provider 逻辑）
  - 用于 WebSocket connect 时构造额外 header：`session_id: <conversation_id>`

### 2.2 `text` controls（verbosity + output_schema）
`text` controls 是 Responses API 的 `text` 字段组合：
- 当 `verbosity` 或 `output_schema` 任一存在时才会设置
- `output_schema` 对应 `text.format`，并使用固定 `name = "codex_output_schema"` 且 `strict=true`

### 2.3 reasoning 与 include
当 model 支持 reasoning summaries 时：
- options.reasoning 会包含 effort/summary（按配置 + model 默认）
- options.include 会包含 `reasoning.encrypted_content`（用于让服务器返回 reasoning 内容）

> 复刻注意：reasoning 的存在会影响 WS connect 的 server headers（`x-reasoning-included`）语义（见 §4.1/§4.2）。

### 2.4 压缩（可选）
当同时满足：
- feature `EnableRequestCompression` enabled
- auth 为 ChatGPT（`CodexAuth::is_chatgpt_auth`）
- provider 为 OpenAI（`provider.is_openai()`）
则请求会启用 `Compression::Zstd`，否则 `Compression::None`。

---

## 3. HTTP SSE：连接、预注入事件、解析与终止条件

### 3.1 连接前的“预注入事件”（headers 驱动）
建立 SSE stream 后，客户端会先发送若干“由响应 headers 推导”的事件（如果存在）：
- `RateLimits(snapshot)`：从 rate-limit headers 解析（若可用）
- `ModelsEtag(etag)`：来自 `X-Models-Etag`（若存在）
- `ServerReasoningIncluded(true)`：当响应 headers 含 `X-Reasoning-Included` 时发送

并且：
- 若响应 headers 含 `x-codex-turn-state`，会将其写入 `turn_state: OnceLock<String>`（仅首次 set 生效）。

复刻要求：
- 这些事件必须在任何 SSE data event 之前发出（否则上层 token/rate-limit 统计会不一致）。

### 3.2 SSE event parsing：从 `type` 到 `ResponseEvent`
每个 SSE data（`sse.data`）会被解析为 JSON 对象 `ResponsesStreamEvent`，其中最关键字段是：
- `type`（字符串，事件种类）
- `response` / `item` / `delta` / `summary_index` / `content_index`（按事件种类选择性存在）

识别并产出的事件（其余均忽略，仅 trace 日志）：
- `response.created` → `ResponseEvent::Created`（要求 `response` 字段存在）
- `response.output_item.added` → `OutputItemAdded(ResponseItem)`（item JSON 需能 parse 为 `ResponseItem`）
- `response.output_item.done` → `OutputItemDone(ResponseItem)`
- `response.output_text.delta` → `OutputTextDelta(delta)`
- `response.reasoning_summary_text.delta` → `ReasoningSummaryDelta { delta, summary_index }`
- `response.reasoning_text.delta` → `ReasoningContentDelta { delta, content_index }`
- `response.reasoning_summary_part.added` → `ReasoningSummaryPartAdded { summary_index }`
- `response.completed` → `Completed { response_id, token_usage }`（解析 `response.id` 与可选 usage）
- `response.done` → `Completed { response_id, token_usage }`（兼容事件；`response` 缺失时也会 emit Completed，id=""）

复刻注意：
- 对 `ResponseItem` parse 失败：只记录 debug 并忽略该 output_item 事件（不终止流）。

### 3.3 SSE 错误处理（重要差异点：response.failed 不会立刻终止）
SSE 解析器对 `response.failed` 的处理是：
- 解析失败原因并把它转换成一个 `ApiError`（见 §6）
- **不立刻发送 Err 到上游 channel**；只把该 error 缓存在 `response_error`
- 继续消费 SSE stream，直到 stream 结束或 idle timeout
- 当 stream **在未收到 Completed 的情况下结束**（EOF），若缓存了 `response_error`，则以该 error 作为最终错误发送；否则发送通用错误 `"stream closed before response.completed"`

因此，SSE 下的 `response.failed` 通常表现为“流结束时才报错”。

### 3.4 SSE 终止条件
解析器在两种情况下退出：
- 发送了 `ResponseEvent::Completed`（立即 return）
- SSE stream 结束/报错/超时（发送 Err 并 return）

idle timeout：
- 若在 `idle_timeout` 内收不到下一条 SSE 事件：发送 `ApiError::Stream("idle timeout waiting for SSE")` 并退出。

---

## 4. WebSocket：连接、turn_state、事件处理与增量 append

### 4.1 WebSocket connect 与 headers
WS URL：
- 基于 provider base_url 推导 websocket base，并连接 `.../responses`（路径固定为 `"responses"`）。

connect 成功后：
- 若握手 response headers 含 `x-codex-turn-state`，会尝试写入 `turn_state OnceLock`（同 SSE）。
- 若握手 response headers 含 `x-reasoning-included`，连接对象会记录 `server_reasoning_included=true`。

### 4.2 WebSocket stream_request：预注入事件
当 `server_reasoning_included=true`：
- WS stream 开始时会先发送 `ResponseEvent::ServerReasoningIncluded(true)`（与 SSE 的 header 注入对应）。

### 4.3 WebSocket 消息处理（与 SSE 的关键差异）
对 WebSocket 文本帧：
- 尝试解析为 `ResponsesStreamEvent`（同 SSE）
- 调用同一个 `process_responses_event(...)` 产生 `ResponseEvent`

差异点：
- 当 `process_responses_event` 返回 Err（例如 `response.failed`）：**WebSocket 会立即返回 Err 并终止 stream**（不会像 SSE 一样缓存到 EOF）。
- 当收到 `Message::Close` 或 stream 关闭但未 Completed：返回错误 `"stream closed before response.completed"`（或 `"websocket closed by server before response.completed"`）
- idle timeout：`"idle timeout waiting for websocket"`
- `Message::Binary`：直接错误 `"unexpected binary websocket event"`
- `Ping`：服务器会回 `Pong`；失败则错误 `"websocket ping failed"`

### 4.4 增量请求：`response.append`
为了减少重复发送历史 items，core 会维护 `websocket_last_items`（上一次 WS 请求的 `ApiPrompt.input`）并在满足条件时改用增量 append：
- 若新请求 `input_items` 以 `websocket_last_items` 为前缀，且更长：
  - WS request 使用 `type = "response.append"`，其 `input` 只包含新增的后缀 items
- 否则：
  - WS request 使用 `type = "response.create"`，包含完整 `instructions`/`input`/`tools` 等

复刻要求：
- append 判断必须按“前缀相等 + 新输入更长”执行（否则会导致服务端上下文错位）。

---

## 5. 重试与回退（WebSocket → HTTPS）

### 5.1 retry budget：按 provider 的 `stream_max_retries`
当一次 sampling request 失败且错误属于 retryable（core `CodexErr::is_retryable()==true`）：
- 若 `retries < stream_max_retries`：
  - `retries += 1`
  - delay：
    - 若错误为 `CodexErr::Stream(_, Some(requested_delay))`：优先用 requested_delay（典型来自 `response.failed` rate_limit_exceeded）
    - 否则使用指数 backoff（`backoff(retries)`）
  - UI 会收到 “Reconnecting... {retries}/{max_retries}” 的提示事件
  - sleep(delay) 后重试

### 5.2 WebSocket 回退触发条件（达到 retry budget）
当：
- 当前使用 WebSocket（且 WS 功能“理论上启用”）
- `retries >= stream_max_retries`
- 且 `TransportManager.activate_http_fallback(...)` 返回 true（首次切换）

则会：
- 发出 warning：`"Falling back from WebSockets to HTTPS transport. <err>"`
- 将 retries 重置为 0
- 清理 WS 连接与增量状态：
  - `connection = None`
  - `websocket_last_items.clear()`
- 后续重试将走 HTTP SSE（因为 websockets 已被禁用）

复刻注意：
- 回退只会触发一次；之后即使 SSE 也失败，不会再尝试切回 WS。

---

## 6. `response.failed` → 错误分类（对重试/用户提示极关键）

当 Responses stream 产生 `response.failed` 且包含 `response.error` 时，会按优先级映射为：

Fatal / 不可重试（core 会直接终止 turn）：
- `code == "context_length_exceeded"` → `ContextWindowExceeded`
- `code == "insufficient_quota"` → `QuotaExceeded`
- `code == "usage_not_included"` → `UsageNotIncluded`
- `code == "invalid_prompt"` → `InvalidRequest { message }`

Retryable（core 会产生 `CodexErr::Stream(message, delay)` 并走重试）：
- 其他错误：`ApiError::Retryable { message, delay }`
  - delay：仅当 `code == "rate_limit_exceeded"` 且 message 可解析出 “try again in <N> <unit>” 时设置
  - 否则 delay=None（由 core backoff 决定）

---

## 7. 测试/调试钩子：SSE fixture

当环境变量 `CODEX_RS_SSE_FIXTURE` 指向本地 fixture 文件时：
- core 会绕过真实网络请求，改从 fixture 生成 SSE stream 并按同一 parser 输出事件。

复刻用途：
- 在不依赖上游服务的情况下复现“事件序列解析”与“错误分类”逻辑。

---

## 8. Source Map（本章关键源码锚点）

- 传输选择与 WS 增量 append：`codex-rs/core/src/client.rs`
- WebSocket → HTTPS 回退触发点（retry budget exhausted）：`codex-rs/core/src/codex.rs`（sampling request loop）
- 回退状态（一次性禁用 WS）：`codex-rs/core/src/transport_manager.rs`
- ApiError → CodexErr 映射（retryable delay）：`codex-rs/core/src/api_bridge.rs`
- SSE 事件解析与 `process_responses_event`：`codex-rs/codex-api/src/sse/responses.rs`
- WebSocket 事件循环与解析：`codex-rs/codex-api/src/endpoint/responses_websocket.rs`
- `ResponseEvent`/`ResponsesWsRequest` 定义：`codex-rs/codex-api/src/common.rs`

