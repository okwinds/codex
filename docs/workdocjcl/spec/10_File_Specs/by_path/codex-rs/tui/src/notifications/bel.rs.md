# `codex-rs/tui/src/notifications/bel.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `825`
- sha256: `6c91889f40ba47273d807e5d6df8ce3919a6109c1c01d2014faac6c5a9846acb`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/notifications/bel.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct BelBackend;`
- `pub fn notify(&mut self, _message: &str) -> io::Result<()> {`
- `pub struct PostNotification;`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/notifications/bel.rs:1` `use std::fmt;`
- `use` `codex-rs/tui/src/notifications/bel.rs:2` `use std::io;`
- `use` `codex-rs/tui/src/notifications/bel.rs:3` `use std::io::stdout;`
- `use` `codex-rs/tui/src/notifications/bel.rs:5` `use crossterm::Command;`
- `use` `codex-rs/tui/src/notifications/bel.rs:6` `use ratatui::crossterm::execute;`
- `struct` `codex-rs/tui/src/notifications/bel.rs:9` `pub struct BelBackend;`
- `impl` `codex-rs/tui/src/notifications/bel.rs:11` `impl BelBackend {`
- `fn` `codex-rs/tui/src/notifications/bel.rs:12` `pub fn notify(&mut self, _message: &str) -> io::Result<()> {`
- `struct` `codex-rs/tui/src/notifications/bel.rs:19` `pub struct PostNotification;`
- `impl` `codex-rs/tui/src/notifications/bel.rs:21` `impl Command for PostNotification {`
- `fn` `codex-rs/tui/src/notifications/bel.rs:22` `fn write_ansi(&self, f: &mut impl fmt::Write) -> fmt::Result {`
- `fn` `codex-rs/tui/src/notifications/bel.rs:27` `fn execute_winapi(&self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/notifications/bel.rs:34` `fn is_ansi_code_supported(&self) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt;`
- `use std::io;`
- `use std::io::stdout;`
- `use crossterm::Command;`
- `use ratatui::crossterm::execute;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
