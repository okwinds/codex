# `codex-rs/core/src/tools/router.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6065`
- sha256: `cd64af142fbd6bed28546ece6eecd1e7f96efb5de68bcf1136199ecb159af5c4`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/router.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ToolCall {`
- `pub struct ToolRouter {`
- `pub fn from_config(`
- `pub fn specs(&self) -> Vec<ToolSpec> {`
- `pub fn tool_supports_parallel(&self, tool_name: &str) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/router.rs:1` `use crate::client_common::tools::ToolSpec;`
- `use` `codex-rs/core/src/tools/router.rs:2` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/router.rs:3` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/router.rs:4` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/router.rs:5` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/router.rs:6` `use crate::tools::context::SharedTurnDiffTracker;`
- `use` `codex-rs/core/src/tools/router.rs:7` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/router.rs:8` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/router.rs:9` `use crate::tools::registry::ConfiguredToolSpec;`
- `use` `codex-rs/core/src/tools/router.rs:10` `use crate::tools::registry::ToolRegistry;`
- `use` `codex-rs/core/src/tools/router.rs:11` `use crate::tools::spec::ToolsConfig;`
- `use` `codex-rs/core/src/tools/router.rs:12` `use crate::tools::spec::build_specs;`
- `use` `codex-rs/core/src/tools/router.rs:13` `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use` `codex-rs/core/src/tools/router.rs:14` `use codex_protocol::models::LocalShellAction;`
- `use` `codex-rs/core/src/tools/router.rs:15` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/tools/router.rs:16` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/tools/router.rs:17` `use codex_protocol::models::ShellToolCallParams;`
- `use` `codex-rs/core/src/tools/router.rs:18` `use rmcp::model::Tool;`
- `use` `codex-rs/core/src/tools/router.rs:19` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/router.rs:20` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/router.rs:21` `use tracing::instrument;`
- `struct` `codex-rs/core/src/tools/router.rs:24` `pub struct ToolCall {`
- `struct` `codex-rs/core/src/tools/router.rs:30` `pub struct ToolRouter {`
- `impl` `codex-rs/core/src/tools/router.rs:35` `impl ToolRouter {`
- `fn` `codex-rs/core/src/tools/router.rs:36` `pub fn from_config(`
- `fn` `codex-rs/core/src/tools/router.rs:47` `pub fn specs(&self) -> Vec<ToolSpec> {`
- `fn` `codex-rs/core/src/tools/router.rs:54` `pub fn tool_supports_parallel(&self, tool_name: &str) -> bool {`
- `fn` `codex-rs/core/src/tools/router.rs:62` `pub async fn build_tool_call(`
- `fn` `codex-rs/core/src/tools/router.rs:134` `pub async fn dispatch_tool_call(`
- `fn` `codex-rs/core/src/tools/router.rs:169` `fn failure_response(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::client_common::tools::ToolSpec;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::sandboxing::SandboxPermissions;`
- `use crate::tools::context::SharedTurnDiffTracker;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::registry::ConfiguredToolSpec;`
- `use crate::tools::registry::ToolRegistry;`
- `use crate::tools::spec::ToolsConfig;`
- `use crate::tools::spec::build_specs;`
- `use codex_protocol::dynamic_tools::DynamicToolSpec;`
- `use codex_protocol::models::LocalShellAction;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::models::ShellToolCallParams;`
- `use rmcp::model::Tool;`
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
