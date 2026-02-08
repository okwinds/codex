# `codex-rs/core/src/tools/parallel.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4875`
- sha256: `9e03704bd49cfafab540314db32cee51923ad1e6a35cb65b57e8e6867351845d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/parallel.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/parallel.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/parallel.rs:2` `use std::time::Instant;`
- `use` `codex-rs/core/src/tools/parallel.rs:4` `use tokio::sync::RwLock;`
- `use` `codex-rs/core/src/tools/parallel.rs:5` `use tokio_util::either::Either;`
- `use` `codex-rs/core/src/tools/parallel.rs:6` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/tools/parallel.rs:7` `use tokio_util::task::AbortOnDropHandle;`
- `use` `codex-rs/core/src/tools/parallel.rs:8` `use tracing::Instrument;`
- `use` `codex-rs/core/src/tools/parallel.rs:9` `use tracing::instrument;`
- `use` `codex-rs/core/src/tools/parallel.rs:10` `use tracing::trace_span;`
- `use` `codex-rs/core/src/tools/parallel.rs:12` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/parallel.rs:13` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/parallel.rs:14` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/tools/parallel.rs:15` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/parallel.rs:16` `use crate::tools::context::SharedTurnDiffTracker;`
- `use` `codex-rs/core/src/tools/parallel.rs:17` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/parallel.rs:18` `use crate::tools::router::ToolCall;`
- `use` `codex-rs/core/src/tools/parallel.rs:19` `use crate::tools::router::ToolRouter;`
- `use` `codex-rs/core/src/tools/parallel.rs:20` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/tools/parallel.rs:21` `use codex_protocol::models::ResponseInputItem;`
- `impl` `codex-rs/core/src/tools/parallel.rs:32` `impl ToolCallRuntime {`
- `impl` `codex-rs/core/src/tools/parallel.rs:108` `impl ToolCallRuntime {`
- `fn` `codex-rs/core/src/tools/parallel.rs:109` `fn aborted_response(call: &ToolCall, secs: f32) -> ResponseInputItem {`
- `fn` `codex-rs/core/src/tools/parallel.rs:129` `fn abort_message(call: &ToolCall, secs: f32) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use std::time::Instant;`
- `use tokio::sync::RwLock;`
- `use tokio_util::either::Either;`
- `use tokio_util::sync::CancellationToken;`
- `use tokio_util::task::AbortOnDropHandle;`
- `use tracing::Instrument;`
- `use tracing::instrument;`
- `use tracing::trace_span;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::error::CodexErr;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::SharedTurnDiffTracker;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::router::ToolCall;`
- `use crate::tools::router::ToolRouter;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::models::ResponseInputItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
