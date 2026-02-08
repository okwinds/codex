# `codex-rs/windows-sandbox-rs/src/logging.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2813`
- sha256: `60c39bf668a5e13c5c56c07e6236eddea348382220576b6f96df53dc0e4340a1`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/logging.rs` (read)
- env: `SBX_DEBUG`

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn log_start(command: &[String], base_dir: Option<&Path>) {`
- `pub fn log_success(command: &[String], base_dir: Option<&Path>) {`
- `pub fn log_failure(command: &[String], detail: &str, base_dir: Option<&Path>) {`
- `pub fn debug_log(msg: &str, base_dir: Option<&Path>) {`
- `pub fn log_note(msg: &str, base_dir: Option<&Path>) {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/logging.rs:1` `use std::fs::OpenOptions;`
- `use` `codex-rs/windows-sandbox-rs/src/logging.rs:2` `use std::io::Write;`
- `use` `codex-rs/windows-sandbox-rs/src/logging.rs:3` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/logging.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/logging.rs:5` `use std::sync::OnceLock;`
- `use` `codex-rs/windows-sandbox-rs/src/logging.rs:7` `use codex_utils_string::take_bytes_at_char_boundary;`
- `const` `codex-rs/windows-sandbox-rs/src/logging.rs:9` `const LOG_COMMAND_PREVIEW_LIMIT: usize = 200;`
- `const` `codex-rs/windows-sandbox-rs/src/logging.rs:10` `pub const LOG_FILE_NAME: &str = "sandbox.log";`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:12` `fn exe_label() -> &'static str {`
- `static` `codex-rs/windows-sandbox-rs/src/logging.rs:13` `static LABEL: OnceLock<String> = OnceLock::new();`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:22` `fn preview(command: &[String]) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:31` `fn log_file_path(base_dir: &Path) -> Option<PathBuf> {`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:39` `fn append_line(line: &str, base_dir: Option<&Path>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:49` `pub fn log_start(command: &[String], base_dir: Option<&Path>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:54` `pub fn log_success(command: &[String], base_dir: Option<&Path>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:59` `pub fn log_failure(command: &[String], detail: &str, base_dir: Option<&Path>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:65` `pub fn debug_log(msg: &str, base_dir: Option<&Path>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:73` `pub fn log_note(msg: &str, base_dir: Option<&Path>) {`
- `use` `codex-rs/windows-sandbox-rs/src/logging.rs:80` `use super::*;`
- `fn` `codex-rs/windows-sandbox-rs/src/logging.rs:83` `fn preview_does_not_panic_on_utf8_boundary() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::OpenOptions;`
- `use std::io::Write;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::OnceLock;`
- `use codex_utils_string::take_bytes_at_char_boundary;`
- `use super::*;`
### Referenced env vars
- `SBX_DEBUG`

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
