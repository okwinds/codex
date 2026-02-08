# `codex-rs/chatgpt/src/apply_command.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2415`
- sha256: `478d69df4e6872e044ce08f7dcd12d4a737a681b87f16ec284ccca67530e3864`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/chatgpt/src/apply_command.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct ApplyCommand {`

## Definitions (auto, per-file)
- `use` `codex-rs/chatgpt/src/apply_command.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:3` `use clap::Parser;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:4` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:5` `use codex_core::config::Config;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:7` `use crate::chatgpt_token::init_chatgpt_token_from_auth;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:8` `use crate::get_task::GetTaskResponse;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:9` `use crate::get_task::OutputItem;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:10` `use crate::get_task::PrOutputItem;`
- `use` `codex-rs/chatgpt/src/apply_command.rs:11` `use crate::get_task::get_task;`
- `struct` `codex-rs/chatgpt/src/apply_command.rs:15` `pub struct ApplyCommand {`
- `fn` `codex-rs/chatgpt/src/apply_command.rs:21` `pub async fn run_apply_command(`
- `fn` `codex-rs/chatgpt/src/apply_command.rs:40` `pub async fn apply_diff_from_task(`
- `fn` `codex-rs/chatgpt/src/apply_command.rs:58` `async fn apply_diff(diff: &str, cwd: Option<PathBuf>) -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use clap::Parser;`
- `use codex_common::CliConfigOverrides;`
- `use codex_core::config::Config;`
- `use crate::chatgpt_token::init_chatgpt_token_from_auth;`
- `use crate::get_task::GetTaskResponse;`
- `use crate::get_task::OutputItem;`
- `use crate::get_task::PrOutputItem;`
- `use crate::get_task::get_task;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
