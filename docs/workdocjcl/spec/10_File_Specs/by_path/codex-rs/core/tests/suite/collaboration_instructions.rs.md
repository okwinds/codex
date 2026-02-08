# `codex-rs/core/tests/suite/collaboration_instructions.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `23411`
- sha256: `5ab6e882d98cfc5945c79e8e683ca59da6b4b861c5a25b5865e8fdde4b08760f`
- generated_utc: `2026-02-08T10:45:35Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/collaboration_instructions.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_core::protocol::COLLABORATION_MODE_CLOSE_TAG;`
- `use codex_core::protocol::COLLABORATION_MODE_OPEN_TAG;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::config_types::CollaborationMode;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::config_types::Settings;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
