# `codex-rs/core/tests/suite/stream_error_allows_next_turn.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4145`
- sha256: `8574cb5df7987eb96168c7175b457d44130c8e4d059145979794b1ed9e5ffb6e`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/stream_error_allows_next_turn.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::ModelProviderInfo;`
- `use codex_core::WireApi;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::sse;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::TestCodex;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::body_string_contains;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
