# `codex-rs/core/src/tools/handlers/mcp.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2254`
- sha256: `f447c747babe05a263952a5797b8e745dd423d6dddc14019805618aefcccd1d2`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/mcp.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct McpHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:1` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:4` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:5` `use crate::mcp_tool_call::handle_mcp_tool_call;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:6` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:7` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:8` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:9` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:10` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/mcp.rs:12` `pub struct McpHandler;`
- `impl` `codex-rs/core/src/tools/handlers/mcp.rs:15` `impl ToolHandler for McpHandler {`
- `fn` `codex-rs/core/src/tools/handlers/mcp.rs:16` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/mcp.rs:20` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use std::sync::Arc;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::mcp_tool_call::handle_mcp_tool_call;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
