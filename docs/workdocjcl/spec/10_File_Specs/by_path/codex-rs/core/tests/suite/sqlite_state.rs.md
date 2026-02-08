# `codex-rs/core/tests/suite/sqlite_state.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `10818`
- sha256: `374e908e23da0fb005077400df1553fb30bb36187ad97288b03b5994ab880f86`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/sqlite_state.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_core::features::Feature;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::RolloutLine;`
- `use codex_protocol::protocol::SessionMeta;`
- `use codex_protocol::protocol::SessionMetaLine;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::protocol::UserMessageEvent;`
- `use codex_state::STATE_DB_FILENAME;`
- `use core_test_support::load_sse_fixture_with_id;`
- `use core_test_support::responses;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::test_codex::test_codex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
