# `codex-rs/app-server/tests/suite/v2/turn_interrupt.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5064`
- sha256: `3679231c69421ebc35015e908b55a077be26599e1e1040ba70b0f7fcc8d13219`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/turn_interrupt.rs` (read)

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
- `use app_test_support::create_shell_command_sse_response;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnCompletedNotification;`
- `use codex_app_server_protocol::TurnInterruptParams;`
- `use codex_app_server_protocol::TurnInterruptResponse;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStartResponse;`
- `use codex_app_server_protocol::TurnStatus;`
- `use codex_app_server_protocol::UserInput as V2UserInput;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
