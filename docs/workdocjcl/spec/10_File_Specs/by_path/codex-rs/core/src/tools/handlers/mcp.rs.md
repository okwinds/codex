# `codex-rs/core/src/tools/handlers/mcp.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2020`
- sha256: `6eea7bd337768f13ff3d44357be7735985cd7bef795b8bdcb2f8be69cf2856d1`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `use` `codex-rs/core/src/tools/handlers/mcp.rs:11` `use codex_protocol::models::ResponseInputItem;`
- `struct` `codex-rs/core/src/tools/handlers/mcp.rs:13` `pub struct McpHandler;`
- `impl` `codex-rs/core/src/tools/handlers/mcp.rs:16` `impl ToolHandler for McpHandler {`
- `fn` `codex-rs/core/src/tools/handlers/mcp.rs:17` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/mcp.rs:21` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`

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
- `use codex_protocol::models::ResponseInputItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
