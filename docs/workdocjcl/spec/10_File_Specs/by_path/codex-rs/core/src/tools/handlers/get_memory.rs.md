# `codex-rs/core/src/tools/handlers/get_memory.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2375`
- sha256: `c9b5b442431361f61651da272eec0c86bc3524cd1a74a64e216cee2c65561a7b`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/get_memory.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct GetMemoryHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:1` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:2` `use crate::state_db;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:3` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:4` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:5` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:6` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:7` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:8` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:9` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:10` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:11` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:12` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/get_memory.rs:13` `use serde_json::json;`
- `struct` `codex-rs/core/src/tools/handlers/get_memory.rs:15` `pub struct GetMemoryHandler;`
- `struct` `codex-rs/core/src/tools/handlers/get_memory.rs:18` `struct GetMemoryArgs {`
- `impl` `codex-rs/core/src/tools/handlers/get_memory.rs:23` `impl ToolHandler for GetMemoryHandler {`
- `fn` `codex-rs/core/src/tools/handlers/get_memory.rs:24` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/get_memory.rs:28` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::function_tool::FunctionCallError;`
- `use crate::state_db;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use async_trait::async_trait;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use serde::Deserialize;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
