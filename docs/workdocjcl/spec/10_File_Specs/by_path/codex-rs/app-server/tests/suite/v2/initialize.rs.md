# `codex-rs/app-server/tests/suite/v2/initialize.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4309`
- sha256: `42352cb812a1dbfbf56d7da4232b55b2d37d8df0abd0e3bfb682a87e27609fa2`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/initialize.rs` (read)

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
- `use app_test_support::create_mock_responses_server_sequence_unchecked;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::ClientInfo;`
- `use codex_app_server_protocol::InitializeResponse;`
- `use codex_app_server_protocol::JSONRPCMessage;`
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
