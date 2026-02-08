# `codex-rs/exec/tests/suite/resume.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `18218`
- sha256: `5a906e69a55dd7c89e1f2040fd089a7845972534b2c4c2c6fbcd56829d4b60dd`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/tests/suite/resume.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use codex_utils_cargo_bin::find_resource;`
- `use core_test_support::test_codex_exec::test_codex_exec;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
- `use std::fs::FileTimes;`
- `use std::fs::OpenOptions;`
- `use std::string::ToString;`
- `use std::time::Duration;`
- `use std::time::SystemTime;`
- `use tempfile::TempDir;`
- `use uuid::Uuid;`
- `use walkdir::WalkDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
