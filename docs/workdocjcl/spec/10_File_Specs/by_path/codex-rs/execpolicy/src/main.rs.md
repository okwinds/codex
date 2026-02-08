# `codex-rs/execpolicy/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `405`
- sha256: `4828253b209715c26e49229c8d4e6f88523fe59eb2c0a64b0d1fb09beede29f3`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/main.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `fn main() -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/main.rs:1` `use anyhow::Result;`
- `use` `codex-rs/execpolicy/src/main.rs:2` `use clap::Parser;`
- `use` `codex-rs/execpolicy/src/main.rs:3` `use codex_execpolicy::execpolicycheck::ExecPolicyCheckCommand;`
- `enum` `codex-rs/execpolicy/src/main.rs:8` `enum Cli {`
- `fn` `codex-rs/execpolicy/src/main.rs:13` `fn main() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use clap::Parser;`
- `use codex_execpolicy::execpolicycheck::ExecPolicyCheckCommand;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
