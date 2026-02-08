# `codex-rs/core/src/compact_remote.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4075`
- sha256: `95201f60e5bfd859af75aa90c41f127cea52704899e1cda2c204745a3befce6f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/compact_remote.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/compact_remote.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/compact_remote.rs:3` `use crate::Prompt;`
- `use` `codex-rs/core/src/compact_remote.rs:4` `use crate::codex::Session;`
- `use` `codex-rs/core/src/compact_remote.rs:5` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/compact_remote.rs:6` `use crate::context_manager::ContextManager;`
- `use` `codex-rs/core/src/compact_remote.rs:7` `use crate::context_manager::is_codex_generated_item;`
- `use` `codex-rs/core/src/compact_remote.rs:8` `use crate::error::Result as CodexResult;`
- `use` `codex-rs/core/src/compact_remote.rs:9` `use crate::protocol::CompactedItem;`
- `use` `codex-rs/core/src/compact_remote.rs:10` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/compact_remote.rs:11` `use crate::protocol::RolloutItem;`
- `use` `codex-rs/core/src/compact_remote.rs:12` `use crate::protocol::TurnStartedEvent;`
- `use` `codex-rs/core/src/compact_remote.rs:13` `use codex_protocol::items::ContextCompactionItem;`
- `use` `codex-rs/core/src/compact_remote.rs:14` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/compact_remote.rs:15` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/compact_remote.rs:16` `use tracing::info;`
- `fn` `codex-rs/core/src/compact_remote.rs:35` `async fn run_remote_compact_task_inner(sess: &Arc<Session>, turn_context: &Arc<TurnContext>) {`
- `fn` `codex-rs/core/src/compact_remote.rs:44` `async fn run_remote_compact_task_inner_impl(`
- `fn` `codex-rs/core/src/compact_remote.rs:102` `fn trim_function_call_history_to_fit_context_window(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use crate::Prompt;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::context_manager::ContextManager;`
- `use crate::context_manager::is_codex_generated_item;`
- `use crate::error::Result as CodexResult;`
- `use crate::protocol::CompactedItem;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::RolloutItem;`
- `use crate::protocol::TurnStartedEvent;`
- `use codex_protocol::items::ContextCompactionItem;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::models::ResponseItem;`
- `use tracing::info;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
