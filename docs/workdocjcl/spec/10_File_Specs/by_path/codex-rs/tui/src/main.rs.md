# `codex-rs/tui/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `876`
- sha256: `7c89cf193575a56f5a7f869e93a0d735127b52b9c3efffc62c06af7ae305fe07`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/main.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `fn main() -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/main.rs:1` `use clap::Parser;`
- `use` `codex-rs/tui/src/main.rs:2` `use codex_arg0::arg0_dispatch_or_else;`
- `use` `codex-rs/tui/src/main.rs:3` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/tui/src/main.rs:4` `use codex_tui::Cli;`
- `use` `codex-rs/tui/src/main.rs:5` `use codex_tui::run_main;`
- `struct` `codex-rs/tui/src/main.rs:8` `struct TopCli {`
- `fn` `codex-rs/tui/src/main.rs:16` `fn main() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Parser;`
- `use codex_arg0::arg0_dispatch_or_else;`
- `use codex_common::CliConfigOverrides;`
- `use codex_tui::Cli;`
- `use codex_tui::run_main;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
