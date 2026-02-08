# `codex-rs/tui/src/resume_picker.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `74907`
- sha256: `637137ece83cdaeb226ad3e6f1be165f06b9e3a0ec62638a36c2dc2547b765df`
- generated_utc: `2026-02-08T10:45:40Z`

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
- `use` `codex-rs/tui/src/resume_picker.rs:17` `use color_eyre::eyre::Result;`
- `use` `codex-rs/tui/src/resume_picker.rs:18` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/resume_picker.rs:19` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/resume_picker.rs:20` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/resume_picker.rs:21` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/resume_picker.rs:22` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/resume_picker.rs:23` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/resume_picker.rs:24` `use ratatui::style::Stylize as _;`
- `use` `codex-rs/tui/src/resume_picker.rs:25` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/resume_picker.rs:26` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/resume_picker.rs:27` `use tokio::sync::mpsc;`
- `use` `codex-rs/tui/src/resume_picker.rs:28` `use tokio_stream::StreamExt;`
- `use` `codex-rs/tui/src/resume_picker.rs:29` `use tokio_stream::wrappers::UnboundedReceiverStream;`
- `use` `codex-rs/tui/src/resume_picker.rs:30` `use unicode_width::UnicodeWidthStr;`
- `use` `codex-rs/tui/src/resume_picker.rs:32` `use crate::diff_render::display_path_for;`
- `use` `codex-rs/tui/src/resume_picker.rs:33` `use crate::key_hint;`
- `use` `codex-rs/tui/src/resume_picker.rs:34` `use crate::text_formatting::truncate_text;`
- `use` `codex-rs/tui/src/resume_picker.rs:35` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/resume_picker.rs:36` `use crate::tui::Tui;`
- `use` `codex-rs/tui/src/resume_picker.rs:37` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/resume_picker.rs:38` `use codex_protocol::ThreadId;`
- `const` `codex-rs/tui/src/resume_picker.rs:40` `const PAGE_SIZE: usize = 25;`
- `const` `codex-rs/tui/src/resume_picker.rs:41` `const LOAD_NEAR_THRESHOLD: usize = 5;`
- `enum` `codex-rs/tui/src/resume_picker.rs:43` `pub enum SessionSelection {`
- `enum` `codex-rs/tui/src/resume_picker.rs:51` `pub enum SessionPickerAction {`
- `impl` `codex-rs/tui/src/resume_picker.rs:56` `impl SessionPickerAction {`
- `fn` `codex-rs/tui/src/resume_picker.rs:57` `fn title(self) -> &'static str {`
- `fn` `codex-rs/tui/src/resume_picker.rs:64` `fn action_label(self) -> &'static str {`
- `fn` `codex-rs/tui/src/resume_picker.rs:71` `fn selection(self, path: PathBuf) -> SessionSelection {`
- `struct` `codex-rs/tui/src/resume_picker.rs:80` `struct PageLoadRequest {`
- `type` `codex-rs/tui/src/resume_picker.rs:89` `type PageLoader = Arc<dyn Fn(PageLoadRequest) + Send + Sync>;`
- `enum` `codex-rs/tui/src/resume_picker.rs:91` `enum BackgroundEvent {`
- `fn` `codex-rs/tui/src/resume_picker.rs:115` `pub async fn run_resume_picker(`
- `fn` `codex-rs/tui/src/resume_picker.rs:131` `pub async fn run_fork_picker(`
- `fn` `codex-rs/tui/src/resume_picker.rs:147` `async fn run_session_picker(`
- `fn` `codex-rs/tui/src/resume_picker.rs:237` `fn sort_key_label(sort_key: ThreadSortKey) -> &'static str {`
- `struct` `codex-rs/tui/src/resume_picker.rs:245` `struct AltScreenGuard<'a> {`
- `impl` `codex-rs/tui/src/resume_picker.rs:249` `impl<'a> AltScreenGuard<'a> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:250` `fn enter(tui: &'a mut Tui) -> Self {`
- `impl` `codex-rs/tui/src/resume_picker.rs:256` `impl Drop for AltScreenGuard<'_> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:257` `fn drop(&mut self) {`
- `struct` `codex-rs/tui/src/resume_picker.rs:262` `struct PickerState {`
- `struct` `codex-rs/tui/src/resume_picker.rs:285` `struct PaginationState {`
- `enum` `codex-rs/tui/src/resume_picker.rs:293` `enum LoadingState {`
- `struct` `codex-rs/tui/src/resume_picker.rs:299` `struct PendingLoad {`
- `enum` `codex-rs/tui/src/resume_picker.rs:305` `enum SearchState {`
- `enum` `codex-rs/tui/src/resume_picker.rs:310` `enum LoadTrigger {`
- `impl` `codex-rs/tui/src/resume_picker.rs:315` `impl LoadingState {`
- `fn` `codex-rs/tui/src/resume_picker.rs:316` `fn is_pending(&self) -> bool {`
- `impl` `codex-rs/tui/src/resume_picker.rs:321` `impl SearchState {`
- `fn` `codex-rs/tui/src/resume_picker.rs:322` `fn active_token(&self) -> Option<usize> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:329` `fn is_active(&self) -> bool {`
- `struct` `codex-rs/tui/src/resume_picker.rs:335` `struct Row {`
- `impl` `codex-rs/tui/src/resume_picker.rs:346` `impl Row {`
- `fn` `codex-rs/tui/src/resume_picker.rs:347` `fn display_preview(&self) -> &str {`
- `fn` `codex-rs/tui/src/resume_picker.rs:351` `fn matches_query(&self, query: &str) -> bool {`
- `impl` `codex-rs/tui/src/resume_picker.rs:364` `impl PickerState {`
- `fn` `codex-rs/tui/src/resume_picker.rs:365` `fn new(`
- `fn` `codex-rs/tui/src/resume_picker.rs:403` `fn request_frame(&self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:407` `async fn handle_key(&mut self, key: KeyEvent) -> Result<Option<SessionSelection>> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:481` `fn start_initial_load(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:514` `async fn handle_background_event(&mut self, event: BackgroundEvent) -> Result<()> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:539` `fn reset_pagination(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:546` `fn ingest_page(&mut self, page: ThreadsPage) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:570` `async fn update_thread_names(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:612` `fn apply_filter(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:633` `fn row_matches_filter(&self, row: &Row) -> bool {`
- `fn` `codex-rs/tui/src/resume_picker.rs:646` `fn set_query(&mut self, new_query: String) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:670` `fn continue_search_if_needed(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:685` `fn continue_search_if_token_matches(&mut self, completed_token: Option<usize>) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:697` `fn ensure_selected_visible(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:719` `fn ensure_minimum_rows_for_view(&mut self, minimum_rows: usize) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:736` `fn update_view_rows(&mut self, rows: usize) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:741` `fn maybe_load_more_for_scroll(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:757` `fn load_more_if_needed(&mut self, trigger: LoadTrigger) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:785` `fn allocate_request_token(&mut self) -> usize {`
- `fn` `codex-rs/tui/src/resume_picker.rs:791` `fn allocate_search_token(&mut self) -> usize {`
- `fn` `codex-rs/tui/src/resume_picker.rs:802` `fn toggle_sort_key(&mut self) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:811` `fn rows_from_items(items: Vec<ThreadItem>) -> Vec<Row> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:815` `fn head_to_row(item: &ThreadItem) -> Row {`
- `fn` `codex-rs/tui/src/resume_picker.rs:843` `fn paths_match(a: &Path, b: &Path) -> bool {`
- `fn` `codex-rs/tui/src/resume_picker.rs:853` `fn parse_timestamp_str(ts: &str) -> Option<DateTime<Utc>> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:859` `fn draw_picker(tui: &mut Tui, state: &PickerState) -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:923` `fn render_list(`
- `fn` `codex-rs/tui/src/resume_picker.rs:1056` `fn render_empty_state_line(state: &PickerState) -> Line<'static> {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1084` `fn human_time_ago(ts: DateTime<Utc>) -> String {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1119` `fn format_updated_label(row: &Row) -> String {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1127` `fn format_created_label(row: &Row) -> String {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1134` `fn render_column_headers(`
- `struct` `codex-rs/tui/src/resume_picker.rs:1190` `struct ColumnMetrics {`
- `struct` `codex-rs/tui/src/resume_picker.rs:1205` `struct ColumnVisibility {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1212` `fn calculate_column_metrics(rows: &[Row], include_cwd: bool) -> ColumnMetrics {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1213` `fn right_elide(s: &str, max: usize) -> String {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1278` `fn column_visibility(`
- `const` `codex-rs/tui/src/resume_picker.rs:1283` `const MIN_PREVIEW_WIDTH: usize = 10;`
- `use` `codex-rs/tui/src/resume_picker.rs:1327` `use super::*;`
- `use` `codex-rs/tui/src/resume_picker.rs:1328` `use chrono::Duration;`
- `use` `codex-rs/tui/src/resume_picker.rs:1329` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/resume_picker.rs:1330` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/tui/src/resume_picker.rs:1331` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/tui/src/resume_picker.rs:1332` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/tui/src/resume_picker.rs:1333` `use codex_protocol::protocol::SessionMeta;`
- `use` `codex-rs/tui/src/resume_picker.rs:1334` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/tui/src/resume_picker.rs:1335` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/tui/src/resume_picker.rs:1336` `use codex_protocol::protocol::UserMessageEvent;`
- `use` `codex-rs/tui/src/resume_picker.rs:1337` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/resume_picker.rs:1338` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/resume_picker.rs:1339` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/resume_picker.rs:1340` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/resume_picker.rs:1341` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/resume_picker.rs:1342` `use serde_json::json;`
- `use` `codex-rs/tui/src/resume_picker.rs:1343` `use std::fs::FileTimes;`
- `use` `codex-rs/tui/src/resume_picker.rs:1344` `use std::fs::OpenOptions;`
- `use` `codex-rs/tui/src/resume_picker.rs:1345` `use std::path::Path;`
- `use` `codex-rs/tui/src/resume_picker.rs:1346` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/resume_picker.rs:1347` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/resume_picker.rs:1348` `use std::sync::Mutex;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1350` `fn make_item(path: &str, ts: &str, preview: &str) -> ThreadItem {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1367` `fn cursor_from_str(repr: &str) -> Cursor {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1372` `fn page(`
- `fn` `codex-rs/tui/src/resume_picker.rs:1386` `fn set_rollout_mtime(path: &Path, updated_at: DateTime<Utc>) {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1397` `async fn resume_picker_orders_by_updated_at() {`
- `use` `codex-rs/tui/src/resume_picker.rs:1398` `use uuid::Uuid;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1483` `fn head_to_row_uses_first_user_message() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1503` `fn rows_from_items_preserves_backend_order() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1541` `fn row_uses_tail_timestamp_for_updated_at() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1570` `fn row_display_preview_prefers_thread_name() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1586` `fn resume_table_snapshot() {`
- `use` `codex-rs/tui/src/resume_picker.rs:1587` `use crate::custom_terminal::Terminal;`
- `use` `codex-rs/tui/src/resume_picker.rs:1588` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/resume_picker.rs:1589` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/resume_picker.rs:1590` `use ratatui::layout::Layout;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1666` `async fn resume_picker_screen_snapshot() {`
- `use` `codex-rs/tui/src/resume_picker.rs:1667` `use crate::custom_terminal::Terminal;`
- `use` `codex-rs/tui/src/resume_picker.rs:1668` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/resume_picker.rs:1669` `use uuid::Uuid;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1837` `async fn resume_picker_thread_names_snapshot() {`
- `use` `codex-rs/tui/src/resume_picker.rs:1838` `use crate::custom_terminal::Terminal;`
- `use` `codex-rs/tui/src/resume_picker.rs:1839` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/resume_picker.rs:1840` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/resume_picker.rs:1841` `use ratatui::layout::Layout;`
- `fn` `codex-rs/tui/src/resume_picker.rs:1935` `fn pageless_scrolling_deduplicates_and_keeps_order() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:1999` `fn ensure_minimum_rows_prefetches_when_underfilled() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:2036` `fn column_visibility_hides_extra_date_column_when_narrow() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:2080` `async fn toggle_sort_key_reloads_with_new_sort() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:2115` `async fn page_navigation_uses_view_rows() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:2160` `async fn up_at_bottom_does_not_scroll_when_visible() {`
- `fn` `codex-rs/tui/src/resume_picker.rs:2200` `async fn set_query_loads_until_match_and_respects_scan_cap() {`

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
- `use color_eyre::eyre::Result;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use ratatui::layout::Constraint;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
