# `codex-rs/mcp-server/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `314`
- sha256: `49a09f7378b478e4ac79eb11b7558e384d7f4c61f0b399530a374146bfa1433f`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/main.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `fn main() -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/main.rs:1` `use codex_arg0::arg0_dispatch_or_else;`
- `use` `codex-rs/mcp-server/src/main.rs:2` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/mcp-server/src/main.rs:3` `use codex_mcp_server::run_main;`
- `fn` `codex-rs/mcp-server/src/main.rs:5` `fn main() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_arg0::arg0_dispatch_or_else;`
- `use codex_common::CliConfigOverrides;`
- `use codex_mcp_server::run_main;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
