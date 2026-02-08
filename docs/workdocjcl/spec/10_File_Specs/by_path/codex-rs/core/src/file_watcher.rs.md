# `codex-rs/core/src/file_watcher.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13716`
- sha256: `c4853dcbc53886d7450a40172e3852695adb7d4b35e3e25fc24fcdb725cbada5`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/file_watcher.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub enum FileWatcherEvent {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/file_watcher.rs:4` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/file_watcher.rs:5` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/file_watcher.rs:6` `use std::path::Path;`
- `use` `codex-rs/core/src/file_watcher.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/file_watcher.rs:8` `use std::sync::Arc;`
- `use` `codex-rs/core/src/file_watcher.rs:9` `use std::sync::Mutex;`
- `use` `codex-rs/core/src/file_watcher.rs:10` `use std::sync::RwLock;`
- `use` `codex-rs/core/src/file_watcher.rs:11` `use std::time::Duration;`
- `use` `codex-rs/core/src/file_watcher.rs:13` `use notify::Event;`
- `use` `codex-rs/core/src/file_watcher.rs:14` `use notify::RecommendedWatcher;`
- `use` `codex-rs/core/src/file_watcher.rs:15` `use notify::RecursiveMode;`
- `use` `codex-rs/core/src/file_watcher.rs:16` `use notify::Watcher;`
- `use` `codex-rs/core/src/file_watcher.rs:17` `use tokio::runtime::Handle;`
- `use` `codex-rs/core/src/file_watcher.rs:18` `use tokio::sync::broadcast;`
- `use` `codex-rs/core/src/file_watcher.rs:19` `use tokio::sync::mpsc;`
- `use` `codex-rs/core/src/file_watcher.rs:20` `use tokio::time::Instant;`
- `use` `codex-rs/core/src/file_watcher.rs:21` `use tokio::time::sleep_until;`
- `use` `codex-rs/core/src/file_watcher.rs:22` `use tracing::info;`
- `use` `codex-rs/core/src/file_watcher.rs:23` `use tracing::warn;`
- `use` `codex-rs/core/src/file_watcher.rs:25` `use crate::config::Config;`
- `use` `codex-rs/core/src/file_watcher.rs:26` `use crate::skills::loader::skill_roots_from_layer_stack_with_agents;`
- `enum` `codex-rs/core/src/file_watcher.rs:29` `pub enum FileWatcherEvent {`
- `struct` `codex-rs/core/src/file_watcher.rs:33` `struct WatchState {`
- `struct` `codex-rs/core/src/file_watcher.rs:37` `struct FileWatcherInner {`
- `const` `codex-rs/core/src/file_watcher.rs:42` `const WATCHER_THROTTLE_INTERVAL: Duration = Duration::from_secs(1);`
- `struct` `codex-rs/core/src/file_watcher.rs:45` `struct ThrottledPaths {`
- `impl` `codex-rs/core/src/file_watcher.rs:50` `impl ThrottledPaths {`
- `fn` `codex-rs/core/src/file_watcher.rs:51` `fn new(now: Instant) -> Self {`
- `fn` `codex-rs/core/src/file_watcher.rs:58` `fn add(&mut self, paths: Vec<PathBuf>) {`
- `fn` `codex-rs/core/src/file_watcher.rs:62` `fn next_deadline(&self, now: Instant) -> Option<Instant> {`
- `fn` `codex-rs/core/src/file_watcher.rs:66` `fn take_ready(&mut self, now: Instant) -> Option<Vec<PathBuf>> {`
- `fn` `codex-rs/core/src/file_watcher.rs:73` `fn take_pending(&mut self, now: Instant) -> Option<Vec<PathBuf>> {`
- `fn` `codex-rs/core/src/file_watcher.rs:80` `fn take_with_next_allowed(&mut self, now: Instant) -> Vec<PathBuf> {`
- `impl` `codex-rs/core/src/file_watcher.rs:94` `impl FileWatcher {`
- `fn` `codex-rs/core/src/file_watcher.rs:143` `fn spawn_event_loop(`
- `fn` `codex-rs/core/src/file_watcher.rs:208` `fn register_skills_root(&self, root: PathBuf) {`
- `fn` `codex-rs/core/src/file_watcher.rs:219` `fn watch_path(&self, path: PathBuf, mode: RecursiveMode) {`
- `fn` `codex-rs/core/src/file_watcher.rs:247` `fn classify_event(event: &Event, state: &RwLock<WatchState>) -> Vec<PathBuf> {`
- `fn` `codex-rs/core/src/file_watcher.rs:266` `fn is_skills_path(path: &Path, roots: &HashSet<PathBuf>) -> bool {`
- `use` `codex-rs/core/src/file_watcher.rs:272` `use super::*;`
- `use` `codex-rs/core/src/file_watcher.rs:273` `use notify::EventKind;`
- `use` `codex-rs/core/src/file_watcher.rs:274` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/file_watcher.rs:275` `use tokio::time::timeout;`
- `fn` `codex-rs/core/src/file_watcher.rs:277` `fn path(name: &str) -> PathBuf {`
- `fn` `codex-rs/core/src/file_watcher.rs:281` `fn notify_event(paths: Vec<PathBuf>) -> Event {`
- `fn` `codex-rs/core/src/file_watcher.rs:290` `fn throttles_and_coalesces_within_interval() {`
- `fn` `codex-rs/core/src/file_watcher.rs:308` `fn flushes_pending_on_shutdown() {`
- `fn` `codex-rs/core/src/file_watcher.rs:325` `fn classify_event_filters_to_skills_roots() {`
- `fn` `codex-rs/core/src/file_watcher.rs:340` `fn classify_event_supports_multiple_roots_without_prefix_false_positives() {`
- `fn` `codex-rs/core/src/file_watcher.rs:360` `fn register_skills_root_dedupes_state_entries() {`
- `fn` `codex-rs/core/src/file_watcher.rs:372` `async fn spawn_event_loop_flushes_pending_changes_on_shutdown() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::RwLock;`
- `use std::time::Duration;`
- `use notify::Event;`
- `use notify::RecommendedWatcher;`
- `use notify::RecursiveMode;`
- `use notify::Watcher;`
- `use tokio::runtime::Handle;`
- `use tokio::sync::broadcast;`
- `use tokio::sync::mpsc;`
- `use tokio::time::Instant;`
- `use tokio::time::sleep_until;`
- `use tracing::info;`
- `use tracing::warn;`
- `use crate::config::Config;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
