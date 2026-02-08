# `codex-rs/core/src/util.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5688`
- sha256: `934368240f709ac70d6388398654b1c9af8b7885bb50741bb87a7be492b0029b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/util.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn resolve_path(base: &Path, path: &PathBuf) -> PathBuf {`
- `pub fn normalize_thread_name(name: &str) -> Option<String> {`
- `pub fn resume_command(thread_name: Option<&str>, thread_id: Option<ThreadId>) -> Option<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/util.rs:1` `use std::path::Path;`
- `use` `codex-rs/core/src/util.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/util.rs:3` `use std::time::Duration;`
- `use` `codex-rs/core/src/util.rs:5` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/util.rs:6` `use rand::Rng;`
- `use` `codex-rs/core/src/util.rs:7` `use tracing::debug;`
- `use` `codex-rs/core/src/util.rs:8` `use tracing::error;`
- `use` `codex-rs/core/src/util.rs:10` `use crate::parse_command::shlex_join;`
- `const` `codex-rs/core/src/util.rs:12` `const INITIAL_DELAY_MS: u64 = 200;`
- `const` `codex-rs/core/src/util.rs:13` `const BACKOFF_FACTOR: f64 = 2.0;`
- `fn` `codex-rs/core/src/util.rs:70` `pub fn resolve_path(base: &Path, path: &PathBuf) -> PathBuf {`
- `fn` `codex-rs/core/src/util.rs:79` `pub fn normalize_thread_name(name: &str) -> Option<String> {`
- `fn` `codex-rs/core/src/util.rs:88` `pub fn resume_command(thread_name: Option<&str>, thread_id: Option<ThreadId>) -> Option<String> {`
- `use` `codex-rs/core/src/util.rs:106` `use super::*;`
- `fn` `codex-rs/core/src/util.rs:109` `fn test_try_parse_error_message() {`
- `fn` `codex-rs/core/src/util.rs:126` `fn test_try_parse_error_message_no_error() {`
- `fn` `codex-rs/core/src/util.rs:133` `fn feedback_tags_macro_compiles() {`
- `struct` `codex-rs/core/src/util.rs:135` `struct OnlyDebug;`
- `fn` `codex-rs/core/src/util.rs:141` `fn normalize_thread_name_trims_and_rejects_empty() {`
- `fn` `codex-rs/core/src/util.rs:150` `fn resume_command_prefers_name_over_id() {`
- `fn` `codex-rs/core/src/util.rs:157` `fn resume_command_with_only_id() {`
- `fn` `codex-rs/core/src/util.rs:167` `fn resume_command_with_no_name_or_id() {`
- `fn` `codex-rs/core/src/util.rs:173` `fn resume_command_quotes_thread_name_when_needed() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use codex_protocol::ThreadId;`
- `use rand::Rng;`
- `use tracing::debug;`
- `use tracing::error;`
- `use crate::parse_command::shlex_join;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
