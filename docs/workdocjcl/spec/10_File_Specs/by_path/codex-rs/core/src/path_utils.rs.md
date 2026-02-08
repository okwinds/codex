# `codex-rs/core/src/path_utils.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7275`
- sha256: `45a267ebb9168de942562fb2e5bf7435c4851e62e6d279933daa35ec33b5511e`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/path_utils.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn normalize_for_path_comparison(path: impl AsRef<Path>) -> std::io::Result<PathBuf> {`
- `pub struct SymlinkWritePaths {`
- `pub fn resolve_symlink_write_paths(path: &Path) -> io::Result<SymlinkWritePaths> {`
- `pub fn write_atomically(write_path: &Path, contents: &str) -> io::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/path_utils.rs:1` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/path_utils.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/path_utils.rs:3` `use std::io;`
- `use` `codex-rs/core/src/path_utils.rs:4` `use std::path::Path;`
- `use` `codex-rs/core/src/path_utils.rs:5` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/path_utils.rs:6` `use tempfile::NamedTempFile;`
- `use` `codex-rs/core/src/path_utils.rs:8` `use crate::env;`
- `fn` `codex-rs/core/src/path_utils.rs:10` `pub fn normalize_for_path_comparison(path: impl AsRef<Path>) -> std::io::Result<PathBuf> {`
- `struct` `codex-rs/core/src/path_utils.rs:15` `pub struct SymlinkWritePaths {`
- `fn` `codex-rs/core/src/path_utils.rs:26` `pub fn resolve_symlink_write_paths(path: &Path) -> io::Result<SymlinkWritePaths> {`
- `fn` `codex-rs/core/src/path_utils.rs:101` `pub fn write_atomically(write_path: &Path, contents: &str) -> io::Result<()> {`
- `fn` `codex-rs/core/src/path_utils.rs:115` `fn normalize_for_wsl(path: PathBuf) -> PathBuf {`
- `fn` `codex-rs/core/src/path_utils.rs:119` `fn normalize_for_wsl_with_flag(path: PathBuf, is_wsl: bool) -> PathBuf {`
- `fn` `codex-rs/core/src/path_utils.rs:131` `fn is_wsl_case_insensitive_path(path: &Path) -> bool {`
- `use` `codex-rs/core/src/path_utils.rs:134` `use std::os::unix::ffi::OsStrExt;`
- `use` `codex-rs/core/src/path_utils.rs:135` `use std::path::Component;`
- `fn` `codex-rs/core/src/path_utils.rs:161` `fn ascii_eq_ignore_case(left: &[u8], right: &[u8]) -> bool {`
- `fn` `codex-rs/core/src/path_utils.rs:170` `fn lower_ascii_path(path: PathBuf) -> PathBuf {`
- `use` `codex-rs/core/src/path_utils.rs:171` `use std::ffi::OsString;`
- `use` `codex-rs/core/src/path_utils.rs:172` `use std::os::unix::ffi::OsStrExt;`
- `use` `codex-rs/core/src/path_utils.rs:173` `use std::os::unix::ffi::OsStringExt;`
- `fn` `codex-rs/core/src/path_utils.rs:185` `fn lower_ascii_path(path: PathBuf) -> PathBuf {`
- `use` `codex-rs/core/src/path_utils.rs:193` `use super::super::resolve_symlink_write_paths;`
- `use` `codex-rs/core/src/path_utils.rs:194` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/path_utils.rs:195` `use std::os::unix::fs::symlink;`
- `fn` `codex-rs/core/src/path_utils.rs:198` `fn symlink_cycles_fall_back_to_root_write_path() -> std::io::Result<()> {`
- `use` `codex-rs/core/src/path_utils.rs:216` `use super::super::normalize_for_wsl_with_flag;`
- `use` `codex-rs/core/src/path_utils.rs:217` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/path_utils.rs:218` `use std::path::PathBuf;`
- `fn` `codex-rs/core/src/path_utils.rs:221` `fn wsl_mnt_drive_paths_lowercase() {`
- `fn` `codex-rs/core/src/path_utils.rs:228` `fn wsl_non_drive_paths_unchanged() {`
- `fn` `codex-rs/core/src/path_utils.rs:236` `fn wsl_non_mnt_paths_unchanged() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use std::collections::HashSet;`
- `use std::io;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tempfile::NamedTempFile;`
- `use crate::env;`
- `use std::os::unix::ffi::OsStrExt;`
- `use std::path::Component;`
- `use std::ffi::OsString;`
- `use std::os::unix::ffi::OsStrExt;`
- `use std::os::unix::ffi::OsStringExt;`
- `use super::super::resolve_symlink_write_paths;`
- `use pretty_assertions::assert_eq;`
- `use std::os::unix::fs::symlink;`
- `use super::super::normalize_for_wsl_with_flag;`
- `use pretty_assertions::assert_eq;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
