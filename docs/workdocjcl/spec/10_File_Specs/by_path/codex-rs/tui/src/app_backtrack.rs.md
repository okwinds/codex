# `codex-rs/tui/src/app_backtrack.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `26610`
- sha256: `8ccb2c8d5591ba79a6ef58bc30f751ad3f0d5b132db7e916b0d3a9221e148f03`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/app_backtrack.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/app_backtrack.rs:26` `use std::any::TypeId;`
- `use` `codex-rs/tui/src/app_backtrack.rs:27` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/app_backtrack.rs:28` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/app_backtrack.rs:30` `use crate::app::App;`
- `use` `codex-rs/tui/src/app_backtrack.rs:31` `use crate::history_cell::SessionInfoCell;`
- `use` `codex-rs/tui/src/app_backtrack.rs:32` `use crate::history_cell::UserHistoryCell;`
- `use` `codex-rs/tui/src/app_backtrack.rs:33` `use crate::pager_overlay::Overlay;`
- `use` `codex-rs/tui/src/app_backtrack.rs:34` `use crate::tui;`
- `use` `codex-rs/tui/src/app_backtrack.rs:35` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/app_backtrack.rs:36` `use codex_core::protocol::CodexErrorInfo;`
- `use` `codex-rs/tui/src/app_backtrack.rs:37` `use codex_core::protocol::ErrorEvent;`
- `use` `codex-rs/tui/src/app_backtrack.rs:38` `use codex_core::protocol::EventMsg;`
- `use` `codex-rs/tui/src/app_backtrack.rs:39` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/app_backtrack.rs:40` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/app_backtrack.rs:41` `use codex_protocol::user_input::TextElement;`
- `use` `codex-rs/tui/src/app_backtrack.rs:42` `use color_eyre::eyre::Result;`
- `use` `codex-rs/tui/src/app_backtrack.rs:43` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/app_backtrack.rs:44` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/app_backtrack.rs:45` `use crossterm::event::KeyEventKind;`
- `impl` `codex-rs/tui/src/app_backtrack.rs:99` `impl App {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:255` `fn prime_backtrack(&mut self) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:263` `fn open_backtrack_preview(&mut self, tui: &mut tui::Tui) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:272` `fn begin_overlay_backtrack_preview(&mut self, tui: &mut tui::Tui) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:284` `fn step_backtrack_and_highlight(&mut self, tui: &mut tui::Tui) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:307` `fn step_forward_backtrack_and_highlight(&mut self, tui: &mut tui::Tui) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:328` `fn apply_backtrack_selection_internal(&mut self, nth_user_message: usize) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:355` `fn overlay_forward_event(&mut self, tui: &mut tui::Tui, event: TuiEvent) -> Result<()> {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:394` `fn overlay_confirm_backtrack(&mut self, tui: &mut tui::Tui) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:405` `fn overlay_step_backtrack(&mut self, tui: &mut tui::Tui, event: TuiEvent) -> Result<()> {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:415` `fn overlay_step_backtrack_forward(`
- `fn` `codex-rs/tui/src/app_backtrack.rs:472` `fn finish_pending_backtrack(&mut self) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:484` `fn backtrack_selection(&self, nth_user_message: usize) -> Option<BacktrackSelection> {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:512` `fn trim_transcript_for_backtrack(&mut self, nth_user_message: usize) {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:517` `fn trim_transcript_cells_to_nth_user(`
- `fn` `codex-rs/tui/src/app_backtrack.rs:534` `fn nth_user_position(`
- `fn` `codex-rs/tui/src/app_backtrack.rs:543` `fn user_positions_iter(`
- `use` `codex-rs/tui/src/app_backtrack.rs:564` `use super::*;`
- `use` `codex-rs/tui/src/app_backtrack.rs:565` `use crate::history_cell::AgentMessageCell;`
- `use` `codex-rs/tui/src/app_backtrack.rs:566` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/app_backtrack.rs:567` `use ratatui::prelude::Line;`
- `use` `codex-rs/tui/src/app_backtrack.rs:568` `use std::sync::Arc;`
- `fn` `codex-rs/tui/src/app_backtrack.rs:571` `fn trim_transcript_for_first_user_drops_user_and_newer_cells() {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:587` `fn trim_transcript_preserves_cells_before_selected_user() {`
- `fn` `codex-rs/tui/src/app_backtrack.rs:617` `fn trim_transcript_for_later_user_keeps_prior_history() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::any::TypeId;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use crate::app::App;`
- `use crate::history_cell::SessionInfoCell;`
- `use crate::history_cell::UserHistoryCell;`
- `use crate::pager_overlay::Overlay;`
- `use crate::tui;`
- `use crate::tui::TuiEvent;`
- `use codex_core::protocol::CodexErrorInfo;`
- `use codex_core::protocol::ErrorEvent;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::user_input::TextElement;`
- `use color_eyre::eyre::Result;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
