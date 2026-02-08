# `codex-rs/core/tests/common/process.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `1380`
- sha256: `4c7012e72869ed870bd239ee10c904e0d5fc3d843e38ff144a402af70b5a2868`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/common/process.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub fn process_is_alive(pid: &str) -> anyhow::Result<bool> {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use std::fs;`
- `use std::path::Path;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
