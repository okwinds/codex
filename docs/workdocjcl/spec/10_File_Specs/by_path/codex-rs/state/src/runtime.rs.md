# `codex-rs/state/src/runtime.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `46594`
- sha256: `03cf38641cde6a4f65f196a4a091e29f549f3c0745f16dee34a825b778bf3c72`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/runtime.rs` (read)

### Outputs / Side Effects
- reads/writes SQLite or DB
- writes to filesystem

## Public Surface (auto)
- `pub struct StateRuntime {`
- `pub fn codex_home(&self) -> &Path {`
- `pub fn state_db_filename() -> String {`
- `pub fn state_db_path(codex_home: &Path) -> PathBuf {`

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/runtime.rs:1` `use crate::DB_ERROR_METRIC;`
- `use` `codex-rs/state/src/runtime.rs:2` `use crate::LogEntry;`
- `use` `codex-rs/state/src/runtime.rs:3` `use crate::LogQuery;`
- `use` `codex-rs/state/src/runtime.rs:4` `use crate::LogRow;`
- `use` `codex-rs/state/src/runtime.rs:5` `use crate::SortKey;`
- `use` `codex-rs/state/src/runtime.rs:6` `use crate::ThreadMemory;`
- `use` `codex-rs/state/src/runtime.rs:7` `use crate::ThreadMetadata;`
- `use` `codex-rs/state/src/runtime.rs:8` `use crate::ThreadMetadataBuilder;`
- `use` `codex-rs/state/src/runtime.rs:9` `use crate::ThreadsPage;`
- `use` `codex-rs/state/src/runtime.rs:10` `use crate::apply_rollout_item;`
- `use` `codex-rs/state/src/runtime.rs:11` `use crate::migrations::MIGRATOR;`
- `use` `codex-rs/state/src/runtime.rs:12` `use crate::model::ThreadMemoryRow;`
- `use` `codex-rs/state/src/runtime.rs:13` `use crate::model::ThreadRow;`
- `use` `codex-rs/state/src/runtime.rs:14` `use crate::model::anchor_from_item;`
- `use` `codex-rs/state/src/runtime.rs:15` `use crate::model::datetime_to_epoch_seconds;`
- `use` `codex-rs/state/src/runtime.rs:16` `use crate::paths::file_modified_time_utc;`
- `use` `codex-rs/state/src/runtime.rs:17` `use chrono::DateTime;`
- `use` `codex-rs/state/src/runtime.rs:18` `use chrono::Utc;`
- `use` `codex-rs/state/src/runtime.rs:19` `use codex_otel::OtelManager;`
- `use` `codex-rs/state/src/runtime.rs:20` `use codex_protocol::ThreadId;`
- `use` `codex-rs/state/src/runtime.rs:21` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/state/src/runtime.rs:22` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/state/src/runtime.rs:23` `use log::LevelFilter;`
- `use` `codex-rs/state/src/runtime.rs:24` `use serde_json::Value;`
- `use` `codex-rs/state/src/runtime.rs:25` `use sqlx::ConnectOptions;`
- `use` `codex-rs/state/src/runtime.rs:26` `use sqlx::QueryBuilder;`
- `use` `codex-rs/state/src/runtime.rs:27` `use sqlx::Row;`
- `use` `codex-rs/state/src/runtime.rs:28` `use sqlx::Sqlite;`
- `use` `codex-rs/state/src/runtime.rs:29` `use sqlx::SqlitePool;`
- `use` `codex-rs/state/src/runtime.rs:30` `use sqlx::sqlite::SqliteConnectOptions;`
- `use` `codex-rs/state/src/runtime.rs:31` `use sqlx::sqlite::SqliteJournalMode;`
- `use` `codex-rs/state/src/runtime.rs:32` `use sqlx::sqlite::SqlitePoolOptions;`
- `use` `codex-rs/state/src/runtime.rs:33` `use sqlx::sqlite::SqliteSynchronous;`
- `use` `codex-rs/state/src/runtime.rs:34` `use std::path::Path;`
- `use` `codex-rs/state/src/runtime.rs:35` `use std::path::PathBuf;`
- `use` `codex-rs/state/src/runtime.rs:36` `use std::sync::Arc;`
- `use` `codex-rs/state/src/runtime.rs:37` `use std::time::Duration;`
- `use` `codex-rs/state/src/runtime.rs:38` `use tracing::warn;`
- `const` `codex-rs/state/src/runtime.rs:40` `pub const STATE_DB_FILENAME: &str = "state";`
- `const` `codex-rs/state/src/runtime.rs:41` `pub const STATE_DB_VERSION: u32 = 4;`
- `const` `codex-rs/state/src/runtime.rs:43` `const METRIC_DB_INIT: &str = "codex.db.init";`
- `struct` `codex-rs/state/src/runtime.rs:46` `pub struct StateRuntime {`
- `impl` `codex-rs/state/src/runtime.rs:52` `impl StateRuntime {`
- `fn` `codex-rs/state/src/runtime.rs:56` `pub async fn init(`
- `fn` `codex-rs/state/src/runtime.rs:90` `pub fn codex_home(&self) -> &Path {`
- `fn` `codex-rs/state/src/runtime.rs:95` `pub async fn get_backfill_state(&self) -> anyhow::Result<crate::BackfillState> {`
- `fn` `codex-rs/state/src/runtime.rs:110` `pub async fn mark_backfill_running(&self) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:127` `pub async fn checkpoint_backfill(&self, watermark: &str) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:145` `pub async fn mark_backfill_complete(&self, last_watermark: Option<&str>) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:169` `pub async fn get_thread(&self, id: ThreadId) -> anyhow::Result<Option<crate::ThreadMetadata>> {`
- `fn` `codex-rs/state/src/runtime.rs:202` `pub async fn get_dynamic_tools(`
- `fn` `codex-rs/state/src/runtime.rs:234` `pub async fn get_thread_memory(`
- `fn` `codex-rs/state/src/runtime.rs:254` `pub async fn find_rollout_path_by_id(`
- `fn` `codex-rs/state/src/runtime.rs:278` `pub async fn list_threads(`
- `fn` `codex-rs/state/src/runtime.rs:344` `pub async fn insert_log(&self, entry: &LogEntry) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:349` `pub async fn insert_logs(&self, entries: &[LogEntry]) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:381` `pub async fn query_logs(&self, query: &LogQuery) -> anyhow::Result<Vec<LogRow>> {`
- `fn` `codex-rs/state/src/runtime.rs:403` `pub async fn max_log_id(&self, query: &LogQuery) -> anyhow::Result<i64> {`
- `fn` `codex-rs/state/src/runtime.rs:413` `pub async fn list_thread_ids(`
- `fn` `codex-rs/state/src/runtime.rs:443` `pub async fn upsert_thread(&self, metadata: &crate::ThreadMetadata) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:512` `pub async fn upsert_thread_memory(`
- `fn` `codex-rs/state/src/runtime.rs:553` `pub async fn get_last_n_thread_memories_for_cwd(`
- `fn` `codex-rs/state/src/runtime.rs:590` `pub async fn persist_dynamic_tools(`
- `fn` `codex-rs/state/src/runtime.rs:631` `pub async fn apply_rollout_items(`
- `fn` `codex-rs/state/src/runtime.rs:674` `pub async fn mark_archived(`
- `fn` `codex-rs/state/src/runtime.rs:698` `pub async fn mark_unarchived(`
- `fn` `codex-rs/state/src/runtime.rs:720` `async fn ensure_backfill_state_row(&self) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:797` `fn extract_dynamic_tools(items: &[RolloutItem]) -> Option<Option<Vec<DynamicToolSpec>>> {`
- `fn` `codex-rs/state/src/runtime.rs:807` `async fn open_sqlite(path: &Path) -> anyhow::Result<SqlitePool> {`
- `fn` `codex-rs/state/src/runtime.rs:823` `pub fn state_db_filename() -> String {`
- `fn` `codex-rs/state/src/runtime.rs:827` `pub fn state_db_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/state/src/runtime.rs:831` `async fn remove_legacy_state_files(codex_home: &Path) {`
- `fn` `codex-rs/state/src/runtime.rs:868` `fn should_remove_state_file(file_name: &str, current_name: &str) -> bool {`
- `fn` `codex-rs/state/src/runtime.rs:947` `fn push_thread_order_and_limit(`
- `use` `codex-rs/state/src/runtime.rs:965` `use super::STATE_DB_FILENAME;`
- `use` `codex-rs/state/src/runtime.rs:966` `use super::STATE_DB_VERSION;`
- `use` `codex-rs/state/src/runtime.rs:967` `use super::StateRuntime;`
- `use` `codex-rs/state/src/runtime.rs:968` `use super::ThreadMetadata;`
- `use` `codex-rs/state/src/runtime.rs:969` `use super::state_db_filename;`
- `use` `codex-rs/state/src/runtime.rs:970` `use chrono::DateTime;`
- `use` `codex-rs/state/src/runtime.rs:971` `use chrono::Utc;`
- `use` `codex-rs/state/src/runtime.rs:972` `use codex_protocol::ThreadId;`
- `use` `codex-rs/state/src/runtime.rs:973` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/state/src/runtime.rs:974` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/state/src/runtime.rs:975` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/state/src/runtime.rs:976` `use sqlx::Row;`
- `use` `codex-rs/state/src/runtime.rs:977` `use std::path::Path;`
- `use` `codex-rs/state/src/runtime.rs:978` `use std::path::PathBuf;`
- `use` `codex-rs/state/src/runtime.rs:979` `use std::time::SystemTime;`
- `use` `codex-rs/state/src/runtime.rs:980` `use std::time::UNIX_EPOCH;`
- `use` `codex-rs/state/src/runtime.rs:981` `use uuid::Uuid;`
- `fn` `codex-rs/state/src/runtime.rs:983` `fn unique_temp_dir() -> PathBuf {`
- `fn` `codex-rs/state/src/runtime.rs:994` `async fn init_removes_legacy_state_db_files() {`
- `fn` `codex-rs/state/src/runtime.rs:1069` `async fn backfill_state_persists_progress_and_completion() {`
- `fn` `codex-rs/state/src/runtime.rs:1122` `async fn upsert_and_get_thread_memory() {`
- `fn` `codex-rs/state/src/runtime.rs:1167` `async fn get_last_n_thread_memories_for_cwd_matches_exactly() {`
- `fn` `codex-rs/state/src/runtime.rs:1237` `async fn upsert_thread_memory_errors_for_unknown_thread() {`
- `fn` `codex-rs/state/src/runtime.rs:1258` `async fn get_last_n_thread_memories_for_cwd_zero_returns_empty() {`
- `fn` `codex-rs/state/src/runtime.rs:1285` `async fn get_last_n_thread_memories_for_cwd_does_not_prefix_match() {`
- `fn` `codex-rs/state/src/runtime.rs:1332` `async fn deleting_thread_cascades_thread_memory() {`
- `fn` `codex-rs/state/src/runtime.rs:1385` `fn test_thread_metadata(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::DB_ERROR_METRIC;`
- `use crate::LogEntry;`
- `use crate::LogQuery;`
- `use crate::LogRow;`
- `use crate::SortKey;`
- `use crate::ThreadMemory;`
- `use crate::ThreadMetadata;`
- `use crate::ThreadMetadataBuilder;`
- `use crate::ThreadsPage;`
- `use crate::apply_rollout_item;`
- `use crate::migrations::MIGRATOR;`
- `use crate::model::ThreadMemoryRow;`
- `use crate::model::ThreadRow;`
- `use crate::model::anchor_from_item;`
- `use crate::model::datetime_to_epoch_seconds;`
- `use crate::paths::file_modified_time_utc;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::ThreadId;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
