# `codex-rs/app-server/tests/suite/v2/turn_steer.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5941`
- sha256: `253ae3ab5e3f2fecd5859e4927adf4317e43a010b1bfaa7ea4f01aa7a553ab8b`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/turn_steer.rs` (read)

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
- `use app_test_support::create_mock_responses_server_sequence;`
- `use app_test_support::create_mock_responses_server_sequence_unchecked;`
- `use app_test_support::create_shell_command_sse_response;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStartResponse;`
- `use codex_app_server_protocol::TurnSteerParams;`
- `use codex_app_server_protocol::TurnSteerResponse;`
- `use codex_app_server_protocol::UserInput as V2UserInput;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
