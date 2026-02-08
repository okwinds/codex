# `codex-rs/core/src/tools/handlers/view_image.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2956`
- sha256: `049d38f717b97e762a937af6913ec844a9598fe181802a6406abcabfe65b441f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/view_image.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ViewImageHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:1` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:2` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:3` `use tokio::fs;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:5` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:6` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:7` `use crate::protocol::ViewImageToolCallEvent;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:8` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:9` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:10` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:11` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:12` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:13` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:14` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:15` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/tools/handlers/view_image.rs:16` `use codex_protocol::models::local_image_content_items_with_label_number;`
- `struct` `codex-rs/core/src/tools/handlers/view_image.rs:18` `pub struct ViewImageHandler;`
- `struct` `codex-rs/core/src/tools/handlers/view_image.rs:21` `struct ViewImageArgs {`
- `impl` `codex-rs/core/src/tools/handlers/view_image.rs:26` `impl ToolHandler for ViewImageHandler {`
- `fn` `codex-rs/core/src/tools/handlers/view_image.rs:27` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/view_image.rs:31` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use serde::Deserialize;`
- `use tokio::fs;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::ViewImageToolCallEvent;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::models::local_image_content_items_with_label_number;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
