# `codex-rs/core/tests/suite/list_dir.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6113`
- sha256: `4867bd3d2493ef5c1ce5ac8c15dd2794a09fae1b21b3d76f890430aeea6e893d`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/list_dir.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use core_test_support::responses::mount_function_call_agent_response;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
