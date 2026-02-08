# `codex-rs/utils/pty/src/pipe.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7329`
- sha256: `6ecafde2ae85b1266cef3a317137ca16f7899acab11690f58a5e4e7f7633208e`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/pipe.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/pipe.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/utils/pty/src/pipe.rs:2` `use std::io;`
- `use` `codex-rs/utils/pty/src/pipe.rs:3` `use std::io::ErrorKind;`
- `use` `codex-rs/utils/pty/src/pipe.rs:4` `use std::path::Path;`
- `use` `codex-rs/utils/pty/src/pipe.rs:5` `use std::process::Stdio;`
- `use` `codex-rs/utils/pty/src/pipe.rs:6` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/utils/pty/src/pipe.rs:7` `use std::sync::Arc;`
- `use` `codex-rs/utils/pty/src/pipe.rs:8` `use std::sync::Mutex as StdMutex;`
- `use` `codex-rs/utils/pty/src/pipe.rs:10` `use anyhow::Result;`
- `use` `codex-rs/utils/pty/src/pipe.rs:11` `use tokio::io::AsyncRead;`
- `use` `codex-rs/utils/pty/src/pipe.rs:12` `use tokio::io::AsyncReadExt;`
- `use` `codex-rs/utils/pty/src/pipe.rs:13` `use tokio::io::AsyncWriteExt;`
- `use` `codex-rs/utils/pty/src/pipe.rs:14` `use tokio::io::BufReader;`
- `use` `codex-rs/utils/pty/src/pipe.rs:15` `use tokio::process::Command;`
- `use` `codex-rs/utils/pty/src/pipe.rs:16` `use tokio::sync::broadcast;`
- `use` `codex-rs/utils/pty/src/pipe.rs:17` `use tokio::sync::mpsc;`
- `use` `codex-rs/utils/pty/src/pipe.rs:18` `use tokio::sync::oneshot;`
- `use` `codex-rs/utils/pty/src/pipe.rs:19` `use tokio::task::JoinHandle;`
- `use` `codex-rs/utils/pty/src/pipe.rs:21` `use crate::process::ChildTerminator;`
- `use` `codex-rs/utils/pty/src/pipe.rs:22` `use crate::process::ProcessHandle;`
- `use` `codex-rs/utils/pty/src/pipe.rs:23` `use crate::process::SpawnedProcess;`
- `use` `codex-rs/utils/pty/src/pipe.rs:26` `use libc;`
- `struct` `codex-rs/utils/pty/src/pipe.rs:28` `struct PipeChildTerminator {`
- `impl` `codex-rs/utils/pty/src/pipe.rs:35` `impl ChildTerminator for PipeChildTerminator {`
- `fn` `codex-rs/utils/pty/src/pipe.rs:36` `fn kill(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/utils/pty/src/pipe.rs:55` `fn kill_process(pid: u32) -> io::Result<()> {`
- `enum` `codex-rs/utils/pty/src/pipe.rs:94` `enum PipeStdinMode {`
- `fn` `codex-rs/utils/pty/src/pipe.rs:99` `async fn spawn_process_with_stdin_mode(`
- `fn` `codex-rs/utils/pty/src/pipe.rs:249` `pub async fn spawn_process(`
- `fn` `codex-rs/utils/pty/src/pipe.rs:260` `pub async fn spawn_process_no_stdin(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::io;`
- `use std::io::ErrorKind;`
- `use std::path::Path;`
- `use std::process::Stdio;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::Arc;`
- `use std::sync::Mutex as StdMutex;`
- `use anyhow::Result;`
- `use tokio::io::AsyncRead;`
- `use tokio::io::AsyncReadExt;`
- `use tokio::io::AsyncWriteExt;`
- `use tokio::io::BufReader;`
- `use tokio::process::Command;`
- `use tokio::sync::broadcast;`
- `use tokio::sync::mpsc;`
- `use tokio::sync::oneshot;`
- `use tokio::task::JoinHandle;`
- `use crate::process::ChildTerminator;`
- `use crate::process::ProcessHandle;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
