# `codex-rs/tui/src/bottom_pane/multi_select_picker.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `27686`
- sha256: `9e65093c744b60b7da98835dd8523c80d5738f5b095c8bdd6825ea914c5bf0c3`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/multi_select_picker.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn builder(`
- `pub fn close(&mut self) {`
- `pub fn new(title: String, subtitle: Option<String>, app_event_tx: AppEventSender) -> Self {`
- `pub fn items(mut self, items: Vec<MultiSelectItem>) -> Self {`
- `pub fn instructions(mut self, instructions: Vec<Span<'static>>) -> Self {`
- `pub fn enable_ordering(mut self) -> Self {`
- `pub fn build(self) -> MultiSelectPicker {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:28` `use codex_common::fuzzy_match::fuzzy_match;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:29` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:30` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:31` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:32` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:33` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:34` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:35` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:36` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:37` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:38` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:39` `use ratatui::widgets::Block;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:40` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:42` `use super::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:43` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:44` `use crate::bottom_pane::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:45` `use crate::bottom_pane::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:46` `use crate::bottom_pane::popup_consts::MAX_POPUP_ROWS;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:47` `use crate::bottom_pane::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:48` `use crate::bottom_pane::selection_popup_common::render_rows_single_line;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:49` `use crate::bottom_pane::selection_popup_common::truncate_line_with_ellipsis_if_overflow;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:50` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:51` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:52` `use crate::render::RectExt;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:53` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:54` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:55` `use crate::style::user_message_style;`
- `use` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:56` `use crate::text_formatting::truncate_text;`
- `const` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:59` `const ITEM_NAME_TRUNCATE_LEN: usize = 21;`
- `const` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:62` `const SEARCH_PLACEHOLDER: &str = "Type to search";`
- `const` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:65` `const SEARCH_PROMPT_PREFIX: &str = "> ";`
- `enum` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:68` `enum Direction {`
- `type` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:75` `pub type ChangeCallBack = Box<dyn Fn(&[MultiSelectItem], &AppEventSender) + Send + Sync>;`
- `type` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:79` `pub type ConfirmCallback = Box<dyn Fn(&[String], &AppEventSender) + Send + Sync>;`
- `type` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:82` `pub type CancelCallback = Box<dyn Fn(&AppEventSender) + Send + Sync>;`
- `type` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:86` `pub type PreviewCallback = Box<dyn Fn(&[MultiSelectItem]) -> Option<Line<'static>> + Send + Sync>;`
- `impl` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:162` `impl MultiSelectPicker {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:170` `pub fn builder(`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:183` `fn apply_filter(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:228` `fn visible_len(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:233` `fn max_visible_rows(len: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:238` `fn rows_width(total_width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:243` `fn rows_height(&self, rows: &[GenericDisplayRow]) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:251` `fn build_rows(&self) -> Vec<GenericDisplayRow> {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:273` `fn move_up(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:281` `fn move_down(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:291` `fn toggle_selected(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:313` `fn confirm_selection(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:337` `fn move_selected_item(&mut self, direction: Direction) {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:385` `fn update_preview_line(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:395` `pub fn close(&mut self) {`
- `impl` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:406` `impl BottomPaneView for MultiSelectPicker {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:407` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:411` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:416` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `impl` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:497` `impl Renderable for MultiSelectPicker {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:498` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:509` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:633` `impl MultiSelectPickerBuilder {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:635` `pub fn new(title: String, subtitle: Option<String>, app_event_tx: AppEventSender) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:651` `pub fn items(mut self, items: Vec<MultiSelectItem>) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:660` `pub fn instructions(mut self, instructions: Vec<Span<'static>>) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:668` `pub fn enable_ordering(mut self) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/multi_select_picker.rs:721` `pub fn build(self) -> MultiSelectPicker {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_common::fuzzy_match::fuzzy_match;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Layout;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Block;`
- `use ratatui::widgets::Widget;`
- `use super::selection_popup_common::GenericDisplayRow;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::bottom_pane::CancellationEvent;`
- `use crate::bottom_pane::bottom_pane_view::BottomPaneView;`
- `use crate::bottom_pane::popup_consts::MAX_POPUP_ROWS;`
- `use crate::bottom_pane::scroll_state::ScrollState;`
- `use crate::bottom_pane::selection_popup_common::render_rows_single_line;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
