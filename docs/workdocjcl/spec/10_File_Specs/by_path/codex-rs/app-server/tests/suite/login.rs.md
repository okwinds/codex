# `codex-rs/app-server/tests/suite/login.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5149`
- sha256: `65ed7e4a18a2d7afab5f4219ca88b223c39dae2122af1222d4caa8067ebd9cde`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/login.rs` (read)

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
- `use codex_app_server_protocol::GetAuthStatusParams;`
- `use codex_app_server_protocol::GetAuthStatusResponse;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::LoginChatGptResponse;`
- `use codex_app_server_protocol::LogoutChatGptResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_login::login_with_api_key;`
- `use serial_test::serial;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
