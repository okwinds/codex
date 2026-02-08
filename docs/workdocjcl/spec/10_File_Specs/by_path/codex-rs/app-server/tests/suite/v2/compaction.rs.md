# `codex-rs/app-server/tests/suite/v2/compaction.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `10156`
- sha256: `6ccbc4f44f676fca16f1e479751c7a0a2992d89b626c79e01a531229ecfcb186`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/compaction.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use app_test_support::ChatGptAuthFixture;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use app_test_support::write_chatgpt_auth;`
- `use app_test_support::write_mock_responses_config_toml;`
- `use codex_app_server_protocol::ItemCompletedNotification;`
- `use codex_app_server_protocol::ItemStartedNotification;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnCompletedNotification;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStartResponse;`
- `use codex_app_server_protocol::UserInput as V2UserInput;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::features::Feature;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
