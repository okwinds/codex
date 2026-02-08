# `codex-rs/core/src/rollout/tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `35492`
- sha256: `d51190626899087c2666f75d1e287fe6e9661978bd7346c9c9ed2d8fb7589be4`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/rollout/tests.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/rollout/tests.rs:3` `use std::ffi::OsStr;`
- `use` `codex-rs/core/src/rollout/tests.rs:4` `use std::fs::File;`
- `use` `codex-rs/core/src/rollout/tests.rs:5` `use std::fs::FileTimes;`
- `use` `codex-rs/core/src/rollout/tests.rs:6` `use std::fs::{self};`
- `use` `codex-rs/core/src/rollout/tests.rs:7` `use std::io::Write;`
- `use` `codex-rs/core/src/rollout/tests.rs:8` `use std::path::Path;`
- `use` `codex-rs/core/src/rollout/tests.rs:10` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/rollout/tests.rs:11` `use tempfile::TempDir;`
- `use` `codex-rs/core/src/rollout/tests.rs:12` `use time::Duration;`
- `use` `codex-rs/core/src/rollout/tests.rs:13` `use time::OffsetDateTime;`
- `use` `codex-rs/core/src/rollout/tests.rs:14` `use time::PrimitiveDateTime;`
- `use` `codex-rs/core/src/rollout/tests.rs:15` `use time::format_description::FormatItem;`
- `use` `codex-rs/core/src/rollout/tests.rs:16` `use time::macros::format_description;`
- `use` `codex-rs/core/src/rollout/tests.rs:17` `use uuid::Uuid;`
- `use` `codex-rs/core/src/rollout/tests.rs:19` `use crate::rollout::INTERACTIVE_SESSION_SOURCES;`
- `use` `codex-rs/core/src/rollout/tests.rs:20` `use crate::rollout::list::Cursor;`
- `use` `codex-rs/core/src/rollout/tests.rs:21` `use crate::rollout::list::ThreadItem;`
- `use` `codex-rs/core/src/rollout/tests.rs:22` `use crate::rollout::list::ThreadSortKey;`
- `use` `codex-rs/core/src/rollout/tests.rs:23` `use crate::rollout::list::ThreadsPage;`
- `use` `codex-rs/core/src/rollout/tests.rs:24` `use crate::rollout::list::get_threads;`
- `use` `codex-rs/core/src/rollout/tests.rs:25` `use crate::rollout::rollout_date_parts;`
- `use` `codex-rs/core/src/rollout/tests.rs:26` `use anyhow::Result;`
- `use` `codex-rs/core/src/rollout/tests.rs:27` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/rollout/tests.rs:28` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/rollout/tests.rs:29` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/rollout/tests.rs:30` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/rollout/tests.rs:31` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/rollout/tests.rs:32` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/core/src/rollout/tests.rs:33` `use codex_protocol::protocol::SessionMeta;`
- `use` `codex-rs/core/src/rollout/tests.rs:34` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/core/src/rollout/tests.rs:35` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/rollout/tests.rs:36` `use codex_protocol::protocol::UserMessageEvent;`
- `const` `codex-rs/core/src/rollout/tests.rs:38` `const NO_SOURCE_FILTER: &[SessionSource] = &[];`
- `const` `codex-rs/core/src/rollout/tests.rs:39` `const TEST_PROVIDER: &str = "test-provider";`
- `fn` `codex-rs/core/src/rollout/tests.rs:41` `fn provider_vec(providers: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/rollout/tests.rs:49` `fn rollout_date_parts_extracts_directory_components() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:58` `fn write_session_file(`
- `fn` `codex-rs/core/src/rollout/tests.rs:75` `fn write_session_file_with_provider(`
- `fn` `codex-rs/core/src/rollout/tests.rs:146` `fn write_session_file_with_delayed_user_event(`
- `fn` `codex-rs/core/src/rollout/tests.rs:203` `fn write_session_file_with_meta_payload(`
- `fn` `codex-rs/core/src/rollout/tests.rs:246` `async fn test_list_conversations_latest_first() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:378` `async fn test_pagination_cursor() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:612` `async fn test_list_threads_scans_past_head_for_user_event() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:637` `async fn test_get_thread_contents() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:718` `async fn test_base_instructions_missing_in_meta_defaults_to_null() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:760` `async fn test_base_instructions_present_in_meta_is_preserved() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:805` `async fn test_created_at_sort_uses_file_mtime_for_updated_at() -> Result<()> {`
- `fn` `codex-rs/core/src/rollout/tests.rs:851` `async fn test_updated_at_uses_file_mtime() -> Result<()> {`
- `fn` `codex-rs/core/src/rollout/tests.rs:939` `async fn test_stable_ordering_same_second_pagination() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:1047` `async fn test_source_filter_excludes_non_matching_sessions() {`
- `fn` `codex-rs/core/src/rollout/tests.rs:1120` `async fn test_model_provider_filter_selects_only_matching_sessions() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsStr;`
- `use std::fs::File;`
- `use std::fs::FileTimes;`
- `use std::fs::{self};`
- `use std::io::Write;`
- `use std::path::Path;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use time::Duration;`
- `use time::OffsetDateTime;`
- `use time::PrimitiveDateTime;`
- `use time::format_description::FormatItem;`
- `use time::macros::format_description;`
- `use uuid::Uuid;`
- `use crate::rollout::INTERACTIVE_SESSION_SOURCES;`
- `use crate::rollout::list::Cursor;`
- `use crate::rollout::list::ThreadItem;`
- `use crate::rollout::list::ThreadSortKey;`
- `use crate::rollout::list::ThreadsPage;`
- `use crate::rollout::list::get_threads;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
