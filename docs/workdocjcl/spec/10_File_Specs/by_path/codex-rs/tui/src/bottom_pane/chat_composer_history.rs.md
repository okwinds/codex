# `codex-rs/tui/src/bottom_pane/chat_composer_history.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11758`
- sha256: `6c332771347f71b0044a6b2c061018200757ecfeb7680305c2d1801ab530ef40`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/chat_composer_history.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub fn new() -> Self {`
- `pub fn set_metadata(&mut self, log_id: u64, entry_count: usize) {`
- `pub fn record_local_submission(&mut self, entry: HistoryEntry) {`
- `pub fn reset_navigation(&mut self) {`
- `pub fn should_handle_navigation(&self, text: &str, cursor: usize) -> bool {`
- `pub fn navigate_up(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {`
- `pub fn navigate_down(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {`
- `pub fn on_entry_response(`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:4` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:5` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:6` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:7` `use codex_protocol::user_input::TextElement;`
- `impl` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:16` `impl HistoryEntry {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:17` `fn empty() -> Self {`
- `impl` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:60` `impl ChatComposerHistory {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:61` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:73` `pub fn set_metadata(&mut self, log_id: u64, entry_count: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:84` `pub fn record_local_submission(&mut self, entry: HistoryEntry) {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:101` `pub fn reset_navigation(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:108` `pub fn should_handle_navigation(&self, text: &str, cursor: usize) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:129` `pub fn navigate_up(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:146` `pub fn navigate_down(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:173` `pub fn on_entry_response(`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:197` `fn populate_history_at_index(`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:228` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:229` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:230` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:231` `use tokio::sync::mpsc::unbounded_channel;`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:234` `fn duplicate_submissions_are_not_recorded() {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:263` `fn navigation_with_async_fetch() {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:317` `fn reset_navigation_resets_cursor() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::user_input::TextElement;`
- `use super::*;`
- `use crate::app_event::AppEvent;`
- `use codex_core::protocol::Op;`
- `use tokio::sync::mpsc::unbounded_channel;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
