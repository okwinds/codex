# `codex-rs/windows-sandbox-rs/src/cwd_junction.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4984`
- sha256: `1128f10139735ae82bc3f0d48dc3b7b80b8d54f9e411f5aa8813c11b3120007e`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/cwd_junction.rs` (read)
- env: `USERPROFILE`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn create_cwd_junction(requested_cwd: &Path, log_dir: Option<&Path>) -> Option<PathBuf> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:3` `use codex_windows_sandbox::log_note;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:4` `use std::collections::hash_map::DefaultHasher;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:5` `use std::hash::Hash;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:6` `use std::hash::Hasher;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:7` `use std::os::windows::fs::MetadataExt as _;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:8` `use std::os::windows::process::CommandExt as _;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:9` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:10` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:11` `use windows_sys::Win32::Storage::FileSystem::FILE_ATTRIBUTE_REPARSE_POINT;`
- `fn` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:13` `fn junction_name_for_path(path: &Path) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:19` `fn junction_root_for_userprofile(userprofile: &str) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/cwd_junction.rs:26` `pub fn create_cwd_junction(requested_cwd: &Path, log_dir: Option<&Path>) -> Option<PathBuf> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_windows_sandbox::log_note;`
- `use std::collections::hash_map::DefaultHasher;`
- `use std::hash::Hash;`
- `use std::hash::Hasher;`
- `use std::os::windows::fs::MetadataExt as _;`
- `use std::os::windows::process::CommandExt as _;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use windows_sys::Win32::Storage::FileSystem::FILE_ATTRIBUTE_REPARSE_POINT;`
### Referenced env vars
- `USERPROFILE`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
