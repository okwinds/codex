# `codex-rs/file-search/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `30900`
- sha256: `a96f4ef0c0e5916a2e1d6187168537e2b571b25fce4795858ddc20a37212f57e`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/file-search/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct FileMatch {`
- `pub fn full_path(&self) -> PathBuf {`
- `pub fn file_name_from_path(path: &str) -> String {`
- `pub struct FileSearchResults {`
- `pub struct FileSearchSnapshot {`
- `pub struct FileSearchOptions {`
- `pub trait SessionReporter: Send + Sync + 'static {`
- `pub struct FileSearchSession {`
- `pub fn update_query(&self, pattern_text: &str) {`
- `pub fn create_session(`
- `pub trait Reporter {`
- `pub fn run(`

## Definitions (auto, per-file)
- `use` `codex-rs/file-search/src/lib.rs:1` `use crossbeam_channel::Receiver;`
- `use` `codex-rs/file-search/src/lib.rs:2` `use crossbeam_channel::Sender;`
- `use` `codex-rs/file-search/src/lib.rs:3` `use crossbeam_channel::after;`
- `use` `codex-rs/file-search/src/lib.rs:4` `use crossbeam_channel::never;`
- `use` `codex-rs/file-search/src/lib.rs:5` `use crossbeam_channel::select;`
- `use` `codex-rs/file-search/src/lib.rs:6` `use crossbeam_channel::unbounded;`
- `use` `codex-rs/file-search/src/lib.rs:7` `use ignore::WalkBuilder;`
- `use` `codex-rs/file-search/src/lib.rs:8` `use ignore::overrides::OverrideBuilder;`
- `use` `codex-rs/file-search/src/lib.rs:9` `use nucleo::Config;`
- `use` `codex-rs/file-search/src/lib.rs:10` `use nucleo::Injector;`
- `use` `codex-rs/file-search/src/lib.rs:11` `use nucleo::Matcher;`
- `use` `codex-rs/file-search/src/lib.rs:12` `use nucleo::Nucleo;`
- `use` `codex-rs/file-search/src/lib.rs:13` `use nucleo::Utf32String;`
- `use` `codex-rs/file-search/src/lib.rs:14` `use nucleo::pattern::CaseMatching;`
- `use` `codex-rs/file-search/src/lib.rs:15` `use nucleo::pattern::Normalization;`
- `use` `codex-rs/file-search/src/lib.rs:16` `use serde::Serialize;`
- `use` `codex-rs/file-search/src/lib.rs:17` `use std::num::NonZero;`
- `use` `codex-rs/file-search/src/lib.rs:18` `use std::path::Path;`
- `use` `codex-rs/file-search/src/lib.rs:19` `use std::path::PathBuf;`
- `use` `codex-rs/file-search/src/lib.rs:20` `use std::sync::Arc;`
- `use` `codex-rs/file-search/src/lib.rs:21` `use std::sync::Condvar;`
- `use` `codex-rs/file-search/src/lib.rs:22` `use std::sync::Mutex;`
- `use` `codex-rs/file-search/src/lib.rs:23` `use std::sync::RwLock;`
- `use` `codex-rs/file-search/src/lib.rs:24` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/file-search/src/lib.rs:25` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/file-search/src/lib.rs:26` `use std::thread;`
- `use` `codex-rs/file-search/src/lib.rs:27` `use std::time::Duration;`
- `use` `codex-rs/file-search/src/lib.rs:28` `use tokio::process::Command;`
- `use` `codex-rs/file-search/src/lib.rs:31` `use nucleo::Utf32Str;`
- `use` `codex-rs/file-search/src/lib.rs:33` `use nucleo::pattern::AtomKind;`
- `use` `codex-rs/file-search/src/lib.rs:35` `use nucleo::pattern::Pattern;`
- `mod` `codex-rs/file-search/src/lib.rs:37` `mod cli;`
- `struct` `codex-rs/file-search/src/lib.rs:52` `pub struct FileMatch {`
- `impl` `codex-rs/file-search/src/lib.rs:60` `impl FileMatch {`
- `fn` `codex-rs/file-search/src/lib.rs:61` `pub fn full_path(&self) -> PathBuf {`
- `fn` `codex-rs/file-search/src/lib.rs:67` `pub fn file_name_from_path(path: &str) -> String {`
- `struct` `codex-rs/file-search/src/lib.rs:75` `pub struct FileSearchResults {`
- `struct` `codex-rs/file-search/src/lib.rs:81` `pub struct FileSearchSnapshot {`
- `struct` `codex-rs/file-search/src/lib.rs:90` `pub struct FileSearchOptions {`
- `impl` `codex-rs/file-search/src/lib.rs:98` `impl Default for FileSearchOptions {`
- `fn` `codex-rs/file-search/src/lib.rs:99` `fn default() -> Self {`
- `trait` `codex-rs/file-search/src/lib.rs:112` `pub trait SessionReporter: Send + Sync + 'static {`
- `fn` `codex-rs/file-search/src/lib.rs:114` `fn on_update(&self, snapshot: &FileSearchSnapshot);`
- `fn` `codex-rs/file-search/src/lib.rs:117` `fn on_complete(&self);`
- `struct` `codex-rs/file-search/src/lib.rs:120` `pub struct FileSearchSession {`
- `impl` `codex-rs/file-search/src/lib.rs:124` `impl FileSearchSession {`
- `fn` `codex-rs/file-search/src/lib.rs:126` `pub fn update_query(&self, pattern_text: &str) {`
- `impl` `codex-rs/file-search/src/lib.rs:134` `impl Drop for FileSearchSession {`
- `fn` `codex-rs/file-search/src/lib.rs:135` `fn drop(&mut self) {`
- `fn` `codex-rs/file-search/src/lib.rs:141` `pub fn create_session(`
- `fn` `codex-rs/file-search/src/lib.rs:154` `fn create_session_inner(`
- `trait` `codex-rs/file-search/src/lib.rs:209` `pub trait Reporter {`
- `fn` `codex-rs/file-search/src/lib.rs:210` `fn report_match(&self, file_match: &FileMatch);`
- `fn` `codex-rs/file-search/src/lib.rs:211` `fn warn_matches_truncated(&self, total_match_count: usize, shown_match_count: usize);`
- `fn` `codex-rs/file-search/src/lib.rs:212` `fn warn_no_search_pattern(&self, search_directory: &Path);`
- `fn` `codex-rs/file-search/src/lib.rs:287` `pub fn run(`
- `fn` `codex-rs/file-search/src/lib.rs:307` `fn sort_matches(matches: &mut [(u32, String)]) {`
- `use` `codex-rs/file-search/src/lib.rs:324` `use std::cmp::Ordering;`
- `fn` `codex-rs/file-search/src/lib.rs:332` `fn create_pattern(pattern: &str) -> Pattern {`
- `struct` `codex-rs/file-search/src/lib.rs:341` `struct SessionInner {`
- `enum` `codex-rs/file-search/src/lib.rs:353` `enum WorkSignal {`
- `fn` `codex-rs/file-search/src/lib.rs:360` `fn build_override_matcher(`
- `fn` `codex-rs/file-search/src/lib.rs:395` `fn walker_worker(`
- `const` `codex-rs/file-search/src/lib.rs:432` `const CHECK_INTERVAL: usize = 1024;`
- `fn` `codex-rs/file-search/src/lib.rs:469` `fn matcher_worker(`
- `const` `codex-rs/file-search/src/lib.rs:474` `const TICK_TIMEOUT_MS: u64 = 10;`
- `struct` `codex-rs/file-search/src/lib.rs:587` `struct RunReporter {`
- `impl` `codex-rs/file-search/src/lib.rs:592` `impl SessionReporter for RunReporter {`
- `fn` `codex-rs/file-search/src/lib.rs:593` `fn on_update(&self, snapshot: &FileSearchSnapshot) {`
- `fn` `codex-rs/file-search/src/lib.rs:599` `fn on_complete(&self) {`
- `impl` `codex-rs/file-search/src/lib.rs:607` `impl RunReporter {`
- `fn` `codex-rs/file-search/src/lib.rs:608` `fn wait_for_complete(&self) -> FileSearchSnapshot {`
- `use` `codex-rs/file-search/src/lib.rs:622` `use super::*;`
- `use` `codex-rs/file-search/src/lib.rs:623` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/file-search/src/lib.rs:624` `use std::fs;`
- `use` `codex-rs/file-search/src/lib.rs:625` `use std::sync::Arc;`
- `use` `codex-rs/file-search/src/lib.rs:626` `use std::sync::Condvar;`
- `use` `codex-rs/file-search/src/lib.rs:627` `use std::sync::Mutex;`
- `use` `codex-rs/file-search/src/lib.rs:628` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/file-search/src/lib.rs:629` `use std::thread;`
- `use` `codex-rs/file-search/src/lib.rs:630` `use std::time::Duration;`
- `use` `codex-rs/file-search/src/lib.rs:631` `use std::time::Instant;`
- `use` `codex-rs/file-search/src/lib.rs:632` `use tempfile::TempDir;`
- `fn` `codex-rs/file-search/src/lib.rs:635` `fn verify_score_is_none_for_non_match() {`
- `fn` `codex-rs/file-search/src/lib.rs:646` `fn tie_breakers_sort_by_path_when_scores_equal() {`
- `fn` `codex-rs/file-search/src/lib.rs:666` `fn file_name_from_path_uses_basename() {`
- `fn` `codex-rs/file-search/src/lib.rs:671` `fn file_name_from_path_falls_back_to_full_path() {`
- `struct` `codex-rs/file-search/src/lib.rs:676` `struct RecordingReporter {`
- `impl` `codex-rs/file-search/src/lib.rs:683` `impl RecordingReporter {`
- `fn` `codex-rs/file-search/src/lib.rs:712` `fn wait_for_complete(&self, timeout: Duration) -> bool {`
- `fn` `codex-rs/file-search/src/lib.rs:720` `fn clear(&self) {`
- `fn` `codex-rs/file-search/src/lib.rs:725` `fn updates(&self) -> Vec<FileSearchSnapshot> {`
- `fn` `codex-rs/file-search/src/lib.rs:729` `fn wait_for_updates_at_least(&self, min_len: usize, timeout: Duration) -> bool {`
- `fn` `codex-rs/file-search/src/lib.rs:735` `fn snapshot(&self) -> FileSearchSnapshot {`
- `impl` `codex-rs/file-search/src/lib.rs:745` `impl SessionReporter for RecordingReporter {`
- `fn` `codex-rs/file-search/src/lib.rs:746` `fn on_update(&self, snapshot: &FileSearchSnapshot) {`
- `fn` `codex-rs/file-search/src/lib.rs:752` `fn on_complete(&self) {`
- `fn` `codex-rs/file-search/src/lib.rs:761` `fn create_temp_tree(file_count: usize) -> TempDir {`
- `fn` `codex-rs/file-search/src/lib.rs:771` `fn session_scanned_file_count_is_monotonic_across_queries() {`
- `fn` `codex-rs/file-search/src/lib.rs:791` `fn session_streams_updates_before_walk_complete() {`
- `fn` `codex-rs/file-search/src/lib.rs:806` `fn session_accepts_query_updates_after_walk_complete() {`
- `fn` `codex-rs/file-search/src/lib.rs:832` `fn session_emits_complete_when_query_changes_with_no_matches() {`
- `fn` `codex-rs/file-search/src/lib.rs:860` `fn dropping_session_does_not_cancel_siblings_with_shared_cancel_flag() {`
- `fn` `codex-rs/file-search/src/lib.rs:894` `fn session_emits_updates_when_query_changes() {`
- `fn` `codex-rs/file-search/src/lib.rs:915` `fn run_returns_matches_for_query() {`
- `fn` `codex-rs/file-search/src/lib.rs:938` `fn cancel_exits_run() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossbeam_channel::Receiver;`
- `use crossbeam_channel::Sender;`
- `use crossbeam_channel::after;`
- `use crossbeam_channel::never;`
- `use crossbeam_channel::select;`
- `use crossbeam_channel::unbounded;`
- `use ignore::WalkBuilder;`
- `use ignore::overrides::OverrideBuilder;`
- `use nucleo::Config;`
- `use nucleo::Injector;`
- `use nucleo::Matcher;`
- `use nucleo::Nucleo;`
- `use nucleo::Utf32String;`
- `use nucleo::pattern::CaseMatching;`
- `use nucleo::pattern::Normalization;`
- `use serde::Serialize;`
- `use std::num::NonZero;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
