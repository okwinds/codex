# `codex-rs/app-server/tests/suite/v2/experimental_api.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4997`
- sha256: `b03184f7dfbbc0131b6f912a7d011fc223ea3ef54b7622465b124b943ee83c84`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/experimental_api.rs` (read)

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
- `use app_test_support::create_mock_responses_server_sequence_unchecked;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::ClientInfo;`
- `use codex_app_server_protocol::InitializeCapabilities;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCMessage;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::MockExperimentalMethodParams;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
- `use std::time::Duration;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
