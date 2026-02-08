# `codex-rs/app-server/tests/suite/v2/turn_start.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `64741`
- sha256: `aa4d434d22322a3a651603363775183140a19580eed4630b6b4d4b0dcc21a82e`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/turn_start.rs` (read)

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
- `use app_test_support::create_apply_patch_sse_response;`
- `use app_test_support::create_exec_command_sse_response;`
- `use app_test_support::create_fake_rollout;`
- `use app_test_support::create_final_assistant_message_sse_response;`
- `use app_test_support::create_mock_responses_server_sequence;`
- `use app_test_support::create_mock_responses_server_sequence_unchecked;`
- `use app_test_support::create_shell_command_sse_response;`
- `use app_test_support::format_with_current_shell_display;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::ByteRange;`
- `use codex_app_server_protocol::ClientInfo;`
- `use codex_app_server_protocol::CommandExecutionApprovalDecision;`
- `use codex_app_server_protocol::CommandExecutionRequestApprovalResponse;`
- `use codex_app_server_protocol::CommandExecutionStatus;`
- `use codex_app_server_protocol::FileChangeApprovalDecision;`
- `use codex_app_server_protocol::FileChangeOutputDeltaNotification;`
- `use codex_app_server_protocol::FileChangeRequestApprovalResponse;`
- `use codex_app_server_protocol::ItemCompletedNotification;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
