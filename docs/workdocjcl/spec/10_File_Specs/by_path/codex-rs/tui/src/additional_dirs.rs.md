# `codex-rs/tui/src/additional_dirs.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2918`
- sha256: `6bab03a5691b502a9b276ab267fa1f07bb88dd32ffe4add9eaa729390b3201fc`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/additional_dirs.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn add_dir_warning_message(`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/additional_dirs.rs:1` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/tui/src/additional_dirs.rs:2` `use std::path::PathBuf;`
- `fn` `codex-rs/tui/src/additional_dirs.rs:7` `pub fn add_dir_warning_message(`
- `fn` `codex-rs/tui/src/additional_dirs.rs:23` `fn format_warning(additional_dirs: &[PathBuf]) -> String {`
- `use` `codex-rs/tui/src/additional_dirs.rs:36` `use super::add_dir_warning_message;`
- `use` `codex-rs/tui/src/additional_dirs.rs:37` `use codex_core::protocol::NetworkAccess;`
- `use` `codex-rs/tui/src/additional_dirs.rs:38` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/tui/src/additional_dirs.rs:39` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/additional_dirs.rs:40` `use std::path::PathBuf;`
- `fn` `codex-rs/tui/src/additional_dirs.rs:43` `fn returns_none_for_workspace_write() {`
- `fn` `codex-rs/tui/src/additional_dirs.rs:50` `fn returns_none_for_danger_full_access() {`
- `fn` `codex-rs/tui/src/additional_dirs.rs:57` `fn returns_none_for_external_sandbox() {`
- `fn` `codex-rs/tui/src/additional_dirs.rs:66` `fn warns_for_read_only() {`
- `fn` `codex-rs/tui/src/additional_dirs.rs:78` `fn returns_none_when_no_additional_dirs() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::protocol::SandboxPolicy;`
- `use std::path::PathBuf;`
- `use super::add_dir_warning_message;`
- `use codex_core::protocol::NetworkAccess;`
- `use codex_core::protocol::SandboxPolicy;`
- `use pretty_assertions::assert_eq;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
