# `codex-rs/cli/src/wsl_paths.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1744`
- sha256: `39c4ad536a03cc81df8593df4c0f38f6669a0d16d19734d0866771ada747d846`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/wsl_paths.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn win_path_to_wsl(path: &str) -> Option<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/wsl_paths.rs:1` `use std::ffi::OsStr;`
- `fn` `codex-rs/cli/src/wsl_paths.rs:8` `pub fn win_path_to_wsl(path: &str) -> Option<String> {`
- `use` `codex-rs/cli/src/wsl_paths.rs:40` `use super::*;`
- `fn` `codex-rs/cli/src/wsl_paths.rs:43` `fn win_to_wsl_basic() {`
- `fn` `codex-rs/cli/src/wsl_paths.rs:56` `fn normalize_is_noop_on_unix_paths() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsStr;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/03_API/CLI.md`
