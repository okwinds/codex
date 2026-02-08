# `codex-rs/core/src/unified_exec/async_watcher.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9413`
- sha256: `cc3c17803208b8beb1aa6522a4f3464b06611b46dc56e98cd3bc9f4aa5652443`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/unified_exec/async_watcher.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:2` `use std::pin::Pin;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:5` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:6` `use tokio::time::Duration;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:7` `use tokio::time::Instant;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:8` `use tokio::time::Sleep;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:10` `use super::UnifiedExecContext;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:11` `use super::process::UnifiedExecProcess;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:12` `use crate::codex::Session;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:13` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:14` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:15` `use crate::exec::MAX_EXEC_OUTPUT_DELTAS_PER_CALL;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:16` `use crate::exec::StreamOutput;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:17` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:18` `use crate::protocol::ExecCommandOutputDeltaEvent;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:19` `use crate::protocol::ExecCommandSource;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:20` `use crate::protocol::ExecOutputStream;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:21` `use crate::tools::events::ToolEmitter;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:22` `use crate::tools::events::ToolEventCtx;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:23` `use crate::tools::events::ToolEventStage;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:24` `use crate::unified_exec::head_tail_buffer::HeadTailBuffer;`
- `const` `codex-rs/core/src/unified_exec/async_watcher.rs:34` `const UNIFIED_EXEC_OUTPUT_DELTA_MAX_BYTES: usize = 8192;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:53` `use tokio::sync::broadcast::error::RecvError;`
- `fn` `codex-rs/core/src/unified_exec/async_watcher.rs:142` `async fn process_chunk(`
- `fn` `codex-rs/core/src/unified_exec/async_watcher.rs:211` `fn split_valid_utf8_prefix(buffer: &mut Vec<u8>) -> Option<Vec<u8>> {`
- `fn` `codex-rs/core/src/unified_exec/async_watcher.rs:215` `fn split_valid_utf8_prefix_with_max(buffer: &mut Vec<u8>, max_bytes: usize) -> Option<Vec<u8>> {`
- `fn` `codex-rs/core/src/unified_exec/async_watcher.rs:241` `async fn resolve_aggregated_output(`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:255` `use super::split_valid_utf8_prefix_with_max;`
- `use` `codex-rs/core/src/unified_exec/async_watcher.rs:257` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/unified_exec/async_watcher.rs:260` `fn split_valid_utf8_prefix_respects_max_bytes_for_ascii() {`
- `fn` `codex-rs/core/src/unified_exec/async_watcher.rs:273` `fn split_valid_utf8_prefix_avoids_splitting_utf8_codepoints() {`
- `fn` `codex-rs/core/src/unified_exec/async_watcher.rs:283` `fn split_valid_utf8_prefix_makes_progress_on_invalid_utf8() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::pin::Pin;`
- `use std::sync::Arc;`
- `use tokio::sync::Mutex;`
- `use tokio::time::Duration;`
- `use tokio::time::Instant;`
- `use tokio::time::Sleep;`
- `use super::UnifiedExecContext;`
- `use super::process::UnifiedExecProcess;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::exec::MAX_EXEC_OUTPUT_DELTAS_PER_CALL;`
- `use crate::exec::StreamOutput;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::ExecCommandOutputDeltaEvent;`
- `use crate::protocol::ExecCommandSource;`
- `use crate::protocol::ExecOutputStream;`
- `use crate::tools::events::ToolEmitter;`
- `use crate::tools::events::ToolEventCtx;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
