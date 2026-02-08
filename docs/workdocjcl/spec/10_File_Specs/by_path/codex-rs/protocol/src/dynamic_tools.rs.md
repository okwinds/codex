# `codex-rs/protocol/src/dynamic_tools.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1170`
- sha256: `dfb667c8069fe8890f484d8185e49384846a6508105606f1e04e63c543842c50`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `pub enum DynamicToolCallOutputContentItem {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/dynamic_tools.rs:1` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:3` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:4` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/protocol/src/dynamic_tools.rs:5` `use ts_rs::TS;`
- `struct` `codex-rs/protocol/src/dynamic_tools.rs:9` `pub struct DynamicToolSpec {`
- `struct` `codex-rs/protocol/src/dynamic_tools.rs:17` `pub struct DynamicToolCallRequest {`
- `struct` `codex-rs/protocol/src/dynamic_tools.rs:26` `pub struct DynamicToolResponse {`
- `enum` `codex-rs/protocol/src/dynamic_tools.rs:34` `pub enum DynamicToolCallOutputContentItem {`

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
- `docs/workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
