# `codex-rs/app-server/tests/suite/v2/thread_unarchive.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5820`
- sha256: `864e2e5a846ccd5a683f2e2ed0e0a0c742a08b6e5af3d38504eb0e04c0095f8a`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_unarchive.rs` (read)

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
- `use app_test_support::create_mock_responses_server_repeating_assistant;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::ThreadArchiveParams;`
- `use codex_app_server_protocol::ThreadArchiveResponse;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::ThreadUnarchiveParams;`
- `use codex_app_server_protocol::ThreadUnarchiveResponse;`
- `use codex_app_server_protocol::TurnStartParams;`
- `use codex_app_server_protocol::TurnStartResponse;`
- `use codex_app_server_protocol::UserInput;`
- `use codex_core::find_archived_thread_path_by_id_str;`
- `use codex_core::find_thread_path_by_id_str;`
- `use std::fs::FileTimes;`
- `use std::fs::OpenOptions;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
