# `codex-rs/utils/pty/src/process_group.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5170`
- sha256: `2ef17e2a43fc8a56acc83b8aafa6c120b2791875b79933bb97e14fe6e960615c`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/process_group.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn set_parent_death_signal(parent_pid: libc::pid_t) -> io::Result<()> {`
- `pub fn set_parent_death_signal(_parent_pid: i32) -> io::Result<()> {`
- `pub fn detach_from_tty() -> io::Result<()> {`
- `pub fn detach_from_tty() -> io::Result<()> {`
- `pub fn set_process_group() -> io::Result<()> {`
- `pub fn set_process_group() -> io::Result<()> {`
- `pub fn kill_process_group_by_pid(pid: u32) -> io::Result<()> {`
- `pub fn kill_process_group_by_pid(_pid: u32) -> io::Result<()> {`
- `pub fn terminate_process_group(process_group_id: u32) -> io::Result<bool> {`
- `pub fn terminate_process_group(_process_group_id: u32) -> io::Result<bool> {`
- `pub fn kill_process_group(process_group_id: u32) -> io::Result<()> {`
- `pub fn kill_process_group(_process_group_id: u32) -> io::Result<()> {`
- `pub fn kill_child_process_group(child: &mut Child) -> io::Result<()> {`
- `pub fn kill_child_process_group(_child: &mut Child) -> io::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/process_group.rs:18` `use std::io;`
- `use` `codex-rs/utils/pty/src/process_group.rs:20` `use tokio::process::Child;`
- `fn` `codex-rs/utils/pty/src/process_group.rs:27` `pub fn set_parent_death_signal(parent_pid: libc::pid_t) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:43` `pub fn set_parent_death_signal(_parent_pid: i32) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:49` `pub fn detach_from_tty() -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:63` `pub fn detach_from_tty() -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:71` `pub fn set_process_group() -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:82` `pub fn set_process_group() -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:90` `pub fn kill_process_group_by_pid(pid: u32) -> io::Result<()> {`
- `use` `codex-rs/utils/pty/src/process_group.rs:91` `use std::io::ErrorKind;`
- `fn` `codex-rs/utils/pty/src/process_group.rs:116` `pub fn kill_process_group_by_pid(_pid: u32) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:125` `pub fn terminate_process_group(process_group_id: u32) -> io::Result<bool> {`
- `use` `codex-rs/utils/pty/src/process_group.rs:126` `use std::io::ErrorKind;`
- `fn` `codex-rs/utils/pty/src/process_group.rs:143` `pub fn terminate_process_group(_process_group_id: u32) -> io::Result<bool> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:149` `pub fn kill_process_group(process_group_id: u32) -> io::Result<()> {`
- `use` `codex-rs/utils/pty/src/process_group.rs:150` `use std::io::ErrorKind;`
- `fn` `codex-rs/utils/pty/src/process_group.rs:166` `pub fn kill_process_group(_process_group_id: u32) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:172` `pub fn kill_child_process_group(child: &mut Child) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:182` `pub fn kill_child_process_group(_child: &mut Child) -> io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use tokio::process::Child;`
- `use std::io::ErrorKind;`
- `use std::io::ErrorKind;`
- `use std::io::ErrorKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
