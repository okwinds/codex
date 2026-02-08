# `codex-rs/core/tests/suite/json_result.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3800`
- sha256: `c4b43fca6e557ce8eb43d2ea369bb279b58c4ec677de76e52dac4c71f70bd5f1`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/json_result.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::TestCodex;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use pretty_assertions::assert_eq;`
- `use responses::ev_assistant_message;`
- `use responses::ev_completed;`
- `use responses::sse;`
- `use responses::start_mock_server;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
