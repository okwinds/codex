# `codex-rs/app-server/tests/suite/archive_thread.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5299`
- sha256: `e14b75163cf2b12540dccf4c7bcbf6d587f32a66f64e4f81c0ebc1e809bec3ab`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/archive_thread.rs` (read)

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
- `use app_test_support::create_mock_responses_server_repeating_assistant;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::AddConversationListenerParams;`
- `use codex_app_server_protocol::AddConversationSubscriptionResponse;`
- `use codex_app_server_protocol::ArchiveConversationParams;`
- `use codex_app_server_protocol::ArchiveConversationResponse;`
- `use codex_app_server_protocol::InputItem;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::NewConversationParams;`
- `use codex_app_server_protocol::NewConversationResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SendUserMessageParams;`
- `use codex_app_server_protocol::SendUserMessageResponse;`
- `use codex_core::ARCHIVED_SESSIONS_SUBDIR;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
