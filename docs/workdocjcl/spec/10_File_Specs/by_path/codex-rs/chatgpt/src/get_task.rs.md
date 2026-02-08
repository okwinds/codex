# `codex-rs/chatgpt/src/get_task.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `891`
- sha256: `35252f6bcb2eb3f07b405dae31ef6822c5310d6f04528a42246630d50ac4acc1`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/chatgpt/src/get_task.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct GetTaskResponse {`
- `pub struct AssistantTurn {`
- `pub enum OutputItem {`
- `pub struct PrOutputItem {`
- `pub struct OutputDiff {`

## Definitions (auto, per-file)
- `use` `codex-rs/chatgpt/src/get_task.rs:1` `use codex_core::config::Config;`
- `use` `codex-rs/chatgpt/src/get_task.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/chatgpt/src/get_task.rs:4` `use crate::chatgpt_client::chatgpt_get_request;`
- `struct` `codex-rs/chatgpt/src/get_task.rs:7` `pub struct GetTaskResponse {`
- `struct` `codex-rs/chatgpt/src/get_task.rs:13` `pub struct AssistantTurn {`
- `enum` `codex-rs/chatgpt/src/get_task.rs:19` `pub enum OutputItem {`
- `struct` `codex-rs/chatgpt/src/get_task.rs:28` `pub struct PrOutputItem {`
- `struct` `codex-rs/chatgpt/src/get_task.rs:33` `pub struct OutputDiff {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::Config;`
- `use serde::Deserialize;`
- `use crate::chatgpt_client::chatgpt_get_request;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
