# `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1261`
- sha256: `7e4014d357a26d6a718aa37568b88182f3af76c391fb788e4241122283580e9c`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `fn main() -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs:1` `use anyhow::Context;`
- `use` `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs:2` `use anyhow::Result;`
- `use` `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs:3` `use clap::Parser;`
- `use` `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs:4` `use std::path::PathBuf;`
- `struct` `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs:8` `struct Args {`
- `fn` `codex-rs/app-server-protocol/src/bin/write_schema_fixtures.rs:22` `fn main() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use clap::Parser;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
