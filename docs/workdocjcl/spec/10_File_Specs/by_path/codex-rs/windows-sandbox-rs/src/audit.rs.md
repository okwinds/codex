# `codex-rs/windows-sandbox-rs/src/audit.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11617`
- sha256: `46fe69311ef2e86372b1b8b0238ba93ec016c8dd7d5d6d82cbbf8a8df339da17`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/audit.rs` (read)
- env: `PATH`, `PUBLIC`, `USERPROFILE`

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn audit_everyone_writable(`
- `pub fn apply_world_writable_scan_and_denies(`
- `pub fn apply_capability_denies_for_world_writable(`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:1` `use crate::acl::add_deny_write_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:2` `use crate::acl::path_mask_allows;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:3` `use crate::cap::cap_sid_file;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:4` `use crate::cap::load_or_create_cap_sids;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:5` `use crate::logging::{debug_log, log_note};`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:6` `use crate::path_normalization::canonical_path_key;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:7` `use crate::policy::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:8` `use crate::token::convert_string_sid_to_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:9` `use crate::token::world_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:10` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:11` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:12` `use std::collections::HashSet;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:13` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:14` `use std::ffi::OsStr;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:15` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:16` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:17` `use std::time::Duration;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:18` `use std::time::Instant;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:19` `use windows_sys::Win32::Storage::FileSystem::FILE_APPEND_DATA;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:20` `use windows_sys::Win32::Storage::FileSystem::FILE_WRITE_ATTRIBUTES;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:21` `use windows_sys::Win32::Storage::FileSystem::FILE_WRITE_DATA;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:22` `use windows_sys::Win32::Storage::FileSystem::FILE_WRITE_EA;`
- `const` `codex-rs/windows-sandbox-rs/src/audit.rs:25` `const MAX_ITEMS_PER_DIR: i32 = 1000;`
- `const` `codex-rs/windows-sandbox-rs/src/audit.rs:26` `const AUDIT_TIME_LIMIT_SECS: i64 = 2;`
- `const` `codex-rs/windows-sandbox-rs/src/audit.rs:27` `const MAX_CHECKED_LIMIT: i32 = 50000;`
- `const` `codex-rs/windows-sandbox-rs/src/audit.rs:29` `const SKIP_DIR_SUFFIXES: &[&str] = &[`
- `fn` `codex-rs/windows-sandbox-rs/src/audit.rs:35` `fn unique_push(set: &mut HashSet<PathBuf>, out: &mut Vec<PathBuf>, p: PathBuf) {`
- `fn` `codex-rs/windows-sandbox-rs/src/audit.rs:43` `fn gather_candidates(cwd: &Path, env: &std::collections::HashMap<String, String>) -> Vec<PathBuf> {`
- `fn` `codex-rs/windows-sandbox-rs/src/audit.rs:87` `pub fn audit_everyone_writable(`
- `fn` `codex-rs/windows-sandbox-rs/src/audit.rs:213` `pub fn apply_world_writable_scan_and_denies(`
- `fn` `codex-rs/windows-sandbox-rs/src/audit.rs:239` `pub fn apply_capability_denies_for_world_writable(`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:301` `use super::gather_candidates;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:302` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/audit.rs:303` `use std::fs;`
- `fn` `codex-rs/windows-sandbox-rs/src/audit.rs:306` `fn gathers_path_entries_by_list_separator() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::acl::add_deny_write_ace;`
- `use crate::acl::path_mask_allows;`
- `use crate::cap::cap_sid_file;`
- `use crate::cap::load_or_create_cap_sids;`
- `use crate::logging::{debug_log, log_note};`
- `use crate::path_normalization::canonical_path_key;`
- `use crate::policy::SandboxPolicy;`
- `use crate::token::convert_string_sid_to_sid;`
- `use crate::token::world_sid;`
- `use anyhow::anyhow;`
- `use anyhow::Result;`
- `use std::collections::HashSet;`
- `use std::ffi::c_void;`
- `use std::ffi::OsStr;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use windows_sys::Win32::Storage::FileSystem::FILE_APPEND_DATA;`
- `use windows_sys::Win32::Storage::FileSystem::FILE_WRITE_ATTRIBUTES;`
### Referenced env vars
- `PATH`
- `PUBLIC`
- `USERPROFILE`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
