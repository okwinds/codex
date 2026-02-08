# `codex-rs/stdio-to-uds/tests/stdio_to_uds.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2083`
- sha256: `031845770a2262b644fe0adee15c06ec98e360d2d9ea5774acf0a8cbcd1c9e48`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/stdio-to-uds/tests/stdio_to_uds.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::ErrorKind;`
- `use std::io::Read;`
- `use std::io::Write;`
- `use std::sync::mpsc;`
- `use std::thread;`
- `use std::time::Duration;`
- `use anyhow::Context;`
- `use assert_cmd::Command;`
- `use pretty_assertions::assert_eq;`
- `use std::os::unix::net::UnixListener;`
- `use uds_windows::UnixListener;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
