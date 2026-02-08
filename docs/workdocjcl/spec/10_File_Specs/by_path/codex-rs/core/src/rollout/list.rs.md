# `codex-rs/core/src/rollout/list.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `40075`
- sha256: `e6fe5e1d2e4d3fa3734c39fe2da1a9512f45691ab1f9dd525aec783fb7259581`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/list.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ThreadsPage {`
- `pub struct ThreadItem {`
- `pub enum ThreadSortKey {`
- `pub struct Cursor {`
- `pub fn parse_cursor(token: &str) -> Option<Cursor> {`
- `pub fn rollout_date_parts(file_name: &OsStr) -> Option<(String, String, String)> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/list.rs:1` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/rollout/list.rs:2` `use std::cmp::Reverse;`
- `use` `codex-rs/core/src/rollout/list.rs:3` `use std::ffi::OsStr;`
- `use` `codex-rs/core/src/rollout/list.rs:4` `use std::io::{self};`
- `use` `codex-rs/core/src/rollout/list.rs:5` `use std::num::NonZero;`
- `use` `codex-rs/core/src/rollout/list.rs:6` `use std::ops::ControlFlow;`
- `use` `codex-rs/core/src/rollout/list.rs:7` `use std::path::Path;`
- `use` `codex-rs/core/src/rollout/list.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/rollout/list.rs:9` `use time::OffsetDateTime;`
- `use` `codex-rs/core/src/rollout/list.rs:10` `use time::PrimitiveDateTime;`
- `use` `codex-rs/core/src/rollout/list.rs:11` `use time::format_description::FormatItem;`
- `use` `codex-rs/core/src/rollout/list.rs:12` `use time::format_description::well_known::Rfc3339;`
- `use` `codex-rs/core/src/rollout/list.rs:13` `use time::macros::format_description;`
- `use` `codex-rs/core/src/rollout/list.rs:14` `use uuid::Uuid;`
- `use` `codex-rs/core/src/rollout/list.rs:16` `use super::ARCHIVED_SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/rollout/list.rs:17` `use super::SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/rollout/list.rs:18` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/rollout/list.rs:19` `use crate::state_db;`
- `use` `codex-rs/core/src/rollout/list.rs:20` `use codex_file_search as file_search;`
- `use` `codex-rs/core/src/rollout/list.rs:21` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/list.rs:22` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/list.rs:23` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/core/src/rollout/list.rs:24` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/rollout/list.rs:25` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/rollout/list.rs:26` `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
- `struct` `codex-rs/core/src/rollout/list.rs:30` `pub struct ThreadsPage {`
- `struct` `codex-rs/core/src/rollout/list.rs:43` `pub struct ThreadItem {`
- `type` `codex-rs/core/src/rollout/list.rs:74` `pub type ConversationItem = ThreadItem;`
- `type` `codex-rs/core/src/rollout/list.rs:77` `pub type ConversationsPage = ThreadsPage;`
- `struct` `codex-rs/core/src/rollout/list.rs:80` `struct HeadTailSummary {`
- `const` `codex-rs/core/src/rollout/list.rs:97` `const MAX_SCAN_FILES: usize = 10000;`
- `const` `codex-rs/core/src/rollout/list.rs:98` `const HEAD_RECORD_LIMIT: usize = 10;`
- `const` `codex-rs/core/src/rollout/list.rs:99` `const USER_EVENT_SCAN_LIMIT: usize = 200;`
- `enum` `codex-rs/core/src/rollout/list.rs:102` `pub enum ThreadSortKey {`
- `struct` `codex-rs/core/src/rollout/list.rs:122` `pub struct Cursor {`
- `impl` `codex-rs/core/src/rollout/list.rs:127` `impl Cursor {`
- `fn` `codex-rs/core/src/rollout/list.rs:128` `fn new(ts: OffsetDateTime, id: Uuid) -> Self {`
- `struct` `codex-rs/core/src/rollout/list.rs:137` `struct AnchorState {`
- `impl` `codex-rs/core/src/rollout/list.rs:143` `impl AnchorState {`
- `fn` `codex-rs/core/src/rollout/list.rs:144` `fn new(anchor: Option<Cursor>) -> Self {`
- `fn` `codex-rs/core/src/rollout/list.rs:159` `fn should_skip(&mut self, ts: OffsetDateTime, id: Uuid) -> bool {`
- `trait` `codex-rs/core/src/rollout/list.rs:178` `trait RolloutFileVisitor {`
- `fn` `codex-rs/core/src/rollout/list.rs:179` `async fn visit(`
- `struct` `codex-rs/core/src/rollout/list.rs:190` `struct FilesByCreatedAtVisitor<'a> {`
- `impl` `codex-rs/core/src/rollout/list.rs:200` `impl<'a> RolloutFileVisitor for FilesByCreatedAtVisitor<'a> {`
- `fn` `codex-rs/core/src/rollout/list.rs:201` `async fn visit(`
- `struct` `codex-rs/core/src/rollout/list.rs:239` `struct FilesByUpdatedAtVisitor<'a> {`
- `impl` `codex-rs/core/src/rollout/list.rs:244` `impl<'a> RolloutFileVisitor for FilesByUpdatedAtVisitor<'a> {`
- `fn` `codex-rs/core/src/rollout/list.rs:245` `async fn visit(`
- `impl` `codex-rs/core/src/rollout/list.rs:262` `impl serde::Serialize for Cursor {`
- `impl` `codex-rs/core/src/rollout/list.rs:275` `impl<'de> serde::Deserialize<'de> for Cursor {`
- `impl` `codex-rs/core/src/rollout/list.rs:285` `impl From<codex_state::Anchor> for Cursor {`
- `fn` `codex-rs/core/src/rollout/list.rs:286` `fn from(anchor: codex_state::Anchor) -> Self {`
- `fn` `codex-rs/core/src/rollout/list.rs:375` `async fn traverse_directories_for_paths(`
- `fn` `codex-rs/core/src/rollout/list.rs:407` `async fn traverse_flat_paths(`
- `fn` `codex-rs/core/src/rollout/list.rs:433` `async fn traverse_directories_for_paths_created(`
- `fn` `codex-rs/core/src/rollout/list.rs:480` `async fn traverse_directories_for_paths_updated(`
- `fn` `codex-rs/core/src/rollout/list.rs:540` `async fn traverse_flat_paths_created(`
- `fn` `codex-rs/core/src/rollout/list.rs:590` `async fn traverse_flat_paths_updated(`
- `fn` `codex-rs/core/src/rollout/list.rs:653` `pub fn parse_cursor(token: &str) -> Option<Cursor> {`
- `fn` `codex-rs/core/src/rollout/list.rs:671` `fn build_next_cursor(items: &[ThreadItem], sort_key: ThreadSortKey) -> Option<Cursor> {`
- `fn` `codex-rs/core/src/rollout/list.rs:685` `async fn build_thread_item(`
- `fn` `codex-rs/core/src/rollout/list.rs:792` `async fn collect_flat_rollout_files(`
- `fn` `codex-rs/core/src/rollout/list.rs:830` `async fn collect_rollout_day_files(`
- `struct` `codex-rs/core/src/rollout/list.rs:863` `struct ThreadCandidate {`
- `fn` `codex-rs/core/src/rollout/list.rs:869` `async fn collect_files_by_updated_at(`
- `fn` `codex-rs/core/src/rollout/list.rs:882` `async fn collect_flat_files_by_updated_at(`
- `fn` `codex-rs/core/src/rollout/list.rs:925` `async fn walk_rollout_files(`
- `struct` `codex-rs/core/src/rollout/list.rs:965` `struct ProviderMatcher<'a> {`
- `impl` `codex-rs/core/src/rollout/list.rs:970` `impl<'a> ProviderMatcher<'a> {`
- `fn` `codex-rs/core/src/rollout/list.rs:971` `fn new(filters: &'a [String], default_provider: &'a str) -> Option<Self> {`
- `fn` `codex-rs/core/src/rollout/list.rs:983` `fn matches(&self, session_provider: Option<&str>) -> bool {`
- `fn` `codex-rs/core/src/rollout/list.rs:991` `async fn read_head_summary(path: &Path, head_limit: usize) -> io::Result<HeadTailSummary> {`
- `use` `codex-rs/core/src/rollout/list.rs:992` `use tokio::io::AsyncBufReadExt;`
- `fn` `codex-rs/core/src/rollout/list.rs:1073` `pub async fn read_head_for_summary(path: &Path) -> io::Result<Vec<serde_json::Value>> {`
- `use` `codex-rs/core/src/rollout/list.rs:1074` `use tokio::io::AsyncBufReadExt;`
- `fn` `codex-rs/core/src/rollout/list.rs:1111` `fn strip_user_message_prefix(text: &str) -> &str {`
- `fn` `codex-rs/core/src/rollout/list.rs:1120` `pub async fn read_session_meta_line(path: &Path) -> io::Result<SessionMetaLine> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1136` `async fn file_modified_time(path: &Path) -> io::Result<Option<OffsetDateTime>> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1148` `fn format_rfc3339(dt: OffsetDateTime) -> Option<String> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1152` `fn truncate_to_seconds(dt: OffsetDateTime) -> Option<OffsetDateTime> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1156` `async fn find_thread_path_by_id_str_in_subdir(`
- `fn` `codex-rs/core/src/rollout/list.rs:1232` `pub async fn find_thread_path_by_id_str(`
- `fn` `codex-rs/core/src/rollout/list.rs:1240` `pub async fn find_archived_thread_path_by_id_str(`
- `fn` `codex-rs/core/src/rollout/list.rs:1248` `pub fn rollout_date_parts(file_name: &OsStr) -> Option<(String, String, String)> {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use std::cmp::Reverse;`
- `use std::ffi::OsStr;`
- `use std::io::{self};`
- `use std::num::NonZero;`
- `use std::ops::ControlFlow;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use time::OffsetDateTime;`
- `use time::PrimitiveDateTime;`
- `use time::format_description::FormatItem;`
- `use time::format_description::well_known::Rfc3339;`
- `use time::macros::format_description;`
- `use uuid::Uuid;`
- `use super::ARCHIVED_SESSIONS_SUBDIR;`
- `use super::SESSIONS_SUBDIR;`
- `use crate::protocol::EventMsg;`
- `use crate::state_db;`
- `use codex_file_search as file_search;`
- `use codex_protocol::ThreadId;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
