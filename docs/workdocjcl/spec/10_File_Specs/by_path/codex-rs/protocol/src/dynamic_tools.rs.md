# `codex-rs/protocol/src/dynamic_tools.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `818`
- sha256: `d1e032d877b887a2e833411dcb24573f915196f8ef88bc0d1597d8a7ceb56ca7`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/dynamic_tools.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct DynamicToolSpec {`
- `pub struct DynamicToolCallRequest {`
- `pub struct DynamicToolResponse {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/dynamic_tools.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:4` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:5` `use ts_rs::TS;`
- `struct` `codex-rs/protocol/src/dynamic_tools.rs:9` `pub struct DynamicToolSpec {`
- `struct` `codex-rs/protocol/src/dynamic_tools.rs:17` `pub struct DynamicToolCallRequest {`
- `struct` `codex-rs/protocol/src/dynamic_tools.rs:26` `pub struct DynamicToolResponse {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde_json::Value as JsonValue;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
