# `codex-rs/core/tests/suite/abort_tasks.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `7701`
- sha256: `ef8c1c92a1223eb7059f6d95089eea413d5adefb84a6169f70eae779fb910f33`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/abort_tasks.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use assert_matches::assert_matches;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use regex_lite::Regex;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
