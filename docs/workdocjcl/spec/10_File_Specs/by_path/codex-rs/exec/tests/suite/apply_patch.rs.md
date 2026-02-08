# `codex-rs/exec/tests/suite/apply_patch.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4668`
- sha256: `901f03c2621cd42c81f6813059653ea3b7fd79b7694244e5ec96bb42475a3294`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/tests/suite/apply_patch.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use assert_cmd::prelude::*;`
- `use codex_core::CODEX_APPLY_PATCH_ARG1;`
- `use core_test_support::responses::ev_apply_patch_custom_tool_call;`
- `use core_test_support::responses::ev_apply_patch_function_call;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use std::fs;`
- `use std::process::Command;`
- `use tempfile::tempdir;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex_exec::test_codex_exec;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex_exec::test_codex_exec;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
