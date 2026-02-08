# `codex-rs/tui/src/file_search.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3962`
- sha256: `b80fc1225198d840249a1d1270c1556da4e6b1472a3c46dc41ba0d38eab7c898`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/file_search.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new(search_dir: PathBuf, tx: AppEventSender) -> Self {`
- `pub fn update_search_dir(&mut self, new_dir: PathBuf) {`
- `pub fn on_user_query(&self, query: String) {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/file_search.rs:8` `use codex_file_search as file_search;`
- `use` `codex-rs/tui/src/file_search.rs:9` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/file_search.rs:10` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/file_search.rs:11` `use std::sync::Mutex;`
- `use` `codex-rs/tui/src/file_search.rs:13` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/file_search.rs:14` `use crate::app_event_sender::AppEventSender;`
- `struct` `codex-rs/tui/src/file_search.rs:22` `struct SearchState {`
- `impl` `codex-rs/tui/src/file_search.rs:28` `impl FileSearchManager {`
- `fn` `codex-rs/tui/src/file_search.rs:29` `pub fn new(search_dir: PathBuf, tx: AppEventSender) -> Self {`
- `fn` `codex-rs/tui/src/file_search.rs:44` `pub fn update_search_dir(&mut self, new_dir: PathBuf) {`
- `fn` `codex-rs/tui/src/file_search.rs:53` `pub fn on_user_query(&self, query: String) {`
- `fn` `codex-rs/tui/src/file_search.rs:75` `fn start_session_locked(&self, st: &mut SearchState) {`
- `struct` `codex-rs/tui/src/file_search.rs:101` `struct TuiSessionReporter {`
- `impl` `codex-rs/tui/src/file_search.rs:107` `impl TuiSessionReporter {`
- `fn` `codex-rs/tui/src/file_search.rs:108` `fn send_snapshot(&self, snapshot: &file_search::FileSearchSnapshot) {`
- `impl` `codex-rs/tui/src/file_search.rs:126` `impl file_search::SessionReporter for TuiSessionReporter {`
- `fn` `codex-rs/tui/src/file_search.rs:127` `fn on_update(&self, snapshot: &file_search::FileSearchSnapshot) {`
- `fn` `codex-rs/tui/src/file_search.rs:131` `fn on_complete(&self) {}`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_file_search as file_search;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
