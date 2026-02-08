# `codex-rs/core/src/tasks/compact.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1378`
- sha256: `21bc42db87d08047b4d95b5bc06d8a2d75678a06453a8b52af1804027b47388b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tasks/compact.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tasks/compact.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tasks/compact.rs:3` `use super::SessionTask;`
- `use` `codex-rs/core/src/tasks/compact.rs:4` `use super::SessionTaskContext;`
- `use` `codex-rs/core/src/tasks/compact.rs:5` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tasks/compact.rs:6` `use crate::state::TaskKind;`
- `use` `codex-rs/core/src/tasks/compact.rs:7` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tasks/compact.rs:8` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/tasks/compact.rs:9` `use tokio_util::sync::CancellationToken;`
- `impl` `codex-rs/core/src/tasks/compact.rs:15` `impl SessionTask for CompactTask {`
- `fn` `codex-rs/core/src/tasks/compact.rs:16` `fn kind(&self) -> TaskKind {`
- `fn` `codex-rs/core/src/tasks/compact.rs:20` `async fn run(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use super::SessionTask;`
- `use super::SessionTaskContext;`
- `use crate::codex::TurnContext;`
- `use crate::state::TaskKind;`
- `use async_trait::async_trait;`
- `use codex_protocol::user_input::UserInput;`
- `use tokio_util::sync::CancellationToken;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
