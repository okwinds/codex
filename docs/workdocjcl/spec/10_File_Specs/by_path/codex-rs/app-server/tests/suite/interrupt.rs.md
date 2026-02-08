# `codex-rs/app-server/tests/suite/interrupt.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6030`
- sha256: `b80c805be3d8eeadaccb6d092f9d5167f0e97c9a577b720a23b77797401e6ead`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/interrupt.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use codex_app_server_protocol::AddConversationListenerParams;`
- `use codex_app_server_protocol::InterruptConversationParams;`
- `use codex_app_server_protocol::InterruptConversationResponse;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::NewConversationParams;`
- `use codex_app_server_protocol::NewConversationResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SendUserMessageParams;`
- `use codex_app_server_protocol::SendUserMessageResponse;`
- `use codex_core::protocol::TurnAbortReason;`
- `use core_test_support::skip_if_no_network;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
- `use app_test_support::McpProcess;`
- `use app_test_support::create_mock_responses_server_sequence;`
- `use app_test_support::create_shell_command_sse_response;`
- `use app_test_support::to_response;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
