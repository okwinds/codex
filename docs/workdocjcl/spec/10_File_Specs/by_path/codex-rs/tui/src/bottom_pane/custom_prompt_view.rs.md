# `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7739`
- sha256: `f7961a52b530dd826177c4254a8e58fef78a6f5d1d9c4d300752ecccbd5570fa`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:2` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:3` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:4` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:5` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:6` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:7` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:8` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:9` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:10` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:11` `use ratatui::widgets::StatefulWidgetRef;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:12` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:13` `use std::cell::RefCell;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:15` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:17` `use super::popup_consts::standard_popup_hint_line;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:19` `use super::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:20` `use super::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:21` `use super::textarea::TextArea;`
- `use` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:22` `use super::textarea::TextAreaState;`
- `impl` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:40` `impl CustomPromptView {`
- `impl` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:59` `impl BottomPaneView for CustomPromptView {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:60` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:90` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:95` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:99` `fn handle_paste(&mut self, pasted: String) -> bool {`
- `impl` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:108` `impl Renderable for CustomPromptView {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:109` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:114` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:216` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `impl` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:237` `impl CustomPromptView {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:238` `fn input_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/custom_prompt_view.rs:245` `fn gutter() -> Span<'static> {`

## Dependencies (auto sample)
### Imports / Includes
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
- `use std::cell::RefCell;`
- `use crate::render::renderable::Renderable;`
- `use super::popup_consts::standard_popup_hint_line;`
- `use super::CancellationEvent;`
- `use super::bottom_pane_view::BottomPaneView;`
- `use super::textarea::TextArea;`
- `use super::textarea::TextAreaState;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
