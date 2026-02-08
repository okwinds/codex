# `codex-rs/core/tests/suite/stream_no_completed.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3666`
- sha256: `ee22fe7f4e088b336e2bfafa833c5dacd9109ced9dd225d4b7905d86b7e3286c`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use core_test_support::load_sse_fixture_with_id;`
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
- `use std::sync::atomic::AtomicUsize;`
- `use std::sync::atomic::Ordering;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
