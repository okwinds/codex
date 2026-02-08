# `codex-rs/protocol/src/request_user_input.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1784`
- sha256: `f617bec633ca8ccc9df9f5b9c567cddb93a366ed51cc16f9948496d23eb492a6`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/request_user_input.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RequestUserInputQuestionOption {`
- `pub struct RequestUserInputQuestion {`
- `pub struct RequestUserInputArgs {`
- `pub struct RequestUserInputAnswer {`
- `pub struct RequestUserInputResponse {`
- `pub struct RequestUserInputEvent {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/request_user_input.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/protocol/src/request_user_input.rs:3` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/request_user_input.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/request_user_input.rs:5` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/request_user_input.rs:6` `use ts_rs::TS;`
- `struct` `codex-rs/protocol/src/request_user_input.rs:9` `pub struct RequestUserInputQuestionOption {`
- `struct` `codex-rs/protocol/src/request_user_input.rs:15` `pub struct RequestUserInputQuestion {`
- `struct` `codex-rs/protocol/src/request_user_input.rs:32` `pub struct RequestUserInputArgs {`
- `struct` `codex-rs/protocol/src/request_user_input.rs:37` `pub struct RequestUserInputAnswer {`
- `struct` `codex-rs/protocol/src/request_user_input.rs:42` `pub struct RequestUserInputResponse {`
- `struct` `codex-rs/protocol/src/request_user_input.rs:47` `pub struct RequestUserInputEvent {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
