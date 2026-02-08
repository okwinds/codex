# `codex-rs/core/tests/suite/model_overrides.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2986`
- sha256: `55260c0f5e8d2095b020a1b47fec8f28292513f506cf896f76ee711a764ca596`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/model_overrides.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
