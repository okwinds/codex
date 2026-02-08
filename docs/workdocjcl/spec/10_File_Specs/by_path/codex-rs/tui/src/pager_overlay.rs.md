# `codex-rs/tui/src/pager_overlay.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `45731`
- sha256: `bb26c10aaf0a0bb51999a8a2ce6291339a22c0b7cc5011e0a9445ec22c779adc`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/pager_overlay.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/pager_overlay.rs:18` `use std::io::Result;`
- `use` `codex-rs/tui/src/pager_overlay.rs:19` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/pager_overlay.rs:21` `use crate::chatwidget::ActiveCellTranscriptKey;`
- `use` `codex-rs/tui/src/pager_overlay.rs:22` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/pager_overlay.rs:23` `use crate::history_cell::UserHistoryCell;`
- `use` `codex-rs/tui/src/pager_overlay.rs:24` `use crate::key_hint;`
- `use` `codex-rs/tui/src/pager_overlay.rs:25` `use crate::key_hint::KeyBinding;`
- `use` `codex-rs/tui/src/pager_overlay.rs:26` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/pager_overlay.rs:27` `use crate::render::renderable::InsetRenderable;`
- `use` `codex-rs/tui/src/pager_overlay.rs:28` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/pager_overlay.rs:29` `use crate::style::user_message_style;`
- `use` `codex-rs/tui/src/pager_overlay.rs:30` `use crate::tui;`
- `use` `codex-rs/tui/src/pager_overlay.rs:31` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/pager_overlay.rs:32` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/pager_overlay.rs:33` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/pager_overlay.rs:34` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/pager_overlay.rs:35` `use ratatui::buffer::Cell;`
- `use` `codex-rs/tui/src/pager_overlay.rs:36` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/pager_overlay.rs:37` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/pager_overlay.rs:38` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/pager_overlay.rs:39` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/pager_overlay.rs:40` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/pager_overlay.rs:41` `use ratatui::text::Text;`
- `use` `codex-rs/tui/src/pager_overlay.rs:42` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/pager_overlay.rs:43` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/pager_overlay.rs:44` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/pager_overlay.rs:45` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/pager_overlay.rs:46` `use ratatui::widgets::Wrap;`
- `impl` `codex-rs/tui/src/pager_overlay.rs:53` `impl Overlay {`
- `const` `codex-rs/tui/src/pager_overlay.rs:84` `const KEY_UP: KeyBinding = key_hint::plain(KeyCode::Up);`
- `const` `codex-rs/tui/src/pager_overlay.rs:85` `const KEY_DOWN: KeyBinding = key_hint::plain(KeyCode::Down);`
- `const` `codex-rs/tui/src/pager_overlay.rs:86` `const KEY_K: KeyBinding = key_hint::plain(KeyCode::Char('k'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:87` `const KEY_J: KeyBinding = key_hint::plain(KeyCode::Char('j'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:88` `const KEY_PAGE_UP: KeyBinding = key_hint::plain(KeyCode::PageUp);`
- `const` `codex-rs/tui/src/pager_overlay.rs:89` `const KEY_PAGE_DOWN: KeyBinding = key_hint::plain(KeyCode::PageDown);`
- `const` `codex-rs/tui/src/pager_overlay.rs:90` `const KEY_SPACE: KeyBinding = key_hint::plain(KeyCode::Char(' '));`
- `const` `codex-rs/tui/src/pager_overlay.rs:91` `const KEY_SHIFT_SPACE: KeyBinding = key_hint::shift(KeyCode::Char(' '));`
- `const` `codex-rs/tui/src/pager_overlay.rs:92` `const KEY_HOME: KeyBinding = key_hint::plain(KeyCode::Home);`
- `const` `codex-rs/tui/src/pager_overlay.rs:93` `const KEY_END: KeyBinding = key_hint::plain(KeyCode::End);`
- `const` `codex-rs/tui/src/pager_overlay.rs:94` `const KEY_LEFT: KeyBinding = key_hint::plain(KeyCode::Left);`
- `const` `codex-rs/tui/src/pager_overlay.rs:95` `const KEY_RIGHT: KeyBinding = key_hint::plain(KeyCode::Right);`
- `const` `codex-rs/tui/src/pager_overlay.rs:96` `const KEY_CTRL_F: KeyBinding = key_hint::ctrl(KeyCode::Char('f'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:97` `const KEY_CTRL_D: KeyBinding = key_hint::ctrl(KeyCode::Char('d'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:98` `const KEY_CTRL_B: KeyBinding = key_hint::ctrl(KeyCode::Char('b'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:99` `const KEY_CTRL_U: KeyBinding = key_hint::ctrl(KeyCode::Char('u'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:100` `const KEY_Q: KeyBinding = key_hint::plain(KeyCode::Char('q'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:101` `const KEY_ESC: KeyBinding = key_hint::plain(KeyCode::Esc);`
- `const` `codex-rs/tui/src/pager_overlay.rs:102` `const KEY_ENTER: KeyBinding = key_hint::plain(KeyCode::Enter);`
- `const` `codex-rs/tui/src/pager_overlay.rs:103` `const KEY_CTRL_T: KeyBinding = key_hint::ctrl(KeyCode::Char('t'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:104` `const KEY_CTRL_C: KeyBinding = key_hint::ctrl(KeyCode::Char('c'));`
- `const` `codex-rs/tui/src/pager_overlay.rs:107` `const PAGER_KEY_HINTS: &[(&[KeyBinding], &str)] = &[`
- `fn` `codex-rs/tui/src/pager_overlay.rs:114` `fn render_key_hints(area: Rect, buf: &mut Buffer, pairs: &[(&[KeyBinding], &str)]) {`
- `struct` `codex-rs/tui/src/pager_overlay.rs:135` `struct PagerView {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:145` `impl PagerView {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:146` `fn new(renderables: Vec<Box<dyn Renderable>>, title: String, scroll_offset: usize) -> Self {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:157` `fn content_height(&self, width: u16) -> usize {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:164` `fn render(&mut self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:185` `fn render_header(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:193` `fn render_content(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:229` `fn render_bottom_bar(`
- `fn` `codex-rs/tui/src/pager_overlay.rs:261` `fn handle_key_event(&mut self, tui: &mut tui::Tui, key_event: KeyEvent) -> Result<()> {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:310` `fn page_height(&self, viewport_area: Rect) -> usize {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:315` `fn update_last_content_height(&mut self, height: u16) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:319` `fn content_area(&self, area: Rect) -> Rect {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:327` `impl PagerView {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:328` `fn is_scrolled_to_bottom(&self) -> bool {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:349` `fn scroll_chunk_into_view(&mut self, chunk_index: usize) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:353` `fn ensure_chunk_visible(&mut self, idx: usize, area: Rect) {`
- `struct` `codex-rs/tui/src/pager_overlay.rs:375` `struct CachedRenderable {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:381` `impl CachedRenderable {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:382` `fn new(renderable: impl Into<Box<dyn Renderable>>) -> Self {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:391` `impl Renderable for CachedRenderable {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:392` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:395` `fn desired_height(&self, width: u16) -> u16 {`
- `struct` `codex-rs/tui/src/pager_overlay.rs:405` `struct CellRenderable {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:410` `impl Renderable for CellRenderable {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:411` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:417` `fn desired_height(&self, width: u16) -> u16 {`
- `struct` `codex-rs/tui/src/pager_overlay.rs:440` `struct LiveTailKey {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:451` `impl TranscriptOverlay {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:470` `fn render_cells(`
- `fn` `codex-rs/tui/src/pager_overlay.rs:606` `fn rebuild_renderables(&mut self) {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:619` `fn take_live_tail_renderable(&mut self) -> Option<Box<dyn Renderable>> {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:623` `fn live_tail_renderable(`
- `fn` `codex-rs/tui/src/pager_overlay.rs:636` `fn render_hints(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:661` `impl TranscriptOverlay {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:690` `impl StaticOverlay {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:703` `fn render_hints(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:720` `impl StaticOverlay {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:744` `fn render_offset_content(`
- `use` `codex-rs/tui/src/pager_overlay.rs:773` `use super::*;`
- `use` `codex-rs/tui/src/pager_overlay.rs:774` `use codex_core::protocol::ExecCommandSource;`
- `use` `codex-rs/tui/src/pager_overlay.rs:775` `use codex_core::protocol::ReviewDecision;`
- `use` `codex-rs/tui/src/pager_overlay.rs:776` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/pager_overlay.rs:777` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/pager_overlay.rs:778` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/pager_overlay.rs:779` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/pager_overlay.rs:780` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/pager_overlay.rs:781` `use std::time::Duration;`
- `use` `codex-rs/tui/src/pager_overlay.rs:783` `use crate::exec_cell::CommandOutput;`
- `use` `codex-rs/tui/src/pager_overlay.rs:784` `use crate::history_cell;`
- `use` `codex-rs/tui/src/pager_overlay.rs:785` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/pager_overlay.rs:786` `use crate::history_cell::new_patch_event;`
- `use` `codex-rs/tui/src/pager_overlay.rs:787` `use codex_core::protocol::FileChange;`
- `use` `codex-rs/tui/src/pager_overlay.rs:788` `use codex_protocol::parse_command::ParsedCommand;`
- `use` `codex-rs/tui/src/pager_overlay.rs:789` `use ratatui::Terminal;`
- `use` `codex-rs/tui/src/pager_overlay.rs:790` `use ratatui::backend::TestBackend;`
- `use` `codex-rs/tui/src/pager_overlay.rs:791` `use ratatui::text::Text;`
- `struct` `codex-rs/tui/src/pager_overlay.rs:794` `struct TestCell {`
- `impl` `codex-rs/tui/src/pager_overlay.rs:798` `impl crate::history_cell::HistoryCell for TestCell {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:799` `fn display_lines(&self, _width: u16) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:803` `fn transcript_lines(&self, _width: u16) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:808` `fn paragraph_block(label: &str, lines: usize) -> Box<dyn Renderable> {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:818` `fn edit_prev_hint_is_visible() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:836` `fn edit_next_hint_is_visible_when_highlighted() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:855` `fn transcript_overlay_snapshot_basic() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:875` `fn transcript_overlay_renders_live_tail() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:896` `fn transcript_overlay_sync_live_tail_is_noop_for_identical_key() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:920` `fn buffer_to_text(buf: &Buffer, area: Rect) -> String {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:941` `fn transcript_overlay_apply_patch_scroll_vt100_clears_previous_page() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1003` `fn transcript_overlay_keeps_scroll_pinned_at_bottom() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1030` `fn transcript_overlay_preserves_manual_scroll_position() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1054` `fn static_overlay_snapshot_basic() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1067` `fn transcript_line_numbers(overlay: &mut TranscriptOverlay, area: Rect) -> Vec<usize> {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1093` `fn transcript_overlay_paging_is_continuous_and_round_trips() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1161` `fn static_overlay_wraps_long_lines() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1173` `fn pager_view_content_height_counts_renderables() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1184` `fn pager_view_ensure_chunk_visible_scrolls_down_when_needed() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1219` `fn pager_view_ensure_chunk_visible_scrolls_up_when_needed() {`
- `fn` `codex-rs/tui/src/pager_overlay.rs:1238` `fn pager_view_is_scrolled_to_bottom_accounts_for_wrapped_height() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::Result;`
- `use std::sync::Arc;`
- `use crate::chatwidget::ActiveCellTranscriptKey;`
- `use crate::history_cell::HistoryCell;`
- `use crate::history_cell::UserHistoryCell;`
- `use crate::key_hint;`
- `use crate::key_hint::KeyBinding;`
- `use crate::render::Insets;`
- `use crate::render::renderable::InsetRenderable;`
- `use crate::render::renderable::Renderable;`
- `use crate::style::user_message_style;`
- `use crate::tui;`
- `use crate::tui::TuiEvent;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::buffer::Cell;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Style;`
- `use ratatui::style::Stylize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
