# `codex-rs/common/src/sandbox_mode_cli_arg.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1467`
- sha256: `761d659959a244dc3780c9fac63be5ac19aa4b47cea26b47379e41e405bffd14`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/sandbox_mode_cli_arg.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum SandboxModeCliArg {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/sandbox_mode_cli_arg.rs:9` `use clap::ValueEnum;`
- `use` `codex-rs/common/src/sandbox_mode_cli_arg.rs:10` `use codex_protocol::config_types::SandboxMode;`
- `enum` `codex-rs/common/src/sandbox_mode_cli_arg.rs:14` `pub enum SandboxModeCliArg {`
- `impl` `codex-rs/common/src/sandbox_mode_cli_arg.rs:20` `impl From<SandboxModeCliArg> for SandboxMode {`
- `fn` `codex-rs/common/src/sandbox_mode_cli_arg.rs:21` `fn from(value: SandboxModeCliArg) -> Self {`
- `use` `codex-rs/common/src/sandbox_mode_cli_arg.rs:32` `use super::*;`
- `use` `codex-rs/common/src/sandbox_mode_cli_arg.rs:33` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/common/src/sandbox_mode_cli_arg.rs:36` `fn maps_cli_args_to_protocol_modes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::ValueEnum;`
- `use codex_protocol::config_types::SandboxMode;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
