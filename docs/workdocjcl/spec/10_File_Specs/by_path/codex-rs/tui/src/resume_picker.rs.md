# `codex-rs/tui/src/resume_picker.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `63413`
- sha256: `37a99479227d6722400e6bcbf165eac47c5f34a6a5fe10576e790f4b25f315a9`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/resume_picker.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub enum SessionSelection {`
- `pub enum SessionPickerAction {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/resume_picker.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/resume_picker.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/tui/src/resume_picker.rs:3` `use std::path::Path;`
- `use` `codex-rs/tui/src/resume_picker.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/resume_picker.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/resume_picker.rs:7` `use chrono::DateTime;`
- `use` `codex-rs/tui/src/resume_picker.rs:8` `use chrono::Utc;`
- `use` `codex-rs/tui/src/resume_picker.rs:9` `use codex_core::Cursor;`
- `use` `codex-rs/tui/src/resume_picker.rs:10` `use codex_core::INTERACTIVE_SESSION_SOURCES;`
- `use` `codex-rs/tui/src/resume_picker.rs:11` `use codex_core::RolloutRecorder;`
- `use` `codex-rs/tui/src/resume_picker.rs:12` `use codex_core::ThreadItem;`
- `use` `codex-rs/tui/src/resume_picker.rs:13` `use codex_core::ThreadSortKey;`
- `use` `codex-rs/tui/src/resume_picker.rs:14` `use codex_core::ThreadsPage;`
- `use` `codex-rs/tui/src/resume_picker.rs:15` `use codex_core::find_thread_names_by_ids;`
- `use` `codex-rs/tui/src/resume_picker.rs:16` `use codex_core::path_utils;`
- `use` `codex-rs/tui/src/resume_picker.rs:17` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/tui/src/resume_picker.rs:18` `use color_eyre::eyre::Result;`
- `use` `codex-rs/tui/src/resume_picker.rs:19` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/resume_picker.rs:20` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/resume_picker.rs:21` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/resume_picker.rs:22` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/resume_picker.rs:23` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/resume_picker.rs:24` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/resume_picker.rs:25` `use ratatui::style::Stylize as _;`
- `use` `codex-rs/tui/src/resume_picker.rs:26` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/resume_picker.rs:27` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/resume_picker.rs:28` `use tokio::sync::mpsc;`
- `use` `codex-rs/tui/src/resume_picker.rs:29` `use tokio_stream::StreamExt;`
- `use` `codex-rs/tui/src/resume_picker.rs:30` `use tokio_stream::wrappers::UnboundedReceiverStream;`
- `use` `codex-rs/tui/src/resume_picker.rs:31` `use unicode_width::UnicodeWidthStr;`
- `use` `codex-rs/tui/src/resume_picker.rs:33` `use crate::diff_render::display_path_for;`
- `use` `codex-rs/tui/src/resume_picker.rs:34` `use crate::key_hint;`
- `use` `codex-rs/tui/src/resume_picker.rs:35` `use crate::text_formatting::truncate_text;`
- `use` `codex-rs/tui/src/resume_picker.rs:36` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/resume_picker.rs:37` `use crate::tui::Tui;`
- `use` `codex-rs/tui/src/resume_picker.rs:38` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/resume_picker.rs:39` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/resume_picker.rs:40` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/tui/src/resume_picker.rs:41` `use codex_protocol::protocol::SessionMetaLine;`
- `const` `codex-rs/tui/src/resume_picker.rs:43` `const PAGE_SIZE: usize = 25;`
- `const` `codex-rs/tui/src/resume_picker.rs:44` `const LOAD_NEAR_THRESHOLD: usize = 5;`
- `enum` `codex-rs/tui/src/resume_picker.rs:46` `pub enum SessionSelection {`
- `enum` `codex-rs/tui/src/resume_picker.rs:54` `pub enum SessionPickerAction {`
- `impl` `codex-rs/tui/src/resume_picker.rs:59` `impl SessionPickerAction {`
- `fn` `codex-rs/tui/src/resume_picker.rs:60` `fn title(self) -> &'static str {`
- `fn` `codex-rs/tui/src/resume_picker.rs:67` `fn action_label(self) -> &'static str {`
- `fn` `codex-rs/tui/src/resume_picker.rs:74` `fn selection(self, path: PathBuf) -> SessionSelection {`
- `struct` `codex-rs/tui/src/resume_picker.rs:83` `struct PageLoadRequest {`
- `type` `codex-rs/tui/src/resume_picker.rs:91` `type PageLoader = Arc<dyn Fn(PageLoadRequest) + Send + Sync>;`
- `enum` `codex-rs/tui/src/resume_picker.rs:93` `enum BackgroundEvent {`
- `fn` `codex-rs/tui/src/resume_picker.rs:105` `pub async fn run_resume_picker(`
- `fn` `codex-rs/tui/src/resume_picker.rs:121` `pub async fn run_fork_picker(`
- `fn` `codex-rs/tui/src/resume_picker.rs:137` `async fn run_session_picker(`
- `struct` `codex-rs/tui/src/resume_picker.rs:227` `struct AltScreenGuard<'a> {`
- `impl` `codex-rs/tui/src/resume_picker.rs:231` `impl<'a> AltScreenGuard<'a> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:232` `fn enter(tui: &'a mut Tui) -> Self {`
- `impl` `codex-rs/tui/src/resume_picker.rs:238` `impl Drop for AltScreenGuard<'_> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:239` `fn drop(&mut self) {`
- `struct` `codex-rs/tui/src/resume_picker.rs:244` `struct PickerState {`
- `struct` `codex-rs/tui/src/resume_picker.rs:266` `struct PaginationState {`
- `enum` `codex-rs/tui/src/resume_picker.rs:274` `enum LoadingState {`
- `struct` `codex-rs/tui/src/resume_picker.rs:280` `struct PendingLoad {`
- `enum` `codex-rs/tui/src/resume_picker.rs:286` `enum SearchState {`
- `enum` `codex-rs/tui/src/resume_picker.rs:291` `enum LoadTrigger {`
- `impl` `codex-rs/tui/src/resume_picker.rs:296` `impl LoadingState {`
- `fn` `codex-rs/tui/src/resume_picker.rs:297` `fn is_pending(&self) -> bool {`
- `impl` `codex-rs/tui/src/resume_picker.rs:302` `impl SearchState {`
- `fn` `codex-rs/tui/src/resume_picker.rs:303` `fn active_token(&self) -> Option<usize> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:310` `fn is_active(&self) -> bool {`
- `struct` `codex-rs/tui/src/resume_picker.rs:316` `struct Row {`
- `impl` `codex-rs/tui/src/resume_picker.rs:327` `impl Row {`
- `fn` `codex-rs/tui/src/resume_picker.rs:328` `fn display_preview(&self) -> &str {`
- `fn` `codex-rs/tui/src/resume_picker.rs:332` `fn matches_query(&self, query: &str) -> bool {`
- `impl` `codex-rs/tui/src/resume_picker.rs:345` `impl PickerState {`
- `fn` `codex-rs/tui/src/resume_picker.rs:346` `fn new(`
- `fn` `codex-rs/tui/src/resume_picker.rs:383` `fn request_frame(&self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:387` `async fn handle_key(&mut self, key: KeyEvent) -> Result<Option<SessionSelection>> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:457` `fn start_initial_load(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:481` `async fn handle_background_event(&mut self, event: BackgroundEvent) -> Result<()> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:506` `fn reset_pagination(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:513` `fn ingest_page(&mut self, page: ThreadsPage) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:537` `async fn update_thread_names(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:579` `fn apply_filter(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:600` `fn row_matches_filter(&self, row: &Row) -> bool {`
- `fn` `codex-rs/tui/src/resume_picker.rs:613` `fn set_query(&mut self, new_query: String) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:637` `fn continue_search_if_needed(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:652` `fn continue_search_if_token_matches(&mut self, completed_token: Option<usize>) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:664` `fn ensure_selected_visible(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:686` `fn ensure_minimum_rows_for_view(&mut self, minimum_rows: usize) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:703` `fn update_view_rows(&mut self, rows: usize) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:708` `fn maybe_load_more_for_scroll(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:724` `fn load_more_if_needed(&mut self, trigger: LoadTrigger) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:751` `fn allocate_request_token(&mut self) -> usize {`
- `fn` `codex-rs/tui/src/resume_picker.rs:757` `fn allocate_search_token(&mut self) -> usize {`
- `fn` `codex-rs/tui/src/resume_picker.rs:764` `fn rows_from_items(items: Vec<ThreadItem>) -> Vec<Row> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:768` `fn head_to_row(item: &ThreadItem) -> Row {`
- `fn` `codex-rs/tui/src/resume_picker.rs:798` `fn extract_session_meta_from_head(`
- `fn` `codex-rs/tui/src/resume_picker.rs:812` `fn paths_match(a: &Path, b: &Path) -> bool {`
- `fn` `codex-rs/tui/src/resume_picker.rs:822` `fn parse_timestamp_str(ts: &str) -> Option<DateTime<Utc>> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:828` `fn extract_timestamp(value: &serde_json::Value) -> Option<DateTime<Utc>> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:836` `fn preview_from_head(head: &[serde_json::Value]) -> Option<String> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:845` `fn draw_picker(tui: &mut Tui, state: &PickerState) -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:898` `fn render_list(`
- `fn` `codex-rs/tui/src/resume_picker.rs:1014` `fn render_empty_state_line(state: &PickerState) -> Line<'static> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1042` `fn human_time_ago(ts: DateTime<Utc>) -> String {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1077` `fn format_updated_label(row: &Row) -> String {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1085` `fn render_column_headers(`
- `struct` `codex-rs/tui/src/resume_picker.rs:1126` `struct ColumnMetrics {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1133` `fn calculate_column_metrics(rows: &[Row], include_cwd: bool) -> ColumnMetrics {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1134` `fn right_elide(s: &str, max: usize) -> String {`
- `use` `codex-rs/tui/src/resume_picker.rs:1192` `use super::*;`
- `use` `codex-rs/tui/src/resume_picker.rs:1193` `use chrono::Duration;`
- `use` `codex-rs/tui/src/resume_picker.rs:1194` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/resume_picker.rs:1195` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/resume_picker.rs:1196` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/resume_picker.rs:1197` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/resume_picker.rs:1198` `use serde_json::json;`
- `use` `codex-rs/tui/src/resume_picker.rs:1199` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/resume_picker.rs:1200` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/resume_picker.rs:1201` `use std::sync::Mutex;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1203` `fn head_with_ts_and_user_text(ts: &str, texts: &[&str]) -> Vec<serde_json::Value> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1217` `fn make_item(path: &str, ts: &str, preview: &str) -> ThreadItem {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1226` `fn cursor_from_str(repr: &str) -> Cursor {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1231` `fn page(`
- `fn` `codex-rs/tui/src/resume_picker.rs:1246` `fn preview_uses_first_message_input_text() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1282` `fn rows_from_items_preserves_backend_order() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1304` `fn row_uses_tail_timestamp_for_updated_at() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1326` `fn row_display_preview_prefers_thread_name() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1342` `fn resume_table_snapshot() {`
- `use` `codex-rs/tui/src/resume_picker.rs:1343` `use crate::custom_terminal::Terminal;`
- `use` `codex-rs/tui/src/resume_picker.rs:1344` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/resume_picker.rs:1345` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/resume_picker.rs:1346` `use ratatui::layout::Layout;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1422` `async fn resume_picker_screen_snapshot() {`
- `use` `codex-rs/tui/src/resume_picker.rs:1423` `use crate::custom_terminal::Terminal;`
- `use` `codex-rs/tui/src/resume_picker.rs:1424` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/resume_picker.rs:1425` `use uuid::Uuid;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1584` `async fn resume_picker_thread_names_snapshot() {`
- `use` `codex-rs/tui/src/resume_picker.rs:1585` `use crate::custom_terminal::Terminal;`
- `use` `codex-rs/tui/src/resume_picker.rs:1586` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/resume_picker.rs:1587` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/resume_picker.rs:1588` `use ratatui::layout::Layout;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1682` `fn pageless_scrolling_deduplicates_and_keeps_order() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1746` `fn ensure_minimum_rows_prefetches_when_underfilled() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1783` `async fn page_navigation_uses_view_rows() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1828` `async fn up_at_bottom_does_not_scroll_when_visible() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1868` `async fn set_query_loads_until_match_and_respects_scan_cap() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_core::Cursor;`
- `use codex_core::INTERACTIVE_SESSION_SOURCES;`
- `use codex_core::RolloutRecorder;`
- `use codex_core::ThreadItem;`
- `use codex_core::ThreadSortKey;`
- `use codex_core::ThreadsPage;`
- `use codex_core::find_thread_names_by_ids;`
- `use codex_core::path_utils;`
- `use codex_protocol::items::TurnItem;`
- `use color_eyre::eyre::Result;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
