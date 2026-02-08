# `codex-rs/app-server/tests/suite/v2/plan_item.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `9102`
- sha256: `dfcd0a38c90bda157ff7d412154ce1b8b2d16307bc3ad2701c86787b9cf0f98e`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/plan_item.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use app_test_support::McpProcess;`
- `use app_test_support::create_mock_responses_server_sequence;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::ItemCompletedNotification;`
- `use codex_app_server_protocol::ItemStartedNotification;`
- `use codex_app_server_protocol::JSONRPCMessage;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::PlanDeltaNotification;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnCompletedNotification;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStartResponse;`
- `use codex_app_server_protocol::TurnStatus;`
- `use codex_app_server_protocol::UserInput as V2UserInput;`
- `use codex_core::features::FEATURES;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
