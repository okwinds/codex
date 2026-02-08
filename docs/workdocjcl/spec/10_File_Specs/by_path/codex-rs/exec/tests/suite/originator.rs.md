# `codex-rs/exec/tests/suite/originator.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1944`
- sha256: `55d25f8ea3e2c868a8c2bab31d8b9ff50378fae59c254d37d785bc88fcf99e6b`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/tests/suite/originator.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::default_client::CODEX_INTERNAL_ORIGINATOR_OVERRIDE_ENV_VAR;`
- `use core_test_support::responses;`
- `use core_test_support::test_codex_exec::test_codex_exec;`
- `use wiremock::matchers::header;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
