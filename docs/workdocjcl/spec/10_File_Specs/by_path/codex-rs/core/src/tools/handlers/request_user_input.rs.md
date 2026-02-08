# `codex-rs/core/src/tools/handlers/request_user_input.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5289`
- sha256: `870f06ed67ff8c4897880a23e8eb5d2add5e30a7ee94765c2c0faa0fbd9554ae`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/request_user_input.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RequestUserInputHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:1` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:2` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:4` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:5` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:6` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:7` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:8` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:9` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:10` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:11` `use codex_protocol::config_types::ModeKind;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:12` `use codex_protocol::config_types::TUI_VISIBLE_COLLABORATION_MODES;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:13` `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:15` `fn format_allowed_modes() -> String {`
- `struct` `codex-rs/core/src/tools/handlers/request_user_input.rs:48` `pub struct RequestUserInputHandler;`
- `impl` `codex-rs/core/src/tools/handlers/request_user_input.rs:51` `impl ToolHandler for RequestUserInputHandler {`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:52` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:56` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:116` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:117` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:120` `fn request_user_input_mode_availability_is_plan_only() {`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:128` `fn request_user_input_unavailable_messages_use_default_name_for_default_modes() {`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:145` `fn request_user_input_tool_description_mentions_plan_only() {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::config_types::TUI_VISIBLE_COLLABORATION_MODES;`
- `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
