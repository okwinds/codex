# `codex-rs/core/tests/suite/stream_no_completed.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3834`
- sha256: `846c3c493123148e19402ff47709e53bdfd6aa5bd64d6b7925ec20539dedb031`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/stream_no_completed.rs` (read)

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
- `use core_test_support::load_sse_fixture;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::sse;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::TestCodex;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::Request;`
- `use wiremock::Respond;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
