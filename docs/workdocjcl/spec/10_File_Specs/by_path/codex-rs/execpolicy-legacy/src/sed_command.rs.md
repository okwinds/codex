# `codex-rs/execpolicy-legacy/src/sed_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `497`
- sha256: `16cf9643fcf913a99b89ffd2a33cd074074d48e5d612b25fa3ee34f2af5234e6`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy-legacy/src/sed_command.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn parse_sed_command(sed_command: &str) -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy-legacy/src/sed_command.rs:1` `use crate::error::Error;`
- `use` `codex-rs/execpolicy-legacy/src/sed_command.rs:2` `use crate::error::Result;`
- `fn` `codex-rs/execpolicy-legacy/src/sed_command.rs:4` `pub fn parse_sed_command(sed_command: &str) -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::Error;`
- `use crate::error::Result;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
