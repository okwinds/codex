# TUI：PasteBurst（非 bracketed paste 检测状态机）

本章给出 `PasteBurst` 的可复刻级规格：它用于解决“终端不提供 bracketed paste 事件时，paste 以高速 `Char`/`Enter` 键流形式到达”的问题。`PasteBurst` 本身**不修改 textarea**，它是一个纯状态机：调用方（`ChatComposer`）喂入事件并按返回决策去执行“插入/缓冲/flush/清理”。

目标行为：
- 避免 paste 触发 UI 短路副作用（例如 `?` 的快捷键提示切换）。
- 避免 paste 中途的 `Enter` 被当作“提交”而不是“换行”。
- 避免“先渲染一个 typed 前缀，随后又回滚为 paste”导致闪烁（flicker）。

---

## 1. 对外 API（调用约定）

### 1.1 输入事件分类（由调用方保证）
`PasteBurst` 只接收“plain char”路径：
- “plain”定义：无 Ctrl/Alt 修饰的 `KeyCode::Char(c)`（调用方负责筛选）。
- ASCII 与 non-ASCII 分为两条入口：
  - ASCII：`on_plain_char(ch, now) -> CharDecision`
  - non-ASCII/IME：`on_plain_char_no_hold(now) -> Option<CharDecision>`（不 holding 第一个字符）

非 plain 输入（箭头、Backspace、Ctrl/Alt 修饰、鼠标等）必须由调用方处理：
- 在应用会修改 textarea 的输入前：调用 `flush_before_modified_input()` 把“潜在 paste 文本”立刻取出并走统一 paste 通道。
- 之后调用 `clear_window_after_non_char()` 清掉分类窗口，避免后续输入被错误归类到之前的 burst。

### 1.2 flush（UI tick）
调用方需周期性（UI tick）调用：
- `flush_if_due(now) -> FlushResult`
  - `Paste(String)`：把 buffer 当作一次显式 paste（交给 composer 的 `handle_paste`）
  - `Typed(char)`：把“被 hold 的第一个 ASCII char”当作正常打字插入
  - `None`：没有到达超时阈值或无状态可 flush

### 1.3 Enter 处理（提交 vs 换行）
调用方在“用户按 Enter”时需要咨询：
- `append_newline_if_active(now) -> bool`：若 burst 处于 active，则把 `\n` 追加到 buffer 并返回 true（调用方不要提交消息）。
- `newline_should_insert_instead_of_submit(now) -> bool`：若处于 burst window（见 2.3），则 Enter 应插入换行而不是 submit。
- `extend_window(now)`：当调用方选择“Enter 插入换行”时，应延长 window（支持 paste 中的空行）。

---

## 2. 状态与时间模型（State/Timing）

### 2.1 内部状态字段（语义）
`PasteBurst` 的核心状态：
- `active: bool`：当前是否仍在“主动接收 burst 字符”。
- `buffer: String`：已累积的 burst 文本；即便 `active==false`，只要 buffer 非空仍视为“处于 burst 上下文”（例如继续 append）。
- `pending_first_char: Option<(char, Instant)>`：仅用于 ASCII 路径的 flicker suppression（短暂 hold 第一个快字符，不立即渲染）。
- `last_plain_char_time: Option<Instant>`：最近一次 plain char 的时间戳（用于超时 flush）。
- `consecutive_plain_char_burst: u16`：连续 plain char 的“burst 计数”（在 `PASTE_BURST_CHAR_INTERVAL` 内累计，否则重置为 1）。
- `burst_window_until: Option<Instant>`：Enter suppression window 的截止时间（即“短时间内 Enter 仍视为 paste 的换行”）。

### 2.2 阈值常量（必须等价）
- `PASTE_BURST_MIN_CHARS = 3`：达到该连续 plain char 计数时才可能判定为 paste-like。
- `PASTE_BURST_CHAR_INTERVAL = 8ms`：相邻 plain char 的最大间隔；也用于 hold 第一个 ASCII char 的最大等待时间。
- `PASTE_ENTER_SUPPRESS_WINDOW = 120ms`：burst 活动后保留的 Enter suppression window。
- `PASTE_BURST_ACTIVE_IDLE_TIMEOUT`：buffering 激活后“多久没收到新 char 就 flush 为 paste”：
  - 非 Windows：`8ms`
  - Windows：`60ms`（观察到更慢的 key 流）

### 2.3 “严格大于”超时比较
`flush_if_due()` 的超时判断使用 `now - last_plain_char_time > timeout`（严格 `>`，不是 `>=`）。  
因此测试与 UI tick 需要跨阈值至少 1ms：
- 推荐：`recommended_flush_delay() = PASTE_BURST_CHAR_INTERVAL + 1ms`
- buffering active 时推荐：`recommended_active_flush_delay() = PASTE_BURST_ACTIVE_IDLE_TIMEOUT + 1ms`（仅测试暴露）

---

## 3. ASCII 路径：holding + 快速进入 buffer

### 3.1 `on_plain_char(ch, now) -> CharDecision`
调用顺序：每次调用先执行 `note_plain_char(now)`（更新连续计数与时间戳）。

决策逻辑（按优先级）：
1) 若 `active==true`：
   - 设置 `burst_window_until = now + 120ms`
   - 返回 `BufferAppend`
2) 若存在 `pending_first_char=(held, held_at)` 且 `now - held_at <= 8ms`：
   - 进入 buffering：`active=true`
   - 清空 pending_first_char
   - 把 held 写入 `buffer.push(held)`
   - 设置 `burst_window_until = now + 120ms`
   - 返回 `BeginBufferFromPending`
3) 若 `consecutive_plain_char_burst >= 3`：
   - 返回 `BeginBuffer{ retro_chars = consecutive_plain_char_burst - 1 }`
   - 说明：该分支主要用于“未 hold 首字符的路径/retro-grab 场景”；ASCII 通常会在第 2 个快字符就进入 `BeginBufferFromPending`，因此该分支在正常 ASCII 流里较少触发，但仍必须实现。
4) 否则：
   - `pending_first_char = Some((ch, now))`
   - 返回 `RetainFirstChar`（调用方不应立刻把 ch 插入 textarea；等 flush 或进入 burst）

### 3.2 `RetainFirstChar` 的 flush 语义
若第一个 ASCII char 被 hold 且之后没有形成 burst，则在超时后：
- `flush_if_due(now)` 返回 `Typed(ch)`  
调用方应把该 char 当作正常输入插入 textarea（不是 paste）。

---

## 4. non-ASCII/IME 路径：不 hold，但允许 retro-capture

### 4.1 `on_plain_char_no_hold(now) -> Option<CharDecision>`
规则：
1) `note_plain_char(now)`
2) 若 `active==true`：设置 window，返回 `Some(BufferAppend)`
3) 若 `consecutive_plain_char_burst >= 3`：返回 `Some(BeginBuffer{retro_chars=...})`
4) 否则返回 `None`

关键差异：
- 该入口**不返回** `RetainFirstChar` / `BeginBufferFromPending`
- 调用方通常会先把 non-ASCII 字符插入 textarea（避免 IME 掉字感），一旦返回 `BeginBuffer{retro_chars}`，需走 `decide_begin_buffer` 做 retro-grab（见 5）

---

## 5. Retro-capture（retro-grab）机制

### 5.1 `retro_start_index(before, retro_chars) -> start_byte`
输入：
- `before: &str`：光标前的字符串片段（必须是合法 UTF-8 且光标已 clamp 到 char boundary）
- `retro_chars: usize`：要 retro-grab 的字符数（按字符，不按字节）

输出：
- `start_byte`：`before` 内的 byte index，使得 `before[start_byte..]` 包含“最后 retro_chars 个字符”（不足则从 0 开始）。

算法：`before.char_indices().rev().nth(retro_chars-1)` 定位；找不到则返回 0；retro_chars==0 则返回 `before.len()`。

### 5.2 `decide_begin_buffer(now, before, retro_chars) -> Option<RetroGrab>`
目的：当我们“后知后觉”认为键流像 paste 时，决定是否把已经插入 textarea 的前缀抓回到 buffer。

步骤：
1) 计算 `start_byte = retro_start_index(before, retro_chars)`
2) `grabbed = before[start_byte..].to_string()`
3) 判定 `looks_pastey`：
   - grabbed 含任意 whitespace，或
   - grabbed 字符数 >= 16
4) 若 looks_pastey：
   - 调用 `begin_with_retro_grabbed(grabbed, now)`：
     - 把 grabbed 追加到 buffer（非空才 push_str）
     - `active=true`
     - 设置 window
   - 返回 `Some(RetroGrab{start_byte, grabbed})`
5) 否则返回 None（不进入 buffering；避免短 IME burst 被误判）

> 调用方职责：若返回 Some(grab)，必须从 textarea 中删除 `[start_byte..cursor)` 对应片段，并继续把当前新字符追加进 buffer（以形成连续 paste 文本）。

---

## 6. flush / clear 的差异（必须区分）

### 6.1 `flush_if_due(now) -> FlushResult`
timeout 选择：
- 若 `is_active_internal()` 为 true（`active==true || !buffer.is_empty()`）：使用 `ACTIVE_IDLE_TIMEOUT`
- 否则：使用 `CHAR_INTERVAL`

超时后：
- 若 timed_out 且 `is_active_internal()==true`：
  - `active=false`
  - `out = take(buffer)`
  - 返回 `Paste(out)`
- 否则若 timed_out（即仅处于 pending_first_char）：
  - 若 `pending_first_char` 存在：take 并返回 `Typed(ch)`
  - 否则 `None`
- 未超时：`None`

### 6.2 `flush_before_modified_input() -> Option<String>`
用途：在应用“非 plain char 的 textarea mutation”前，立即把 burst 相关内容吐出来走统一 paste 路径，防止 buffer 卡住或状态泄漏。

规则：
- 若 `!is_active()`（既无 buffer/active，也无 pending_first_char）→ None
- 否则：
  - `active=false`
  - `out = take(buffer)`
  - 若存在 pending_first_char，则把该 char 追加到 out 的末尾（注意：这意味着“hold 的首字符”在此路径下会被当作 paste 内容的一部分）
  - 返回 Some(out)

### 6.3 `clear_window_after_non_char()`
用途：当非 plain key 被按下（或 Ctrl/Alt 修饰导致“这不是 paste 流”），清掉分类窗口，避免下一次输入被错误归到之前的 burst。

规则：
- 重置：`consecutive_plain_char_burst=0`、`last_plain_char_time=None`、`burst_window_until=None`、`active=false`、`pending_first_char=None`
- **不清空 buffer**（因此调用方必须先 flush buffer；否则 buffer 会“悬空”）

### 6.4 `clear_after_explicit_paste()`
用途：当终端提供了“显式 paste 事件”或调用方已把 burst flush 成一次 paste 并处理完毕后，用它彻底清空状态，确保 Enter suppression 不会影响后续真实 Enter。

规则：重置 timing/window/active，并 `buffer.clear()`，并清空 pending_first_char。

---

## 7. Enter suppression window

### 7.1 `append_newline_if_active(now)`
- 若 `is_active()==true`：`buffer.push('\n')`，window=now+120ms，返回 true
- 否则返回 false

### 7.2 `newline_should_insert_instead_of_submit(now)`
返回 true 当：
- `is_active()==true`，或
- `burst_window_until` 存在且 `now <= until`

含义：即使 buffer 已 flush（active=false、buffer 空），window 仍可能在短时间内有效，保证“稍晚到达的 Enter”仍被视为 paste 的换行。

---

## 8. 与 ChatComposer 的集成（复刻要求）

复刻时必须保持以下约束（在 `TUI_COMPOSER.md` 已描述，这里强调 PasteBurst 自身的契约）：
- 只有 plain char 进入 `on_plain_char`/`on_plain_char_no_hold`；含 Ctrl/Alt 的 Char 需要 `clear_window_after_non_char`。
- UI tick 必须调用 `flush_if_due`，否则 hold 的首字符可能永远不渲染。
- 任何可能清掉 timing window 的非 char 输入前，必须先 `flush_before_modified_input`（否则 buffer 可能无法依靠超时 flush）。
- 当发生显式 paste（`handle_paste`）后，必须 `clear_after_explicit_paste`。

---

## 9. 来源（Source）
- 状态机实现：`codex-rs/tui/src/bottom_pane/paste_burst.rs`
- 与 composer 的集成入口：`codex-rs/tui/src/bottom_pane/chat_composer.rs`
- 叙述性笔记（repo 内）：`docs/tui-chat-composer.md`

