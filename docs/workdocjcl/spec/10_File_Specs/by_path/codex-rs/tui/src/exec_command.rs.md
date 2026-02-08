# `codex-rs/tui/src/exec_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2220`
- sha256: `3db95e7f9f3463a7bbaa0c861617b4b45f21326b0fe62e7ee8ce1efd910f0a8d`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/exec_command.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/exec_command.rs:1` `use std::path::Path;`
- `use` `codex-rs/tui/src/exec_command.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/exec_command.rs:4` `use codex_core::parse_command::extract_shell_command;`
- `use` `codex-rs/tui/src/exec_command.rs:5` `use dirs::home_dir;`
- `use` `codex-rs/tui/src/exec_command.rs:6` `use shlex::try_join;`
- `use` `codex-rs/tui/src/exec_command.rs:39` `use super::*;`
- `fn` `codex-rs/tui/src/exec_command.rs:42` `fn test_escape_command() {`
- `fn` `codex-rs/tui/src/exec_command.rs:49` `fn test_strip_bash_lc_and_escape() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_core::parse_command::extract_shell_command;`
- `use dirs::home_dir;`
- `use shlex::try_join;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
