# `codex-rs/tui/src/cli.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4507`
- sha256: `77b7abaa97230b5e01a5b2d222821ecb4c3d1eb0e052a6514dccfe067e411e6a`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/cli.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Cli {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/cli.rs:1` `use clap::Parser;`
- `use` `codex-rs/tui/src/cli.rs:2` `use clap::ValueHint;`
- `use` `codex-rs/tui/src/cli.rs:3` `use codex_common::ApprovalModeCliArg;`
- `use` `codex-rs/tui/src/cli.rs:4` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/tui/src/cli.rs:5` `use std::path::PathBuf;`
- `struct` `codex-rs/tui/src/cli.rs:9` `pub struct Cli {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Parser;`
- `use clap::ValueHint;`
- `use codex_common::ApprovalModeCliArg;`
- `use codex_common::CliConfigOverrides;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
