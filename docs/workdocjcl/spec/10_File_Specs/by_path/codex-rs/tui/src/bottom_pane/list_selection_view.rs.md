# `codex-rs/tui/src/bottom_pane/list_selection_view.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `41827`
- sha256: `69a0568c6c574d215d5f654bda6203f4e29396924bf4ef105f58056b8053df0f`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/list_selection_view.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new(params: SelectionViewParams, app_event_tx: AppEventSender) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:2` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:3` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:4` `use itertools::Itertools as _;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:5` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:6` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:7` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:8` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:9` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:10` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:11` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:12` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:13` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:15` `use super::selection_popup_common::render_menu_surface;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:16` `use super::selection_popup_common::wrap_styled_line;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:17` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:18` `use crate::key_hint::KeyBinding;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:19` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:20` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:22` `use super::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:23` `use super::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:24` `use super::popup_consts::MAX_POPUP_ROWS;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:25` `use super::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:27` `use super::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:28` `use super::selection_popup_common::measure_rows_height;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:29` `use super::selection_popup_common::measure_rows_height_stable_col_widths;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:30` `use super::selection_popup_common::measure_rows_height_with_col_width_mode;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:31` `use super::selection_popup_common::render_rows;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:32` `use super::selection_popup_common::render_rows_stable_col_widths;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:33` `use super::selection_popup_common::render_rows_with_col_width_mode;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:34` `use unicode_width::UnicodeWidthStr;`
- `impl` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:83` `impl Default for SelectionViewParams {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:84` `fn default() -> Self {`
- `impl` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:122` `impl ListSelectionView {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:130` `pub fn new(params: SelectionViewParams, app_event_tx: AppEventSender) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:165` `fn visible_len(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:169` `fn max_visible_rows(len: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:173` `fn apply_filter(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:223` `fn build_rows(&self) -> Vec<GenericDisplayRow> {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:271` `fn move_up(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:279` `fn move_down(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:287` `fn accept(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:323` `fn rows_width(total_width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:327` `fn skip_disabled_down(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:344` `fn skip_disabled_up(&mut self) {`
- `impl` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:362` `impl BottomPaneView for ListSelectionView {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:363` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:459` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:463` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `impl` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:469` `impl Renderable for ListSelectionView {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:470` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:514` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:672` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:673` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:674` `use crate::bottom_pane::popup_consts::standard_popup_hint_line;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:675` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:676` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:677` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:678` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:679` `use tokio::sync::mpsc::unbounded_channel;`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:681` `fn make_selection_view(subtitle: Option<&str>) -> ListSelectionView {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:712` `fn render_lines(view: &ListSelectionView) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:716` `fn render_lines_with_width(view: &ListSelectionView, width: u16) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:739` `fn description_col(rendered: &str, item_marker: &str, description: &str) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:748` `fn make_scrolling_width_items() -> Vec<SelectionItem> {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:766` `fn render_before_after_scroll_snapshot(col_width_mode: ColumnWidthMode, width: u16) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:789` `fn renders_blank_line_between_title_and_items_without_subtitle() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:798` `fn renders_blank_line_between_subtitle_and_items() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:804` `fn snapshot_footer_note_wraps() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:836` `fn renders_search_query_line_when_enabled() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:867` `fn wraps_long_option_without_overflowing_columns() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:908` `fn width_changes_do_not_hide_rows() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:962` `fn narrow_width_keeps_all_rows_visible() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:990` `fn snapshot_model_picker_width_80() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:1037` `fn snapshot_narrow_width_preserves_third_option() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:1064` `fn snapshot_auto_visible_col_width_mode_scroll_behavior() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:1072` `fn snapshot_auto_all_rows_col_width_mode_scroll_behavior() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:1080` `fn snapshot_fixed_col_width_mode_scroll_behavior() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:1088` `fn auto_all_rows_col_width_does_not_shift_when_scrolling() {`
- `fn` `codex-rs/tui/src/bottom_pane/list_selection_view.rs:1122` `fn fixed_col_width_is_30_70_and_does_not_shift_when_scrolling() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyModifiers;`
- `use itertools::Itertools as _;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Layout;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::Widget;`
- `use super::selection_popup_common::render_menu_surface;`
- `use super::selection_popup_common::wrap_styled_line;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::key_hint::KeyBinding;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
- `use super::CancellationEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
