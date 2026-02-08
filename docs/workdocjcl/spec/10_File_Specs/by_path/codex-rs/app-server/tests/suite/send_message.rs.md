# `codex-rs/app-server/tests/suite/send_message.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `15349`
- sha256: `c2f976ff02f2d2fe9f233cdd69f9a838a3c2cb34accf6adc2a480a87655c799e`
- generated_utc: `2026-02-03T16:08:28Z`

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
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::AddConversationListenerParams;`
- `use codex_app_server_protocol::AddConversationSubscriptionResponse;`
- `use codex_app_server_protocol::InputItem;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::NewConversationParams;`
- `use codex_app_server_protocol::NewConversationResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SendUserMessageParams;`
- `use codex_app_server_protocol::SendUserMessageResponse;`
- `use codex_execpolicy::Policy;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::DeveloperInstructions;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::RawResponseItemEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
