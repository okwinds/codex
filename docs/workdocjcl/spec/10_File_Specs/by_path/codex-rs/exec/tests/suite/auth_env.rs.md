# `codex-rs/exec/tests/suite/auth_env.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `969`
- sha256: `18021a3cbc353700030aa63771c2d8a514e1e9b5b4ded71b5246c3919b71ce64`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/tests/suite/auth_env.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::mount_sse_once_match;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::test_codex_exec::test_codex_exec;`
- `use wiremock::matchers::header;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
