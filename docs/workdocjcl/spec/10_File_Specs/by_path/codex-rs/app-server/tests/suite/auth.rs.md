# `codex-rs/app-server/tests/suite/auth.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `7341`
- sha256: `4e746f08ff4f67d99f0c914ab7d7ca22da97c08badbc758829b0d2564b0503df`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/auth.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_app_server_protocol::GetAuthStatusParams;`
- `use codex_app_server_protocol::GetAuthStatusResponse;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::LoginApiKeyParams;`
- `use codex_app_server_protocol::LoginApiKeyResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
