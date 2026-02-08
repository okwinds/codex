# `codex-rs/core/src/state_db.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17423`
- sha256: `291039b1c51bd778f643fe7940c67dca00bc13348ea7c51d77dd7d0db1c5c994`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/state_db.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn record_discrepancy(stage: &str, reason: &str) {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/state_db.rs:1` `use crate::config::Config;`
- `use` `codex-rs/core/src/state_db.rs:2` `use crate::features::Feature;`
- `use` `codex-rs/core/src/state_db.rs:3` `use crate::rollout::list::Cursor;`
- `use` `codex-rs/core/src/state_db.rs:4` `use crate::rollout::list::ThreadSortKey;`
- `use` `codex-rs/core/src/state_db.rs:5` `use crate::rollout::metadata;`
- `use` `codex-rs/core/src/state_db.rs:6` `use chrono::DateTime;`
- `use` `codex-rs/core/src/state_db.rs:7` `use chrono::NaiveDateTime;`
- `use` `codex-rs/core/src/state_db.rs:8` `use chrono::Timelike;`
- `use` `codex-rs/core/src/state_db.rs:9` `use chrono::Utc;`
- `use` `codex-rs/core/src/state_db.rs:10` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/state_db.rs:11` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/state_db.rs:12` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/core/src/state_db.rs:13` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/state_db.rs:14` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/state_db.rs:15` `use codex_state::DB_METRIC_COMPARE_ERROR;`
- `use` `codex-rs/core/src/state_db.rs:17` `use codex_state::STATE_DB_VERSION;`
- `use` `codex-rs/core/src/state_db.rs:18` `use codex_state::ThreadMetadataBuilder;`
- `use` `codex-rs/core/src/state_db.rs:19` `use serde_json::Value;`
- `use` `codex-rs/core/src/state_db.rs:20` `use std::path::Path;`
- `use` `codex-rs/core/src/state_db.rs:21` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/state_db.rs:22` `use std::sync::Arc;`
- `use` `codex-rs/core/src/state_db.rs:23` `use tracing::warn;`
- `use` `codex-rs/core/src/state_db.rs:24` `use uuid::Uuid;`
- `type` `codex-rs/core/src/state_db.rs:27` `pub type StateDbHandle = Arc<codex_state::StateRuntime>;`
- `fn` `codex-rs/core/src/state_db.rs:80` `pub async fn get_state_db(config: &Config, otel: Option<&OtelManager>) -> Option<StateDbHandle> {`
- `fn` `codex-rs/core/src/state_db.rs:100` `pub async fn open_if_present(codex_home: &Path, default_provider: &str) -> Option<StateDbHandle> {`
- `fn` `codex-rs/core/src/state_db.rs:115` `async fn require_backfill_complete(`
- `fn` `codex-rs/core/src/state_db.rs:139` `fn cursor_to_anchor(cursor: Option<&Cursor>) -> Option<codex_state::Anchor> {`
- `fn` `codex-rs/core/src/state_db.rs:161` `pub async fn list_thread_ids_db(`
- `fn` `codex-rs/core/src/state_db.rs:215` `pub async fn list_threads_db(`
- `fn` `codex-rs/core/src/state_db.rs:267` `pub async fn find_rollout_path_by_id(`
- `fn` `codex-rs/core/src/state_db.rs:283` `pub async fn get_dynamic_tools(`
- `fn` `codex-rs/core/src/state_db.rs:299` `pub async fn persist_dynamic_tools(`
- `fn` `codex-rs/core/src/state_db.rs:314` `pub async fn get_thread_memory(`
- `fn` `codex-rs/core/src/state_db.rs:330` `pub async fn upsert_thread_memory(`
- `fn` `codex-rs/core/src/state_db.rs:351` `pub async fn get_last_n_thread_memories_for_cwd(`
- `fn` `codex-rs/core/src/state_db.rs:368` `pub async fn reconcile_rollout(`
- `fn` `codex-rs/core/src/state_db.rs:436` `pub async fn read_repair_rollout_path(`
- `fn` `codex-rs/core/src/state_db.rs:486` `pub async fn apply_rollout_items(`
- `fn` `codex-rs/core/src/state_db.rs:521` `pub fn record_discrepancy(stage: &str, reason: &str) {`
- `use` `codex-rs/core/src/state_db.rs:540` `use super::*;`
- `use` `codex-rs/core/src/state_db.rs:541` `use crate::rollout::list::parse_cursor;`
- `use` `codex-rs/core/src/state_db.rs:542` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/state_db.rs:545` `fn cursor_to_anchor_normalizes_timestamp_format() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::Config;`
- `use crate::features::Feature;`
- `use crate::rollout::list::Cursor;`
- `use crate::rollout::list::ThreadSortKey;`
- `use crate::rollout::metadata;`
- `use chrono::DateTime;`
- `use chrono::NaiveDateTime;`
- `use chrono::Timelike;`
- `use chrono::Utc;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_state::DB_METRIC_COMPARE_ERROR;`
- `use codex_state::STATE_DB_VERSION;`
- `use codex_state::ThreadMetadataBuilder;`
- `use serde_json::Value;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
