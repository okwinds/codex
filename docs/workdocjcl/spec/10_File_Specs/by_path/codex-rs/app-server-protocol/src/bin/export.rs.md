# `codex-rs/app-server-protocol/src/bin/export.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `684`
- sha256: `6c9e8650c402faabc8dad1dcdf8b62592d2660c41e1b8439e30bac69216b03c9`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/bin/export.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `fn main() -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/bin/export.rs:1` `use anyhow::Result;`
- `use` `codex-rs/app-server-protocol/src/bin/export.rs:2` `use clap::Parser;`
- `use` `codex-rs/app-server-protocol/src/bin/export.rs:3` `use std::path::PathBuf;`
- `struct` `codex-rs/app-server-protocol/src/bin/export.rs:9` `struct Args {`
- `fn` `codex-rs/app-server-protocol/src/bin/export.rs:19` `fn main() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use clap::Parser;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
