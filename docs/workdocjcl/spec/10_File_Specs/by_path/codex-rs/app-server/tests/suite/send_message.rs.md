# `codex-rs/app-server/tests/suite/send_message.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `20528`
- sha256: `1e093b496c0bb8b04087e8d8137e43737405c3c18b896a48ea3eeab04f6350e2`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/send_message.rs` (read)

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
- `use app_test_support::create_fake_rollout;`
- `use app_test_support::rollout_path;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::AddConversationListenerParams;`
- `use codex_app_server_protocol::AddConversationSubscriptionResponse;`
- `use codex_app_server_protocol::InputItem;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::NewConversationParams;`
- `use codex_app_server_protocol::NewConversationResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ResumeConversationParams;`
- `use codex_app_server_protocol::ResumeConversationResponse;`
- `use codex_app_server_protocol::SendUserMessageParams;`
- `use codex_app_server_protocol::SendUserMessageResponse;`
- `use codex_execpolicy::Policy;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::ReasoningSummary;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
