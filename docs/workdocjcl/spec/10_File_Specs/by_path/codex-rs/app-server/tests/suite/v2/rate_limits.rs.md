# `codex-rs/app-server/tests/suite/v2/rate_limits.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6120`
- sha256: `860b318bda04611c9ff76f04cb0325231aabb9504c4096a6a2876832d2a6f093`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/rate_limits.rs` (read)

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
- `use codex_app_server_protocol::GetAccountRateLimitsResponse;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::LoginApiKeyParams;`
- `use codex_app_server_protocol::RateLimitSnapshot;`
- `use codex_app_server_protocol::RateLimitWindow;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_protocol::account::PlanType as AccountPlanType;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::json;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
- `use wiremock::Mock;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
