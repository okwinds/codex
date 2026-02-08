# `codex-rs/linux-sandbox/src/linux_run_main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13019`
- sha256: `3e723ff1bce8897c8f506fa1c3cea5505d72176dddd8c8ccd393915c59fe93f6`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/src/linux_run_main.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct LandlockCommand {`
- `pub fn run_main() -> ! {`

## Definitions (auto, per-file)
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:1` `use clap::Parser;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:2` `use std::ffi::CString;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:3` `use std::fs::File;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:4` `use std::io::Read;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:5` `use std::os::fd::FromRawFd;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:6` `use std::path::Path;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:9` `use crate::bwrap::BwrapOptions;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:10` `use crate::bwrap::create_bwrap_command_args;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:11` `use crate::landlock::apply_sandbox_policy_to_current_thread;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:12` `use crate::vendored_bwrap::exec_vendored_bwrap;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:13` `use crate::vendored_bwrap::run_vendored_bwrap_main;`
- `struct` `codex-rs/linux-sandbox/src/linux_run_main.rs:20` `pub struct LandlockCommand {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:61` `pub fn run_main() -> ! {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:117` `fn run_bwrap_with_proc_fallback(`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:135` `fn build_bwrap_argv(`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:158` `fn preflight_proc_mount_support(`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:173` `fn resolve_true_command() -> String {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:193` `fn run_bwrap_in_child_capture_stderr(argv: Vec<String>) -> String {`
- `const` `codex-rs/linux-sandbox/src/linux_run_main.rs:194` `const MAX_PREFLIGHT_STDERR_BYTES: u64 = 64 * 1024;`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:252` `fn close_fd_or_panic(fd: libc::c_int, context: &str) {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:260` `fn is_proc_mount_failure(stderr: &str) -> bool {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:267` `fn build_inner_seccomp_command(`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:299` `fn exec_or_panic(command: Vec<String>) -> ! {`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:323` `use super::*;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:324` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/linux-sandbox/src/linux_run_main.rs:325` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:328` `fn detects_proc_mount_invalid_argument_failure() {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:334` `fn ignores_non_proc_mount_errors() {`
- `fn` `codex-rs/linux-sandbox/src/linux_run_main.rs:340` `fn inserts_bwrap_argv0_before_command_separator() {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Parser;`
- `use std::ffi::CString;`
- `use std::fs::File;`
- `use std::io::Read;`
- `use std::os::fd::FromRawFd;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use crate::bwrap::BwrapOptions;`
- `use crate::bwrap::create_bwrap_command_args;`
- `use crate::landlock::apply_sandbox_policy_to_current_thread;`
- `use crate::vendored_bwrap::exec_vendored_bwrap;`
- `use crate::vendored_bwrap::run_vendored_bwrap_main;`
- `use super::*;`
- `use codex_core::protocol::SandboxPolicy;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
