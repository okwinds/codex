# `codex-rs/app-server/tests/suite/v2/thread_loaded_list.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4357`
- sha256: `324315ea808655fe525dd778cfa5eb04807c18fafe914a446a7896d23b4e841a`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_loaded_list.rs` (read)

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
- `use codex_app_server_protocol::ThreadLoadedListParams;`
- `use codex_app_server_protocol::ThreadLoadedListResponse;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
