# `codex-rs/core/src/rollout/session_index.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12534`
- sha256: `bd946f9bf11f60c75e544c99a552cbc18b39b09506c367ce657d953497e6c886`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/session_index.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct SessionIndexEntry {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/session_index.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/rollout/session_index.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/rollout/session_index.rs:3` `use std::fs::File;`
- `use` `codex-rs/core/src/rollout/session_index.rs:4` `use std::io::Read;`
- `use` `codex-rs/core/src/rollout/session_index.rs:5` `use std::io::Seek;`
- `use` `codex-rs/core/src/rollout/session_index.rs:6` `use std::io::SeekFrom;`
- `use` `codex-rs/core/src/rollout/session_index.rs:7` `use std::path::Path;`
- `use` `codex-rs/core/src/rollout/session_index.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/rollout/session_index.rs:10` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/session_index.rs:11` `use serde::Deserialize;`
- `use` `codex-rs/core/src/rollout/session_index.rs:12` `use serde::Serialize;`
- `use` `codex-rs/core/src/rollout/session_index.rs:13` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/core/src/rollout/session_index.rs:14` `use tokio::io::AsyncWriteExt;`
- `const` `codex-rs/core/src/rollout/session_index.rs:16` `const SESSION_INDEX_FILE: &str = "session_index.jsonl";`
- `const` `codex-rs/core/src/rollout/session_index.rs:17` `const READ_CHUNK_SIZE: usize = 8192;`
- `struct` `codex-rs/core/src/rollout/session_index.rs:20` `pub struct SessionIndexEntry {`
- `fn` `codex-rs/core/src/rollout/session_index.rs:28` `pub async fn append_thread_name(`
- `use` `codex-rs/core/src/rollout/session_index.rs:33` `use time::OffsetDateTime;`
- `use` `codex-rs/core/src/rollout/session_index.rs:34` `use time::format_description::well_known::Rfc3339;`
- `fn` `codex-rs/core/src/rollout/session_index.rs:49` `pub async fn append_session_index_entry(`
- `fn` `codex-rs/core/src/rollout/session_index.rs:67` `pub async fn find_thread_name_by_id(`
- `fn` `codex-rs/core/src/rollout/session_index.rs:83` `pub async fn find_thread_names_by_ids(`
- `fn` `codex-rs/core/src/rollout/session_index.rs:115` `pub async fn find_thread_id_by_name(`
- `fn` `codex-rs/core/src/rollout/session_index.rs:135` `pub async fn find_thread_path_by_name_str(`
- `fn` `codex-rs/core/src/rollout/session_index.rs:145` `fn session_index_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/core/src/rollout/session_index.rs:149` `fn scan_index_from_end_by_id(`
- `fn` `codex-rs/core/src/rollout/session_index.rs:156` `fn scan_index_from_end_by_name(`
- `use` `codex-rs/core/src/rollout/session_index.rs:233` `use super::*;`
- `use` `codex-rs/core/src/rollout/session_index.rs:234` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/rollout/session_index.rs:235` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/rollout/session_index.rs:236` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/rollout/session_index.rs:237` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/rollout/session_index.rs:238` `fn write_index(path: &Path, lines: &[SessionIndexEntry]) -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/session_index.rs:248` `fn find_thread_id_by_name_prefers_latest_entry() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/session_index.rs:273` `fn find_thread_name_by_id_prefers_latest_entry() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/session_index.rs:300` `fn scan_index_returns_none_when_entry_missing() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/session_index.rs:320` `async fn find_thread_names_by_ids_prefers_latest_entry() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/rollout/session_index.rs:358` `fn scan_index_finds_latest_match_among_mixed_entries() -> std::io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::fs::File;`
- `use std::io::Read;`
- `use std::io::Seek;`
- `use std::io::SeekFrom;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_protocol::ThreadId;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::io::AsyncWriteExt;`
- `use time::OffsetDateTime;`
- `use time::format_description::well_known::Rfc3339;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
