# `codex-rs/mcp-server/src/codex_tool_config.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15433`
- sha256: `9bace577a564711cfb7dd0eb706bb622e38c3492b1540a6cf526611886cc4d11`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/codex_tool_config.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CodexToolCallParam {`
- `pub enum CodexToolCallApprovalPolicy {`
- `pub enum CodexToolCallSandboxMode {`
- `pub struct CodexToolCallReplyParam {`

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:3` `use codex_core::config::Config;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:4` `use codex_core::config::ConfigOverrides;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:5` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:6` `use codex_protocol::ThreadId;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:7` `use codex_protocol::config_types::SandboxMode;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:8` `use codex_utils_json_to_toml::json_to_toml;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:9` `use rmcp::model::JsonObject;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:10` `use rmcp::model::Tool;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:11` `use schemars::JsonSchema;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:12` `use schemars::r#gen::SchemaSettings;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:13` `use serde::Deserialize;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:14` `use serde::Serialize;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:15` `use std::collections::HashMap;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:16` `use std::path::PathBuf;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:17` `use std::sync::Arc;`
- `struct` `codex-rs/mcp-server/src/codex_tool_config.rs:22` `pub struct CodexToolCallParam {`
- `enum` `codex-rs/mcp-server/src/codex_tool_config.rs:70` `pub enum CodexToolCallApprovalPolicy {`
- `impl` `codex-rs/mcp-server/src/codex_tool_config.rs:77` `impl From<CodexToolCallApprovalPolicy> for AskForApproval {`
- `fn` `codex-rs/mcp-server/src/codex_tool_config.rs:78` `fn from(value: CodexToolCallApprovalPolicy) -> Self {`
- `enum` `codex-rs/mcp-server/src/codex_tool_config.rs:92` `pub enum CodexToolCallSandboxMode {`
- `impl` `codex-rs/mcp-server/src/codex_tool_config.rs:98` `impl From<CodexToolCallSandboxMode> for SandboxMode {`
- `fn` `codex-rs/mcp-server/src/codex_tool_config.rs:99` `fn from(value: CodexToolCallSandboxMode) -> Self {`
- `fn` `codex-rs/mcp-server/src/codex_tool_config.rs:135` `fn codex_tool_output_schema() -> Arc<JsonObject> {`
- `impl` `codex-rs/mcp-server/src/codex_tool_config.rs:150` `impl CodexToolCallParam {`
- `fn` `codex-rs/mcp-server/src/codex_tool_config.rs:153` `pub async fn into_config(`
- `struct` `codex-rs/mcp-server/src/codex_tool_config.rs:199` `pub struct CodexToolCallReplyParam {`
- `impl` `codex-rs/mcp-server/src/codex_tool_config.rs:214` `impl CodexToolCallReplyParam {`
- `fn` `codex-rs/mcp-server/src/codex_tool_config.rs:256` `fn create_tool_input_schema(`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:282` `use super::*;`
- `use` `codex-rs/mcp-server/src/codex_tool_config.rs:283` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/mcp-server/src/codex_tool_config.rs:297` `fn verify_codex_tool_json_schema() {`
- `fn` `codex-rs/mcp-server/src/codex_tool_config.rs:384` `fn verify_codex_tool_reply_json_schema() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::Config;`
- `use codex_core::config::ConfigOverrides;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::SandboxMode;`
- `use codex_utils_json_to_toml::json_to_toml;`
- `use rmcp::model::JsonObject;`
- `use rmcp::model::Tool;`
- `use schemars::JsonSchema;`
- `use schemars::r#gen::SchemaSettings;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
