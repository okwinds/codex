# `codex-rs/app-server/tests/suite/v2/thread_read.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5288`
- sha256: `09df1b0c7e974e02c50a8f700039d225a22fe9d110dbd9792e2a3029f59ca2f1`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_read.rs` (read)

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
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SessionSource;`
- `use codex_app_server_protocol::ThreadItem;`
- `use codex_app_server_protocol::ThreadReadParams;`
- `use codex_app_server_protocol::ThreadReadResponse;`
- `use codex_app_server_protocol::TurnStatus;`
- `use codex_app_server_protocol::UserInput;`
- `use codex_protocol::user_input::ByteRange;`
- `use codex_protocol::user_input::TextElement;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
