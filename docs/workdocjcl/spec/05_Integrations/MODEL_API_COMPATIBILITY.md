# 集成：模型 API 交互与兼容性矩阵（Provider / WireApi / Headers / Events）复刻级规格

本章目标：把 Codex 与“OpenAI-compatible HTTP API”交互的**可复刻细节**落盘到规格层，使实现者仅靠本章与仓库其他 specs，即可：
- 正确实现 provider 配置、wire API 选择（Responses；Chat wire 已移除）
- 正确实现 streaming 请求（SSE / WebSocket）与重试策略对齐
- 正确处理 **headers → 内部事件** 的注入逻辑（RateLimits / ModelsEtag / ReasoningIncluded / turn_state）
- 形成“跨 provider / 跨模型”的**兼容性矩阵**（哪些能力是必需、哪些仅在特定 provider 上存在）

本章重点是“兼容性与复刻边界”，不重复展开：
- Responses SSE/WS 的完整事件解析与重试/回退：`docs/workdocjcl/spec/05_Integrations/RESPONSES_STREAMING.md`
- Prompt 组装（initial context / personality / skills）：`docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`
- Tools 的 schema 与逐 tool 行为：`docs/workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.md` + `docs/workdocjcl/spec/05_Integrations/TOOLS_DETAILED/*`
- Skills 发现、mentions 消歧与 `<skill>` 注入：`docs/workdocjcl/spec/05_Integrations/SKILLS.md`

---

## 1. 概念与边界（必须统一）

### 1.1 Provider（部署端点配置）
Codex 将“一个可访问的 OpenAI-compatible API 部署”抽象为 provider。其最终 wire 层形态由：
- core 的 `ModelProviderInfo`（配置层）→ `codex_api::Provider`（网络层）

配置来源：
- 内置默认 providers：`codex-rs/core/src/model_provider_info.rs::built_in_model_providers`
- 用户自定义 providers：`~/.codex/config.toml` 的 `model_providers`（覆盖/扩展内置）

### 1.2 WireApi（协议形状，不可自动探测）
`WireApi` 必须显式声明（否则请求/响应 shape 不匹配）：
- `responses`：POST `.../responses`，以 Responses API shape 发送 `instructions + input + tools`
- `chat`：**已移除**（`wire_api = "chat"` 配置解析阶段直接失败；见 `docs/workdocjcl/spec/05_Integrations/CHAT_WIRE_MAPPING.md`）

对应代码：
- 配置层：`codex-rs/core/src/model_provider_info.rs::WireApi`
- 网络层：`codex-rs/codex-api/src/provider.rs::WireApi`
- 路径选择（ResponsesClient/ChatClient）：`codex-rs/codex-api/src/endpoint/responses.rs`、`codex-rs/codex-api/src/endpoint/chat.rs`

> 复刻要点：**wire API 不做运行时探测**。复刻时必须要求 provider entry 显式设置或有稳定默认值，否则会出现“看似能连通但语义完全错误”的失败模式。

---

## 2. Provider 解析与能力面（配置 → 网络）

### 2.1 built-in providers 的“真实默认矩阵”
内置 providers（默认即可开箱用）：
- `openai`：Responses + 支持 WebSocket + 需要 OpenAI/ChatGPT auth
- `ollama`：Responses（OSS）+ 不支持 WebSocket
- `lmstudio`：Responses（OSS）+ 不支持 WebSocket

来源：`codex-rs/core/src/model_provider_info.rs::built_in_model_providers`

复刻含义：
- “跨 provider 的兼容性矩阵”至少要覆盖 **OpenAI vs OSS（localhost）** 两条主路径；
- Azure / 其它第三方 provider 通过 config.toml 扩展进入系统（见 §2.4 / §4.4）。

### 2.2 base_url 默认值（ChatGPT auth vs API key）
当 `ModelProviderInfo.to_api_provider(auth_mode)` 被调用时，base_url 的默认值取决于 auth mode：
- ChatGPT 登录态：`https://chatgpt.com/backend-api/codex`
- 其他（API key）：`https://api.openai.com/v1`

来源：`codex-rs/core/src/model_provider_info.rs::ModelProviderInfo::to_api_provider`

复刻要点：
- 这是“同一 provider 名称 openai”在不同 auth_mode 下行为差异的根源。

### 2.3 query params 拼接规则（无 URL encoding）
`codex_api::Provider.url_for_path(path)`：
- 规则：`{base_url}/{path}`（处理末尾/开头 `/`）
- 若 `query_params` 非空：以 `k=v&k2=v2` 直接 join，并 append `?`（**不做 URL encoding**）

来源：`codex-rs/codex-api/src/provider.rs::Provider::url_for_path`

复刻风险：
- 若复刻实现做了 URL encoding，会改变最终 URL，影响兼容性（特别是 Azure 的 `api-version` 等参数）。

### 2.4 Azure Responses endpoint 检测（影响默认 store + 行为分支）
Azure 识别仅对 `WireApi::Responses` 生效：
- 如果 provider name 是 "Azure"（不区分大小写）→ 认为是 Azure
- 或 base_url 包含 `openai.azure.` / `windows.net/openai` / `cognitiveservices.azure.` / `aoai.azure.` / `azure-api.` / `azurefd.` 等 marker → 认为是 Azure

来源：`codex-rs/codex-api/src/provider.rs::is_azure_responses_wire_base_url`

影响点：
- Responses API 默认 `store`（见 §4.2）
- Azure 的 `rate_limit_exceeded` 文案解析（见 §6.2）

---

## 3. Streaming 请求的 wire-level “共同行为”（Chat & Responses）

### 3.1 StreamingClient 固定请求形态（SSE over HTTP）
对 Chat 与 Responses 的 SSE streaming，`StreamingClient.stream(...)` 固定做：
- `POST {provider.url_for_path(path)}`
- `Accept: text/event-stream`（固定）
- body：JSON
- compression：`RequestCompression::{None|Zstd}`（由上层选择）
- retries：使用 provider.retry 转换出的 `RetryPolicy`（transport 级重试）
- idle timeout：provider.stream_idle_timeout（解析/等待下一 SSE 事件）

来源：`codex-rs/codex-api/src/endpoint/streaming.rs`

复刻注意：
- transport 级 retry 与 core 级 “stream reconnect retry budget” 是两个层次；后者见 `RESPONSES_STREAMING.md`。

---

## 4. Responses API 兼容性（请求体/headers/事件注入）

### 4.1 请求体字段（ResponsesApiRequest）
Responses streaming 请求体的 canonical 结构（字段名必须一致）：
- `model: string`
- `instructions: string`
- `input: ResponseItem[]`
- `tools: any[]`（JSON tool defs）
- `tool_choice: "auto"`（固定）
- `parallel_tool_calls: bool`
- `reasoning?: { effort?: ..., summary?: ... }`
- `store: bool`
- `stream: true`（固定）
- `include: string[]`
- `prompt_cache_key?: string`
- `text?: { verbosity?: low|medium|high, format?: { type: "json_schema", strict: true, schema: object, name: "codex_output_schema" } }`

来源：
- shape：`codex-rs/codex-api/src/common.rs::ResponsesApiRequest`
- 构造：`codex-rs/codex-api/src/requests/responses.rs::ResponsesRequestBuilder`
- `text` 的生成逻辑：`codex-rs/codex-api/src/common.rs::create_text_param_for_request`

### 4.2 store 的默认与 Azure 特例（必须复刻）
`store` 默认值：
- 若未显式传入 `store_override`：`store = provider.is_azure_responses_endpoint()`
  - OpenAI / OSS：默认 `false`
  - Azure（被检测为 Azure Responses endpoint）：默认 `true`

Azure 特例（只在 `store == true && provider.is_azure_responses_endpoint()` 时触发）：
- 对 `input` 数组中的部分 item，**把已有 id 写回 payload**（attach_item_ids）
- 仅对以下类型且 id 非空：
  - `ResponseItem::Reasoning { id }`
  - `ResponseItem::Message { id: Some(id) }`
  - `ResponseItem::WebSearchCall/FunctionCall/LocalShellCall/CustomToolCall`（均要求 `id: Some`）

来源：`codex-rs/codex-api/src/requests/responses.rs`

复刻意义：
- 这是 “Azure 默认 store=true” + “attach ids” 的组合契约；复刻缺失会导致 Azure 端上下文/存储行为偏离，进而影响 streaming 的一致性。

### 4.3 headers → 事件注入（仅当 headers 存在时）
对 Responses SSE stream，建立连接后会先做“header 驱动的预注入事件”：
- `RateLimits(snapshot)`：来自 **Codex bespoke headers**（见 §4.5）
- `ModelsEtag(etag)`：header `X-Models-Etag`（存在则注入）
- `ServerReasoningIncluded(true)`：header `x-reasoning-included`（存在则注入 true）
- `turn_state`：header `x-codex-turn-state`（存在则写入 `OnceLock<String>`）

来源：`codex-rs/codex-api/src/sse/responses.rs::spawn_response_stream`

复刻注意：
- “这些事件必须早于任何 data event 发出”，否则 core 对 token/rate-limit 的 UI 初始化会不一致（详见 `RESPONSES_STREAMING.md` §3.1）。

### 4.4 Responses WebSocket 兼容性边界（provider 必须显式声明）
Responses WebSocket 只在以下条件组合时启用（**缺一不可**）：
- provider 配置 `supports_websockets = true`
- feature flag `responses_websockets` 启用
- session 未被 TransportManager 禁用 websockets（一次性回退后会永久禁用）

来源（启用判定）：`codex-rs/core/src/client.rs`

WebSocket handshake headers 处理：
- `x-reasoning-included`：存在则连接记录 `server_reasoning_included=true`，随后 stream 开始时预注入 `ServerReasoningIncluded(true)`
- `x-codex-turn-state`：存在则写入 `OnceLock<String>`

来源：`codex-rs/codex-api/src/endpoint/responses_websocket.rs`

复刻边界：
- 内置 `openai` provider 才默认 `supports_websockets=true`；OSS providers 默认为 false（见 §2.1）。
- 如果第三方 provider 实际支持 WS，但 config 未声明为 true，Codex 也不会尝试 WS（这是预期行为）。

### 4.5 RateLimit headers（Codex bespoke，不是 OpenAI 标准）
`RateLimits(snapshot)` 的来源不是标准 OpenAI headers，而是 Codex bespoke 头：
- primary：`x-codex-primary-used-percent` / `x-codex-primary-window-minutes` / `x-codex-primary-reset-at`
- secondary：`x-codex-secondary-used-percent` / `x-codex-secondary-window-minutes` / `x-codex-secondary-reset-at`
- credits：`x-codex-credits-has-credits` / `x-codex-credits-unlimited` / `x-codex-credits-balance`
- promo：`x-codex-promo-message`（单独解析函数）

来源：`codex-rs/codex-api/src/rate_limits.rs`

兼容性矩阵结论：
- OpenAI（ChatGPT backend / Codex proxy）可能提供这些头 → UI 可即时显示 rate-limit/credits
- 绝大多数第三方 OpenAI-compatible provider **不会提供这些头** → 不会注入 RateLimits 事件（这不是错误）

---

## 5. Chat Completions 兼容性（已移除）

当前基准提交中，`wire_api = "chat"` 不再支持：配置解析阶段会直接失败（不会进入“请求映射 / SSE 解析”分支）。

- 复刻要求：错误文案与迁移指引一致（见 `docs/workdocjcl/spec/05_Integrations/CHAT_WIRE_MAPPING.md` §3）。
- 来源：`codex-rs/core/src/model_provider_info.rs`（`CHAT_WIRE_API_REMOVED_ERROR`）

---

## 6. 错误与重试兼容性（“跨 provider”差异必须落盘）

### 6.1 Responses：`response.failed` 的 delay 解析
Responses streaming 的 retry delay 主要来自 `response.failed` 的 error message 文案解析：
- OpenAI 风格：`Please try again in 28ms` / `... in 1.898s`
- Azure 风格：`Rate limit exceeded. Try again in 35 seconds.`

来源：
- 解析器：`codex-rs/codex-api/src/sse/responses.rs::try_parse_retry_after`
- 相关测试用例覆盖了上述两类文案

兼容性矩阵结论：
- provider 可能返回 `rate_limit_exceeded` 但文案不匹配以上模式 → delay=None，上层会走指数 backoff
- 只有 `code == "rate_limit_exceeded"` 才会尝试解析 delay

### 6.2 transport vs core 的重试分层
复刻实现必须分清：
- transport retry（HTTP 层）：由 `provider.retry` 驱动，负责重试 5xx/网络错误；默认不重试 429
- stream reconnect retry（应用层）：由 `stream_max_retries` + backoff + WS→HTTP fallback 驱动（详见 `RESPONSES_STREAMING.md` §5）

如果把两者合并，重试次数、回退时机与 UI “Reconnecting...” 语义将显著偏离。

---

## 7. “跨 provider / 跨模型”兼容性矩阵（可复刻决策表）

### 7.1 Provider 维度（默认值 + 必须显式声明的能力）
| Provider 类别 | wire_api | supports_websockets | 默认 store | RateLimit headers | ModelsEtag / reasoning_included / turn_state |
|---|---|---:|---:|---:|---|
| OpenAI（内置 openai） | responses | true | false | 可能有（取决于后端） | 可能有（headers 存在才生效） |
| OSS（ollama/lmstudio） | responses 或 chat | false | false | 基本不会 | 基本不会 |
| Azure（用户自定义） | responses（推荐） | 通常 false | true（自动检测） | 基本不会（非 codex bespoke） | 取决于实现；未提供则无注入 |

> 复刻提示：第三方 provider 如果要启用 WS，必须在 config.toml 明确 `supports_websockets=true`，且需要服务器真的提供 websocket endpoint（`wss://.../responses`）。

### 7.2 Model 维度（影响请求参数，而非 headers）
模型能力（由 `ModelInfo`/features 驱动）会影响：
- `parallel_tool_calls`（是否允许并行）
- `reasoning` 与 `include`（是否请求 reasoning summaries / encrypted_content）
- `text` controls（verbosity/output_schema）
- tool schema（例如 `apply_patch` 以 function 还是 freeform 形式）

这些属于“模型适配”，详见：
- `docs/workdocjcl/spec/04_Business_Logic/PROMPT_ASSEMBLY.md`
- `docs/workdocjcl/spec/05_Integrations/TOOLS_SCHEMA_REFERENCE.md`

## 来源（Source）
- `codex-rs/core/src/model_provider_info.rs`
- `codex-rs/core/src/client.rs`
- `codex-rs/codex-api/src/sse/responses.rs:383`
- `codex-rs/core/src/models_manager/model_info.rs`
