# `codex-rs/app-server/tests/suite/user_info.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1498`
- sha256: `381d5363c8f511817f65694a3d91cf42babbe37bf8ab560bfc7eea57f15015b3`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/user_info.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use app_test_support::ChatGptAuthFixture;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use app_test_support::write_chatgpt_auth;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::UserInfoResponse;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use pretty_assertions::assert_eq;`
- `use std::time::Duration;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
