# Rollout 语义（Resume / Fork / Truncation / Metadata Extraction）

本文件补齐 `ROLLOUT_FORMAT.md` 未覆盖的“行为语义”：仅靠 JSONL 格式不足以复刻 `resume/fork` 与 state.sqlite 同步行为。

## 1. Rollout 的生成（写入）
实现入口：`codex-rs/core/src/rollout/recorder.rs::RolloutRecorder`

### 1.1 Rollout 文件命名与目录
创建逻辑：`create_log_file(config, conversation_id)`
- 根目录：`<CODEX_HOME>/sessions/`
- 子目录：按本地时间分层：`YYYY/MM/DD/`
- 文件名：
  - `rollout-{YYYY-MM-DDThh-mm-ss}-{conversation_id}.jsonl`
  - 其中时间分隔符用 `-` 代替 `:`（跨文件系统兼容）

### 1.2 写入单位：RolloutLine
每次写入会把 `RolloutItem` 包装为 `RolloutLine { timestamp, item }`（见 `codex_protocol::protocol::RolloutLine`），并按 JSONL 一行一条落盘。

### 1.3 持久化过滤（Persist policy）
**非常关键：rollout 文件不是“全事件日志”，而是经过过滤后的持久化子集。**写入端使用：
- `codex-rs/core/src/rollout/policy.rs::is_persisted_response_item(item: &RolloutItem) -> bool`

过滤语义（复刻必须一致）：
- `RolloutItem::SessionMeta(_)/TurnContext(_)/Compacted(_)`：**始终写入**
- `RolloutItem::ResponseItem(item)`：仅当 `should_persist_response_item(item)` 为真才写入
  - **写入**：`Message/Reasoning/LocalShellCall/FunctionCall/FunctionCallOutput/CustomToolCall/CustomToolCallOutput/WebSearchCall/GhostSnapshot/Compaction`
  - **不写入**：`ResponseItem::Other`
- `RolloutItem::EventMsg(ev)`：仅当 `should_persist_event_msg(ev)` 为真才写入
  - **写入**（用于 resume 后“回放 UI 状态”）：`UserMessage/AgentMessage/AgentReasoning/AgentReasoningRawContent/TokenCount/ContextCompacted/EnteredReviewMode/ExitedReviewMode/ThreadRolledBack/UndoCompleted/TurnAborted`
  - `EventMsg::ItemCompleted`：仅当 `item` 是 `TurnItem::Plan(_)` 才写入（plan item 生命周期不在 raw ResponseItem history 中）
  - **不写入**：大量纯 UI/stream 生命周期事件（如 `TurnStarted/TurnComplete/*Delta/RawResponseItem/...` 等）

> 复刻含义：如果你用“全量事件回放”替代过滤策略，会导致 rollout 体积与 resume 行为（尤其是 UI replay）显著偏离。

### 1.4 flush 与 shutdown
RolloutRecorder 内部是一个异步 writer task：
- `AddItems(Vec<RolloutItem>)`：追加写入
- `Flush`：确保之前所有写入落盘
- `Shutdown`：优雅停止

> 复刻要求：writer 必须是“按 item 顺序追加”的模型，否则回放与截断行为会偏离。

### 1.5 写入顺序与边界（SessionMeta first + 每行 flush）
rollout writer 线程的关键顺序约束：
- 若存在 `SessionMeta`：**必须写为文件第一条 item**（写入前会异步收集 git 信息并写入 `SessionMetaLine`）
- 后续所有 `AddItems`：对每个 item 做 persist policy 过滤；通过的 item **按提交顺序逐条写入**
- 每次写入会生成 UTC timestamp（带毫秒，`...Z`），并在写入后 flush（见 `JsonlWriter::write_rollout_item` / `write_line`）

> 复刻注意：该实现是“每行都 flush”，因此实现层面上是强一致/低吞吐的写入模型；如果复刻成批量缓冲写入，会导致崩溃恢复边界不同。

## 2. Resume（从 rollout 恢复会话）
入口：`codex-rs/core/src/thread_manager.rs::resume_thread_from_rollout`

### 2.1 加载历史
`RolloutRecorder::get_rollout_history(path)`：
1) `load_rollout_items(path)` 解析 JSONL 为 `Vec<RolloutItem>`
2) 从 rollout 文件名或内容解析 `thread_id`
3) 若 items 为空 → `InitialHistory::New`
4) 否则 → `InitialHistory::Resumed(ResumedHistory { conversation_id, history: items, rollout_path })`

> 复刻要点：`conversation_id` 来自解析出的 thread id；不是新生成。

### 2.2 record_initial_history：New / Resumed / Forked 的差异
入口：`codex-rs/core/src/codex.rs::Session::record_initial_history`

三种模式语义（必须按实现复刻，否则 resume/fork 的“历史 + 初始上下文”会偏离）：

**A) InitialHistory::New**
- 立即构建 `initial_context = build_initial_context(turn_context)`（developer instructions + collab + personality + user instructions + environment context）
- 调用 `record_conversation_items`：
  - 追加到内存历史（ContextManager）
  - 追加到 rollout（作为 ResponseItem）
  - 同时对 client 发 `RawResponseItem`（用于 UI 初始化）
- 设置 `state.initial_context_seeded = true`
- `flush_rollout()` 确保初始化项可被立即读取（测试/fork 依赖）

**B) InitialHistory::Resumed(ResumedHistory { history: rollout_items, ... })**
- 设置 `state.initial_context_seeded = false`（关键：延迟种子）
- “模型一致性警告”：
  - 若 rollout 中最后一个 `RolloutItem::TurnContext` 的 `model` 与当前 turn 的 model 不同 → 发送 `EventMsg::Warning(...)`
- 用 `reconstruct_history_from_rollout(turn_context, rollout_items)` 重建并写入内存 history（**不会复制/重写 rollout items**）
- 从 rollout 末尾回溯最近一次 `EventMsg::TokenCount` 的 `info`，写入 `state.token_info`（UI 能在 resume 时立即显示 token 计数）
- `flush_rollout()`；并明确注释：**延迟写入本次 session 的 initial context，直到第一轮 turn 开始**（用于合并 turn/start overrides 后再写）

> 复刻注意：resume 会话的 rollout 文件是“在原文件基础上继续 append”；并非创建新文件，也不会在 resume 时重写历史。

**C) InitialHistory::Forked(rollout_items)**
- 用 `reconstruct_history_from_rollout` 重建并写入内存 history
- 同样从 `TokenCount` 回溯，初始化 token_info（用于 UI）
- 若 `rollout_items` 非空：调用 `persist_rollout_items(&rollout_items)` 把“被截断后的历史”按原样写入新 rollout 文件（写入端仍会进行 persist policy 过滤）
- 然后追加“当前 session 的 initial_context”：
  - `record_conversation_items(initial_context)` → 内存 + rollout + RawResponseItem
- 设置 `state.initial_context_seeded = true`
- `flush_rollout()`（包含“历史复制 + initial context”）

> 复刻意义：fork 的新 rollout 文件同时包含“复制的历史（filtered）”与“fork 时刻的新初始上下文”，这会造成与原 session 在同一 turn 的 prompt 前缀不同（预期行为）。

### 2.3 seed_initial_context_if_needed：Resumed 的“首 turn 种子”
入口：`codex-rs/core/src/codex.rs::Session::seed_initial_context_if_needed`

语义：
- 这是一个**幂等的单次种子**：若 `state.initial_context_seeded` 已为真，直接 return。
- 若为假：先在锁内置为真（避免并发重复种子），然后：
  1) `initial_context = build_initial_context(turn_context)`
  2) `record_conversation_items(initial_context)`（会持久化到 rollout + 发 RawResponseItem）
  3) `flush_rollout()`

> 复刻注意：因为 resume 的历史 reconstruction 可能已经包含旧 session 的 initial context（尤其是发生过 compaction 的历史），所以 resume 后首 turn 会再次 append “新的 initial context”（这是实现设计的一部分，用于记录新的 policies/cwd/personality 等）。

### 2.4 reconstruct_history_from_rollout：从 rollout items 还原 prompt history
入口：`codex-rs/core/src/codex.rs::Session::reconstruct_history_from_rollout`

这是 resume/fork 能复刻对话的关键算法（必须按实现复刻）：

- 内部维护一个 `ContextManager history`
- 遍历 `rollout_items`，只处理三类：

**A) RolloutItem::ResponseItem(response_item)**
- 调用 `history.record_items(once(response_item), turn_context.truncation_policy)`
- 含义：重建时仍会应用当前 turn 的 truncation_policy（因此不同 model/context window 可能导致“重建后的 prompt”与原始录制时略有不同；这是实现选择）

**B) RolloutItem::Compacted(compacted)**
- 若 `compacted.replacement_history` 存在：`history.replace(replacement.clone())`
- 否则：按“live compaction”规则重建：
  1) `user_messages = collect_user_messages(history.raw_items())`
  2) `rebuilt = compact::build_compacted_history(build_initial_context(turn_context), &user_messages, compacted.message)`
  3) `history.replace(rebuilt)`

> 复刻注意：`collect_user_messages` 会过滤掉 session prefix（例如 AGENTS 指令块与 `<ENVIRONMENT_CONTEXT>`），并保留 `<turn_aborted>` marker；`build_compacted_history` 会在 token 上限内选择最近的 user messages，并追加一条“summary message”（role 仍为 user；空 summary 会变为 `(no summary available)`）。

**C) RolloutItem::EventMsg(EventMsg::ThreadRolledBack(rollback))**
- 调用 `history.drop_last_n_user_turns(rollback.num_turns)`
- 含义：回放时删除最近 N 个“用户 turn”（这与 fork 截断计数的 rollback 处理保持一致）

**其它 RolloutItem**
- 全部忽略（不会进入 prompt history）

输出：
- `history.raw_items().to_vec()`

### 2.5 回放一致性的边界（Fidelity limits）
由于 persist policy 的存在，rollout 中并不包含所有 UI/stream 生命周期事件，因此：
- “prompt 可复刻”（依赖 ResponseItem + Compacted + ThreadRolledBack）
- “UI replay 部分可复刻”（依赖被持久化的 EventMsg 子集，如 token_count、review mode、turn_aborted、plan item completion）
- “增量 streaming 生命周期不可复刻”（大量 `*Delta` / `TurnStarted/TurnComplete` / `RawResponseItem` 等不会被写入）

复刻实现如果需要做到“与原 UI 完全一致的回放”，必须在持久化层引入额外日志；但这将偏离当前仓库实现。

## 3. Fork（从历史截断并分叉）
入口：`codex-rs/core/src/thread_manager.rs::fork_thread`

参数：
- `nth_user_message: usize`：从起始处数第 N 个 user message（0-based），并 **在该条 user message 之前** 截断（不包含第 N 条 user message）
- `usize::MAX`：保留全量 rollout（不截断）

### 3.1 截断函数
`truncate_before_nth_user_message(history, n)`：
- 取 `items = history.get_rollout_items()`
- 调用 `truncate_rollout_before_nth_user_message_from_start(&items, n)`
- 若截断结果为空 → `InitialHistory::New`；否则 `InitialHistory::Forked(rolled)`

实现位置：`codex-rs/core/src/thread_manager.rs`

### 3.2 user message 边界判定（非常关键）
实现：`codex-rs/core/src/rollout/truncation.rs::user_message_positions_in_rollout`

判定规则：
- 仅当 rollout item 是：
  - `RolloutItem::ResponseItem(ResponseItem::Message { .. })`
  - 并且 `event_mapping::parse_turn_item(item)` 返回 `Some(TurnItem::UserMessage(_))`
  才视为“用户 turn 的边界”。

### 3.3 ThreadRolledBack 标记对截断计数的影响
rollout 可能包含：
- `RolloutItem::EventMsg(EventMsg::ThreadRolledBack(ThreadRolledBackEvent { num_turns }))`

语义：
- 该标记表示“有效 thread history”回滚了最后 N 个 user turns
- `user_message_positions_in_rollout` 会对已收集的 user_positions 做：
  - `user_positions.truncate(user_positions.len().saturating_sub(num_turns))`
- 因此 fork 时的 `nth_user_message` 计数是基于“应用 rollback 后”的有效用户历史，而不是 raw stream。

### 3.4 out-of-range 语义
实现：`truncate_rollout_before_nth_user_message_from_start`
- 若 `n_from_start == usize::MAX`：不截断，返回全量 items
- 若 user message 数量 `<= n_from_start`：返回空列表（视为 out of range）

## 4. state.sqlite 元数据抽取（rollout → ThreadMetadata）
state crate 的职责：把 rollout 的“可检索元数据”同步进 SQLite。

### 4.1 Apply 逻辑入口
实现：`codex-rs/state/src/extract.rs::apply_rollout_item(metadata, item, default_provider)`

分支（对 metadata 的影响）：
- `SessionMeta`：
  - 若 `metadata.id != meta_line.meta.id`：忽略（用于处理 forked rollouts 中嵌入的源 session_meta）
  - 否则更新：`id/source/model_provider/cwd/git_sha/git_branch/git_origin_url`
- `TurnContext`：更新 `cwd/sandbox_policy/approval_mode`
- `EventMsg`：
  - `TokenCount`：若存在 usage info → `tokens_used = total_tokens.max(0)`
  - `UserMessage`：标记 `has_user_event=true`；若 title 为空则从 message 中抽取 title
- `ResponseItem`：
  - 若是用户 Message：标记 `has_user_event=true`；若 title 为空则从文本抽取（忽略 local image 标签）
- `Compacted`：忽略（metadata 不更新）

兜底：
- 若 `metadata.model_provider` 为空 → 填入 `default_provider`

### 4.2 用户消息文本抽取（title）
实现：`extract_user_message_text(item)`：
1) 只处理 `ResponseItem::Message { role:"user", content }`
2) 从 content 中提取 `ContentItem::InputText.text`（忽略 InputImage/OutputText）
3) 过滤掉本地图片开闭标签（`is_local_image_open_tag_text` / `is_local_image_close_tag_text`）
4) 将剩余文本按 `\n` join
5) 去掉 `USER_MESSAGE_BEGIN` 之前的前缀（若存在），并 trim

## 5. 复刻检查清单（Replication checklist）
- 能生成与原实现相同目录结构/文件名的 rollout jsonl
- 能按顺序写入 RolloutLine（timestamp + item）
- 必须实现与当前版本一致的 persist policy（否则 rollout 尺寸与 resume 语义偏离）
- 能从 rollout 正确恢复 InitialHistory::Resumed（conversation_id + history + rollout_path）
- 必须按 `record_initial_history` 的 New/Resumed/Forked 差异处理“复制历史/延迟种子/追加 initial context”
- 必须按 `reconstruct_history_from_rollout` 规则处理 `ResponseItem/Compacted/ThreadRolledBack`（其余忽略）
- fork 截断必须使用与原实现一致的 “user message boundary” 判定规则
- 必须正确应用 ThreadRolledBack 标记，否则 fork/resume 的历史选择会偏离
- state 元数据抽取必须遵守 “只取 title 的第一条 user message（事件或 response）” 规则

## 6. 代码映射
- 写入：`codex-rs/core/src/rollout/recorder.rs`
- 持久化过滤：`codex-rs/core/src/rollout/policy.rs`
- fork/resume：`codex-rs/core/src/thread_manager.rs`
- resume/fork 初始上下文与 reconstruction：`codex-rs/core/src/codex.rs`（`record_initial_history` / `seed_initial_context_if_needed` / `reconstruct_history_from_rollout`）
- 截断：`codex-rs/core/src/rollout/truncation.rs`
- 元数据抽取：`codex-rs/state/src/extract.rs`
