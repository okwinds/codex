# `codex-rs/state/src/runtime.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `22553`
- sha256: `9f15aa2f5753bd148a31ca4561b2a20183a926d543e6ad9ac9444ae7529a50f3`
- generated_utc: `2026-02-03T16:08:30Z`

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

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/runtime.rs:1` `use crate::DB_ERROR_METRIC;`
- `use` `codex-rs/state/src/runtime.rs:2` `use crate::LogEntry;`
- `use` `codex-rs/state/src/runtime.rs:3` `use crate::LogQuery;`
- `use` `codex-rs/state/src/runtime.rs:4` `use crate::LogRow;`
- `use` `codex-rs/state/src/runtime.rs:5` `use crate::SortKey;`
- `use` `codex-rs/state/src/runtime.rs:6` `use crate::ThreadMetadata;`
- `use` `codex-rs/state/src/runtime.rs:7` `use crate::ThreadMetadataBuilder;`
- `use` `codex-rs/state/src/runtime.rs:8` `use crate::ThreadsPage;`
- `use` `codex-rs/state/src/runtime.rs:9` `use crate::apply_rollout_item;`
- `use` `codex-rs/state/src/runtime.rs:10` `use crate::migrations::MIGRATOR;`
- `use` `codex-rs/state/src/runtime.rs:11` `use crate::model::ThreadRow;`
- `use` `codex-rs/state/src/runtime.rs:12` `use crate::model::anchor_from_item;`
- `use` `codex-rs/state/src/runtime.rs:13` `use crate::model::datetime_to_epoch_seconds;`
- `use` `codex-rs/state/src/runtime.rs:14` `use crate::paths::file_modified_time_utc;`
- `use` `codex-rs/state/src/runtime.rs:15` `use chrono::DateTime;`
- `use` `codex-rs/state/src/runtime.rs:16` `use chrono::Utc;`
- `use` `codex-rs/state/src/runtime.rs:17` `use codex_otel::OtelManager;`
- `use` `codex-rs/state/src/runtime.rs:18` `use codex_protocol::ThreadId;`
- `use` `codex-rs/state/src/runtime.rs:19` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/state/src/runtime.rs:20` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/state/src/runtime.rs:21` `use log::LevelFilter;`
- `use` `codex-rs/state/src/runtime.rs:22` `use serde_json::Value;`
- `use` `codex-rs/state/src/runtime.rs:23` `use sqlx::ConnectOptions;`
- `use` `codex-rs/state/src/runtime.rs:24` `use sqlx::QueryBuilder;`
- `use` `codex-rs/state/src/runtime.rs:25` `use sqlx::Row;`
- `use` `codex-rs/state/src/runtime.rs:26` `use sqlx::Sqlite;`
- `use` `codex-rs/state/src/runtime.rs:27` `use sqlx::SqlitePool;`
- `use` `codex-rs/state/src/runtime.rs:28` `use sqlx::sqlite::SqliteConnectOptions;`
- `use` `codex-rs/state/src/runtime.rs:29` `use sqlx::sqlite::SqliteJournalMode;`
- `use` `codex-rs/state/src/runtime.rs:30` `use sqlx::sqlite::SqlitePoolOptions;`
- `use` `codex-rs/state/src/runtime.rs:31` `use sqlx::sqlite::SqliteSynchronous;`
- `use` `codex-rs/state/src/runtime.rs:32` `use std::path::Path;`
- `use` `codex-rs/state/src/runtime.rs:33` `use std::path::PathBuf;`
- `use` `codex-rs/state/src/runtime.rs:34` `use std::sync::Arc;`
- `use` `codex-rs/state/src/runtime.rs:35` `use std::time::Duration;`
- `use` `codex-rs/state/src/runtime.rs:36` `use tracing::warn;`
- `const` `codex-rs/state/src/runtime.rs:38` `pub const STATE_DB_FILENAME: &str = "state.sqlite";`
- `const` `codex-rs/state/src/runtime.rs:40` `const METRIC_DB_INIT: &str = "codex.db.init";`
- `struct` `codex-rs/state/src/runtime.rs:43` `pub struct StateRuntime {`
- `impl` `codex-rs/state/src/runtime.rs:49` `impl StateRuntime {`
- `fn` `codex-rs/state/src/runtime.rs:53` `pub async fn init(`
- `fn` `codex-rs/state/src/runtime.rs:86` `pub fn codex_home(&self) -> &Path {`
- `fn` `codex-rs/state/src/runtime.rs:91` `pub async fn get_thread(&self, id: ThreadId) -> anyhow::Result<Option<crate::ThreadMetadata>> {`
- `fn` `codex-rs/state/src/runtime.rs:123` `pub async fn get_dynamic_tools(`
- `fn` `codex-rs/state/src/runtime.rs:155` `pub async fn find_rollout_path_by_id(`
- `fn` `codex-rs/state/src/runtime.rs:179` `pub async fn list_threads(`
- `fn` `codex-rs/state/src/runtime.rs:244` `pub async fn insert_log(&self, entry: &LogEntry) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:249` `pub async fn insert_logs(&self, entries: &[LogEntry]) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:281` `pub async fn query_logs(&self, query: &LogQuery) -> anyhow::Result<Vec<LogRow>> {`
- `fn` `codex-rs/state/src/runtime.rs:303` `pub async fn max_log_id(&self, query: &LogQuery) -> anyhow::Result<i64> {`
- `fn` `codex-rs/state/src/runtime.rs:313` `pub async fn list_thread_ids(`
- `fn` `codex-rs/state/src/runtime.rs:343` `pub async fn upsert_thread(&self, metadata: &crate::ThreadMetadata) -> anyhow::Result<()> {`
- `fn` `codex-rs/state/src/runtime.rs:410` `pub async fn persist_dynamic_tools(`
- `fn` `codex-rs/state/src/runtime.rs:459` `pub async fn apply_rollout_items(`
- `fn` `codex-rs/state/src/runtime.rs:502` `pub async fn mark_archived(`
- `fn` `codex-rs/state/src/runtime.rs:526` `pub async fn mark_unarchived(`
- `fn` `codex-rs/state/src/runtime.rs:609` `fn extract_dynamic_tools(items: &[RolloutItem]) -> Option<Option<Vec<DynamicToolSpec>>> {`
- `fn` `codex-rs/state/src/runtime.rs:619` `async fn open_sqlite(path: &Path) -> anyhow::Result<SqlitePool> {`
- `fn` `codex-rs/state/src/runtime.rs:688` `fn push_thread_order_and_limit(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::DB_ERROR_METRIC;`
- `use crate::LogEntry;`
- `use crate::LogQuery;`
- `use crate::LogRow;`
- `use crate::SortKey;`
- `use crate::ThreadMetadata;`
- `use crate::ThreadMetadataBuilder;`
- `use crate::ThreadsPage;`
- `use crate::apply_rollout_item;`
- `use crate::migrations::MIGRATOR;`
- `use crate::model::ThreadRow;`
- `use crate::model::anchor_from_item;`
- `use crate::model::datetime_to_epoch_seconds;`
- `use crate::paths::file_modified_time_utc;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use codex_protocol::protocol::RolloutItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/02_Data/ENTITIES.md`
