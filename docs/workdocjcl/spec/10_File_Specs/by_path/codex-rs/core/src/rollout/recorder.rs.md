# `codex-rs/core/src/rollout/recorder.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `22995`
- sha256: `03286b8e9cd540a270804b9c5f3462d353eb93737fd1235fc07e4a5ddb49ea9f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/recorder.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct RolloutRecorder {`
- `pub enum RolloutRecorderParams {`
- `pub fn new(`
- `pub fn resume(path: PathBuf) -> Self {`
- `pub fn rollout_path(&self) -> &Path {`
- `pub fn state_db(&self) -> Option<StateDbHandle> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/recorder.rs:3` `use std::fs::File;`
- `use` `codex-rs/core/src/rollout/recorder.rs:4` `use std::fs::{self};`
- `use` `codex-rs/core/src/rollout/recorder.rs:5` `use std::io::Error as IoError;`
- `use` `codex-rs/core/src/rollout/recorder.rs:6` `use std::path::Path;`
- `use` `codex-rs/core/src/rollout/recorder.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/rollout/recorder.rs:9` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/recorder.rs:10` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/core/src/rollout/recorder.rs:11` `use codex_protocol::models::BaseInstructions;`
- `use` `codex-rs/core/src/rollout/recorder.rs:12` `use serde_json::Value;`
- `use` `codex-rs/core/src/rollout/recorder.rs:13` `use time::OffsetDateTime;`
- `use` `codex-rs/core/src/rollout/recorder.rs:14` `use time::format_description::FormatItem;`
- `use` `codex-rs/core/src/rollout/recorder.rs:15` `use time::macros::format_description;`
- `use` `codex-rs/core/src/rollout/recorder.rs:16` `use tokio::io::AsyncWriteExt;`
- `use` `codex-rs/core/src/rollout/recorder.rs:17` `use tokio::sync::mpsc::Sender;`
- `use` `codex-rs/core/src/rollout/recorder.rs:18` `use tokio::sync::mpsc::{self};`
- `use` `codex-rs/core/src/rollout/recorder.rs:19` `use tokio::sync::oneshot;`
- `use` `codex-rs/core/src/rollout/recorder.rs:20` `use tracing::info;`
- `use` `codex-rs/core/src/rollout/recorder.rs:21` `use tracing::warn;`
- `use` `codex-rs/core/src/rollout/recorder.rs:23` `use super::ARCHIVED_SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/rollout/recorder.rs:24` `use super::SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/rollout/recorder.rs:25` `use super::list::Cursor;`
- `use` `codex-rs/core/src/rollout/recorder.rs:26` `use super::list::ThreadListConfig;`
- `use` `codex-rs/core/src/rollout/recorder.rs:27` `use super::list::ThreadListLayout;`
- `use` `codex-rs/core/src/rollout/recorder.rs:28` `use super::list::ThreadSortKey;`
- `use` `codex-rs/core/src/rollout/recorder.rs:29` `use super::list::ThreadsPage;`
- `use` `codex-rs/core/src/rollout/recorder.rs:30` `use super::list::get_threads;`
- `use` `codex-rs/core/src/rollout/recorder.rs:31` `use super::list::get_threads_in_root;`
- `use` `codex-rs/core/src/rollout/recorder.rs:32` `use super::metadata;`
- `use` `codex-rs/core/src/rollout/recorder.rs:33` `use super::policy::is_persisted_response_item;`
- `use` `codex-rs/core/src/rollout/recorder.rs:34` `use crate::config::Config;`
- `use` `codex-rs/core/src/rollout/recorder.rs:35` `use crate::default_client::originator;`
- `use` `codex-rs/core/src/rollout/recorder.rs:36` `use crate::git_info::collect_git_info;`
- `use` `codex-rs/core/src/rollout/recorder.rs:37` `use crate::path_utils;`
- `use` `codex-rs/core/src/rollout/recorder.rs:38` `use crate::state_db;`
- `use` `codex-rs/core/src/rollout/recorder.rs:39` `use crate::state_db::StateDbHandle;`
- `use` `codex-rs/core/src/rollout/recorder.rs:40` `use codex_protocol::protocol::InitialHistory;`
- `use` `codex-rs/core/src/rollout/recorder.rs:41` `use codex_protocol::protocol::ResumedHistory;`
- `use` `codex-rs/core/src/rollout/recorder.rs:42` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/recorder.rs:43` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/core/src/rollout/recorder.rs:44` `use codex_protocol::protocol::SessionMeta;`
- `use` `codex-rs/core/src/rollout/recorder.rs:45` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/rollout/recorder.rs:46` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/rollout/recorder.rs:47` `use codex_state::ThreadMetadataBuilder;`
- `struct` `codex-rs/core/src/rollout/recorder.rs:59` `pub struct RolloutRecorder {`
- `enum` `codex-rs/core/src/rollout/recorder.rs:66` `pub enum RolloutRecorderParams {`
- `enum` `codex-rs/core/src/rollout/recorder.rs:79` `enum RolloutCmd {`
- `impl` `codex-rs/core/src/rollout/recorder.rs:90` `impl RolloutRecorderParams {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:91` `pub fn new(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:107` `pub fn resume(path: PathBuf) -> Self {`
- `impl` `codex-rs/core/src/rollout/recorder.rs:112` `impl RolloutRecorder {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:114` `pub async fn list_threads(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:164` `pub async fn list_archived_threads(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:219` `pub async fn find_latest_thread_path(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:254` `pub async fn new(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:343` `pub fn rollout_path(&self) -> &Path {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:347` `pub fn state_db(&self) -> Option<StateDbHandle> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:371` `pub async fn flush(&self) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:446` `pub async fn get_rollout_history(path: &Path) -> std::io::Result<InitialHistory> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:463` `pub async fn shutdown(&self) -> std::io::Result<()> {`
- `struct` `codex-rs/core/src/rollout/recorder.rs:479` `struct LogFileInfo {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:493` `fn create_log_file(config: &Config, conversation_id: ThreadId) -> std::io::Result<LogFileInfo> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:529` `async fn rollout_writer(`
- `struct` `codex-rs/core/src/rollout/recorder.rs:613` `struct JsonlWriter {`
- `struct` `codex-rs/core/src/rollout/recorder.rs:618` `struct RolloutLineRef<'a> {`
- `impl` `codex-rs/core/src/rollout/recorder.rs:624` `impl JsonlWriter {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:625` `async fn write_rollout_item(&mut self, rollout_item: &RolloutItem) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:639` `async fn write_line(&mut self, item: &impl serde::Serialize) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:648` `fn select_resume_path(page: &ThreadsPage, filter_cwd: Option<&Path>) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:661` `fn session_cwd_matches(head: &[serde_json::Value], cwd: &Path) -> bool {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:674` `fn extract_session_cwd(head: &[serde_json::Value]) -> Option<PathBuf> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::File;`
- `use std::fs::{self};`
- `use std::io::Error as IoError;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use codex_protocol::models::BaseInstructions;`
- `use serde_json::Value;`
- `use time::OffsetDateTime;`
- `use time::format_description::FormatItem;`
- `use time::macros::format_description;`
- `use tokio::io::AsyncWriteExt;`
- `use tokio::sync::mpsc::Sender;`
- `use tokio::sync::mpsc::{self};`
- `use tokio::sync::oneshot;`
- `use tracing::info;`
- `use tracing::warn;`
- `use super::ARCHIVED_SESSIONS_SUBDIR;`
- `use super::SESSIONS_SUBDIR;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
