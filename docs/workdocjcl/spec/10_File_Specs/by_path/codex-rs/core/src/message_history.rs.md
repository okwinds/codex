# `codex-rs/core/src/message_history.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19861`
- sha256: `eadfd39b185c3b2476c4d37ced709292300982f6a7b1a610db04b2bbd63a3bfd`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/message_history.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct HistoryEntry {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/message_history.rs:19` `use std::fs::File;`
- `use` `codex-rs/core/src/message_history.rs:20` `use std::fs::OpenOptions;`
- `use` `codex-rs/core/src/message_history.rs:21` `use std::io::BufRead;`
- `use` `codex-rs/core/src/message_history.rs:22` `use std::io::BufReader;`
- `use` `codex-rs/core/src/message_history.rs:23` `use std::io::Read;`
- `use` `codex-rs/core/src/message_history.rs:24` `use std::io::Result;`
- `use` `codex-rs/core/src/message_history.rs:25` `use std::io::Seek;`
- `use` `codex-rs/core/src/message_history.rs:26` `use std::io::SeekFrom;`
- `use` `codex-rs/core/src/message_history.rs:27` `use std::io::Write;`
- `use` `codex-rs/core/src/message_history.rs:28` `use std::path::Path;`
- `use` `codex-rs/core/src/message_history.rs:29` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/message_history.rs:31` `use serde::Deserialize;`
- `use` `codex-rs/core/src/message_history.rs:32` `use serde::Serialize;`
- `use` `codex-rs/core/src/message_history.rs:34` `use std::time::Duration;`
- `use` `codex-rs/core/src/message_history.rs:35` `use tokio::fs;`
- `use` `codex-rs/core/src/message_history.rs:36` `use tokio::io::AsyncReadExt;`
- `use` `codex-rs/core/src/message_history.rs:38` `use crate::config::Config;`
- `use` `codex-rs/core/src/message_history.rs:39` `use crate::config::types::HistoryPersistence;`
- `use` `codex-rs/core/src/message_history.rs:41` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/message_history.rs:43` `use std::os::unix::fs::OpenOptionsExt;`
- `use` `codex-rs/core/src/message_history.rs:45` `use std::os::unix::fs::PermissionsExt;`
- `const` `codex-rs/core/src/message_history.rs:48` `const HISTORY_FILENAME: &str = "history.jsonl";`
- `const` `codex-rs/core/src/message_history.rs:51` `const HISTORY_SOFT_CAP_RATIO: f64 = 0.8;`
- `const` `codex-rs/core/src/message_history.rs:53` `const MAX_RETRIES: usize = 10;`
- `const` `codex-rs/core/src/message_history.rs:54` `const RETRY_SLEEP: Duration = Duration::from_millis(100);`
- `struct` `codex-rs/core/src/message_history.rs:57` `pub struct HistoryEntry {`
- `fn` `codex-rs/core/src/message_history.rs:63` `fn history_filepath(config: &Config) -> PathBuf {`
- `fn` `codex-rs/core/src/message_history.rs:163` `fn enforce_history_limit(file: &mut File, max_bytes: Option<usize>) -> Result<()> {`
- `fn` `codex-rs/core/src/message_history.rs:238` `fn trim_target_bytes(max_bytes: u64, newest_entry_len: u64) -> u64 {`
- `fn` `codex-rs/core/src/message_history.rs:269` `async fn ensure_owner_only_permissions(file: &File) -> Result<()> {`
- `fn` `codex-rs/core/src/message_history.rs:284` `async fn ensure_owner_only_permissions(_file: &File) -> Result<()> {`
- `fn` `codex-rs/core/src/message_history.rs:288` `async fn history_metadata_for_file(path: &Path) -> (u64, usize) {`
- `fn` `codex-rs/core/src/message_history.rs:317` `fn lookup_history_entry(path: &Path, log_id: u64, offset: usize) -> Option<HistoryEntry> {`
- `use` `codex-rs/core/src/message_history.rs:318` `use std::io::BufRead;`
- `use` `codex-rs/core/src/message_history.rs:319` `use std::io::BufReader;`
- `fn` `codex-rs/core/src/message_history.rs:387` `fn history_log_id(metadata: &std::fs::Metadata) -> Option<u64> {`
- `use` `codex-rs/core/src/message_history.rs:388` `use std::os::unix::fs::MetadataExt;`
- `fn` `codex-rs/core/src/message_history.rs:393` `fn history_log_id(metadata: &std::fs::Metadata) -> Option<u64> {`
- `use` `codex-rs/core/src/message_history.rs:394` `use std::os::windows::fs::MetadataExt;`
- `fn` `codex-rs/core/src/message_history.rs:399` `fn history_log_id(_metadata: &std::fs::Metadata) -> Option<u64> {`
- `use` `codex-rs/core/src/message_history.rs:405` `use super::*;`
- `use` `codex-rs/core/src/message_history.rs:406` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/message_history.rs:407` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/message_history.rs:408` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/message_history.rs:409` `use std::fs::File;`
- `use` `codex-rs/core/src/message_history.rs:410` `use std::io::Write;`
- `use` `codex-rs/core/src/message_history.rs:411` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/message_history.rs:414` `async fn lookup_reads_history_entries() {`
- `fn` `codex-rs/core/src/message_history.rs:450` `async fn lookup_uses_stable_log_id_after_appends() {`
- `fn` `codex-rs/core/src/message_history.rs:493` `async fn append_entry_trims_history_when_beyond_max_bytes() {`
- `fn` `codex-rs/core/src/message_history.rs:540` `async fn append_entry_trims_history_to_soft_cap() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::File;`
- `use std::fs::OpenOptions;`
- `use std::io::BufRead;`
- `use std::io::BufReader;`
- `use std::io::Read;`
- `use std::io::Result;`
- `use std::io::Seek;`
- `use std::io::SeekFrom;`
- `use std::io::Write;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::time::Duration;`
- `use tokio::fs;`
- `use tokio::io::AsyncReadExt;`
- `use crate::config::Config;`
- `use crate::config::types::HistoryPersistence;`
- `use codex_protocol::ThreadId;`
- `use std::os::unix::fs::OpenOptionsExt;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
