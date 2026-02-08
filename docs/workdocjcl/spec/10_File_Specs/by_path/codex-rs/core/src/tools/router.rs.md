# `codex-rs/core/src/tools/router.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6103`
- sha256: `427550de8d3d6b51e20d18663e87e3dce1cc824e04c8ba39aa3c6f6a15293260`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `use` `codex-rs/core/src/tools/router.rs:14` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/router.rs:15` `use codex_protocol::models::LocalShellAction;`
- `use` `codex-rs/core/src/tools/router.rs:16` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/tools/router.rs:17` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/tools/router.rs:18` `use codex_protocol::models::ShellToolCallParams;`
- `use` `codex-rs/core/src/tools/router.rs:19` `use rmcp::model::Tool;`
- `use` `codex-rs/core/src/tools/router.rs:20` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/router.rs:21` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/router.rs:22` `use tracing::instrument;`
- `struct` `codex-rs/core/src/tools/router.rs:25` `pub struct ToolCall {`
- `struct` `codex-rs/core/src/tools/router.rs:31` `pub struct ToolRouter {`
- `impl` `codex-rs/core/src/tools/router.rs:36` `impl ToolRouter {`
- `fn` `codex-rs/core/src/tools/router.rs:37` `pub fn from_config(`
- `fn` `codex-rs/core/src/tools/router.rs:48` `pub fn specs(&self) -> Vec<ToolSpec> {`
- `fn` `codex-rs/core/src/tools/router.rs:55` `pub fn tool_supports_parallel(&self, tool_name: &str) -> bool {`
- `fn` `codex-rs/core/src/tools/router.rs:63` `pub async fn build_tool_call(`
- `fn` `codex-rs/core/src/tools/router.rs:135` `pub async fn dispatch_tool_call(`
- `fn` `codex-rs/core/src/tools/router.rs:170` `fn failure_response(`

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
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use codex_protocol::models::LocalShellAction;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::models::ShellToolCallParams;`
- `use rmcp::model::Tool;`
- `use std::collections::HashMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
