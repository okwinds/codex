# `codex-rs/core/src/powershell.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7132`
- sha256: `a6964d5cd360cfa0e98e5b5d1d5768e7761e8cc656c668deae9b915113beaaa3`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/powershell.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn extract_powershell_command(command: &[String]) -> Option<(&str, &str)> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/powershell.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/powershell.rs:4` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/powershell.rs:6` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/powershell.rs:7` `use crate::shell::detect_shell_type;`
- `const` `codex-rs/core/src/powershell.rs:9` `const POWERSHELL_FLAGS: &[&str] = &["-nologo", "-noprofile", "-command", "-c"];`
- `fn` `codex-rs/core/src/powershell.rs:43` `pub fn extract_powershell_command(command: &[String]) -> Option<(&str, &str)> {`
- `fn` `codex-rs/core/src/powershell.rs:130` `fn try_find_powershellish_executable_in_path(candidates: &[&str]) -> Option<AbsolutePathBuf> {`
- `fn` `codex-rs/core/src/powershell.rs:151` `fn is_powershellish_executable_available(powershell_or_pwsh_exe: &std::path::Path) -> bool {`
- `use` `codex-rs/core/src/powershell.rs:162` `use super::extract_powershell_command;`
- `fn` `codex-rs/core/src/powershell.rs:165` `fn extracts_basic_powershell_command() {`
- `fn` `codex-rs/core/src/powershell.rs:176` `fn extracts_lowercase_flags() {`
- `fn` `codex-rs/core/src/powershell.rs:188` `fn extracts_full_path_powershell_command() {`
- `fn` `codex-rs/core/src/powershell.rs:200` `fn extracts_with_noprofile_and_alias() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use crate::shell::ShellType;`
- `use crate::shell::detect_shell_type;`
- `use super::extract_powershell_command;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
