# `codex-rs/app-server/tests/suite/user_agent.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1585`
- sha256: `45fb767241e0bf661e63ee2157411964528339af82f29df1d16bc017b88b07f6`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/user_agent.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use app_test_support::DEFAULT_CLIENT_NAME;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::GetUserAgentResponse;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
