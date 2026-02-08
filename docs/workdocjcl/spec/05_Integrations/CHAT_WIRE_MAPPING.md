# Chat wire 已移除（wire_api=chat）

本章描述 **当前仓库基准提交** 下 `wire_api = "chat"` 的真实状态：**已不再支持**。

复刻目标（必须满足）：
- 当用户在 provider 配置中设置 `wire_api = "chat"` 时，配置解析阶段直接失败（错误文案需一致）。
- 复刻者应把迁移路径写清楚：统一使用 `wire_api = "responses"`。

> 注：本仓库历史上曾存在 Chat Completions wire 兼容层。为了便于考古与对照，本文末尾保留了**已废弃**的 legacy 规格（不会被当前代码路径执行）。

---

## 1. 适用范围与非目标（以当前实现为准）

适用范围（当前实现）：
- provider config 解析：拒绝 `wire_api = "chat"`。
- 文档层迁移指引：如何切到 `responses`。

非目标（本章不展开）：
- 不再描述 Chat Completions 请求组装与 SSE 解析（因为当前代码不再走该路径）。

---

## 2. 来源（Source）

### 2.1 wire_api=chat 的移除与报错
- `codex-rs/core/src/model_provider_info.rs#CHAT_WIRE_API_REMOVED_ERROR`
- `codex-rs/core/src/model_provider_info.rs#WireApi`
- `codex-rs/core/src/model_provider_info.rs:52`

---

## 3. 当前行为（必须复刻）

### 3.1 错误文案（需要一致）

当 provider config 中出现 `wire_api = "chat"` 时，反序列化直接报错（完整字符串如下）：

```text
`wire_api = "chat"` is no longer supported.
How to fix: set `wire_api = "responses"` in your provider config.
More info: https://github.com/openai/codex/discussions/7782
```

---

## 4. Legacy（归档，仅供历史对照；当前实现不会执行）

以下内容为历史版本的 Chat wire 映射规格，保留用于考古/对照；若你要复刻**当前**仓库行为，可跳过本节余下部分。

### 3.1 Wire API 选择

`ModelClientSession::stream` 根据 provider 的 `wire_api` 选择：
- `WireApi::Responses`：走 Responses SSE / Responses WS（见 `RESPONSES_STREAMING.md`）。
- `WireApi::Chat`：走 Chat Completions SSE（本章）。

### 3.2 `show_raw_agent_reasoning` 对输出模式的影响

在 Chat wire 分支中：
- `config.show_raw_agent_reasoning = true`：使用 `api_stream.streaming_mode()`（尽量保留增量事件）。
- `config.show_raw_agent_reasoning = false`：使用 `api_stream.aggregate()`（对上层进行聚合）。

> 这不会改变 Chat SSE 解析的基础规则，只影响上层消费事件的聚合方式。

### 3.3 `output_schema` 不支持

`stream_chat_completions` 在 Chat wire 下明确拒绝 `prompt.output_schema`：
- 若 `prompt.output_schema.is_some()`：返回 `UnsupportedOperation("output_schema is not supported for Chat Completions API")`。

---

## 4. Chat 请求：headers + body 组装规格

### 4.1 输出：`ChatRequest`

请求组装输出为：
- `ChatRequest.body`：JSON（serde_json::Value）
- `ChatRequest.headers`：`http::HeaderMap`

### 4.2 固定字段

`body` 固定包含：
```json
{
  "model": "<model>",
  "messages": [...],
  "stream": true,
  "tools": [...]
}
```

其中：
- `model` 使用 `ChatRequestBuilder::new(model, ...)` 传入的 model 字符串
- `stream` 恒为 `true`
- `tools` 直接使用 `ChatRequestBuilder::new(..., tools)` 传入的 tools JSON 数组（tools 的生成规则在 core 层，非本章重点）

### 4.3 headers 规则

headers 在 `build_conversation_headers(conversation_id)` 的基础上追加：
- `session_id: <conversation_id>`（若 `conversation_id` 存在）
- `x-openai-subagent: <subagent>`（若 `session_source` 解析得出 subagent）

`x-openai-subagent` 的值来自 `subagent_header(session_source)`，典型取值如：
- `review`
- `compact`
- `collab_spawn`
- `Other(label)` → `label`

> 注：该 header 仅在 Chat 请求构建层插入；Responses wire 的 header 注入规则见其它章节。

---

## 5. messages 组装：总览

### 5.1 第一条消息：system instructions（必有）

messages 数组 **永远以 system message 开头**：
```json
{"role": "system", "content": "<instructions>"}
```

### 5.2 之后的输入来自 `Prompt.input: ResponseItem[]`

`ChatRequestBuilder` 对 `input: &[ResponseItem]` 做两阶段处理：
1) **Reasoning 预处理（attach 到某个 anchor index）**
2) **逐 item 生成 messages（Message / tool_call message / tool output）**

---

## 6. Reasoning 预处理与 attach 规则（逐分支）

Reasoning attach 的核心目标：把 `ResponseItem::Reasoning` 的文本内容，作为 `"reasoning"` 字段挂在某条 **assistant message** 或 **assistant(tool_calls) message** 上。

### 6.1 关键状态：`last_emitted_role`

先扫描整段 `input`，得到 `last_emitted_role`（最后一个“可发往 chat 的角色”）：
- `ResponseItem::Message { role, .. }` → `last_emitted_role = role`
- `ResponseItem::FunctionCall` / `ResponseItem::LocalShellCall` → `last_emitted_role = "assistant"`
- `ResponseItem::FunctionCallOutput` / `ResponseItem::CustomToolCallOutput` → `last_emitted_role = "tool"`
- 其它（`Reasoning`/`Other`/`CustomToolCall`/`WebSearchCall`/`GhostSnapshot`/`Compaction`）不改变 `last_emitted_role`

**门禁条件：**
- 仅当 `last_emitted_role != "user"` 时，才会执行后续的 reasoning attach 流程。

含义（复刻时必须保留）：如果输入以 user 结束，后续 reasoning 不会被 attach（因为本次 turn 的 assistant 尚未开始输出，避免把 reasoning 锚到错误位置）。

### 6.2 关键状态：`last_user_index`

第二次扫描 `input`，找到最后一个 `ResponseItem::Message { role == "user" }` 的 index，记为 `last_user_index`。

### 6.3 attach 范围门禁（跳过用户之前）

在执行 reasoning attach 时，遍历 `input` 的每个 `idx`：
- 若 `idx <= last_user_index`：**跳过**（不 attach）
- 仅考虑 `idx > last_user_index` 的 reasoning item

含义：只把“发生在最后一个 user 之后”的 reasoning attach 到 assistant/tool 侧输出，避免污染历史 user 之前的内容。

### 6.4 提取 reasoning 文本

对 `ResponseItem::Reasoning { content: Some(items), .. }`：
- 只识别两种 content entry：
  - `ReasoningItemContent::ReasoningText { text }`
  - `ReasoningItemContent::Text { text }`
- 把所有 entry 的 `text` **按顺序拼接**成一个字符串 `text`
- 若 `text.trim().is_empty()`：跳过

### 6.5 anchor 选择（优先级与分支）

对满足条件的 reasoning item（idx）按以下优先级选择 anchor：

1) **前一个 item 是 assistant message**
   - 若 `idx > 0` 且 `input[idx-1]` 是 `ResponseItem::Message { role == "assistant" }`
   - 则 attach 到 anchor `idx-1`

2) 否则（未 attach）且 **后一个 item 是 FunctionCall / LocalShellCall**
   - 若 `idx + 1 < len` 且 `input[idx+1]` 是 `ResponseItem::FunctionCall` 或 `ResponseItem::LocalShellCall`
   - 则 attach 到 anchor `idx+1`

3) 否则（仍未 attach）且 **后一个 item 是 assistant message**
   - 若 `idx + 1 < len` 且 `input[idx+1]` 是 `ResponseItem::Message { role == "assistant" }`
   - 则 attach 到 anchor `idx+1`

4) 否则：不 attach（丢弃该 reasoning）

### 6.6 多条 reasoning 拼接规则

`reasoning_by_anchor_index` 是 `HashMap<usize, String>`。

当多个 reasoning attach 到同一 anchor：
- 使用 `push_str` 直接拼接（**无分隔符**）

注意：这与 tool_call message 的 reasoning 拼接不同（见 8.3），后者会在已有 reasoning 非空时插入 `\n`。

---

## 7. `ResponseItem::Message` → chat message 映射（逐规则）

对 `ResponseItem::Message { role, content, .. }`：

### 7.1 content 扫描：文本拼接 + 可选多段结构

遍历 `content: Vec<ContentItem>`：
- 若是 `ContentItem::InputText { text }` 或 `ContentItem::OutputText { text }`
  - 将 `text` 追加到字符串 `text_acc`
  - 同时向 `items_acc` push：`{"type":"text","text": "<text>"}`
- 若是 `ContentItem::InputImage { image_url }`
  - 标记 `saw_image = true`
  - 向 `items_acc` push：`{"type":"image_url","image_url":{"url":"<image_url>"}}`

### 7.2 assistant 消息去重（必须保持）

若 `role == "assistant"`：
- 维护 `last_assistant_text: Option<String>`
- 如果 `last_assistant_text == text_acc`（完全相等）：**跳过**该 message（不生成 chat message）
- 否则：更新 `last_assistant_text = Some(text_acc.clone())` 并继续生成

该规则用于去除输入序列中“重复的 assistant 输出文本消息”。

### 7.3 最终 chat message 的 `content` 取值规则

`content_value` 的选择：
- 若 `role == "assistant"`：`content` **强制为字符串**（`text_acc`）
- 否则（非 assistant）：
  - 若 `saw_image == true`：`content` 为 **数组**（`items_acc`）
  - 否则：`content` 为字符串（`text_acc`）

因此：
- user + image → `content: [ {type:text...}, {type:image_url...} ]`
- assistant → 永远 `content: "<string>"`

### 7.4 reasoning 字段插入（仅 assistant）

若满足：
- `role == "assistant"`
- 且 `reasoning_by_anchor_index.contains_key(idx)`

则向该 chat message object 插入：
```json
{"reasoning": "<attached_reasoning_text>"}
```

---

## 8. Tool calls：`ResponseItem::*Call` → assistant(tool_calls) message

Chat Completions 要求：**所有 tool calls 必须被分组到一个 assistant message 中（`content:null`, `tool_calls:[...]`）**，并在其后用 `role:"tool"` 的 tool output messages 逐个响应。

### 8.1 `ResponseItem::FunctionCall`

输入：
- `name: String`
- `arguments: String`（JSON 字符串）
- `call_id: String`

映射为 tool_call object：
```json
{
  "id": "<call_id>",
  "type": "function",
  "function": { "name": "<name>", "arguments": "<arguments>" }
}
```

并调用 `push_tool_call_message(messages, tool_call, reasoning_opt)`。

其中 `reasoning_opt` 来自 `reasoning_by_anchor_index.get(idx)`。

### 8.2 `ResponseItem::LocalShellCall`

输入字段：
- `id: Option<String>`（注意：这里使用 `id`，而不是 `call_id`）
- `status`
- `action`

映射为 tool_call object：
```json
{
  "id": "<id_or_empty_string>",
  "type": "local_shell_call",
  "status": "<status>",
  "action": "<action>"
}
```

并调用 `push_tool_call_message(messages, tool_call, reasoning_opt)`。

> 重要：`id` 缺失时使用空字符串（`unwrap_or_default()`），这会影响 tool 输出与 tool_call 的关联能力（复刻必须保持这一行为）。

### 8.3 `ResponseItem::CustomToolCall`

输入字段：
- `id`
- `name`
- `input`（JSON value）

映射为 tool_call object：
```json
{
  "id": "<id>",
  "type": "custom",
  "custom": { "name": "<name>", "input": <input_json> }
}
```

并调用 `push_tool_call_message(messages, tool_call, reasoning_opt)`。

### 8.4 `push_tool_call_message`：分组与 reasoning 合并规则

该函数实现“连续 tool calls 合并到同一条 assistant message”的逻辑：

如果 `messages` 的最后一条满足：
- `role == "assistant"`
- `content == null`
- 存在 `tool_calls` 数组

则：
- 向该 `tool_calls` 数组 append 新的 `tool_call`
- 若本次 `reasoning_opt` 存在：
  - 若已有 `"reasoning": "<existing>"` 且 existing 非空：先追加 `\n` 再追加新 reasoning
  - 否则直接设置 `"reasoning": "<reasoning>"`

否则（最后一条不是 tool_calls message）：
- 新建一条 assistant message：
```json
{
  "role": "assistant",
  "content": null,
  "tool_calls": [ <tool_call> ],
  "reasoning": "<optional_reasoning>"
}
```

---

## 9. Tool outputs：`ResponseItem::*CallOutput` → role=tool messages

### 9.1 `ResponseItem::FunctionCallOutput`

输出 chat message：
```json
{
  "role": "tool",
  "tool_call_id": "<call_id>",
  "content": <content_value>
}
```

其中 `content_value` 的选择：
- 若 `output.content_items: Option<Vec<FunctionCallOutputContentItem>>` 存在：
  - 映射为数组：
    - `InputText { text }` → `{"type":"text","text":"<text>"}`
    - `InputImage { image_url }` → `{"type":"image_url","image_url":{"url":"<url>"}}`
- 否则：`content_value = output.content`（字符串）

### 9.2 `ResponseItem::CustomToolCallOutput`

输出 chat message：
```json
{
  "role": "tool",
  "tool_call_id": "<call_id>",
  "content": <output_json>
}
```

其中 `<output_json>` 原样使用 `ResponseItem::CustomToolCallOutput.output`（serde_json::Value）。

---

## 10. 被忽略/不下发的输入 item 类型（必须保持）

以下 `ResponseItem` 在 Chat 请求组装中不会生成任何 chat message（即“丢弃”）：
- `ResponseItem::GhostSnapshot`
- `ResponseItem::Reasoning`（仅参与 attach 预处理，**自身不下发**）
- `ResponseItem::WebSearchCall`
- `ResponseItem::Other`
- `ResponseItem::Compaction`

> 复刻提醒：如果你的实现把这些类型也下发到 Chat messages，将导致与原实现不一致（上游模型上下文变化）。

---

## 11. Chat SSE 解析：事件到 `ResponseEvent` 的映射规格

### 11.1 SSE 输入与 idle timeout

解析器持续从 `eventsource_stream` 读取 SSE events：
- 若 `idle_timeout` 内没有新 event：发送 `ApiError::Stream("idle timeout waiting for SSE")` 并终止。
- 若底层 stream 结束（`Ok(None)`）：若尚未发送完成事件，执行“flush + completed”并返回。

### 11.2 终止哨兵：`[DONE]` 与 `DONE`（必须支持二者）

当 `data.trim()` 等于：
- `"[DONE]"` 或
- `"DONE"`

解析器立刻执行 `flush_and_complete` 并返回。

flush_and_complete 的行为：
1) 若存在未完成的 reasoning item：发送 `ResponseEvent::OutputItemDone(reasoning_item)`
2) 若存在未完成的 assistant item：发送 `ResponseEvent::OutputItemDone(assistant_item)`
3) 发送 `ResponseEvent::Completed { response_id: "", token_usage: None }`

> 设计动机：某些 mock server 在发送 `[DONE]` 后仍保持连接不关闭；因此不能依赖“HTTP 连接关闭”来触发 Completed。

### 11.3 JSON 解析失败的处理

对非空且非哨兵的 `data`：
- 尝试 `serde_json::from_str(data)`
- 若解析失败：记录 debug 日志并 `continue`（跳过该 event，不终止）

### 11.4 解析 choices：delta 与 message.reasoning

若 JSON 顶层没有 `choices: array`：跳过。

对每个 `choice`：

#### (a) `choice.delta.reasoning`

如果 `delta.reasoning` 存在，按以下优先级提取字符串：
1) `reasoning` 是字符串
2) `reasoning.text` 是字符串
3) `reasoning.content` 是字符串

每取到一个片段 `text`，调用 `append_reasoning_text(text)`：
- 如果这是首次出现 reasoning：
  - 创建 `ResponseItem::Reasoning { id:"", summary:[], content: Some([]), encrypted_content: None }`
  - 发送 `ResponseEvent::OutputItemAdded(reasoning_item)`
- 每个片段都会：
  - 向 reasoning.content 追加 `ReasoningText { text }`
  - 发送 `ResponseEvent::ReasoningContentDelta { delta: text, content_index }`

#### (b) `choice.delta.content`

如果 `delta.content` 存在：
- 若是数组：对每个 item 取 `item.text`（字符串）并追加到 assistant
- 若是字符串：直接追加到 assistant

追加通过 `append_assistant_text(text)`：
- 如果这是首次出现 assistant 文本：
  - 创建 `ResponseItem::Message { role:"assistant", content: [], ... }`
  - 发送 `ResponseEvent::OutputItemAdded(assistant_item)`
- 每个片段都会：
  - 向 assistant.content 追加 `ContentItem::OutputText { text }`
  - 发送 `ResponseEvent::OutputTextDelta(text)`

#### (c) `choice.message.reasoning`

除了 delta.reasoning，解析器也会检查 `choice.message.reasoning`（同样按字符串/text/content 三种形式提取）并追加到 reasoning item。

### 11.5 tool_calls delta：拼接状态机与 flush 规则

解析器维护一个 tool_calls 状态机（按“tool call index”聚合）：
- `tool_calls: HashMap<usize, ToolCallState { id, name, arguments }>`
- `tool_call_order: Vec<usize>`（按首次看到的顺序）
- `tool_call_index_by_id: HashMap<String, usize>`（id → index，用于跨 event 复用 index）
- `last_tool_call_index: Option<usize>`（用于缺失 index/id 的兜底）

对 `delta.tool_calls: array` 中每个 tool_call：
1) 首选 `tool_call.index`（u64 → usize）作为 index
2) 若 `tool_call.id` 存在且已在 `tool_call_index_by_id` 中出现过：复用该既有 index（覆盖 1）
3) 若 index 缺失且 id 也缺失：使用 `last_tool_call_index`
4) 若仍无 index：分配一个新的 index（跳过已占用的 index；从 `next_tool_call_index` 递增）

聚合字段：
- `id`：首次出现时记录
- `function.name`：若非空且此前未记录则记录
- `function.arguments`：如果存在字符串片段，**按出现顺序追加**（允许跨 delta 拼接）

最后更新 `last_tool_call_index = Some(index)`。

#### tool_calls flush（finish_reason = "tool_calls"）

当 `choice.finish_reason == "tool_calls"`：
1) 若有 reasoning_item：先发送 `OutputItemDone(reasoning_item)`（并清空）
2) 依 `tool_call_order` 的顺序逐个取出 ToolCallState，生成 `ResponseItem::FunctionCall` 并发送 `OutputItemDone`：
   - `name` 必须存在，否则 debug 并跳过该 call
   - `call_id`：
     - 优先使用 ToolCallState.id
     - 否则使用 `format!("tool-call-{index}")`
   - `arguments` 使用已拼接的 arguments 字符串
3) 继续等待后续 SSE（不会在此处自动发送 Completed）

> 注意：Chat SSE 解析器把 tool_calls 统一转换为 `ResponseItem::FunctionCall`（不会产生 `LocalShellCall` / `CustomToolCall`）。

### 11.6 finish_reason 处理

- `finish_reason == "stop"`：
  - 若有 reasoning_item：发送 `OutputItemDone`
  - 若有 assistant_item：发送 `OutputItemDone`
  - 若尚未发送 completed：发送 `ResponseEvent::Completed { response_id:"", token_usage: None }`，并标记 `completed_sent = true`
- `finish_reason == "length"`：发送 `ApiError::ContextWindowExceeded` 并终止
- 其它/缺失：继续读取 SSE

---

## 12. ChatClient endpoint 与聚合层（AggregatedStream）

本节补齐 `codex-rs/codex-api/src/endpoint/chat.rs` 中的“请求路径选择”与“流聚合”语义。它们决定了：
- HTTP path 是否为 `chat/completions`
- 上层收到的 `ResponseEvent` 序列是否被“合并成单条 assistant message per turn”

### 12.1 HTTP path 选择

`ChatClient::path()`：
- 当 provider wire 为 `WireApi::Chat`：返回 `"chat/completions"`
- 否则：返回 `"responses"`

> 复刻边界：在 core 路由中，只有 `WireApi::Chat` 才会走 `ApiChatClient`，但 `ChatClient` 仍保留该分支。复刻实现应保持一致，避免未来切换 wire 时行为漂移。

### 12.2 StreamingClient 调用参数（必须保持）

`ChatClient::stream(body, extra_headers)` 通过 `StreamingClient::stream(...)` 发起请求，关键固定参数：
- `RequestCompression::None`（Chat wire 不启用请求压缩）
- SSE parser factory：`spawn_chat_stream`

### 12.3 AggregateMode 与事件序列变换

上层对 `ResponseStream` 的消费模式由 `AggregateStreamExt` 决定：
- `ResponseStream::streaming_mode()`：直接透传（不做聚合）
- `ResponseStream::aggregate()`：包装为 `AggregatedStream`，模式为 `AggregateMode::AggregatedOnly`

core 的选择规则见本章 §3.2（`show_raw_agent_reasoning`）。

### 12.4 `AggregatedStream` 聚合规则（逐事件）

`AggregatedStream` 的目标：把一整个 turn 的增量输出（text + reasoning）聚合为：
- （可选）1 条 `ResponseItem::Reasoning` done
- （可选）1 条 `ResponseItem::Message(role="assistant")` done
- 最后 1 条 `ResponseEvent::Completed`

内部状态：
- `cumulative: String`：累计 assistant 文本 delta
- `cumulative_reasoning: String`：累计 reasoning delta
- `pending: VecDeque<ResponseEvent>`：在某些分支中用于“先入队再吐出”
- `mode: AggregateMode`

事件处理（关键分支）：

1) `ResponseEvent::OutputTextDelta(delta)`
   - 永远 `cumulative += delta`
   - 若 `mode == Streaming`：向上游继续透传 `OutputTextDelta(delta)`
   - 若 `mode == AggregatedOnly`：不透传

2) `ResponseEvent::ReasoningContentDelta { delta, content_index }`
   - 永远 `cumulative_reasoning += delta`
   - 若 `mode == Streaming`：透传原事件
   - 若 `mode == AggregatedOnly`：不透传

3) `ResponseEvent::OutputItemDone(item)`
   - 如果 `item` 是 `ResponseItem::Message(role="assistant")`：
     - `AggregateMode::AggregatedOnly`：
       - 如果 `cumulative` 仍为空，并且该 item 的 content 中存在第一个 `ContentItem::OutputText { text }`：
         - 把该 text 复制进 `cumulative`
       - 无论是否复制，都 **吞掉该 OutputItemDone**（不向上游输出）
     - `AggregateMode::Streaming`：
       - 若 `cumulative` 为空：透传该 OutputItemDone（意味着上游已经拿到了完整 assistant message）
       - 若 `cumulative` 非空：吞掉（避免出现“既有 delta 又有 done message”的重复）
   - 非 assistant message 的 OutputItemDone：直接透传

4) `ResponseEvent::Completed { response_id, token_usage }`
   - 如果 `cumulative_reasoning` 非空：
     - 生成并入队一个聚合后的 `ResponseItem::Reasoning` done，其中 content 只含 1 条 `ReasoningText{text:<cumulative_reasoning>}`
   - 如果 `cumulative` 非空：
     - 生成并入队一个聚合后的 `ResponseItem::Message(role="assistant")` done，其中 content 只含 1 条 `OutputText{text:<cumulative>}`
   - 如果上述任一入队发生（emitted_any=true）：
     - 再入队一条 Completed（同 response_id/token_usage）
     - 然后从 `pending` pop 第一条返回
   - 如果没有任何累计内容（两者都空）：
     - 直接透传原 Completed

5) 其它事件：
   - `Created`：吞掉（continue）
   - `ServerReasoningIncluded/RateLimits/ModelsEtag/OutputItemAdded`：透传
   - `ReasoningSummaryDelta/ReasoningSummaryPartAdded`：吞掉

> 复刻提醒：`AggregatedStream` 只聚合“delta”类的文本与 reasoning；tool_calls 在 Chat SSE 中会被解析成 `ResponseItem::FunctionCall` 的 done 事件，属于 OutputItemDone 的“非 assistant message”分支，会被直接透传。

## 13. 最小示例（用于复刻自测）

### 12.1 user 含图片（messages.content 为数组）

输入（抽象）：
- system instructions：`"inst"`
- `ResponseItem::Message(role="user", content=[InputText("look"), InputImage("https://...")])`

输出 messages（省略 tools 等字段）：
```json
[
  {"role":"system","content":"inst"},
  {"role":"user","content":[
    {"type":"text","text":"look"},
    {"type":"image_url","image_url":{"url":"https://..."}}
  ]}
]
```

### 12.2 连续 FunctionCall 合并为单条 assistant(tool_calls)

输入顺序：
1) user message
2) FunctionCall(call-a)
3) FunctionCall(call-b)
4) FunctionCallOutput(call-a)
5) FunctionCallOutput(call-b)

输出 messages（核心结构）：
```json
[
  {"role":"system","content":"..."},
  {"role":"user","content":"..."},
  {"role":"assistant","content":null,"tool_calls":[
    {"id":"call-a","type":"function","function":{"name":"...","arguments":"..."}},
    {"id":"call-b","type":"function","function":{"name":"...","arguments":"..."}}
  ]},
  {"role":"tool","tool_call_id":"call-a","content":"..."},
  {"role":"tool","tool_call_id":"call-b","content":"..."}
]
```
