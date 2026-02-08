# `codex-rs/protocol/src/parse_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `846`
- sha256: `aa57d7d46ece71f10601d0178db6ef2d50a0bfa91c756359ee22f60139be9f31`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/parse_command.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ParsedCommand {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/parse_command.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/parse_command.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/parse_command.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/parse_command.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/protocol/src/parse_command.rs:5` `use ts_rs::TS;`
- `enum` `codex-rs/protocol/src/parse_command.rs:9` `pub enum ParsedCommand {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::path::PathBuf;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
