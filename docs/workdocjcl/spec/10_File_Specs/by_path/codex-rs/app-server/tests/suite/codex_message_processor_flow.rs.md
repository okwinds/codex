# `codex-rs/app-server/tests/suite/codex_message_processor_flow.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `19546`
- sha256: `ed35d5f4e64d526e9b053ba1f3cf0fea6e362639a5e508f77013fe7b0eb06ec3`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/codex_message_processor_flow.rs` (read)

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
- `use app_test_support::create_final_assistant_message_sse_response;`
- `use app_test_support::create_mock_responses_server_sequence;`
- `use app_test_support::create_shell_command_sse_response;`
- `use app_test_support::format_with_current_shell;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::AddConversationListenerParams;`
- `use codex_app_server_protocol::AddConversationSubscriptionResponse;`
- `use codex_app_server_protocol::ExecCommandApprovalParams;`
- `use codex_app_server_protocol::InputItem;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::NewConversationParams;`
- `use codex_app_server_protocol::NewConversationResponse;`
- `use codex_app_server_protocol::RemoveConversationListenerParams;`
- `use codex_app_server_protocol::RemoveConversationSubscriptionResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SendUserMessageParams;`
- `use codex_app_server_protocol::SendUserMessageResponse;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
