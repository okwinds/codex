# `codex-rs/core/src/rollout/metadata.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14350`
- sha256: `a7fe550738ec2b6495763a346a4623df105c3cb8a6656f6b86c2d1b7db7ea86e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/metadata.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/metadata.rs:1` `use crate::config::Config;`
- `use` `codex-rs/core/src/rollout/metadata.rs:2` `use crate::rollout;`
- `use` `codex-rs/core/src/rollout/metadata.rs:3` `use crate::rollout::list::parse_timestamp_uuid_from_filename;`
- `use` `codex-rs/core/src/rollout/metadata.rs:4` `use crate::rollout::recorder::RolloutRecorder;`
- `use` `codex-rs/core/src/rollout/metadata.rs:5` `use chrono::DateTime;`
- `use` `codex-rs/core/src/rollout/metadata.rs:6` `use chrono::NaiveDateTime;`
- `use` `codex-rs/core/src/rollout/metadata.rs:7` `use chrono::Timelike;`
- `use` `codex-rs/core/src/rollout/metadata.rs:8` `use chrono::Utc;`
- `use` `codex-rs/core/src/rollout/metadata.rs:9` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/rollout/metadata.rs:10` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/metadata.rs:11` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/rollout/metadata.rs:12` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/metadata.rs:13` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/rollout/metadata.rs:14` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/rollout/metadata.rs:15` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/rollout/metadata.rs:16` `use codex_state::BackfillStats;`
- `use` `codex-rs/core/src/rollout/metadata.rs:17` `use codex_state::DB_ERROR_METRIC;`
- `use` `codex-rs/core/src/rollout/metadata.rs:18` `use codex_state::DB_METRIC_BACKFILL;`
- `use` `codex-rs/core/src/rollout/metadata.rs:19` `use codex_state::DB_METRIC_BACKFILL_DURATION_MS;`
- `use` `codex-rs/core/src/rollout/metadata.rs:20` `use codex_state::ExtractionOutcome;`
- `use` `codex-rs/core/src/rollout/metadata.rs:21` `use codex_state::ThreadMetadataBuilder;`
- `use` `codex-rs/core/src/rollout/metadata.rs:22` `use codex_state::apply_rollout_item;`
- `use` `codex-rs/core/src/rollout/metadata.rs:23` `use std::cmp::Reverse;`
- `use` `codex-rs/core/src/rollout/metadata.rs:24` `use std::path::Path;`
- `use` `codex-rs/core/src/rollout/metadata.rs:25` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/rollout/metadata.rs:26` `use tracing::info;`
- `use` `codex-rs/core/src/rollout/metadata.rs:27` `use tracing::warn;`
- `const` `codex-rs/core/src/rollout/metadata.rs:29` `const ROLLOUT_PREFIX: &str = "rollout-";`
- `const` `codex-rs/core/src/rollout/metadata.rs:30` `const ROLLOUT_SUFFIX: &str = ".jsonl";`
- `fn` `codex-rs/core/src/rollout/metadata.rs:250` `async fn file_modified_time_utc(path: &Path) -> Option<DateTime<Utc>> {`
- `fn` `codex-rs/core/src/rollout/metadata.rs:256` `fn parse_timestamp_to_utc(ts: &str) -> Option<DateTime<Utc>> {`
- `const` `codex-rs/core/src/rollout/metadata.rs:257` `const FILENAME_TS_FORMAT: &str = "%Y-%m-%dT%H-%M-%S";`
- `fn` `codex-rs/core/src/rollout/metadata.rs:268` `async fn collect_rollout_paths(root: &Path) -> std::io::Result<Vec<PathBuf>> {`
- `use` `codex-rs/core/src/rollout/metadata.rs:303` `use super::*;`
- `use` `codex-rs/core/src/rollout/metadata.rs:304` `use chrono::DateTime;`
- `use` `codex-rs/core/src/rollout/metadata.rs:305` `use chrono::NaiveDateTime;`
- `use` `codex-rs/core/src/rollout/metadata.rs:306` `use chrono::Timelike;`
- `use` `codex-rs/core/src/rollout/metadata.rs:307` `use chrono::Utc;`
- `use` `codex-rs/core/src/rollout/metadata.rs:308` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/metadata.rs:309` `use codex_protocol::protocol::CompactedItem;`
- `use` `codex-rs/core/src/rollout/metadata.rs:310` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/metadata.rs:311` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/core/src/rollout/metadata.rs:312` `use codex_protocol::protocol::SessionMeta;`
- `use` `codex-rs/core/src/rollout/metadata.rs:313` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/rollout/metadata.rs:314` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/rollout/metadata.rs:315` `use codex_state::ThreadMetadataBuilder;`
- `use` `codex-rs/core/src/rollout/metadata.rs:316` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/rollout/metadata.rs:317` `use std::fs::File;`
- `use` `codex-rs/core/src/rollout/metadata.rs:318` `use std::io::Write;`
- `use` `codex-rs/core/src/rollout/metadata.rs:319` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/rollout/metadata.rs:320` `use uuid::Uuid;`
- `fn` `codex-rs/core/src/rollout/metadata.rs:323` `async fn extract_metadata_from_rollout_uses_session_meta() {`
- `fn` `codex-rs/core/src/rollout/metadata.rs:370` `fn builder_from_items_falls_back_to_filename() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::Config;`
- `use crate::rollout;`
- `use crate::rollout::list::parse_timestamp_uuid_from_filename;`
- `use crate::rollout::recorder::RolloutRecorder;`
- `use chrono::DateTime;`
- `use chrono::NaiveDateTime;`
- `use chrono::Timelike;`
- `use chrono::Utc;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::protocol::SessionMetaLine;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_state::BackfillStats;`
- `use codex_state::DB_ERROR_METRIC;`
- `use codex_state::DB_METRIC_BACKFILL;`
- `use codex_state::DB_METRIC_BACKFILL_DURATION_MS;`
- `use codex_state::ExtractionOutcome;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
