# `codex-rs/core/src/tools/handlers/request_user_input.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2953`
- sha256: `9c12a7702bc213a03f8998beb48597ce5a6f8b51bd59e2d04241316a0b8fc19d`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:3` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:4` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:5` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:6` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:7` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:8` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:9` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:10` `use codex_protocol::config_types::ModeKind;`
- `use` `codex-rs/core/src/tools/handlers/request_user_input.rs:11` `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `struct` `codex-rs/core/src/tools/handlers/request_user_input.rs:13` `pub struct RequestUserInputHandler;`
- `impl` `codex-rs/core/src/tools/handlers/request_user_input.rs:16` `impl ToolHandler for RequestUserInputHandler {`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:17` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/request_user_input.rs:21` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::request_user_input::RequestUserInputArgs;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
