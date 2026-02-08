# `codex-rs/mcp-server/src/exec_approval.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4654`
- sha256: `8c5d06fc0eb9291bbabb846c1721ce5182c043592c9880b5bcf0d7dc29d94653`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/exec_approval.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct ExecApprovalElicitRequestParams {`
- `pub struct ExecApprovalResponse {`

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/exec_approval.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:4` `use codex_core::CodexThread;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:5` `use codex_core::protocol::Op;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:6` `use codex_core::protocol::ReviewDecision;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:7` `use codex_protocol::ThreadId;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:8` `use codex_protocol::parse_command::ParsedCommand;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:9` `use rmcp::model::ErrorData;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:10` `use rmcp::model::RequestId;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:11` `use serde::Deserialize;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:12` `use serde::Serialize;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:13` `use serde_json::Value;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:14` `use serde_json::json;`
- `use` `codex-rs/mcp-server/src/exec_approval.rs:15` `use tracing::error;`
- `struct` `codex-rs/mcp-server/src/exec_approval.rs:20` `pub struct ExecApprovalElicitRequestParams {`
- `struct` `codex-rs/mcp-server/src/exec_approval.rs:46` `pub struct ExecApprovalResponse {`
- `fn` `codex-rs/mcp-server/src/exec_approval.rs:110` `async fn on_exec_approval_response(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use codex_core::CodexThread;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::ReviewDecision;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::parse_command::ParsedCommand;`
- `use rmcp::model::ErrorData;`
- `use rmcp::model::RequestId;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use serde_json::json;`
- `use tracing::error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
