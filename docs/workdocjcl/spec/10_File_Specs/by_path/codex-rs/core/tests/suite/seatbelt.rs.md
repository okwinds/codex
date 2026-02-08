# `codex-rs/core/tests/suite/seatbelt.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `9974`
- sha256: `55139e4feb7ba05d82b6d8b378a0b6d3ca76ddaa858b9eddde3328775de00856`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/seatbelt.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::seatbelt::spawn_command_under_seatbelt;`
- `use codex_core::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use codex_core::spawn::StdioPolicy;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
