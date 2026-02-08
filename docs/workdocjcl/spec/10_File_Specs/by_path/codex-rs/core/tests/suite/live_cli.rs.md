# `codex-rs/core/tests/suite/live_cli.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5104`
- sha256: `e47c21a4bd7803efe5f20c61162e9aab8bf8451599759374a002604d6cadd245`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/live_cli.rs` (read)
- env: `OPENAI_API_KEY`

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use assert_cmd::prelude::*;`
- `use predicates::prelude::*;`
- `use std::process::Command;`
- `use std::process::Stdio;`
- `use tempfile::TempDir;`
- `use std::io::Read;`
- `use std::io::Write;`
- `use std::thread;`
### Referenced env vars
- `OPENAI_API_KEY`

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
