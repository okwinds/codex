# `codex-rs/utils/pty/src/pty.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4984`
- sha256: `d76ecb60f404f08aac5282aa096c2dcd416f05bd9d0d4b93508103f90937ecd1`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/pty.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn conpty_supported() -> bool {`
- `pub fn conpty_supported() -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/pty.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/utils/pty/src/pty.rs:2` `use std::io::ErrorKind;`
- `use` `codex-rs/utils/pty/src/pty.rs:3` `use std::path::Path;`
- `use` `codex-rs/utils/pty/src/pty.rs:4` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/utils/pty/src/pty.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/utils/pty/src/pty.rs:6` `use std::sync::Mutex as StdMutex;`
- `use` `codex-rs/utils/pty/src/pty.rs:7` `use std::time::Duration;`
- `use` `codex-rs/utils/pty/src/pty.rs:9` `use anyhow::Result;`
- `use` `codex-rs/utils/pty/src/pty.rs:11` `use portable_pty::native_pty_system;`
- `use` `codex-rs/utils/pty/src/pty.rs:12` `use portable_pty::CommandBuilder;`
- `use` `codex-rs/utils/pty/src/pty.rs:13` `use portable_pty::PtySize;`
- `use` `codex-rs/utils/pty/src/pty.rs:14` `use tokio::sync::broadcast;`
- `use` `codex-rs/utils/pty/src/pty.rs:15` `use tokio::sync::mpsc;`
- `use` `codex-rs/utils/pty/src/pty.rs:16` `use tokio::sync::oneshot;`
- `use` `codex-rs/utils/pty/src/pty.rs:17` `use tokio::task::JoinHandle;`
- `use` `codex-rs/utils/pty/src/pty.rs:19` `use crate::process::ChildTerminator;`
- `use` `codex-rs/utils/pty/src/pty.rs:20` `use crate::process::ProcessHandle;`
- `use` `codex-rs/utils/pty/src/pty.rs:21` `use crate::process::PtyHandles;`
- `use` `codex-rs/utils/pty/src/pty.rs:22` `use crate::process::SpawnedProcess;`
- `fn` `codex-rs/utils/pty/src/pty.rs:26` `pub fn conpty_supported() -> bool {`
- `fn` `codex-rs/utils/pty/src/pty.rs:32` `pub fn conpty_supported() -> bool {`
- `struct` `codex-rs/utils/pty/src/pty.rs:36` `struct PtyChildTerminator {`
- `impl` `codex-rs/utils/pty/src/pty.rs:40` `impl ChildTerminator for PtyChildTerminator {`
- `fn` `codex-rs/utils/pty/src/pty.rs:41` `fn kill(&mut self) -> std::io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/pty.rs:46` `fn platform_native_pty_system() -> Box<dyn portable_pty::PtySystem + Send> {`
- `fn` `codex-rs/utils/pty/src/pty.rs:59` `pub async fn spawn_process(`
- `use` `codex-rs/utils/pty/src/pty.rs:122` `use std::io::Write;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::io::ErrorKind;`
- `use std::path::Path;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::Arc;`
- `use std::sync::Mutex as StdMutex;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use portable_pty::native_pty_system;`
- `use portable_pty::CommandBuilder;`
- `use portable_pty::PtySize;`
- `use tokio::sync::broadcast;`
- `use tokio::sync::mpsc;`
- `use tokio::sync::oneshot;`
- `use tokio::task::JoinHandle;`
- `use crate::process::ChildTerminator;`
- `use crate::process::ProcessHandle;`
- `use crate::process::PtyHandles;`
- `use crate::process::SpawnedProcess;`
- `use std::io::Write;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
