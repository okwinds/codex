# `codex-rs/chatgpt/tests/suite/apply_command_e2e.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5781`
- sha256: `91cb4db5b7229f171fe1bf7b3203287f0da80a7c269ab5b26341aa3c236676cb`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/chatgpt/tests/suite/apply_command_e2e.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_chatgpt::apply_command::apply_diff_from_task;`
- `use codex_chatgpt::get_task::GetTaskResponse;`
- `use codex_utils_cargo_bin::find_resource;`
- `use tempfile::TempDir;`
- `use tokio::process::Command;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
