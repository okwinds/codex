# `codex-rs/utils/pty/src/process_group.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4402`
- sha256: `1b243258199ad932aff7646ed82f2ee319fa5830ebc1d5f1c68b19eaf949737d`
- generated_utc: `2026-02-03T16:08:31Z`

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
- `fn` `codex-rs/utils/pty/src/process_group.rs:122` `pub fn kill_process_group(process_group_id: u32) -> io::Result<()> {`
- `use` `codex-rs/utils/pty/src/process_group.rs:123` `use std::io::ErrorKind;`
- `fn` `codex-rs/utils/pty/src/process_group.rs:139` `pub fn kill_process_group(_process_group_id: u32) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:145` `pub fn kill_child_process_group(child: &mut Child) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/process_group.rs:155` `pub fn kill_child_process_group(_child: &mut Child) -> io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use tokio::process::Child;`
- `use std::io::ErrorKind;`
- `use std::io::ErrorKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
