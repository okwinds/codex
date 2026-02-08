# `codex-rs/app-server/tests/suite/v2/thread_resume.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `18075`
- sha256: `612ec6a6a7438c43bc112337f653193936c04ecfa3656cac05aa7c45c0fb16c8`
- generated_utc: `2026-02-03T16:08:28Z`

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
- `use codex_protocol::models::ContentItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
