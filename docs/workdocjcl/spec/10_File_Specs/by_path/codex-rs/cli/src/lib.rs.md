# `codex-rs/cli/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1682`
- sha256: `2db038a3f393e97c1efc577838a56d38c70247818d4a38a4a62d729abd47c5a5`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct SeatbeltCommand {`
- `pub struct LandlockCommand {`
- `pub struct WindowsCommand {`

## Definitions (auto, per-file)
- `mod` `codex-rs/cli/src/lib.rs:1` `pub mod debug_sandbox;`
- `mod` `codex-rs/cli/src/lib.rs:2` `mod exit_status;`
- `mod` `codex-rs/cli/src/lib.rs:3` `pub mod login;`
- `use` `codex-rs/cli/src/lib.rs:5` `use clap::Parser;`
- `use` `codex-rs/cli/src/lib.rs:6` `use codex_common::CliConfigOverrides;`
- `struct` `codex-rs/cli/src/lib.rs:9` `pub struct SeatbeltCommand {`
- `struct` `codex-rs/cli/src/lib.rs:27` `pub struct LandlockCommand {`
- `struct` `codex-rs/cli/src/lib.rs:41` `pub struct WindowsCommand {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Parser;`
- `use codex_common::CliConfigOverrides;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/03_API/CLI.md`
