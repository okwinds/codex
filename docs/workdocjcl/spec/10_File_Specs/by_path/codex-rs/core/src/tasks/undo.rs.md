# `codex-rs/core/src/tasks/undo.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4036`
- sha256: `ffb9282e964f659c45a827a3c160191c3a470c36e27941ed2e8eebe627b2f577`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tasks/undo.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tasks/undo.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tasks/undo.rs:3` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tasks/undo.rs:4` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tasks/undo.rs:5` `use crate::protocol::UndoCompletedEvent;`
- `use` `codex-rs/core/src/tasks/undo.rs:6` `use crate::protocol::UndoStartedEvent;`
- `use` `codex-rs/core/src/tasks/undo.rs:7` `use crate::state::TaskKind;`
- `use` `codex-rs/core/src/tasks/undo.rs:8` `use crate::tasks::SessionTask;`
- `use` `codex-rs/core/src/tasks/undo.rs:9` `use crate::tasks::SessionTaskContext;`
- `use` `codex-rs/core/src/tasks/undo.rs:10` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tasks/undo.rs:11` `use codex_git::RestoreGhostCommitOptions;`
- `use` `codex-rs/core/src/tasks/undo.rs:12` `use codex_git::restore_ghost_commit_with_options;`
- `use` `codex-rs/core/src/tasks/undo.rs:13` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/tasks/undo.rs:14` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/tasks/undo.rs:15` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/tasks/undo.rs:16` `use tracing::error;`
- `use` `codex-rs/core/src/tasks/undo.rs:17` `use tracing::info;`
- `use` `codex-rs/core/src/tasks/undo.rs:18` `use tracing::warn;`
- `impl` `codex-rs/core/src/tasks/undo.rs:22` `impl UndoTask {`
- `impl` `codex-rs/core/src/tasks/undo.rs:29` `impl SessionTask for UndoTask {`
- `fn` `codex-rs/core/src/tasks/undo.rs:30` `fn kind(&self) -> TaskKind {`
- `fn` `codex-rs/core/src/tasks/undo.rs:34` `async fn run(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use crate::codex::TurnContext;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::UndoCompletedEvent;`
- `use crate::protocol::UndoStartedEvent;`
- `use crate::state::TaskKind;`
- `use crate::tasks::SessionTask;`
- `use crate::tasks::SessionTaskContext;`
- `use async_trait::async_trait;`
- `use codex_git::RestoreGhostCommitOptions;`
- `use codex_git::restore_ghost_commit_with_options;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::user_input::UserInput;`
- `use tokio_util::sync::CancellationToken;`
- `use tracing::error;`
- `use tracing::info;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
