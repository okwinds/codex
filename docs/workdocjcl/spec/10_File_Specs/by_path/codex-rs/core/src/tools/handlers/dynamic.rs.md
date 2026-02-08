# `codex-rs/core/src/tools/handlers/dynamic.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3024`
- sha256: `57108b806f3d38845c93fdd4b25e0ae2febfb58ebcaeabafa277324e82cd048f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/dynamic.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct DynamicToolHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:1` `use crate::codex::Session;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:2` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:3` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:4` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:5` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:6` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:7` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:8` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:9` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:10` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:11` `use codex_protocol::dynamic_tools::DynamicToolCallRequest;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:12` `use codex_protocol::dynamic_tools::DynamicToolResponse;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:13` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:14` `use serde_json::Value;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:15` `use tokio::sync::oneshot;`
- `use` `codex-rs/core/src/tools/handlers/dynamic.rs:16` `use tracing::warn;`
- `struct` `codex-rs/core/src/tools/handlers/dynamic.rs:18` `pub struct DynamicToolHandler;`
- `impl` `codex-rs/core/src/tools/handlers/dynamic.rs:21` `impl ToolHandler for DynamicToolHandler {`
- `fn` `codex-rs/core/src/tools/handlers/dynamic.rs:22` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/dynamic.rs:26` `async fn is_mutating(&self, _invocation: &ToolInvocation) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/dynamic.rs:30` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/dynamic.rs:66` `async fn request_dynamic_tool(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use async_trait::async_trait;`
- `use codex_protocol::dynamic_tools::DynamicToolCallRequest;`
- `use codex_protocol::dynamic_tools::DynamicToolResponse;`
- `use codex_protocol::protocol::EventMsg;`
- `use serde_json::Value;`
- `use tokio::sync::oneshot;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
