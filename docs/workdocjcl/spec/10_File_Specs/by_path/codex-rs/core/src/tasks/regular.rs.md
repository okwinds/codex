# `codex-rs/core/src/tasks/regular.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1107`
- sha256: `0190ce243f25c997443acf84e09bb5fb661286e8ff851d6953ab0111f14635f2`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tasks/regular.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tasks/regular.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tasks/regular.rs:3` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tasks/regular.rs:4` `use crate::codex::run_turn;`
- `use` `codex-rs/core/src/tasks/regular.rs:5` `use crate::state::TaskKind;`
- `use` `codex-rs/core/src/tasks/regular.rs:6` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tasks/regular.rs:7` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/tasks/regular.rs:8` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/tasks/regular.rs:9` `use tracing::Instrument;`
- `use` `codex-rs/core/src/tasks/regular.rs:10` `use tracing::trace_span;`
- `use` `codex-rs/core/src/tasks/regular.rs:12` `use super::SessionTask;`
- `use` `codex-rs/core/src/tasks/regular.rs:13` `use super::SessionTaskContext;`
- `impl` `codex-rs/core/src/tasks/regular.rs:19` `impl SessionTask for RegularTask {`
- `fn` `codex-rs/core/src/tasks/regular.rs:20` `fn kind(&self) -> TaskKind {`
- `fn` `codex-rs/core/src/tasks/regular.rs:24` `async fn run(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use crate::codex::TurnContext;`
- `use crate::codex::run_turn;`
- `use crate::state::TaskKind;`
- `use async_trait::async_trait;`
- `use codex_protocol::user_input::UserInput;`
- `use tokio_util::sync::CancellationToken;`
- `use tracing::Instrument;`
- `use tracing::trace_span;`
- `use super::SessionTask;`
- `use super::SessionTaskContext;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
