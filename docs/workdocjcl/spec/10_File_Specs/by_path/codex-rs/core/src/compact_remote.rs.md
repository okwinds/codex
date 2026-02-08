# `codex-rs/core/src/compact_remote.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4584`
- sha256: `5f5f778a4189dc73caf85384e2317a30c598126dca9f2a1ec7fed5aacb49e449`
- generated_utc: `2026-02-08T10:45:28Z`

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
- `use` `codex-rs/core/src/compact_remote.rs:15` `use codex_protocol::models::BaseInstructions;`
- `use` `codex-rs/core/src/compact_remote.rs:16` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/compact_remote.rs:17` `use tracing::info;`
- `fn` `codex-rs/core/src/compact_remote.rs:40` `async fn run_remote_compact_task_inner(`
- `fn` `codex-rs/core/src/compact_remote.rs:54` `async fn run_remote_compact_task_inner_impl(`
- `fn` `codex-rs/core/src/compact_remote.rs:124` `fn trim_function_call_history_to_fit_context_window(`

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
- `use codex_protocol::models::BaseInstructions;`
- `use codex_protocol::models::ResponseItem;`
- `use tracing::info;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
