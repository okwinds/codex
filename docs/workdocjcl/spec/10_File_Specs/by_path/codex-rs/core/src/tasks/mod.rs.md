# `codex-rs/core/src/tasks/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10721`
- sha256: `86b7159fa398264d53d10433ba982fcdd6d2dc1cf14212e21d90b86bb7bb4ff9`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tasks/mod.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/core/src/tasks/mod.rs:1` `mod compact;`
- `mod` `codex-rs/core/src/tasks/mod.rs:2` `mod ghost_snapshot;`
- `mod` `codex-rs/core/src/tasks/mod.rs:3` `mod regular;`
- `mod` `codex-rs/core/src/tasks/mod.rs:4` `mod review;`
- `mod` `codex-rs/core/src/tasks/mod.rs:5` `mod undo;`
- `mod` `codex-rs/core/src/tasks/mod.rs:6` `mod user_shell;`
- `use` `codex-rs/core/src/tasks/mod.rs:8` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tasks/mod.rs:9` `use std::time::Duration;`
- `use` `codex-rs/core/src/tasks/mod.rs:11` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tasks/mod.rs:12` `use tokio::select;`
- `use` `codex-rs/core/src/tasks/mod.rs:13` `use tokio::sync::Notify;`
- `use` `codex-rs/core/src/tasks/mod.rs:14` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/tasks/mod.rs:15` `use tokio_util::task::AbortOnDropHandle;`
- `use` `codex-rs/core/src/tasks/mod.rs:16` `use tracing::Instrument;`
- `use` `codex-rs/core/src/tasks/mod.rs:17` `use tracing::Span;`
- `use` `codex-rs/core/src/tasks/mod.rs:18` `use tracing::trace;`
- `use` `codex-rs/core/src/tasks/mod.rs:19` `use tracing::warn;`
- `use` `codex-rs/core/src/tasks/mod.rs:21` `use crate::AuthManager;`
- `use` `codex-rs/core/src/tasks/mod.rs:22` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tasks/mod.rs:23` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tasks/mod.rs:24` `use crate::models_manager::manager::ModelsManager;`
- `use` `codex-rs/core/src/tasks/mod.rs:25` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tasks/mod.rs:26` `use crate::protocol::TurnAbortReason;`
- `use` `codex-rs/core/src/tasks/mod.rs:27` `use crate::protocol::TurnAbortedEvent;`
- `use` `codex-rs/core/src/tasks/mod.rs:28` `use crate::protocol::TurnCompleteEvent;`
- `use` `codex-rs/core/src/tasks/mod.rs:29` `use crate::session_prefix::TURN_ABORTED_OPEN_TAG;`
- `use` `codex-rs/core/src/tasks/mod.rs:30` `use crate::state::ActiveTurn;`
- `use` `codex-rs/core/src/tasks/mod.rs:31` `use crate::state::RunningTask;`
- `use` `codex-rs/core/src/tasks/mod.rs:32` `use crate::state::TaskKind;`
- `use` `codex-rs/core/src/tasks/mod.rs:33` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/tasks/mod.rs:34` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/tasks/mod.rs:35` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/tasks/mod.rs:36` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/tasks/mod.rs:37` `use codex_protocol::user_input::UserInput;`
- `const` `codex-rs/core/src/tasks/mod.rs:48` `const GRACEFULL_INTERRUPTION_TIMEOUT_MS: u64 = 100;`
- `const` `codex-rs/core/src/tasks/mod.rs:49` `const TURN_ABORTED_INTERRUPTED_GUIDANCE: &str = "The user interrupted the previous turn on purpose. If any tools/commands were aborted, they may have partially executed; verify current state before retrying.";`
- `impl` `codex-rs/core/src/tasks/mod.rs:57` `impl SessionTaskContext {`
- `fn` `codex-rs/core/src/tasks/mod.rs:87` `fn kind(&self) -> TaskKind;`
- `fn` `codex-rs/core/src/tasks/mod.rs:97` `async fn run(`
- `fn` `codex-rs/core/src/tasks/mod.rs:110` `async fn abort(&self, session: Arc<SessionTaskContext>, ctx: Arc<TurnContext>) {`
- `impl` `codex-rs/core/src/tasks/mod.rs:115` `impl Session {`
- `fn` `codex-rs/core/src/tasks/mod.rs:180` `pub async fn abort_all_tasks(self: &Arc<Self>, reason: TurnAbortReason) {`
- `fn` `codex-rs/core/src/tasks/mod.rs:187` `pub async fn on_task_finished(`
- `fn` `codex-rs/core/src/tasks/mod.rs:221` `async fn register_new_active_task(&self, task: RunningTask) {`
- `fn` `codex-rs/core/src/tasks/mod.rs:228` `async fn take_all_running_tasks(&self) -> Vec<RunningTask> {`
- `fn` `codex-rs/core/src/tasks/mod.rs:240` `async fn close_unified_exec_processes(&self) {`
- `fn` `codex-rs/core/src/tasks/mod.rs:247` `async fn handle_task_abort(self: &Arc<Self>, task: RunningTask, reason: TurnAbortReason) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use async_trait::async_trait;`
- `use tokio::select;`
- `use tokio::sync::Notify;`
- `use tokio_util::sync::CancellationToken;`
- `use tokio_util::task::AbortOnDropHandle;`
- `use tracing::Instrument;`
- `use tracing::Span;`
- `use tracing::trace;`
- `use tracing::warn;`
- `use crate::AuthManager;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::models_manager::manager::ModelsManager;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::TurnAbortReason;`
- `use crate::protocol::TurnAbortedEvent;`
- `use crate::protocol::TurnCompleteEvent;`
- `use crate::session_prefix::TURN_ABORTED_OPEN_TAG;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
