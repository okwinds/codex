# `codex-rs/app-server/tests/suite/v2/dynamic_tools.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `15521`
- sha256: `dc2b5ff8bff8c2da81dc330f5c4532efff084adbd5a7a5d4afccdb10903b2b86`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/dynamic_tools.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use app_test_support::McpProcess;`
- `use app_test_support::create_final_assistant_message_sse_response;`
- `use app_test_support::create_mock_responses_server_sequence_unchecked;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::DynamicToolCallOutputContentItem;`
- `use codex_app_server_protocol::DynamicToolCallParams;`
- `use codex_app_server_protocol::DynamicToolCallResponse;`
- `use codex_app_server_protocol::DynamicToolSpec;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ServerRequest;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStartResponse;`
- `use codex_app_server_protocol::UserInput as V2UserInput;`
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use codex_protocol::models::FunctionCallOutputContentItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
