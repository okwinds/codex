# `codex-rs/core/src/rollout/recorder.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `32724`
- sha256: `9a9212545ccc0369f49bac5b7f9124a9edf2e46a5aa250feaf0e5e49efd451ba`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `use` `codex-rs/core/src/rollout/recorder.rs:9` `use chrono::SecondsFormat;`
- `use` `codex-rs/core/src/rollout/recorder.rs:10` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/recorder.rs:11` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/core/src/rollout/recorder.rs:12` `use codex_protocol::models::BaseInstructions;`
- `use` `codex-rs/core/src/rollout/recorder.rs:13` `use serde_json::Value;`
- `use` `codex-rs/core/src/rollout/recorder.rs:14` `use time::OffsetDateTime;`
- `use` `codex-rs/core/src/rollout/recorder.rs:15` `use time::format_description::FormatItem;`
- `use` `codex-rs/core/src/rollout/recorder.rs:16` `use time::macros::format_description;`
- `use` `codex-rs/core/src/rollout/recorder.rs:17` `use tokio::io::AsyncWriteExt;`
- `use` `codex-rs/core/src/rollout/recorder.rs:18` `use tokio::sync::mpsc::Sender;`
- `use` `codex-rs/core/src/rollout/recorder.rs:19` `use tokio::sync::mpsc::{self};`
- `use` `codex-rs/core/src/rollout/recorder.rs:20` `use tokio::sync::oneshot;`
- `use` `codex-rs/core/src/rollout/recorder.rs:21` `use tracing::info;`
- `use` `codex-rs/core/src/rollout/recorder.rs:22` `use tracing::trace;`
- `use` `codex-rs/core/src/rollout/recorder.rs:23` `use tracing::warn;`
- `use` `codex-rs/core/src/rollout/recorder.rs:25` `use super::ARCHIVED_SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/rollout/recorder.rs:26` `use super::SESSIONS_SUBDIR;`
- `use` `codex-rs/core/src/rollout/recorder.rs:27` `use super::list::Cursor;`
- `use` `codex-rs/core/src/rollout/recorder.rs:28` `use super::list::ThreadItem;`
- `use` `codex-rs/core/src/rollout/recorder.rs:29` `use super::list::ThreadListConfig;`
- `use` `codex-rs/core/src/rollout/recorder.rs:30` `use super::list::ThreadListLayout;`
- `use` `codex-rs/core/src/rollout/recorder.rs:31` `use super::list::ThreadSortKey;`
- `use` `codex-rs/core/src/rollout/recorder.rs:32` `use super::list::ThreadsPage;`
- `use` `codex-rs/core/src/rollout/recorder.rs:33` `use super::list::get_threads;`
- `use` `codex-rs/core/src/rollout/recorder.rs:34` `use super::list::get_threads_in_root;`
- `use` `codex-rs/core/src/rollout/recorder.rs:35` `use super::metadata;`
- `use` `codex-rs/core/src/rollout/recorder.rs:36` `use super::policy::is_persisted_response_item;`
- `use` `codex-rs/core/src/rollout/recorder.rs:37` `use crate::config::Config;`
- `use` `codex-rs/core/src/rollout/recorder.rs:38` `use crate::default_client::originator;`
- `use` `codex-rs/core/src/rollout/recorder.rs:39` `use crate::git_info::collect_git_info;`
- `use` `codex-rs/core/src/rollout/recorder.rs:40` `use crate::path_utils;`
- `use` `codex-rs/core/src/rollout/recorder.rs:41` `use crate::state_db;`
- `use` `codex-rs/core/src/rollout/recorder.rs:42` `use crate::state_db::StateDbHandle;`
- `use` `codex-rs/core/src/rollout/recorder.rs:43` `use codex_protocol::protocol::InitialHistory;`
- `use` `codex-rs/core/src/rollout/recorder.rs:44` `use codex_protocol::protocol::ResumedHistory;`
- `use` `codex-rs/core/src/rollout/recorder.rs:45` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/recorder.rs:46` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/core/src/rollout/recorder.rs:47` `use codex_protocol::protocol::SessionMeta;`
- `use` `codex-rs/core/src/rollout/recorder.rs:48` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/rollout/recorder.rs:49` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/rollout/recorder.rs:50` `use codex_state::StateRuntime;`
- `use` `codex-rs/core/src/rollout/recorder.rs:51` `use codex_state::ThreadMetadataBuilder;`
- `struct` `codex-rs/core/src/rollout/recorder.rs:63` `pub struct RolloutRecorder {`
- `enum` `codex-rs/core/src/rollout/recorder.rs:70` `pub enum RolloutRecorderParams {`
- `enum` `codex-rs/core/src/rollout/recorder.rs:83` `enum RolloutCmd {`
- `impl` `codex-rs/core/src/rollout/recorder.rs:97` `impl RolloutRecorderParams {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:98` `pub fn new(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:114` `pub fn resume(path: PathBuf) -> Self {`
- `impl` `codex-rs/core/src/rollout/recorder.rs:119` `impl RolloutRecorder {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:121` `pub async fn list_threads(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:144` `pub async fn list_archived_threads(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:167` `async fn list_threads_with_db_fallback(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:226` `pub async fn find_latest_thread_path(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:292` `pub async fn new(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:381` `pub fn rollout_path(&self) -> &Path {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:385` `pub fn state_db(&self) -> Option<StateDbHandle> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:411` `pub async fn persist(&self) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:422` `pub async fn flush(&self) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:497` `pub async fn get_rollout_history(path: &Path) -> std::io::Result<InitialHistory> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:514` `pub async fn shutdown(&self) -> std::io::Result<()> {`
- `struct` `codex-rs/core/src/rollout/recorder.rs:530` `struct LogFileInfo {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:541` `fn precompute_log_file_info(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:573` `fn open_log_file(path: &Path) -> std::io::Result<File> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:588` `async fn rollout_writer(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:720` `async fn write_session_meta(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:754` `async fn write_and_reconcile_items(`
- `struct` `codex-rs/core/src/rollout/recorder.rs:782` `struct JsonlWriter {`
- `struct` `codex-rs/core/src/rollout/recorder.rs:787` `struct RolloutLineRef<'a> {`
- `impl` `codex-rs/core/src/rollout/recorder.rs:793` `impl JsonlWriter {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:794` `async fn write_rollout_item(&mut self, rollout_item: &RolloutItem) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:808` `async fn write_line(&mut self, item: &impl serde::Serialize) -> std::io::Result<()> {`
- `impl` `codex-rs/core/src/rollout/recorder.rs:817` `impl From<codex_state::ThreadsPage> for ThreadsPage {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:818` `fn from(db_page: codex_state::ThreadsPage) -> Self {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:849` `fn select_resume_path(page: &ThreadsPage, filter_cwd: Option<&Path>) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/rollout/recorder.rs:866` `fn select_resume_path_from_db_page(`
- `fn` `codex-rs/core/src/rollout/recorder.rs:882` `fn cwd_matches(session_cwd: &Path, cwd: &Path) -> bool {`
- `use` `codex-rs/core/src/rollout/recorder.rs:894` `use super::*;`
- `use` `codex-rs/core/src/rollout/recorder.rs:895` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/rollout/recorder.rs:896` `use codex_protocol::protocol::AgentMessageEvent;`
- `use` `codex-rs/core/src/rollout/recorder.rs:897` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/rollout/recorder.rs:898` `use codex_protocol::protocol::UserMessageEvent;`
- `use` `codex-rs/core/src/rollout/recorder.rs:899` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/rollout/recorder.rs:902` `async fn recorder_materializes_only_after_explicit_persist() -> std::io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::File;`
- `use std::fs::{self};`
- `use std::io::Error as IoError;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use chrono::SecondsFormat;`
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
- `use tracing::trace;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
