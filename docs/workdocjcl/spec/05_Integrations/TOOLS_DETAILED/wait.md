# Tool: `wait` (function)

## 0. 目的
等待一个或多个 agent 到达“终态”（final status），并返回状态映射；可设置超时避免 busy polling。

## 1. 暴露/启用条件
仅当 `ToolsConfig.collab_tools == true`：
- push_spec：`create_wait_tool`
- handler：`builder.register_handler("wait", CollabHandler)`

## 2. 输入
schema：`codex-rs/core/src/tools/spec.rs::create_wait_tool`
解析类型：`codex-rs/core/src/tools/handlers/collab.rs::wait::WaitArgs`

字段：
- `ids`（必填，非空数组）：agent ids
- `timeout_ms`（可选）：等待超时（毫秒）
  - 默认 `DEFAULT_WAIT_TIMEOUT_MS=30000`
  - clamp 到 `[MIN_WAIT_TIMEOUT_MS=10000, MAX_WAIT_TIMEOUT_MS=300000]`

## 3. 运行时语义
handler：`CollabHandler` → `wait::handle`

步骤：
1) 校验 ids 非空
2) 解析 ids → `Vec<ThreadId>`
3) 校验 timeout：
   - `<=0` → 错误 `"timeout_ms must be greater than zero"`
   - 其他 → clamp 到 min/max
4) 发 begin 事件：`CollabWaitingBeginEvent`
5) 对每个 id 尝试 `agent_control.subscribe_status(id)`：
   - Ok(rx)：若当前 status 已是终态，记入 `initial_final_statuses`
   - ThreadNotFound：记录 status=NotFound
   - 其他错误：发 end 事件并返回错误
6) 若 `initial_final_statuses` 非空：直接使用它作为结果
7) 否则：并发等待“第一个到终态的 agent”：
   - 使用 `FuturesUnordered` + `timeout_at(deadline, futures.next())`
   - 如果在 deadline 前拿到至少一个终态结果，会额外 drain 一次 `now_or_never` 以避免竞态
8) 构造 `WaitResult { status: HashMap<ThreadId, AgentStatus>, timed_out: statuses.is_empty() }`
9) 发 end 事件：`CollabWaitingEndEvent`
10) 返回 JSON 字符串（注意：本 handler 设置 `success: None`）

## 4. 输出
`ToolOutput::Function { content: <JSON string>, success: None }`

JSON 形状（`WaitResult`）：
- `status`: { "<thread_id>": <AgentStatus enum> , ... }
- `timed_out`: bool

## 5. 代码映射
- tool spec：`codex-rs/core/src/tools/spec.rs::create_wait_tool`
- handler：`codex-rs/core/src/tools/handlers/collab.rs`（wait 模块）

