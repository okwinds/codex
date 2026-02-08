# `codex-rs/app-server/src/dynamic_tools.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2340`
- sha256: `abc72364fd7ad1dce71a1d02b97834076140ceb5d91f41cb5341be2f96977c80`
- generated_utc: `2026-02-08T10:45:15Z`

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
- `use` `codex-rs/app-server/src/dynamic_tools.rs:3` `use codex_protocol::dynamic_tools::DynamicToolCallOutputContentItem as CoreDynamicToolCallOutputContentItem;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:4` `use codex_protocol::dynamic_tools::DynamicToolResponse as CoreDynamicToolResponse;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:5` `use codex_protocol::protocol::Op;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:6` `use std::sync::Arc;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:7` `use tokio::sync::oneshot;`
- `use` `codex-rs/app-server/src/dynamic_tools.rs:8` `use tracing::error;`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_app_server_protocol::DynamicToolCallResponse;`
- `use codex_core::CodexThread;`
- `use codex_protocol::dynamic_tools::DynamicToolCallOutputContentItem as CoreDynamicToolCallOutputContentItem;`
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
