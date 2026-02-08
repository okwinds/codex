# `codex-rs/app-server/src/dynamic_tools.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1848`
- sha256: `ae82ca9da77be91604b250d4e831c614b6304d2bac64a69fc148eb7303e9b9da`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/dynamic_tools.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/dynamic_tools.rs:1` `use codex_app_server_protocol::DynamicToolCallResponse;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:2` `use codex_core::CodexThread;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:3` `use codex_protocol::dynamic_tools::DynamicToolResponse as CoreDynamicToolResponse;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:4` `use codex_protocol::protocol::Op;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:6` `use tokio::sync::oneshot;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:7` `use tracing::error;`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_app_server_protocol::DynamicToolCallResponse;`
- `use codex_core::CodexThread;`
- `use codex_protocol::dynamic_tools::DynamicToolResponse as CoreDynamicToolResponse;`
- `use codex_protocol::protocol::Op;`
- `use std::sync::Arc;`
- `use tokio::sync::oneshot;`
- `use tracing::error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
