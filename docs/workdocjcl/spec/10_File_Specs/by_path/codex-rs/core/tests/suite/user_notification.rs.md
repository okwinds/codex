# `codex-rs/core/tests/suite/user_notification.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2938`
- sha256: `0d4112c791f84962d0ee21076b15371e296256178c9a2f2598deee3d7a852ceb`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/user_notification.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::os::unix::fs::PermissionsExt;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::fs_wait;`
- `use core_test_support::responses;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::TestCodex;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
- `use serde_json::json;`
- `use tempfile::TempDir;`
- `use responses::ev_assistant_message;`
- `use responses::ev_completed;`
- `use responses::sse;`
- `use responses::start_mock_server;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
