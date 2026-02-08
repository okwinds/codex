# `codex-rs/process-hardening/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5720`
- sha256: `c08a887c3d5eb6db2b344c86b3fad7f28a110784ab59acf5bc01c227a7d134a5`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/process-hardening/src/lib.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn pre_main_hardening() {`

## Definitions (auto, per-file)
- `use` `codex-rs/process-hardening/src/lib.rs:2` `use std::ffi::OsString;`
- `use` `codex-rs/process-hardening/src/lib.rs:5` `use std::os::unix::ffi::OsStrExt;`
- `fn` `codex-rs/process-hardening/src/lib.rs:12` `pub fn pre_main_hardening() {`
- `const` `codex-rs/process-hardening/src/lib.rs:28` `const PRCTL_FAILED_EXIT_CODE: i32 = 5;`
- `const` `codex-rs/process-hardening/src/lib.rs:31` `const PTRACE_DENY_ATTACH_FAILED_EXIT_CODE: i32 = 6;`
- `const` `codex-rs/process-hardening/src/lib.rs:41` `const SET_RLIMIT_CORE_FAILED_EXIT_CODE: i32 = 7;`
- `fn` `codex-rs/process-hardening/src/lib.rs:109` `fn set_core_file_size_limit_to_zero() {`
- `use` `codex-rs/process-hardening/src/lib.rs:147` `use super::*;`
- `use` `codex-rs/process-hardening/src/lib.rs:148` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/process-hardening/src/lib.rs:149` `use std::ffi::OsStr;`
- `use` `codex-rs/process-hardening/src/lib.rs:150` `use std::os::unix::ffi::OsStrExt;`
- `use` `codex-rs/process-hardening/src/lib.rs:151` `use std::os::unix::ffi::OsStringExt;`
- `fn` `codex-rs/process-hardening/src/lib.rs:154` `fn env_keys_with_prefix_handles_non_utf8_entries() {`
- `fn` `codex-rs/process-hardening/src/lib.rs:178` `fn env_keys_with_prefix_filters_only_matching_keys() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsString;`
- `use std::os::unix::ffi::OsStrExt;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use std::ffi::OsStr;`
- `use std::os::unix::ffi::OsStrExt;`
- `use std::os::unix::ffi::OsStringExt;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
