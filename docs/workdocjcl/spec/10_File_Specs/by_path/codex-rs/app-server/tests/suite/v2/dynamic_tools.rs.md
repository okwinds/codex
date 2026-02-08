# `codex-rs/app-server/tests/suite/v2/dynamic_tools.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `9658`
- sha256: `26694f9ae4334880575407e3cce38c89af5e4d6b04dfb8af2820a137330ae33b`
- generated_utc: `2026-02-03T16:08:28Z`

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
- `use core_test_support::responses;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
