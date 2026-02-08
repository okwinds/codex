# `codex-rs/tui/src/external_editor.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4904`
- sha256: `6cafdadcb9d8bd40562241d21c50f16808012aeb1a3d24116d721c9f72214359`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/external_editor.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/external_editor.rs:1` `use std::env;`
- `use` `codex-rs/tui/src/external_editor.rs:2` `use std::fs;`
- `use` `codex-rs/tui/src/external_editor.rs:3` `use std::process::Stdio;`
- `use` `codex-rs/tui/src/external_editor.rs:5` `use color_eyre::eyre::Report;`
- `use` `codex-rs/tui/src/external_editor.rs:6` `use color_eyre::eyre::Result;`
- `use` `codex-rs/tui/src/external_editor.rs:7` `use tempfile::Builder;`
- `use` `codex-rs/tui/src/external_editor.rs:8` `use thiserror::Error;`
- `use` `codex-rs/tui/src/external_editor.rs:9` `use tokio::process::Command;`
- `fn` `codex-rs/tui/src/external_editor.rs:25` `fn resolve_windows_program(program: &str) -> std::path::PathBuf {`
- `use` `codex-rs/tui/src/external_editor.rs:95` `use super::*;`
- `use` `codex-rs/tui/src/external_editor.rs:96` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/external_editor.rs:97` `use serial_test::serial;`
- `use` `codex-rs/tui/src/external_editor.rs:99` `use tempfile::tempdir;`
- `struct` `codex-rs/tui/src/external_editor.rs:101` `struct EnvGuard {`
- `impl` `codex-rs/tui/src/external_editor.rs:106` `impl EnvGuard {`
- `fn` `codex-rs/tui/src/external_editor.rs:107` `fn new() -> Self {`
- `impl` `codex-rs/tui/src/external_editor.rs:115` `impl Drop for EnvGuard {`
- `fn` `codex-rs/tui/src/external_editor.rs:116` `fn drop(&mut self) {`
- `fn` `codex-rs/tui/src/external_editor.rs:122` `fn restore_env(key: &str, value: Option<String>) {`
- `fn` `codex-rs/tui/src/external_editor.rs:131` `fn resolve_editor_prefers_visual() {`
- `fn` `codex-rs/tui/src/external_editor.rs:143` `fn resolve_editor_errors_when_unset() {`
- `fn` `codex-rs/tui/src/external_editor.rs:157` `async fn run_editor_returns_updated_content() {`
- `use` `codex-rs/tui/src/external_editor.rs:158` `use std::os::unix::fs::PermissionsExt;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::env;`
- `use std::fs;`
- `use std::process::Stdio;`
- `use color_eyre::eyre::Report;`
- `use color_eyre::eyre::Result;`
- `use tempfile::Builder;`
- `use thiserror::Error;`
- `use tokio::process::Command;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use serial_test::serial;`
- `use tempfile::tempdir;`
- `use std::os::unix::fs::PermissionsExt;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
