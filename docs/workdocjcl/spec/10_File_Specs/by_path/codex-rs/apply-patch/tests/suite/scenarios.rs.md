# `codex-rs/apply-patch/tests/suite/scenarios.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3786`
- sha256: `e35fc05d72f638862f1dbfa5a1d5f93e4750196d1503b9dc632718724f1c67d2`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/apply-patch/tests/suite/scenarios.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_utils_cargo_bin::find_resource;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::BTreeMap;`
- `use std::fs;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Command;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
