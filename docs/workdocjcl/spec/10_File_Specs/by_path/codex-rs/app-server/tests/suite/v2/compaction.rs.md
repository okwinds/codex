# `codex-rs/app-server/tests/suite/v2/compaction.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `14475`
- sha256: `ee22cb458d804a11ba696393a0ff34d01bdc9a87a065aa7d2737786d4a645be4`
- generated_utc: `2026-02-08T10:45:15Z`

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
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadCompactStartParams;`
- `use codex_app_server_protocol::ThreadCompactStartResponse;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnCompletedNotification;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStartResponse;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
