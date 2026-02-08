# `codex-rs/utils/git/src/branch.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8134`
- sha256: `5e955a0e855265f4e0c9ff7880551110826292fb90a01af2a8844fbb78a81584`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/git/src/branch.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn merge_base_with_head(`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/git/src/branch.rs:1` `use std::ffi::OsString;`
- `use` `codex-rs/utils/git/src/branch.rs:2` `use std::path::Path;`
- `use` `codex-rs/utils/git/src/branch.rs:4` `use crate::GitToolingError;`
- `use` `codex-rs/utils/git/src/branch.rs:5` `use crate::operations::ensure_git_repository;`
- `use` `codex-rs/utils/git/src/branch.rs:6` `use crate::operations::resolve_head;`
- `use` `codex-rs/utils/git/src/branch.rs:7` `use crate::operations::resolve_repository_root;`
- `use` `codex-rs/utils/git/src/branch.rs:8` `use crate::operations::run_git_for_stdout;`
- `fn` `codex-rs/utils/git/src/branch.rs:15` `pub fn merge_base_with_head(`
- `fn` `codex-rs/utils/git/src/branch.rs:50` `fn resolve_branch_ref(repo_root: &Path, branch: &str) -> Result<Option<String>, GitToolingError> {`
- `fn` `codex-rs/utils/git/src/branch.rs:68` `fn resolve_upstream_if_remote_ahead(`
- `use` `codex-rs/utils/git/src/branch.rs:121` `use super::merge_base_with_head;`
- `use` `codex-rs/utils/git/src/branch.rs:122` `use crate::GitToolingError;`
- `use` `codex-rs/utils/git/src/branch.rs:123` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/utils/git/src/branch.rs:124` `use std::path::Path;`
- `use` `codex-rs/utils/git/src/branch.rs:125` `use std::process::Command;`
- `use` `codex-rs/utils/git/src/branch.rs:126` `use tempfile::tempdir;`
- `fn` `codex-rs/utils/git/src/branch.rs:128` `fn run_git_in(repo_path: &Path, args: &[&str]) {`
- `fn` `codex-rs/utils/git/src/branch.rs:137` `fn run_git_stdout(repo_path: &Path, args: &[&str]) -> String {`
- `fn` `codex-rs/utils/git/src/branch.rs:147` `fn init_test_repo(repo_path: &Path) {`
- `fn` `codex-rs/utils/git/src/branch.rs:152` `fn commit(repo_path: &Path, message: &str) {`
- `fn` `codex-rs/utils/git/src/branch.rs:168` `fn merge_base_returns_shared_commit() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/branch.rs:197` `fn merge_base_prefers_upstream_when_remote_ahead() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/branch.rs:242` `fn merge_base_returns_none_when_branch_missing() -> Result<(), GitToolingError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsString;`
- `use std::path::Path;`
- `use crate::GitToolingError;`
- `use crate::operations::ensure_git_repository;`
- `use crate::operations::resolve_head;`
- `use crate::operations::resolve_repository_root;`
- `use crate::operations::run_git_for_stdout;`
- `use super::merge_base_with_head;`
- `use crate::GitToolingError;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
- `use std::process::Command;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
