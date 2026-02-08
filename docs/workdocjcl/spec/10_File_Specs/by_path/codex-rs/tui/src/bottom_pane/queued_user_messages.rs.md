# `codex-rs/tui/src/bottom_pane/queued_user_messages.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5106`
- sha256: `b04758991686df0a208c05b54e35c8b7967da28e37c303ce44971695f6bd0d14`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/queued_user_messages.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:2` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:3` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:4` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:5` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:6` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:8` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:9` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:10` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:11` `use crate::wrapping::word_wrap_lines;`
- `impl` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:18` `impl QueuedUserMessages {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:25` `fn as_renderable(&self, width: u16) -> Box<dyn Renderable> {`
- `impl` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:61` `impl Renderable for QueuedUserMessages {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:62` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:70` `fn desired_height(&self, width: u16) -> u16 {`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:77` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:78` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:79` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:82` `fn desired_height_empty() {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:88` `fn desired_height_one_message() {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:95` `fn render_one_message() {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:106` `fn render_two_messages() {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:118` `fn render_more_than_three_messages() {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:132` `fn render_wrapped_message() {`
- `fn` `codex-rs/tui/src/bottom_pane/queued_user_messages.rs:146` `fn render_many_line_message() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyCode;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Paragraph;`
- `use crate::key_hint;`
- `use crate::render::renderable::Renderable;`
- `use crate::wrapping::RtOptions;`
- `use crate::wrapping::word_wrap_lines;`
- `use super::*;`
- `use insta::assert_snapshot;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
