# `codex-rs/cloud-tasks/src/cli.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3376`
- sha256: `2eca31f0e9003a2dfdc30c7e73e675dc0824341e797a5891dd526bd15479a773`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/cli.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Cli {`
- `pub enum Command {`
- `pub struct ExecCommand {`
- `pub struct StatusCommand {`
- `pub struct ListCommand {`
- `pub struct ApplyCommand {`
- `pub struct DiffCommand {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks/src/cli.rs:1` `use clap::Args;`
- `use` `codex-rs/cloud-tasks/src/cli.rs:2` `use clap::Parser;`
- `use` `codex-rs/cloud-tasks/src/cli.rs:3` `use codex_common::CliConfigOverrides;`
- `struct` `codex-rs/cloud-tasks/src/cli.rs:7` `pub struct Cli {`
- `enum` `codex-rs/cloud-tasks/src/cli.rs:16` `pub enum Command {`
- `struct` `codex-rs/cloud-tasks/src/cli.rs:30` `pub struct ExecCommand {`
- `fn` `codex-rs/cloud-tasks/src/cli.rs:52` `fn parse_attempts(input: &str) -> Result<usize, String> {`
- `fn` `codex-rs/cloud-tasks/src/cli.rs:63` `fn parse_limit(input: &str) -> Result<i64, String> {`
- `struct` `codex-rs/cloud-tasks/src/cli.rs:75` `pub struct StatusCommand {`
- `struct` `codex-rs/cloud-tasks/src/cli.rs:82` `pub struct ListCommand {`
- `struct` `codex-rs/cloud-tasks/src/cli.rs:101` `pub struct ApplyCommand {`
- `struct` `codex-rs/cloud-tasks/src/cli.rs:112` `pub struct DiffCommand {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Args;`
- `use clap::Parser;`
- `use codex_common::CliConfigOverrides;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
