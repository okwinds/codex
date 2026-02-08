# `codex-rs/protocol/src/custom_prompts.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `635`
- sha256: `47f55008c2206bf7b069bce88eaf2efe8965d715ce6079fbe04e785faa70d7f5`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/custom_prompts.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CustomPrompt {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/custom_prompts.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/custom_prompts.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/custom_prompts.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/custom_prompts.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/protocol/src/custom_prompts.rs:5` `use ts_rs::TS;`
- `const` `codex-rs/protocol/src/custom_prompts.rs:11` `pub const PROMPTS_CMD_PREFIX: &str = "prompts";`
- `struct` `codex-rs/protocol/src/custom_prompts.rs:14` `pub struct CustomPrompt {`

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
