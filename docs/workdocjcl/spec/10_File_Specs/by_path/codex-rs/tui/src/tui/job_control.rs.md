# `codex-rs/tui/src/tui/job_control.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7249`
- sha256: `09da1c570a6b967f575dd7ec984f54de513685ccfed060d109dbdcc8df2cb03b`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/tui/job_control.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct SuspendContext {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/tui/job_control.rs:1` `use std::io::Result;`
- `use` `codex-rs/tui/src/tui/job_control.rs:2` `use std::io::stdout;`
- `use` `codex-rs/tui/src/tui/job_control.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/tui/job_control.rs:4` `use std::sync::Mutex;`
- `use` `codex-rs/tui/src/tui/job_control.rs:5` `use std::sync::PoisonError;`
- `use` `codex-rs/tui/src/tui/job_control.rs:6` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/tui/src/tui/job_control.rs:7` `use std::sync::atomic::AtomicU16;`
- `use` `codex-rs/tui/src/tui/job_control.rs:8` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/tui/src/tui/job_control.rs:10` `use crossterm::cursor::MoveTo;`
- `use` `codex-rs/tui/src/tui/job_control.rs:11` `use crossterm::cursor::Show;`
- `use` `codex-rs/tui/src/tui/job_control.rs:12` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/tui/job_control.rs:13` `use crossterm::terminal::EnterAlternateScreen;`
- `use` `codex-rs/tui/src/tui/job_control.rs:14` `use crossterm::terminal::LeaveAlternateScreen;`
- `use` `codex-rs/tui/src/tui/job_control.rs:15` `use ratatui::crossterm::execute;`
- `use` `codex-rs/tui/src/tui/job_control.rs:16` `use ratatui::layout::Position;`
- `use` `codex-rs/tui/src/tui/job_control.rs:17` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/tui/job_control.rs:19` `use crate::key_hint;`
- `use` `codex-rs/tui/src/tui/job_control.rs:21` `use super::DisableAlternateScroll;`
- `use` `codex-rs/tui/src/tui/job_control.rs:22` `use super::EnableAlternateScroll;`
- `use` `codex-rs/tui/src/tui/job_control.rs:23` `use super::Terminal;`
- `const` `codex-rs/tui/src/tui/job_control.rs:25` `pub const SUSPEND_KEY: key_hint::KeyBinding = key_hint::ctrl(KeyCode::Char('z'));`
- `struct` `codex-rs/tui/src/tui/job_control.rs:43` `pub struct SuspendContext {`
- `impl` `codex-rs/tui/src/tui/job_control.rs:50` `impl SuspendContext {`
- `fn` `codex-rs/tui/src/tui/job_control.rs:116` `fn set_resume_action(&self, value: ResumeAction) {`
- `fn` `codex-rs/tui/src/tui/job_control.rs:124` `fn take_resume_action(&self) -> Option<ResumeAction> {`
- `impl` `codex-rs/tui/src/tui/job_control.rs:155` `impl PreparedResumeAction {`
- `fn` `codex-rs/tui/src/tui/job_control.rs:176` `fn suspend_process() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::Result;`
- `use std::io::stdout;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::PoisonError;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::atomic::AtomicU16;`
- `use std::sync::atomic::Ordering;`
- `use crossterm::cursor::MoveTo;`
- `use crossterm::cursor::Show;`
- `use crossterm::event::KeyCode;`
- `use crossterm::terminal::EnterAlternateScreen;`
- `use crossterm::terminal::LeaveAlternateScreen;`
- `use ratatui::crossterm::execute;`
- `use ratatui::layout::Position;`
- `use ratatui::layout::Rect;`
- `use crate::key_hint;`
- `use super::DisableAlternateScroll;`
- `use super::EnableAlternateScroll;`
- `use super::Terminal;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
