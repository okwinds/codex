# `codex-rs/core/src/tasks/compact.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1330`
- sha256: `a1b549d387b0b9922ae65c914f6d4bb390dd6df974827ef47f810b461e34afb4`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
