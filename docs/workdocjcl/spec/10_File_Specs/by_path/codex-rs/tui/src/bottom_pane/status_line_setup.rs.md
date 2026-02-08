# `codex-rs/tui/src/bottom_pane/status_line_setup.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10341`
- sha256: `1846bb95f2338afc44f1a17f8ce73316ccdc928b47d55d24d60eac35a93ae211`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/status_line_setup.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:20` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:21` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:22` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:23` `use std::collections::HashSet;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:24` `use strum::IntoEnumIterator;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:25` `use strum_macros::Display;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:26` `use strum_macros::EnumIter;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:27` `use strum_macros::EnumString;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:29` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:30` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:31` `use crate::bottom_pane::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:32` `use crate::bottom_pane::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:33` `use crate::bottom_pane::multi_select_picker::MultiSelectItem;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:34` `use crate::bottom_pane::multi_select_picker::MultiSelectPicker;`
- `use` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:35` `use crate::render::renderable::Renderable;`
- `impl` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:96` `impl StatusLineItem {`
- `impl` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:167` `impl StatusLineSetupView {`
- `fn` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:245` `fn status_line_select_item(item: StatusLineItem, enabled: bool) -> MultiSelectItem {`
- `impl` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:255` `impl BottomPaneView for StatusLineSetupView {`
- `fn` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:256` `fn handle_key_event(&mut self, key_event: crossterm::event::KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:260` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:264` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `impl` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:270` `impl Renderable for StatusLineSetupView {`
- `fn` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:271` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/status_line_setup.rs:275` `fn desired_height(&self, width: u16) -> u16 {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::text::Line;`
- `use std::collections::HashSet;`
- `use strum::IntoEnumIterator;`
- `use strum_macros::Display;`
- `use strum_macros::EnumIter;`
- `use strum_macros::EnumString;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::bottom_pane::CancellationEvent;`
- `use crate::bottom_pane::bottom_pane_view::BottomPaneView;`
- `use crate::bottom_pane::multi_select_picker::MultiSelectItem;`
- `use crate::bottom_pane::multi_select_picker::MultiSelectPicker;`
- `use crate::render::renderable::Renderable;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
