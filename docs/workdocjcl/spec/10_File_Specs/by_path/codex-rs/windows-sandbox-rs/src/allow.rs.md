# `codex-rs/windows-sandbox-rs/src/allow.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7445`
- sha256: `4a5701ff270c0a10501462da20b99e6c38410d5eb8cfa62f6f14effa6924511f`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/allow.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct AllowDenyPaths {`
- `pub fn compute_allow_paths(`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:1` `use crate::policy::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:2` `use dunce::canonicalize;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:3` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:4` `use std::collections::HashSet;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:5` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:6` `use std::path::PathBuf;`
- `struct` `codex-rs/windows-sandbox-rs/src/allow.rs:9` `pub struct AllowDenyPaths {`
- `fn` `codex-rs/windows-sandbox-rs/src/allow.rs:14` `pub fn compute_allow_paths(`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:95` `use super::*;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:96` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:97` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:98` `use std::fs;`
- `use` `codex-rs/windows-sandbox-rs/src/allow.rs:99` `use tempfile::TempDir;`
- `fn` `codex-rs/windows-sandbox-rs/src/allow.rs:102` `fn includes_additional_writable_roots() {`
- `fn` `codex-rs/windows-sandbox-rs/src/allow.rs:128` `fn excludes_tmp_env_vars_when_requested() {`
- `fn` `codex-rs/windows-sandbox-rs/src/allow.rs:156` `fn denies_git_dir_inside_writable_root() {`
- `fn` `codex-rs/windows-sandbox-rs/src/allow.rs:182` `fn denies_git_file_inside_writable_root() {`
- `fn` `codex-rs/windows-sandbox-rs/src/allow.rs:209` `fn skips_git_dir_when_missing() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::policy::SandboxPolicy;`
- `use dunce::canonicalize;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use super::*;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use std::fs;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
