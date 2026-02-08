# `codex-rs/tui/src/bottom_pane/chat_composer_history.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13157`
- sha256: `96c9c3a616bb8d28111b7a3fa0f5204780cff033aecf1b3af2ca09f942fa50f9`
- generated_utc: `2026-02-08T10:45:39Z`

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
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:6` `use crate::bottom_pane::MentionBinding;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:7` `use crate::mention_codec::decode_history_mentions;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:8` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:9` `use codex_protocol::user_input::TextElement;`
- `impl` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:26` `impl HistoryEntry {`
- `impl` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:89` `impl ChatComposerHistory {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:90` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:102` `pub fn set_metadata(&mut self, log_id: u64, entry_count: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:113` `pub fn record_local_submission(&mut self, entry: HistoryEntry) {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:134` `pub fn reset_navigation(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:141` `pub fn should_handle_navigation(&self, text: &str, cursor: usize) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:162` `pub fn navigate_up(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:179` `pub fn navigate_down(&mut self, app_event_tx: &AppEventSender) -> Option<HistoryEntry> {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:206` `pub fn on_entry_response(`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:229` `fn populate_history_at_index(`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:260` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:261` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:262` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:263` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:264` `use tokio::sync::mpsc::unbounded_channel;`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:267` `fn duplicate_submissions_are_not_recorded() {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:296` `fn navigation_with_async_fetch() {`
- `fn` `codex-rs/tui/src/bottom_pane/chat_composer_history.rs:350` `fn reset_navigation_resets_cursor() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::bottom_pane::MentionBinding;`
- `use crate::mention_codec::decode_history_mentions;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::user_input::TextElement;`
- `use super::*;`
- `use crate::app_event::AppEvent;`
- `use codex_core::protocol::Op;`
- `use pretty_assertions::assert_eq;`
- `use tokio::sync::mpsc::unbounded_channel;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
