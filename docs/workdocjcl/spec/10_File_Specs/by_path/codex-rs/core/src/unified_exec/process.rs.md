# `codex-rs/core/src/unified_exec/process.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7023`
- sha256: `10b14ebb85997bfb0dcc89b825d26973deaf6638a7cc729704e015a774349ca3`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/unified_exec/process.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/unified_exec/process.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/core/src/unified_exec/process.rs:4` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/unified_exec/process.rs:5` `use tokio::sync::Notify;`
- `use` `codex-rs/core/src/unified_exec/process.rs:6` `use tokio::sync::mpsc;`
- `use` `codex-rs/core/src/unified_exec/process.rs:7` `use tokio::sync::oneshot::error::TryRecvError;`
- `use` `codex-rs/core/src/unified_exec/process.rs:8` `use tokio::task::JoinHandle;`
- `use` `codex-rs/core/src/unified_exec/process.rs:9` `use tokio::time::Duration;`
- `use` `codex-rs/core/src/unified_exec/process.rs:10` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/unified_exec/process.rs:12` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/unified_exec/process.rs:13` `use crate::exec::SandboxType;`
- `use` `codex-rs/core/src/unified_exec/process.rs:14` `use crate::exec::StreamOutput;`
- `use` `codex-rs/core/src/unified_exec/process.rs:15` `use crate::exec::is_likely_sandbox_denied;`
- `use` `codex-rs/core/src/unified_exec/process.rs:16` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/unified_exec/process.rs:17` `use crate::truncate::formatted_truncate_text;`
- `use` `codex-rs/core/src/unified_exec/process.rs:18` `use codex_utils_pty::ExecCommandSession;`
- `use` `codex-rs/core/src/unified_exec/process.rs:19` `use codex_utils_pty::SpawnedPty;`
- `use` `codex-rs/core/src/unified_exec/process.rs:21` `use super::UNIFIED_EXEC_OUTPUT_MAX_TOKENS;`
- `use` `codex-rs/core/src/unified_exec/process.rs:22` `use super::UnifiedExecError;`
- `use` `codex-rs/core/src/unified_exec/process.rs:23` `use super::head_tail_buffer::HeadTailBuffer;`
- `impl` `codex-rs/core/src/unified_exec/process.rs:43` `impl UnifiedExecProcess {`
- `fn` `codex-rs/core/src/unified_exec/process.rs:120` `async fn snapshot_output(&self) -> Vec<Vec<u8>> {`
- `fn` `codex-rs/core/src/unified_exec/process.rs:215` `fn signal_exit(&self) {`
- `impl` `codex-rs/core/src/unified_exec/process.rs:220` `impl Drop for UnifiedExecProcess {`
- `fn` `codex-rs/core/src/unified_exec/process.rs:221` `fn drop(&mut self) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::Notify;`
- `use tokio::sync::mpsc;`
- `use tokio::sync::oneshot::error::TryRecvError;`
- `use tokio::task::JoinHandle;`
- `use tokio::time::Duration;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::exec::SandboxType;`
- `use crate::exec::StreamOutput;`
- `use crate::exec::is_likely_sandbox_denied;`
- `use crate::truncate::TruncationPolicy;`
- `use crate::truncate::formatted_truncate_text;`
- `use codex_utils_pty::ExecCommandSession;`
- `use codex_utils_pty::SpawnedPty;`
- `use super::UNIFIED_EXEC_OUTPUT_MAX_TOKENS;`
- `use super::UnifiedExecError;`
- `use super::head_tail_buffer::HeadTailBuffer;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
