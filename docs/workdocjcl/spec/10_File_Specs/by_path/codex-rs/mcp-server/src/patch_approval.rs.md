# `codex-rs/mcp-server/src/patch_approval.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4319`
- sha256: `fd11330316f329962035ade047c6501106ea17226d7510dcc7c8875f2299112e`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/patch_approval.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct PatchApprovalElicitRequestParams {`
- `pub struct PatchApprovalResponse {`

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/patch_approval.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:5` `use codex_core::CodexThread;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:6` `use codex_core::protocol::FileChange;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:7` `use codex_core::protocol::Op;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:8` `use codex_core::protocol::ReviewDecision;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:9` `use codex_protocol::ThreadId;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:10` `use rmcp::model::ErrorData;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:11` `use rmcp::model::RequestId;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:12` `use serde::Deserialize;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:13` `use serde::Serialize;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:14` `use serde_json::Value;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:15` `use serde_json::json;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:16` `use tracing::error;`
- `use` `codex-rs/mcp-server/src/patch_approval.rs:18` `use crate::outgoing_message::OutgoingMessageSender;`
- `struct` `codex-rs/mcp-server/src/patch_approval.rs:21` `pub struct PatchApprovalElicitRequestParams {`
- `struct` `codex-rs/mcp-server/src/patch_approval.rs:39` `pub struct PatchApprovalResponse {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use codex_core::CodexThread;`
- `use codex_core::protocol::FileChange;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::ReviewDecision;`
- `use codex_protocol::ThreadId;`
- `use rmcp::model::ErrorData;`
- `use rmcp::model::RequestId;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use serde_json::json;`
- `use tracing::error;`
- `use crate::outgoing_message::OutgoingMessageSender;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
