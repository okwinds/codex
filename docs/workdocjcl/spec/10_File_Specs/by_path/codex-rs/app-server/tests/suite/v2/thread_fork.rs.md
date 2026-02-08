# `codex-rs/app-server/tests/suite/v2/thread_fork.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6168`
- sha256: `dcbb7283e9911b71cc280505f57616ca4f666cf36be640794cf28b96cba42099`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_fork.rs` (read)

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
- `use app_test_support::create_mock_responses_server_repeating_assistant;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCNotification;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SessionSource;`
- `use codex_app_server_protocol::ThreadForkParams;`
- `use codex_app_server_protocol::ThreadForkResponse;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::ThreadStartedNotification;`
- `use codex_app_server_protocol::TurnStatus;`
- `use codex_app_server_protocol::UserInput;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
