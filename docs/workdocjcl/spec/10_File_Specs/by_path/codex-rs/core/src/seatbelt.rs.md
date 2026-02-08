# `codex-rs/core/src/seatbelt.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `23584`
- sha256: `e4a406602774c217d3bbe353141f4e6ba41ab33573537700d25637c1eb33d92d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/seatbelt.rs` (read)
- env: `TMPDIR`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/seatbelt.rs:3` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/seatbelt.rs:4` `use std::ffi::CStr;`
- `use` `codex-rs/core/src/seatbelt.rs:5` `use std::path::Path;`
- `use` `codex-rs/core/src/seatbelt.rs:6` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/seatbelt.rs:7` `use tokio::process::Child;`
- `use` `codex-rs/core/src/seatbelt.rs:9` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/seatbelt.rs:10` `use crate::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use` `codex-rs/core/src/seatbelt.rs:11` `use crate::spawn::StdioPolicy;`
- `use` `codex-rs/core/src/seatbelt.rs:12` `use crate::spawn::spawn_child_async;`
- `const` `codex-rs/core/src/seatbelt.rs:14` `const MACOS_SEATBELT_BASE_POLICY: &str = include_str!("seatbelt_base_policy.sbpl");`
- `const` `codex-rs/core/src/seatbelt.rs:15` `const MACOS_SEATBELT_NETWORK_POLICY: &str = include_str!("seatbelt_network_policy.sbpl");`
- `fn` `codex-rs/core/src/seatbelt.rs:23` `pub async fn spawn_command_under_seatbelt(`
- `fn` `codex-rs/core/src/seatbelt.rs:138` `fn confstr(name: libc::c_int) -> Option<String> {`
- `fn` `codex-rs/core/src/seatbelt.rs:150` `fn confstr_path(name: libc::c_int) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/seatbelt.rs:156` `fn macos_dir_params() -> Vec<(String, PathBuf)> {`
- `use` `codex-rs/core/src/seatbelt.rs:165` `use super::MACOS_SEATBELT_BASE_POLICY;`
- `use` `codex-rs/core/src/seatbelt.rs:166` `use super::create_seatbelt_command_args;`
- `use` `codex-rs/core/src/seatbelt.rs:167` `use super::macos_dir_params;`
- `use` `codex-rs/core/src/seatbelt.rs:168` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/seatbelt.rs:169` `use crate::seatbelt::MACOS_PATH_TO_SEATBELT_EXECUTABLE;`
- `use` `codex-rs/core/src/seatbelt.rs:170` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/seatbelt.rs:171` `use std::fs;`
- `use` `codex-rs/core/src/seatbelt.rs:172` `use std::path::Path;`
- `use` `codex-rs/core/src/seatbelt.rs:173` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/seatbelt.rs:174` `use std::process::Command;`
- `use` `codex-rs/core/src/seatbelt.rs:175` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/seatbelt.rs:177` `fn assert_seatbelt_denied(stderr: &[u8], path: &Path) {`
- `fn` `codex-rs/core/src/seatbelt.rs:188` `fn create_seatbelt_args_with_read_only_git_and_codex_subpaths() {`
- `fn` `codex-rs/core/src/seatbelt.rs:375` `fn create_seatbelt_args_with_read_only_git_pointer_file() {`
- `fn` `codex-rs/core/src/seatbelt.rs:460` `fn create_seatbelt_args_for_cwd_as_git_repo() {`
- `struct` `codex-rs/core/src/seatbelt.rs:565` `struct PopulatedTmp {`
- `fn` `codex-rs/core/src/seatbelt.rs:584` `fn populate_tmpdir(tmp: &Path) -> PopulatedTmp {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::ffi::CStr;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tokio::process::Child;`
- `use crate::protocol::SandboxPolicy;`
- `use crate::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use crate::spawn::StdioPolicy;`
- `use crate::spawn::spawn_child_async;`
- `use super::MACOS_SEATBELT_BASE_POLICY;`
- `use super::create_seatbelt_command_args;`
- `use super::macos_dir_params;`
- `use crate::protocol::SandboxPolicy;`
- `use crate::seatbelt::MACOS_PATH_TO_SEATBELT_EXECUTABLE;`
- `use pretty_assertions::assert_eq;`
- `use std::fs;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Command;`
- `use tempfile::TempDir;`
### Referenced env vars
- `TMPDIR`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
