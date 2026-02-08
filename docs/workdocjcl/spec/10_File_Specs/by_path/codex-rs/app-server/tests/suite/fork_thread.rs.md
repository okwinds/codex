# `codex-rs/app-server/tests/suite/fork_thread.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4732`
- sha256: `a69b529e4611d1880d9f5a51402a71e47a6d0ff6903dd2897aaf00700885bff9`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/fork_thread.rs` (read)

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
- `use codex_app_server_protocol::ForkConversationParams;`
- `use codex_app_server_protocol::ForkConversationResponse;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::NewConversationParams; // reused for overrides shape`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ServerNotification;`
- `use codex_app_server_protocol::SessionConfiguredNotification;`
- `use codex_core::protocol::EventMsg;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
