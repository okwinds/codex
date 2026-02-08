# `codex-rs/app-server/tests/suite/list_resume.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `15520`
- sha256: `956e6a0445190df33ab8ceb52e29d75dc2b6012b96b1e60be2a2253e7fb0058e`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/list_resume.rs` (read)

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
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::ListConversationsParams;`
- `use codex_app_server_protocol::ListConversationsResponse;`
- `use codex_app_server_protocol::NewConversationParams;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ResumeConversationParams;`
- `use codex_app_server_protocol::ResumeConversationResponse;`
- `use codex_app_server_protocol::ServerNotification;`
- `use codex_app_server_protocol::SessionConfiguredNotification;`
- `use codex_core::protocol::EventMsg;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
