# `codex-rs/tui/src/bottom_pane/approval_overlay.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `23707`
- sha256: `102f25b12aa9589c97bd8ae99242a8d18b4ca1a49e32090bfd38a2738ea17997`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/approval_overlay.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new(request: ApprovalRequest, app_event_tx: AppEventSender, features: Features) -> Self {`
- `pub fn enqueue_request(&mut self, req: ApprovalRequest) {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:4` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:5` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:6` `use crate::bottom_pane::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:7` `use crate::bottom_pane::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:8` `use crate::bottom_pane::list_selection_view::ListSelectionView;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:9` `use crate::bottom_pane::list_selection_view::SelectionItem;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:10` `use crate::bottom_pane::list_selection_view::SelectionViewParams;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:11` `use crate::diff_render::DiffSummary;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:12` `use crate::exec_command::strip_bash_lc_and_escape;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:13` `use crate::history_cell;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:14` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:15` `use crate::key_hint::KeyBinding;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:16` `use crate::render::highlight::highlight_bash_to_lines;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:17` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:18` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:19` `use codex_core::features::Features;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:20` `use codex_core::protocol::ElicitationAction;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:21` `use codex_core::protocol::ExecPolicyAmendment;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:22` `use codex_core::protocol::FileChange;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:23` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:24` `use codex_core::protocol::ReviewDecision;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:25` `use codex_protocol::mcp::RequestId;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:26` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:27` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:28` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:29` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:30` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:31` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:32` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:33` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:34` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:35` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:36` `use ratatui::widgets::Wrap;`
- `impl` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:73` `impl ApprovalOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:74` `pub fn new(request: ApprovalRequest, app_event_tx: AppEventSender, features: Features) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:90` `pub fn enqueue_request(&mut self, req: ApprovalRequest) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:94` `fn set_current(&mut self, request: ApprovalRequest) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:104` `fn build_options(`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:161` `fn apply_selection(&mut self, actual_idx: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:193` `fn handle_exec_decision(&self, id: &str, command: &[String], decision: ReviewDecision) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:202` `fn handle_patch_decision(&self, id: &str, decision: ReviewDecision) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:209` `fn handle_elicitation_decision(`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:223` `fn advance_queue(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:231` `fn try_handle_shortcut(&mut self, key_event: &KeyEvent) -> bool {`
- `impl` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:263` `impl BottomPaneView for ApprovalOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:264` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:274` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:305` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:309` `fn try_consume_approval_request(`
- `impl` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:318` `impl Renderable for ApprovalOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:319` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:323` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:327` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `struct` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:332` `struct ApprovalRequestState {`
- `impl` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:337` `impl From<ApprovalRequest> for ApprovalRequestState {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:338` `fn from(value: ApprovalRequest) -> Self {`
- `enum` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:412` `enum ApprovalVariant {`
- `enum` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:428` `enum ApprovalDecision {`
- `struct` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:434` `struct ApprovalOption {`
- `impl` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:441` `impl ApprovalOption {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:442` `fn shortcuts(&self) -> impl Iterator<Item = KeyBinding> + '_ {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:449` `fn exec_options(proposed_execpolicy_amendment: Option<ExecPolicyAmendment>) -> Vec<ApprovalOption> {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:483` `fn patch_options() -> Vec<ApprovalOption> {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:506` `fn elicitation_options() -> Vec<ApprovalOption> {`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:531` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:532` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:533` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:534` `use tokio::sync::mpsc::unbounded_channel;`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:536` `fn make_exec_request() -> ApprovalRequest {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:546` `fn ctrl_c_aborts_and_clears_queue() {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:557` `fn shortcut_triggers_selection() {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:575` `fn exec_prefix_option_emits_execpolicy_amendment() {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:613` `fn header_includes_command_snippet() {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:644` `fn exec_history_cell_wraps_with_two_space_indent() {`
- `fn` `codex-rs/tui/src/bottom_pane/approval_overlay.rs:671` `fn enter_sets_last_selected_index_without_dismissing() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::bottom_pane::BottomPaneView;`
- `use crate::bottom_pane::CancellationEvent;`
- `use crate::bottom_pane::list_selection_view::ListSelectionView;`
- `use crate::bottom_pane::list_selection_view::SelectionItem;`
- `use crate::bottom_pane::list_selection_view::SelectionViewParams;`
- `use crate::diff_render::DiffSummary;`
- `use crate::exec_command::strip_bash_lc_and_escape;`
- `use crate::history_cell;`
- `use crate::key_hint;`
- `use crate::key_hint::KeyBinding;`
- `use crate::render::highlight::highlight_bash_to_lines;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
- `use codex_core::features::Features;`
- `use codex_core::protocol::ElicitationAction;`
- `use codex_core::protocol::ExecPolicyAmendment;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
