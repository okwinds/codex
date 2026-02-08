# `codex-rs/core/tests/suite/web_search.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `7581`
- sha256: `64e3350350375a2b3cd763e96433cf9c5eb1ad6edf693a8cdede30d2d6360039`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/web_search.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::WireApi;`
- `use codex_core::built_in_model_providers;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use core_test_support::load_sse_fixture_with_id;`
- `use core_test_support::responses;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
