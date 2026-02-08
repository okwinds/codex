# `codex-rs/core/tests/suite/fork_thread.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6049`
- sha256: `ba61a1a400087b0c22eec57aa8fc92d0613a009474f2885fc9bc6f3194fee25b`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/fork_thread.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::NewThread;`
- `use codex_core::parse_turn_item;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::RolloutItem;`
- `use codex_core::protocol::RolloutLine;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::sse;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
