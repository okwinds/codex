# `codex-rs/core/tests/suite/websocket_fallback.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6255`
- sha256: `6089220ad5ae4bf2c9b5de9b51520a25c54c3e0a8e9dc4b1a5de80a3d0cc818d`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/websocket_fallback.rs` (read)

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
- `use core_test_support::responses;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use pretty_assertions::assert_eq;`
- `use wiremock::Mock;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::http::Method;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path_regex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
