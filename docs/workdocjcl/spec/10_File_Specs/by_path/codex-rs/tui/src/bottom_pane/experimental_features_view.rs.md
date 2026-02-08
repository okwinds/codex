# `codex-rs/tui/src/bottom_pane/experimental_features_view.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8838`
- sha256: `c1bdaec74ac3a3affc6b3f4cf6249059a9549d8df1e27fad70f80fe87e58b127`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/experimental_features_view.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:2` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:3` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:4` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:5` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:6` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:7` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:8` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:9` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:10` `use ratatui::widgets::Block;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:11` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:13` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:14` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:15` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:16` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:17` `use crate::render::RectExt as _;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:18` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:19` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:20` `use crate::style::user_message_style;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:22` `use codex_core::features::Feature;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:24` `use super::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:25` `use super::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:26` `use super::popup_consts::MAX_POPUP_ROWS;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:27` `use super::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:28` `use super::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:29` `use super::selection_popup_common::measure_rows_height;`
- `use` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:30` `use super::selection_popup_common::render_rows;`
- `impl` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:48` `impl ExperimentalFeaturesView {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:71` `fn initialize_selection(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:79` `fn visible_len(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:83` `fn build_rows(&self) -> Vec<GenericDisplayRow> {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:104` `fn move_up(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:113` `fn move_down(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:122` `fn toggle_selected(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:132` `fn rows_width(total_width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:137` `impl BottomPaneView for ExperimentalFeaturesView {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:138` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:196` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:200` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `impl` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:217` `impl Renderable for ExperimentalFeaturesView {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:218` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:276` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/experimental_features_view.rs:292` `fn experimental_popup_hint_line() -> Line<'static> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Layout;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Block;`
- `use ratatui::widgets::Widget;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::key_hint;`
- `use crate::render::Insets;`
- `use crate::render::RectExt as _;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
- `use crate::style::user_message_style;`
- `use codex_core::features::Feature;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
