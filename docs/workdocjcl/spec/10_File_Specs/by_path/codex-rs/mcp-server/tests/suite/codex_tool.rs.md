# `codex-rs/mcp-server/tests/suite/codex_tool.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `18001`
- sha256: `f44f4635a84b36a032c1ae27d081a4a86359d27237d7901f5f1fed71dcbde9d2`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/tests/suite/codex_tool.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct McpHandle {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::env;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_core::parse_command;`
- `use codex_core::protocol::FileChange;`
- `use codex_core::protocol::ReviewDecision;`
- `use codex_core::spawn::CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR;`
- `use codex_mcp_server::CodexToolCallParam;`
- `use codex_mcp_server::ExecApprovalElicitRequestParams;`
- `use codex_mcp_server::ExecApprovalResponse;`
- `use codex_mcp_server::PatchApprovalElicitRequestParams;`
- `use codex_mcp_server::PatchApprovalResponse;`
- `use pretty_assertions::assert_eq;`
- `use rmcp::model::JsonRpcResponse;`
- `use rmcp::model::JsonRpcVersion2_0;`
- `use rmcp::model::RequestId;`
- `use serde_json::json;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
