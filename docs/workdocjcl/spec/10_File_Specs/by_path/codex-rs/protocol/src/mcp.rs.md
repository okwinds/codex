# `codex-rs/protocol/src/mcp.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10015`
- sha256: `1ada8bfee02d9971cedb3e4efc3ffd6f78d1934c67b8f78e99e8f2272f095908`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/mcp.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum RequestId {`
- `pub struct Tool {`
- `pub struct Resource {`
- `pub struct ResourceTemplate {`
- `pub struct CallToolResult {`
- `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {`
- `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {`
- `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/mcp.rs:6` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/mcp.rs:7` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/mcp.rs:8` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/mcp.rs:9` `use ts_rs::TS;`
- `enum` `codex-rs/protocol/src/mcp.rs:14` `pub enum RequestId {`
- `impl` `codex-rs/protocol/src/mcp.rs:20` `impl std::fmt::Display for RequestId {`
- `fn` `codex-rs/protocol/src/mcp.rs:21` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/protocol/src/mcp.rs:32` `pub struct Tool {`
- `struct` `codex-rs/protocol/src/mcp.rs:58` `pub struct Resource {`
- `struct` `codex-rs/protocol/src/mcp.rs:88` `pub struct ResourceTemplate {`
- `struct` `codex-rs/protocol/src/mcp.rs:108` `pub struct CallToolResult {`
- `struct` `codex-rs/protocol/src/mcp.rs:147` `struct ToolSerde {`
- `impl` `codex-rs/protocol/src/mcp.rs:165` `impl From<ToolSerde> for Tool {`
- `fn` `codex-rs/protocol/src/mcp.rs:166` `fn from(value: ToolSerde) -> Self {`
- `struct` `codex-rs/protocol/src/mcp.rs:192` `struct ResourceSerde {`
- `impl` `codex-rs/protocol/src/mcp.rs:211` `impl From<ResourceSerde> for Resource {`
- `fn` `codex-rs/protocol/src/mcp.rs:212` `fn from(value: ResourceSerde) -> Self {`
- `struct` `codex-rs/protocol/src/mcp.rs:240` `struct ResourceTemplateSerde {`
- `impl` `codex-rs/protocol/src/mcp.rs:254` `impl From<ResourceTemplateSerde> for ResourceTemplate {`
- `fn` `codex-rs/protocol/src/mcp.rs:255` `fn from(value: ResourceTemplateSerde) -> Self {`
- `impl` `codex-rs/protocol/src/mcp.rs:275` `impl Tool {`
- `fn` `codex-rs/protocol/src/mcp.rs:276` `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {`
- `impl` `codex-rs/protocol/src/mcp.rs:281` `impl Resource {`
- `fn` `codex-rs/protocol/src/mcp.rs:282` `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {`
- `impl` `codex-rs/protocol/src/mcp.rs:287` `impl ResourceTemplate {`
- `fn` `codex-rs/protocol/src/mcp.rs:288` `pub fn from_mcp_value(value: serde_json::Value) -> Result<Self, serde_json::Error> {`
- `use` `codex-rs/protocol/src/mcp.rs:295` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/protocol/src/mcp.rs:297` `use super::*;`
- `fn` `codex-rs/protocol/src/mcp.rs:300` `fn resource_size_deserializes_without_narrowing() {`

## Dependencies (auto sample)
### Imports / Includes
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
- `use pretty_assertions::assert_eq;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
