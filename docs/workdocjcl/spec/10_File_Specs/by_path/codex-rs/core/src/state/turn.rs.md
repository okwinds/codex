# `codex-rs/core/src/state/turn.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4603`
- sha256: `47dbd2533d526322f29514e7eb580ac1c0cb601a3b64794bde0126ff674a4c10`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/state/turn.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/state/turn.rs:3` `use indexmap::IndexMap;`
- `use` `codex-rs/core/src/state/turn.rs:4` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/state/turn.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/core/src/state/turn.rs:6` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/state/turn.rs:7` `use tokio::sync::Notify;`
- `use` `codex-rs/core/src/state/turn.rs:8` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/state/turn.rs:9` `use tokio_util::task::AbortOnDropHandle;`
- `use` `codex-rs/core/src/state/turn.rs:11` `use codex_protocol::dynamic_tools::DynamicToolResponse;`
- `use` `codex-rs/core/src/state/turn.rs:12` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/state/turn.rs:13` `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use` `codex-rs/core/src/state/turn.rs:14` `use tokio::sync::oneshot;`
- `use` `codex-rs/core/src/state/turn.rs:16` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/state/turn.rs:17` `use crate::protocol::ReviewDecision;`
- `use` `codex-rs/core/src/state/turn.rs:18` `use crate::tasks::SessionTask;`
- `impl` `codex-rs/core/src/state/turn.rs:26` `impl Default for ActiveTurn {`
- `fn` `codex-rs/core/src/state/turn.rs:27` `fn default() -> Self {`
- `impl` `codex-rs/core/src/state/turn.rs:53` `impl ActiveTurn {`
- `impl` `codex-rs/core/src/state/turn.rs:78` `impl TurnState {`
- `impl` `codex-rs/core/src/state/turn.rs:150` `impl ActiveTurn {`

## Dependencies (auto sample)
### Imports / Includes
- `use indexmap::IndexMap;`
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::Notify;`
- `use tokio_util::sync::CancellationToken;`
- `use tokio_util::task::AbortOnDropHandle;`
- `use codex_protocol::dynamic_tools::DynamicToolResponse;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use tokio::sync::oneshot;`
- `use crate::codex::TurnContext;`
- `use crate::protocol::ReviewDecision;`
- `use crate::tasks::SessionTask;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
