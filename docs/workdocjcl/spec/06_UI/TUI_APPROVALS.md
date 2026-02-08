# TUI：审批弹窗（Approval Overlay）复刻级规格

本章目标：复刻 Codex TUI 在收到 core 的审批事件后，如何：
- 将事件转化为 UI 弹窗（bottom pane modal）
- 展示命令/变更/原因
- 提供快捷键与选项（Approved / ApprovedForSession / ApprovedExecpolicyAmendment / Abort）
- 将用户选择回传为 `Op::*Approval`（驱动 core 继续执行或中断）
- 支持全屏查看（Alt screen pager overlay）

> 协议层/编排器层的审批语义（缓存、sandbox deny 重试、ReviewDecision）见：
> - `docs/workdocjcl/spec/07_Infrastructure/APPROVALS.md`
> - `docs/workdocjcl/spec/07_Infrastructure/EXEC_POLICY.md`（proposed_execpolicy_amendment 来源）

---

## 1. 事件入口：ChatWidget 接收审批事件

TUI 事件分发点：`codex-rs/tui/src/chatwidget.rs:dispatch_event_msg(...)`

当收到：
- `EventMsg::ExecApprovalRequest(ev)` → `on_exec_approval_request(id, ev)`
- `EventMsg::ApplyPatchApprovalRequest(ev)` → `on_apply_patch_approval_request(id, ev)`
- `EventMsg::ElicitationRequest(ev)` → `on_elicitation_request(ev)`

### 1.1 中断队列（InterruptManager）与“延迟处理”
ChatWidget 为避免在流式输出/活跃 cell 更新期间打乱事件顺序，使用 `defer_or_handle(...)`：
- 若当前正在流式输出（`stream_controller.is_some()`）**或** 已经有 queued interrupts：
  - 将审批事件 push 进 `InterruptManager.queue`（FIFO：VecDeque）
- 否则立即处理

流式结束时（`handle_stream_finished`）会 `flush_interrupt_queue()`，将 queued interrupts 按 FIFO 顺序依次执行：
- `QueuedInterrupt::ExecApproval` → `handle_exec_approval_now`
- `QueuedInterrupt::ApplyPatchApproval` → `handle_apply_patch_approval_now`
- `QueuedInterrupt::Elicitation` → `handle_elicitation_request_now`

来源：
- `codex-rs/tui/src/chatwidget.rs:defer_or_handle`、`flush_interrupt_queue`
- `codex-rs/tui/src/chatwidget/interrupts.rs`

---

## 2. 将事件转为 bottom pane 的 ApprovalRequest

### 2.1 Exec approval
`ChatWidget::handle_exec_approval_now(id, ev)`：
1. `flush_answer_stream_with_separator()`：把正在流的回答收束，确保审批弹窗与输出分隔清晰
2. 发送通知 `Notification::ExecApprovalRequested { command }`：
   - `command` 用 `shlex::try_join(ev.command)` 渲染；失败则 `join(" ")`
3. 构造 `ApprovalRequest::Exec { id, command, reason, proposed_execpolicy_amendment }`
4. 调用 `bottom_pane.push_approval_request(request, &features)`

来源：
- `codex-rs/tui/src/chatwidget.rs:handle_exec_approval_now`
- 通知：`codex-rs/tui/src/chatwidget.rs:Notification::*`

### 2.2 ApplyPatch approval
`ChatWidget::handle_apply_patch_approval_now(id, ev)`：
1. `flush_answer_stream_with_separator()`
2. 构造 `ApprovalRequest::ApplyPatch { id, reason, changes, cwd }`
   - 注意：这里的 `cwd` 使用 TUI 的 `config.cwd`（不是事件里的 cwd 字段）
3. `bottom_pane.push_approval_request(...)`
4. 发送通知 `Notification::EditApprovalRequested { cwd, changes(paths) }`

### 2.3 MCP elicitation approval
`ChatWidget::handle_elicitation_request_now(ev)`：
1. `flush_answer_stream_with_separator()`
2. 通知 `Notification::ElicitationRequested { server_name }`
3. 构造 `ApprovalRequest::McpElicitation { server_name, request_id, message }`
4. `bottom_pane.push_approval_request(...)`

---

## 3. BottomPane：弹窗栈与“请求合并”

入口：`codex-rs/tui/src/bottom_pane/mod.rs:push_approval_request`

算法：
1. 若当前 bottom pane 已有活动 view（`view_stack.last_mut()`）：
   - 调用该 view 的 `try_consume_approval_request(request)`
   - 若返回 `None`：代表已被 view 消费（例如当前已在审批弹窗中，则将请求排队到弹窗内部队列）
   - 若返回 `Some(request)`：代表 view 不消费，继续走创建新弹窗逻辑
2. 若未被消费：创建新的 `ApprovalOverlay::new(request, ...)`，并：
   - `pause_status_timer_for_modal()`
   - `push_view(modal)`

重要结论：
- 当审批弹窗已经打开时，新来的审批请求**不会再打开第二个弹窗**，而是进入弹窗内部队列（见 §4.5）。

来源：
- `codex-rs/tui/src/bottom_pane/mod.rs:push_approval_request`
- `codex-rs/tui/src/bottom_pane/approval_overlay.rs:impl BottomPaneView for ApprovalOverlay`

---

## 4. ApprovalOverlay：UI 展示、选项、快捷键与输出

实现：`codex-rs/tui/src/bottom_pane/approval_overlay.rs`

### 4.1 ApprovalRequest（弹窗输入）
弹窗支持三类请求：
- `Exec { id, command, reason, proposed_execpolicy_amendment }`
- `ApplyPatch { id, reason, cwd, changes }`
- `McpElicitation { server_name, request_id, message }`

### 4.2 Header 的渲染规则
`ApprovalRequestState::from(request)` 构造：

#### Exec header
- 若 `reason.is_some()`：
  - 第一行显示 `Reason: <reason>`（`reason` 斜体）
  - 然后插入空行
- 命令显示：
  - 用 `strip_bash_lc_and_escape(&command)` 生成 `full_cmd`：
    - 若命令是 `bash/zsh/sh -lc "<script>"`（或绝对路径形式），则只显示 `<script>`
    - 否则使用 `shlex::try_join(...)` 转义（失败则简单 join）
  - `highlight_bash_to_lines(&full_cmd)` 做语法高亮并生成多行
  - 在第一行前加 `$ ` 前缀

#### ApplyPatch header
- 若 `reason` 非空：显示 `Reason: <reason>`（斜体）+ 空行
- 然后渲染 `DiffSummary::new(changes, cwd)`

#### MCP elicitation header
- 显示 `Server: <server_name>`（粗体）+ 空行 + `message`

来源：
- `codex-rs/tui/src/bottom_pane/approval_overlay.rs:ApprovalRequestState::from`
- `codex-rs/tui/src/exec_command.rs:strip_bash_lc_and_escape`

### 4.3 选项（Options）与快捷键（Shortcuts）
选项由 `build_options(variant, ...)` 生成，并交给 `ListSelectionView` 渲染与导航。

#### 4.3.1 Exec options
基础选项（始终存在）：
- `Yes, proceed` → `ReviewDecision::Approved`
  - 快捷键：`y`（Enter 也可确认当前选中项）
- `No, and tell Codex what to do differently` → `ReviewDecision::Abort`
  - 快捷键：`Esc` 或 `n`

可选的 execpolicy 前缀保存选项（条件同时满足才出现）：
- `proposed_execpolicy_amendment.is_some()`
- `features.enabled(Feature::ExecPolicy)` 为 true
- `rendered_prefix = strip_bash_lc_and_escape(prefix.command())` 不包含 `\n` 或 `\r`

出现时的 label：
- `Yes, and don't ask again for commands that start with `<rendered_prefix>``
并产生决策：
- `ReviewDecision::ApprovedExecpolicyAmendment { proposed_execpolicy_amendment: prefix }`
快捷键：
- `p`

#### 4.3.2 ApplyPatch options
- `Yes, proceed` → `ReviewDecision::Approved`（快捷键 `y`）
- `Yes, and don't ask again for these files` → `ReviewDecision::ApprovedForSession`（快捷键 `a`）
- `No, and tell Codex what to do differently` → `ReviewDecision::Abort`（快捷键 `Esc` 或 `n`）

#### 4.3.3 MCP elicitation options
- `Yes, provide the requested info` → `ElicitationAction::Accept`（快捷键 `y`）
- `No, but continue without it` → `ElicitationAction::Decline`（快捷键 `n`）
- `Cancel this request` → `ElicitationAction::Cancel`（快捷键 `Esc` 或 `c`）

来源：
- `codex-rs/tui/src/bottom_pane/approval_overlay.rs:exec_options/patch_options/elicitation_options`

### 4.4 用户确认后产生的 Op（回传 core）
当用户确认选项（Enter 或快捷键）：
- Exec：
  - 插入一条 history cell（`new_approval_decision_cell`）用于展示“你批准/拒绝了什么”
  - 发送 `AppEvent::CodexOp(Op::ExecApproval { id, decision })`
- ApplyPatch：
  - 发送 `AppEvent::CodexOp(Op::PatchApproval { id, decision })`
- Elicitation：
  - 发送 `AppEvent::CodexOp(Op::ResolveElicitation { server_name, request_id, decision })`

来源：
- `codex-rs/tui/src/bottom_pane/approval_overlay.rs:handle_*_decision`

### 4.5 多请求队列语义（重要：LIFO）
ApprovalOverlay 内部队列字段：`queue: Vec<ApprovalRequest>`

- 新请求到来：`enqueue_request` 使用 `push`（追加到 Vec 尾部）
- 当前请求完成后：`advance_queue` 使用 `queue.pop()` 取下一个

因此：**弹窗内部队列的处理顺序是 LIFO（后来的请求先处理）**。

这与 ChatWidget 的 `InterruptManager` FIFO（用于保持事件序）是两层不同队列，复刻时要分别一致。

### 4.6 Ctrl+C 与 Ctrl+A 的特殊语义
- `Ctrl+C`（在弹窗中）：
  - 若弹窗已 done：只返回 Handled
  - 否则对当前请求发送：
    - Exec/ApplyPatch：`ReviewDecision::Abort`
    - Elicitation：`ElicitationAction::Cancel`
  - 清空内部 queue，标记 done
- `Ctrl+A`（在弹窗中）：
  - 发送 `AppEvent::FullScreenApprovalRequest(current_request.clone())`
  - 进入“全屏查看”模式（见 §5）

来源：
- `codex-rs/tui/src/bottom_pane/approval_overlay.rs:on_ctrl_c`
- `codex-rs/tui/src/bottom_pane/approval_overlay.rs:try_handle_shortcut`

---

## 5. 全屏查看（Alt screen StaticOverlay）

触发方式：
- 在审批弹窗内按 `Ctrl+A`
- App 处理 `AppEvent::FullScreenApprovalRequest(request)` 并 `enter_alt_screen()`

显示内容：
- Exec：`strip_bash_lc_and_escape(command)` → `highlight_bash_to_lines` → `Overlay::new_static_with_lines(..., "E X E C")`
- Patch：`DiffSummary::new(changes, cwd)` → `Overlay::new_static_with_renderables(..., "P A T C H")`
- Elicitation：Paragraph（server/message）→ `"E L I C I T A T I O N"`

退出方式：
- Static overlay 退出键：`q` 或 `Ctrl+C`（由 `pager_overlay.rs:StaticOverlay` 定义）
- 退出后 App 会 `leave_alt_screen()` 并恢复主 UI

来源：
- 触发：`codex-rs/tui/src/bottom_pane/approval_overlay.rs`
- 处理：`codex-rs/tui/src/app.rs:AppEvent::FullScreenApprovalRequest`
- overlay 生命周期：`codex-rs/tui/src/app_backtrack.rs:overlay_forward_event`（done → `leave_alt_screen`）
- pager：`codex-rs/tui/src/pager_overlay.rs:StaticOverlay`

