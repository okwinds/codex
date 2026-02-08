# `codex-rs/app-server/tests/suite/v2/thread_resume.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `21589`
- sha256: `fd6a2c3a00f41e6f8e57582d09ab8c5b32879952d94397c44865e0d3a8e5b89c`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_resume.rs` (read)

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
- `use app_test_support::create_fake_rollout_with_text_elements;`
- `use app_test_support::create_mock_responses_server_repeating_assistant;`
- `use app_test_support::rollout_path;`
- `use app_test_support::to_response;`
- `use chrono::Utc;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SessionSource;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadResumeParams;`
- `use codex_app_server_protocol::ThreadResumeResponse;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStatus;`
- `use codex_app_server_protocol::UserInput;`
- `use codex_protocol::config_types::Personality;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
