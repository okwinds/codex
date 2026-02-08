# `codex-rs/tui/src/bottom_pane/feedback_view.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `22500`
- sha256: `4b1a773ee45bed3ec49e297b8ef97e30263026867c0aa47e9d656c6140f46839`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/feedback_view.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:1` `use std::cell::RefCell;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:4` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:5` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:6` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:7` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:8` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:9` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:10` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:11` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:12` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:13` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:14` `use ratatui::widgets::StatefulWidgetRef;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:15` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:17` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:18` `use crate::app_event::FeedbackCategory;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:19` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:20` `use crate::history_cell;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:21` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:22` `use codex_core::protocol::SessionSource;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:24` `use super::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:25` `use super::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:26` `use super::popup_consts::standard_popup_hint_line;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:27` `use super::textarea::TextArea;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:28` `use super::textarea::TextAreaState;`
- `const` `codex-rs/tui/src/bottom_pane/feedback_view.rs:30` `const BASE_BUG_ISSUE_URL: &str =`
- `const` `codex-rs/tui/src/bottom_pane/feedback_view.rs:33` `const CODEX_FEEDBACK_INTERNAL_URL: &str = "http://go/codex-feedback-internal";`
- `impl` `codex-rs/tui/src/bottom_pane/feedback_view.rs:61` `impl FeedbackNoteView {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:83` `fn submit(&mut self) {`
- `impl` `codex-rs/tui/src/bottom_pane/feedback_view.rs:172` `impl BottomPaneView for FeedbackNoteView {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:173` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:199` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:204` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:208` `fn handle_paste(&mut self, pasted: String) -> bool {`
- `impl` `codex-rs/tui/src/bottom_pane/feedback_view.rs:217` `impl Renderable for FeedbackNoteView {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:218` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:222` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:241` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/bottom_pane/feedback_view.rs:330` `impl FeedbackNoteView {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:331` `fn input_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:338` `fn gutter() -> Span<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:342` `fn feedback_title_and_placeholder(category: FeedbackCategory) -> (String, String) {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:363` `fn feedback_classification(category: FeedbackCategory) -> &'static str {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:372` `fn issue_url_for_category(`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:397` `fn slack_feedback_url(_thread_id: &str) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:452` `fn make_feedback_item(`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:476` `use super::popup_consts::standard_popup_hint_line;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:542` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:543` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/feedback_view.rs:544` `use crate::app_event_sender::AppEventSender;`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:546` `fn render(view: &FeedbackNoteView, width: u16) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:576` `fn make_view(category: FeedbackCategory) -> FeedbackNoteView {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:591` `fn feedback_view_bad_result() {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:598` `fn feedback_view_good_result() {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:605` `fn feedback_view_bug() {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:612` `fn feedback_view_other() {`
- `fn` `codex-rs/tui/src/bottom_pane/feedback_view.rs:619` `fn issue_url_available_for_bug_bad_result_and_other() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::cell::RefCell;`
- `use std::path::PathBuf;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Clear;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::StatefulWidgetRef;`
- `use ratatui::widgets::Widget;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event::FeedbackCategory;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::history_cell;`
- `use crate::render::renderable::Renderable;`
- `use codex_core::protocol::SessionSource;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
