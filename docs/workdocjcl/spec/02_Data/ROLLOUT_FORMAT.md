# Rollout 文件格式（JSONL）

除了 `state.sqlite` 以外，Codex 还会把会话过程以“rollout”形式记录下来，用于：
- 会话恢复（resume/fork）
- 历史回放与诊断
- state.sqlite 的元数据抽取（state crate 从 rollout 读取并同步到 DB）

本章定义 rollout 的 **数据格式契约**。复刻时必须保证：
- 每行 JSON 的结构与 `RolloutLine`/`RolloutItem` 一致
- item 的 tag/字段名一致（serde tag/rename 规则）

> 仅有格式不足以复刻 `resume/fork` 与 state.sqlite 同步逻辑；语义见：`docs/workdocjcl/spec/02_Data/ROLLOUT_SEMANTICS.md`。

## 1. 顶层：`RolloutLine`
每一行是一个 JSON 对象，形如：
```json
{
  "timestamp": "2026-02-03T07:00:00Z",
  "type": "session_meta",
  "payload": { /* ... */ }
}
```

其中：
- `timestamp`: string（时间戳）
- `type` + `payload`: 由 `RolloutItem` 决定（采用 serde `tag = "type", content = "payload"` 且 `snake_case`）

## 2. `RolloutItem` 枚举（type 列表）
来源：`codex-rs/protocol/src/protocol.rs`

```text
type=session_meta   payload=SessionMetaLine
type=response_item  payload=ResponseItem
type=compacted      payload=CompactedItem
type=turn_context   payload=TurnContextItem
type=event_msg      payload=EventMsg
```

### 2.1 `session_meta`（会话级元数据）
payload：`SessionMetaLine`：
- `meta`（flatten）：`SessionMeta`
  - `id`: ThreadId
  - `forked_from_id`: optional ThreadId
  - `timestamp`: string
  - `cwd`: path
  - `originator`: string
  - `cli_version`: string
  - `source`: SessionSource（默认）
  - `model_provider`: optional string
  - `base_instructions`: optional BaseInstructions
  - `dynamic_tools`: optional [DynamicToolSpec]
- `git`: optional `GitInfo`（commit_hash/branch/repository_url）

复刻要点：
- `SessionMeta` 中不再保存 `instructions`（历史字段已移除）；当前把 user/developer instructions 放到 `turn_context`。

### 2.2 `turn_context`（某一轮 turn 的上下文快照）
payload：`TurnContextItem`：
- `cwd`
- `approval_policy`
- `sandbox_policy`
- `model`
- `personality?`
- `collaboration_mode?`
- `effort?` / `summary`
- `user_instructions?` / `developer_instructions?`
- `final_output_json_schema?`
- `truncation_policy?`

用途：保证恢复/回放时能重建当时的运行配置与约束。

### 2.3 `event_msg`（事件流）
payload：`EventMsg`（一个巨大的枚举，代表 UI/调用方看到的事件）。
复刻要点：
- rollout 记录必须能重放事件序列
- `AgentStatus` 等生命周期状态可从事件推导（见 `04_Business_Logic/STATE_MACHINES.md`）

### 2.4 `response_item`（模型输出 items）
payload：`ResponseItem`（模型响应项，包含 message、tool call 等）。

### 2.5 `compacted`（压缩记录）
payload：`CompactedItem`
- `message`: string（压缩后的摘要）
- `replacement_history?`: optional [ResponseItem]（用于替换历史）

## 3. 与 state.sqlite 的关系
`state` crate 的核心工作是：
- 扫描 rollout JSONL
- 提取 session/thread 元数据并同步到 `threads` 表
- 提取 logs/dynamic_tools 等并同步到对应表

因此复刻时必须保证：
- rollout 存在、可扫描
- schema 与 event semantics 足以推导 threads 表字段

## 4. 来源（Source）
- 类型定义：`codex-rs/protocol/src/protocol.rs#RolloutLine`、`codex-rs/protocol/src/protocol.rs#RolloutItem`、`codex-rs/protocol/src/protocol.rs#SessionMetaLine`、`codex-rs/protocol/src/protocol.rs#TurnContextItem`
- state 抽取：`codex-rs/state/src/extract.rs`、`codex-rs/state/src/runtime.rs`
