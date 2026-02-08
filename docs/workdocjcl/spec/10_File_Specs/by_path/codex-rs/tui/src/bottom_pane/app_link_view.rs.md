# `codex-rs/tui/src/bottom_pane/app_link_view.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4782`
- sha256: `adcf827e526a33e9d009fa258c5e28c6d8a87876bc79854d5e9472b5f82d2baa`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/app_link_view.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:2` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:3` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:4` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:5` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:6` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:7` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:8` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:9` `use ratatui::widgets::Block;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:10` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:11` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:12` `use textwrap::wrap;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:14` `use super::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:15` `use super::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:16` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:17` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:18` `use crate::render::RectExt as _;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:19` `use crate::style::user_message_style;`
- `use` `codex-rs/tui/src/bottom_pane/app_link_view.rs:20` `use crate::wrapping::word_wrap_lines;`
- `impl` `codex-rs/tui/src/bottom_pane/app_link_view.rs:31` `impl AppLinkView {`
- `fn` `codex-rs/tui/src/bottom_pane/app_link_view.rs:49` `fn content_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `impl` `codex-rs/tui/src/bottom_pane/app_link_view.rs:102` `impl BottomPaneView for AppLinkView {`
- `fn` `codex-rs/tui/src/bottom_pane/app_link_view.rs:103` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/app_link_view.rs:112` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/app_link_view.rs:117` `fn is_complete(&self) -> bool {`
- `impl` `codex-rs/tui/src/bottom_pane/app_link_view.rs:122` `impl crate::render::renderable::Renderable for AppLinkView {`
- `fn` `codex-rs/tui/src/bottom_pane/app_link_view.rs:123` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/app_link_view.rs:129` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/app_link_view.rs:157` `fn hint_line() -> Line<'static> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Layout;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Block;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::Widget;`
- `use textwrap::wrap;`
- `use super::CancellationEvent;`
- `use super::bottom_pane_view::BottomPaneView;`
- `use crate::key_hint;`
- `use crate::render::Insets;`
- `use crate::render::RectExt as _;`
- `use crate::style::user_message_style;`
- `use crate::wrapping::word_wrap_lines;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
