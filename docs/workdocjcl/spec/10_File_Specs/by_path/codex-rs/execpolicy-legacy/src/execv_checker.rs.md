# `codex-rs/execpolicy-legacy/src/execv_checker.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8951`
- sha256: `2c2c281d491be77afd204ebfa774813267330c8e0f10bbe1316bb5bc91807a6c`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/execv_checker.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct ExecvChecker {`
- `pub fn new(execv_policy: Policy) -> Self {`
- `pub fn check(`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:1` `use std::borrow::Cow;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:2` `use std::ffi::OsString;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:3` `use std::path::Path;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:6` `use crate::ArgType;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:7` `use crate::Error::CannotCanonicalizePath;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:8` `use crate::Error::CannotCheckRelativePath;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:9` `use crate::Error::ReadablePathNotInReadableFolders;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:10` `use crate::Error::WriteablePathNotInWriteableFolders;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:11` `use crate::ExecCall;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:12` `use crate::MatchedExec;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:13` `use crate::Policy;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:14` `use crate::Result;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:15` `use crate::ValidExec;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:16` `use path_absolutize::*;`
- `struct` `codex-rs/execpolicy-legacy/src/execv_checker.rs:29` `pub struct ExecvChecker {`
- `impl` `codex-rs/execpolicy-legacy/src/execv_checker.rs:33` `impl ExecvChecker {`
- `fn` `codex-rs/execpolicy-legacy/src/execv_checker.rs:34` `pub fn new(execv_policy: Policy) -> Self {`
- `fn` `codex-rs/execpolicy-legacy/src/execv_checker.rs:44` `pub fn check(`
- `fn` `codex-rs/execpolicy-legacy/src/execv_checker.rs:101` `fn ensure_absolute_path(path: &str, cwd: &Option<OsString>) -> Result<PathBuf> {`
- `fn` `codex-rs/execpolicy-legacy/src/execv_checker.rs:119` `fn is_executable_file(path: &str) -> bool {`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:125` `use std::os::unix::fs::PermissionsExt;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:144` `use tempfile::TempDir;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:146` `use super::*;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:147` `use crate::MatchedArg;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:148` `use crate::PolicyParser;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:149` `use anyhow::Result;`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:150` `use anyhow::anyhow;`
- `fn` `codex-rs/execpolicy-legacy/src/execv_checker.rs:152` `fn setup(fake_cp: &Path) -> ExecvChecker {`
- `fn` `codex-rs/execpolicy-legacy/src/execv_checker.rs:168` `fn test_check_valid_input_files() -> Result<()> {`
- `use` `codex-rs/execpolicy-legacy/src/execv_checker.rs:175` `use std::os::unix::fs::PermissionsExt;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::borrow::Cow;`
- `use std::ffi::OsString;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use crate::ArgType;`
- `use crate::Error::CannotCanonicalizePath;`
- `use crate::Error::CannotCheckRelativePath;`
- `use crate::Error::ReadablePathNotInReadableFolders;`
- `use crate::Error::WriteablePathNotInWriteableFolders;`
- `use crate::ExecCall;`
- `use crate::MatchedExec;`
- `use crate::Policy;`
- `use crate::Result;`
- `use crate::ValidExec;`
- `use path_absolutize::*;`
- `use std::os::unix::fs::PermissionsExt;`
- `use tempfile::TempDir;`
- `use super::*;`
- `use crate::MatchedArg;`
- `use crate::PolicyParser;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
