# `codex-rs/app-server/tests/common/mock_model_server.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2494`
- sha256: `12af8ba409f902369c1b8352f8b5e164ada4443ef7b8e848df500ac82793f055`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/common/mock_model_server.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::atomic::AtomicUsize;`
- `use std::sync::atomic::Ordering;`
- `use core_test_support::responses;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::Respond;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path_regex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
