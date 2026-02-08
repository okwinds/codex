# `codex-rs/core/src/stream_events_utils.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9192`
- sha256: `7bd661afac77870f1e4ea1885e9f523082b60fd885ff3582f6472ee40fa198ef`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/stream_events_utils.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/stream_events_utils.rs:1` `use std::pin::Pin;`
- `use` `codex-rs/core/src/stream_events_utils.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/stream_events_utils.rs:4` `use codex_protocol::config_types::ModeKind;`
- `use` `codex-rs/core/src/stream_events_utils.rs:5` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/stream_events_utils.rs:6` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/stream_events_utils.rs:8` `use crate::codex::Session;`
- `use` `codex-rs/core/src/stream_events_utils.rs:9` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/stream_events_utils.rs:10` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/stream_events_utils.rs:11` `use crate::error::Result;`
- `use` `codex-rs/core/src/stream_events_utils.rs:12` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/stream_events_utils.rs:13` `use crate::parse_turn_item;`
- `use` `codex-rs/core/src/stream_events_utils.rs:14` `use crate::proposed_plan_parser::strip_proposed_plan_blocks;`
- `use` `codex-rs/core/src/stream_events_utils.rs:15` `use crate::tools::parallel::ToolCallRuntime;`
- `use` `codex-rs/core/src/stream_events_utils.rs:16` `use crate::tools::router::ToolRouter;`
- `use` `codex-rs/core/src/stream_events_utils.rs:17` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/stream_events_utils.rs:18` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/stream_events_utils.rs:19` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/stream_events_utils.rs:20` `use futures::Future;`
- `use` `codex-rs/core/src/stream_events_utils.rs:21` `use tracing::debug;`
- `use` `codex-rs/core/src/stream_events_utils.rs:22` `use tracing::instrument;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::pin::Pin;`
- `use std::sync::Arc;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::items::TurnItem;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::error::CodexErr;`
- `use crate::error::Result;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::parse_turn_item;`
- `use crate::proposed_plan_parser::strip_proposed_plan_blocks;`
- `use crate::tools::parallel::ToolCallRuntime;`
- `use crate::tools::router::ToolRouter;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::models::ResponseItem;`
- `use futures::Future;`
- `use tracing::debug;`
- `use tracing::instrument;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
