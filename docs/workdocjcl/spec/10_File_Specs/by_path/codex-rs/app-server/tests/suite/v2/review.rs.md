# `codex-rs/app-server/tests/suite/v2/review.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `15189`
- sha256: `0a2327a61695c8dc3c8240ebf6365e903a7e7a04d77e854f9486699149f4141f`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/review.rs` (read)

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
- `use app_test_support::create_mock_responses_server_repeating_assistant;`
- `use app_test_support::create_mock_responses_server_sequence;`
- `use app_test_support::create_shell_command_sse_response;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::ItemCompletedNotification;`
- `use codex_app_server_protocol::ItemStartedNotification;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ReviewDelivery;`
- `use codex_app_server_protocol::ReviewStartParams;`
- `use codex_app_server_protocol::ReviewStartResponse;`
- `use codex_app_server_protocol::ReviewTarget;`
- `use codex_app_server_protocol::ServerRequest;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadStartParams;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
