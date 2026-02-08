# `codex-rs/utils/pty/src/process.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4589`
- sha256: `d313e95fe0c998b8e24d8062659e8b1364b23ab824c3749d3346bf413c9ce4d3`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/pty/src/process.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PtyHandles {`
- `pub struct ProcessHandle {`
- `pub fn writer_sender(&self) -> mpsc::Sender<Vec<u8>> {`
- `pub fn output_receiver(&self) -> broadcast::Receiver<Vec<u8>> {`
- `pub fn has_exited(&self) -> bool {`
- `pub fn exit_code(&self) -> Option<i32> {`
- `pub fn terminate(&self) {`
- `pub struct SpawnedProcess {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/pty/src/process.rs:1` `use core::fmt;`
- `use` `codex-rs/utils/pty/src/process.rs:2` `use std::io;`
- `use` `codex-rs/utils/pty/src/process.rs:3` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/utils/pty/src/process.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/utils/pty/src/process.rs:5` `use std::sync::Mutex as StdMutex;`
- `use` `codex-rs/utils/pty/src/process.rs:7` `use portable_pty::MasterPty;`
- `use` `codex-rs/utils/pty/src/process.rs:8` `use portable_pty::SlavePty;`
- `use` `codex-rs/utils/pty/src/process.rs:9` `use tokio::sync::broadcast;`
- `use` `codex-rs/utils/pty/src/process.rs:10` `use tokio::sync::mpsc;`
- `use` `codex-rs/utils/pty/src/process.rs:11` `use tokio::sync::oneshot;`
- `use` `codex-rs/utils/pty/src/process.rs:12` `use tokio::task::AbortHandle;`
- `use` `codex-rs/utils/pty/src/process.rs:13` `use tokio::task::JoinHandle;`
- `fn` `codex-rs/utils/pty/src/process.rs:16` `fn kill(&mut self) -> io::Result<()>;`
- `struct` `codex-rs/utils/pty/src/process.rs:19` `pub struct PtyHandles {`
- `impl` `codex-rs/utils/pty/src/process.rs:24` `impl fmt::Debug for PtyHandles {`
- `fn` `codex-rs/utils/pty/src/process.rs:25` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `struct` `codex-rs/utils/pty/src/process.rs:31` `pub struct ProcessHandle {`
- `impl` `codex-rs/utils/pty/src/process.rs:46` `impl fmt::Debug for ProcessHandle {`
- `fn` `codex-rs/utils/pty/src/process.rs:47` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `impl` `codex-rs/utils/pty/src/process.rs:52` `impl ProcessHandle {`
- `fn` `codex-rs/utils/pty/src/process.rs:85` `pub fn writer_sender(&self) -> mpsc::Sender<Vec<u8>> {`
- `fn` `codex-rs/utils/pty/src/process.rs:90` `pub fn output_receiver(&self) -> broadcast::Receiver<Vec<u8>> {`
- `fn` `codex-rs/utils/pty/src/process.rs:95` `pub fn has_exited(&self) -> bool {`
- `fn` `codex-rs/utils/pty/src/process.rs:100` `pub fn exit_code(&self) -> Option<i32> {`
- `fn` `codex-rs/utils/pty/src/process.rs:105` `pub fn terminate(&self) {`
- `impl` `codex-rs/utils/pty/src/process.rs:135` `impl Drop for ProcessHandle {`
- `fn` `codex-rs/utils/pty/src/process.rs:136` `fn drop(&mut self) {`
- `struct` `codex-rs/utils/pty/src/process.rs:143` `pub struct SpawnedProcess {`

## Dependencies (auto sample)
### Imports / Includes
- `use core::fmt;`
- `use std::io;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::Arc;`
- `use std::sync::Mutex as StdMutex;`
- `use portable_pty::MasterPty;`
- `use portable_pty::SlavePty;`
- `use tokio::sync::broadcast;`
- `use tokio::sync::mpsc;`
- `use tokio::sync::oneshot;`
- `use tokio::task::AbortHandle;`
- `use tokio::task::JoinHandle;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
