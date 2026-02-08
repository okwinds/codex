# `codex-rs/core/src/rollout/list.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `36628`
- sha256: `9b724369224f660e66774017406f98b599269f0b336a1d692d993c0f553abf53`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/rollout/list.rs:18` `use crate::instructions::UserInstructions;`
- `use` `codex-rs/core/src/rollout/list.rs:19` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/rollout/list.rs:20` `use crate::session_prefix::is_session_prefix_content;`
- `use` `codex-rs/core/src/rollout/list.rs:21` `use crate::state_db;`
- `use` `codex-rs/core/src/rollout/list.rs:22` `use codex_file_search as file_search;`
- `use` `codex-rs/core/src/rollout/list.rs:23` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/list.rs:24` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/list.rs:25` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/core/src/rollout/list.rs:26` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/rollout/list.rs:27` `use codex_protocol::protocol::SessionSource;`
- `struct` `codex-rs/core/src/rollout/list.rs:31` `pub struct ThreadsPage {`
- `struct` `codex-rs/core/src/rollout/list.rs:44` `pub struct ThreadItem {`
- `type` `codex-rs/core/src/rollout/list.rs:59` `pub type ConversationItem = ThreadItem;`
- `type` `codex-rs/core/src/rollout/list.rs:62` `pub type ConversationsPage = ThreadsPage;`
- `struct` `codex-rs/core/src/rollout/list.rs:65` `struct HeadTailSummary {`
- `const` `codex-rs/core/src/rollout/list.rs:76` `const MAX_SCAN_FILES: usize = 10000;`
- `const` `codex-rs/core/src/rollout/list.rs:77` `const HEAD_RECORD_LIMIT: usize = 10;`
- `const` `codex-rs/core/src/rollout/list.rs:78` `const USER_EVENT_SCAN_LIMIT: usize = 200;`
- `enum` `codex-rs/core/src/rollout/list.rs:81` `pub enum ThreadSortKey {`
- `struct` `codex-rs/core/src/rollout/list.rs:101` `pub struct Cursor {`
- `impl` `codex-rs/core/src/rollout/list.rs:106` `impl Cursor {`
- `fn` `codex-rs/core/src/rollout/list.rs:107` `fn new(ts: OffsetDateTime, id: Uuid) -> Self {`
- `struct` `codex-rs/core/src/rollout/list.rs:116` `struct AnchorState {`
- `impl` `codex-rs/core/src/rollout/list.rs:122` `impl AnchorState {`
- `fn` `codex-rs/core/src/rollout/list.rs:123` `fn new(anchor: Option<Cursor>) -> Self {`
- `fn` `codex-rs/core/src/rollout/list.rs:138` `fn should_skip(&mut self, ts: OffsetDateTime, id: Uuid) -> bool {`
- `trait` `codex-rs/core/src/rollout/list.rs:157` `trait RolloutFileVisitor {`
- `fn` `codex-rs/core/src/rollout/list.rs:158` `async fn visit(`
- `struct` `codex-rs/core/src/rollout/list.rs:169` `struct FilesByCreatedAtVisitor<'a> {`
- `impl` `codex-rs/core/src/rollout/list.rs:179` `impl<'a> RolloutFileVisitor for FilesByCreatedAtVisitor<'a> {`
- `fn` `codex-rs/core/src/rollout/list.rs:180` `async fn visit(`
- `struct` `codex-rs/core/src/rollout/list.rs:218` `struct FilesByUpdatedAtVisitor<'a> {`
- `impl` `codex-rs/core/src/rollout/list.rs:223` `impl<'a> RolloutFileVisitor for FilesByUpdatedAtVisitor<'a> {`
- `fn` `codex-rs/core/src/rollout/list.rs:224` `async fn visit(`
- `impl` `codex-rs/core/src/rollout/list.rs:241` `impl serde::Serialize for Cursor {`
- `impl` `codex-rs/core/src/rollout/list.rs:254` `impl<'de> serde::Deserialize<'de> for Cursor {`
- `fn` `codex-rs/core/src/rollout/list.rs:346` `async fn traverse_directories_for_paths(`
- `fn` `codex-rs/core/src/rollout/list.rs:378` `async fn traverse_flat_paths(`
- `fn` `codex-rs/core/src/rollout/list.rs:404` `async fn traverse_directories_for_paths_created(`
- `fn` `codex-rs/core/src/rollout/list.rs:451` `async fn traverse_directories_for_paths_updated(`
- `fn` `codex-rs/core/src/rollout/list.rs:511` `async fn traverse_flat_paths_created(`
- `fn` `codex-rs/core/src/rollout/list.rs:561` `async fn traverse_flat_paths_updated(`
- `fn` `codex-rs/core/src/rollout/list.rs:624` `pub fn parse_cursor(token: &str) -> Option<Cursor> {`
- `fn` `codex-rs/core/src/rollout/list.rs:642` `fn build_next_cursor(items: &[ThreadItem], sort_key: ThreadSortKey) -> Option<Cursor> {`
- `fn` `codex-rs/core/src/rollout/list.rs:656` `async fn build_thread_item(`
- `fn` `codex-rs/core/src/rollout/list.rs:746` `async fn collect_flat_rollout_files(`
- `fn` `codex-rs/core/src/rollout/list.rs:784` `async fn collect_rollout_day_files(`
- `struct` `codex-rs/core/src/rollout/list.rs:817` `struct ThreadCandidate {`
- `fn` `codex-rs/core/src/rollout/list.rs:823` `async fn collect_files_by_updated_at(`
- `fn` `codex-rs/core/src/rollout/list.rs:836` `async fn collect_flat_files_by_updated_at(`
- `fn` `codex-rs/core/src/rollout/list.rs:879` `async fn walk_rollout_files(`
- `struct` `codex-rs/core/src/rollout/list.rs:919` `struct ProviderMatcher<'a> {`
- `impl` `codex-rs/core/src/rollout/list.rs:924` `impl<'a> ProviderMatcher<'a> {`
- `fn` `codex-rs/core/src/rollout/list.rs:925` `fn new(filters: &'a [String], default_provider: &'a str) -> Option<Self> {`
- `fn` `codex-rs/core/src/rollout/list.rs:937` `fn matches(&self, session_provider: Option<&str>) -> bool {`
- `fn` `codex-rs/core/src/rollout/list.rs:945` `async fn read_head_summary(path: &Path, head_limit: usize) -> io::Result<HeadTailSummary> {`
- `use` `codex-rs/core/src/rollout/list.rs:946` `use tokio::io::AsyncBufReadExt;`
- `fn` `codex-rs/core/src/rollout/list.rs:1024` `pub async fn read_head_for_summary(path: &Path) -> io::Result<Vec<serde_json::Value>> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1031` `pub async fn read_session_meta_line(path: &Path) -> io::Result<SessionMetaLine> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1047` `async fn file_modified_time(path: &Path) -> io::Result<Option<OffsetDateTime>> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1059` `fn format_rfc3339(dt: OffsetDateTime) -> Option<String> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1063` `fn truncate_to_seconds(dt: OffsetDateTime) -> Option<OffsetDateTime> {`
- `fn` `codex-rs/core/src/rollout/list.rs:1067` `async fn find_thread_path_by_id_str_in_subdir(`
- `fn` `codex-rs/core/src/rollout/list.rs:1129` `pub async fn find_thread_path_by_id_str(`
- `fn` `codex-rs/core/src/rollout/list.rs:1137` `pub async fn find_archived_thread_path_by_id_str(`
- `fn` `codex-rs/core/src/rollout/list.rs:1145` `pub fn rollout_date_parts(file_name: &OsStr) -> Option<(String, String, String)> {`

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
- `use crate::instructions::UserInstructions;`
- `use crate::protocol::EventMsg;`
- `use crate::session_prefix::is_session_prefix_content;`
- `use crate::state_db;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
