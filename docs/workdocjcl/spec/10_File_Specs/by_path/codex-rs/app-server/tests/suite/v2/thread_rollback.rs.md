# `codex-rs/app-server/tests/suite/v2/thread_rollback.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6064`
- sha256: `b4f809837fd6328bc057f835a2bfe1df0b3a504bf293de84fc6befd3acb299bf`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_rollback.rs` (read)

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
- `use app_test_support::create_final_assistant_message_sse_response;`
- `use app_test_support::create_mock_responses_server_sequence_unchecked;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadResumeParams;`
- `use codex_app_server_protocol::ThreadResumeResponse;`
- `use codex_app_server_protocol::ThreadRollbackParams;`
- `use codex_app_server_protocol::ThreadRollbackResponse;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::UserInput as V2UserInput;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
