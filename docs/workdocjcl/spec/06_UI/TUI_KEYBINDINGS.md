# TUI：Keybindings（全局按键与路由）复刻级规格（阶段一）

本章目标：以“可复刻交互语义”为准，描述 Codex TUI 的**按键路由优先级**与若干关键全局快捷键/overlay 导航键。

> 说明：TUI keybindings 体量非常大（涉及 composer、slash popup、review、skills、resume picker 等）。本章先把“全局路由 + overlay/pager/backtrack + approvals”闭环写清；其余弹窗与输入框快捷键会在后续章节继续补齐。

相关章节：
- 审批弹窗快捷键：`docs/workdocjcl/spec/06_UI/TUI_APPROVALS.md`
- 审批系统语义：`docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`

---

## 1. 按键事件路由优先级（App 层）

实现入口：`codex-rs/tui/src/app.rs:handle_tui_event` → `handle_key_event`

### 1.1 Overlay 优先（Alt screen）
当 `self.overlay.is_some()`：
- 所有 `TuiEvent` 都交给 `handle_backtrack_overlay_event(tui, event)` 处理
- `handle_backtrack_overlay_event` 会：
  - 在 transcript overlay 上支持 backtrack preview（Esc/Left/Right/Enter）
  - 否则把事件转发给 overlay widget（`overlay_forward_event`）
  - overlay widget 标记 done 后会 `leave_alt_screen()` 并关闭 overlay

来源：
- `codex-rs/tui/src/app.rs:handle_tui_event`
- `codex-rs/tui/src/app_backtrack.rs:handle_backtrack_overlay_event` / `overlay_forward_event` / `close_transcript_overlay`

### 1.2 非 overlay 时：App 级全局快捷键优先
当没有 overlay：
- `Ctrl+T`：打开 transcript overlay（Alt screen）
- `Ctrl+G`：尝试启动外部编辑器（需满足若干安全条件）
- `Esc`：在“正常 backtrack 模式”下用于 backtrack priming/advance，否则下发给 ChatWidget（让 bottom pane/弹窗/popup 自行处理）
- `Enter`：当 backtrack 已 primed 且有有效选择且 composer 为空时，确认 backtrack 并提交 rollback；否则下发给 ChatWidget
- 其它按键：下发给 ChatWidget；此外，任意非 Esc 键会取消 primed backtrack

来源：
- `codex-rs/tui/src/app.rs:handle_key_event`

---

## 2. 全局快捷键（主界面）

### 2.1 `Ctrl+T`：打开 transcript overlay（全屏历史）
触发：`KeyCode::Char('t') + Ctrl`（Press）

效果：
- `tui.enter_alt_screen()`
- `self.overlay = Some(Overlay::new_transcript(self.transcript_cells.clone()))`

关闭（在 overlay 内）：
- `q` / `Ctrl+C` / `Ctrl+T`（详见 §3.2）

来源：
- `codex-rs/tui/src/app.rs:handle_key_event`
- `codex-rs/tui/src/pager_overlay.rs:TranscriptOverlay::handle_event`

### 2.2 `Ctrl+G`：启动外部编辑器（External editor）
触发：`KeyCode::Char('g') + Ctrl`（Press）

前置条件（必须同时满足）：
- 当前没有 overlay
- bottom pane 允许 launch 外部编辑器（`chat_widget.can_launch_external_editor()`）
- 外部编辑器状态为 `Closed`

来源：
- `codex-rs/tui/src/app.rs:handle_key_event`
- `codex-rs/tui/src/bottom_pane/mod.rs:can_launch_external_editor`

### 2.3 `Esc` / `Enter`：Backtrack（主界面）

#### Esc：priming/advance
触发：`Esc`（Press 或 Repeat）

仅当满足“正常 backtrack 模式”才由 App 消费：
- `chat_widget.is_normal_backtrack_mode()` 为 true
- 且 `chat_widget.composer_is_empty()` 为 true

否则：直接转发给 `chat_widget.handle_key_event`（让弹窗/选择器/输入框消费 Esc）。

#### Enter：确认 backtrack
触发：`Enter`（Press）

仅当满足：
- `self.backtrack.primed == true`
- 且 `self.backtrack.nth_user_message != usize::MAX`（存在有效选择）
- 且 composer 为空

才会：
- `confirm_backtrack_from_main()` 并 `apply_backtrack_selection(...)`（提交 rollback Op）

#### 取消规则
任何非 Esc 的按键（Press 或 Repeat）都会取消 primed backtrack（避免“用户开始打字后仍然处于 Esc-primed 状态”）。

来源：
- `codex-rs/tui/src/app.rs:handle_key_event`
- `codex-rs/tui/src/app_backtrack.rs:handle_backtrack_esc_key` / `confirm_backtrack_from_main`

---

## 3. Overlay（Alt screen）键位与行为

Overlay 类型定义：`codex-rs/tui/src/pager_overlay.rs:Overlay`
- `Overlay::Transcript`：transcript overlay（Ctrl+T）
- `Overlay::Static`：静态 pager overlay（例如审批弹窗 Ctrl+A 全屏查看）

### 3.1 Pager 导航键（PagerView）
适用于 transcript/static 两种 overlay 的滚动导航（由 `PagerView::handle_key_event` 定义）：

| 动作 | 按键 |
|---|---|
| 上滚 1 行 | `Up` / `k` |
| 下滚 1 行 | `Down` / `j` |
| 上翻页 | `PageUp` / `Shift+Space` / `Ctrl+B` |
| 下翻页 | `PageDown` / `Space` / `Ctrl+F` |
| 下滚半页 | `Ctrl+D` |
| 上滚半页 | `Ctrl+U` |
| 跳到顶部 | `Home` |
| 跳到底部 | `End` |

来源：
- `codex-rs/tui/src/pager_overlay.rs:PagerView::handle_key_event`

### 3.2 Overlay 退出键

#### Static overlay（审批全屏查看等）
退出：`q` 或 `Ctrl+C`

来源：
- `codex-rs/tui/src/pager_overlay.rs:StaticOverlay::handle_event`

#### Transcript overlay（Ctrl+T）
退出：`q` 或 `Ctrl+C` 或 `Ctrl+T`

来源：
- `codex-rs/tui/src/pager_overlay.rs:TranscriptOverlay::handle_event`

### 3.3 Transcript overlay 内的 backtrack preview（Esc/Left/Right/Enter）
当 transcript overlay 打开时，App 会在 `handle_backtrack_overlay_event` 中提供额外的 backtrack preview 层：

1. 若尚未进入 preview：
   - `Esc`（Press/Repeat）开始 preview，并默认选中“最新用户消息”
2. 在 preview 中：
   - `Esc` 或 `Left`：向更旧的用户消息移动选择
   - `Right`：向更新的用户消息移动选择
   - `Enter`：确认选择并触发 rollback（同时关闭 overlay）
3. 其它事件：转发给 overlay（继续可滚动浏览）

来源：
- `codex-rs/tui/src/app_backtrack.rs:handle_backtrack_overlay_event`

---

## 4. 审批弹窗快捷键（引用）
审批弹窗（ApprovalOverlay）的快捷键、队列语义（LIFO）、Ctrl+A 全屏查看、Ctrl+C abort 等详见：
- `docs/workdocjcl/spec/06_UI/TUI_APPROVALS.md`

## 来源（Source）
- `codex-rs/tui/src/app.rs`
- `codex-rs/tui/src/pager_overlay.rs`
- `codex-rs/tui/src/app_backtrack.rs`
