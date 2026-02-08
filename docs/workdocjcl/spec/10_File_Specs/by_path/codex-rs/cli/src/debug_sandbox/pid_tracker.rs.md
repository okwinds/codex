# `codex-rs/cli/src/debug_sandbox/pid_tracker.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10005`
- sha256: `e15438e8252a5d2a9485374f5e99a23f16a9c0c26a34779535e027f846f93449`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/debug_sandbox/pid_tracker.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:1` `use std::collections::HashSet;`
- `use` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:2` `use tokio::task::JoinHandle;`
- `use` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:3` `use tracing::warn;`
- `impl` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:12` `impl PidTracker {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:31` `fn proc_listchildpids(`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:39` `fn list_child_pids(parent: i32) -> Vec<i32> {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:62` `fn pid_is_alive(pid: i32) -> bool {`
- `enum` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:77` `enum WatchPidError {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:83` `fn watch_pid(kq: libc::c_int, pid: i32) -> Result<(), WatchPidError> {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:110` `fn watch_children(`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:122` `fn add_pid_watch(kq: libc::c_int, pid: i32, seen: &mut HashSet<i32>, active: &mut HashSet<i32>) {`
- `const` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:151` `const STOP_IDENT: libc::uintptr_t = 1;`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:153` `fn register_stop_event(kq: libc::c_int) -> bool {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:167` `fn trigger_stop_event(kq: libc::c_int) {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:185` `fn track_descendants(kq: libc::c_int, root_pid: i32) -> HashSet<i32> {`
- `const` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:204` `const EVENTS_CAP: usize = 32;`
- `use` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:279` `use super::*;`
- `use` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:280` `use std::process::Command;`
- `use` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:281` `use std::process::Stdio;`
- `use` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:282` `use std::time::Duration;`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:285` `fn pid_is_alive_detects_current_process() {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:292` `fn list_child_pids_includes_spawned_child() {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:319` `async fn pid_tracker_collects_spawned_children() {`
- `fn` `codex-rs/cli/src/debug_sandbox/pid_tracker.rs:347` `async fn pid_tracker_collects_bash_subshell_descendants() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashSet;`
- `use tokio::task::JoinHandle;`
- `use tracing::warn;`
- `use super::*;`
- `use std::process::Command;`
- `use std::process::Stdio;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/03_API/CLI.md`
