# `codex-rs/core/src/mcp_tool_call.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13258`
- sha256: `a39be82dbad69101d6a20e986de1083133075cb614d9d7494511918dd8769ccd`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/mcp_tool_call.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/mcp_tool_call.rs:1` `use std::time::Duration;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:2` `use std::time::Instant;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:4` `use tracing::error;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:6` `use crate::codex::Session;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:7` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:8` `use crate::mcp::CODEX_APPS_MCP_SERVER_NAME;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:9` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:10` `use crate::protocol::McpInvocation;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:11` `use crate::protocol::McpToolCallBeginEvent;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:12` `use crate::protocol::McpToolCallEndEvent;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:13` `use codex_protocol::mcp::CallToolResult;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:14` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:15` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:16` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:17` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:18` `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:19` `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:20` `use codex_protocol::request_user_input::RequestUserInputQuestionOption;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:21` `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:22` `use rmcp::model::ToolAnnotations;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:23` `use std::sync::Arc;`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:163` `async fn notify_mcp_tool_call_event(sess: &Session, turn_context: &TurnContext, event: EventMsg) {`
- `enum` `codex-rs/core/src/mcp_tool_call.rs:168` `enum McpToolApprovalDecision {`
- `struct` `codex-rs/core/src/mcp_tool_call.rs:174` `struct McpToolApprovalMetadata {`
- `const` `codex-rs/core/src/mcp_tool_call.rs:180` `const MCP_TOOL_APPROVAL_QUESTION_ID_PREFIX: &str = "mcp_tool_call_approval";`
- `const` `codex-rs/core/src/mcp_tool_call.rs:181` `const MCP_TOOL_APPROVAL_ACCEPT: &str = "Accept";`
- `const` `codex-rs/core/src/mcp_tool_call.rs:182` `const MCP_TOOL_APPROVAL_DECLINE: &str = "Decline";`
- `const` `codex-rs/core/src/mcp_tool_call.rs:183` `const MCP_TOOL_APPROVAL_CANCEL: &str = "Cancel";`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:185` `async fn maybe_request_mcp_tool_approval(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:221` `fn is_full_access_mode(turn_context: &TurnContext) -> bool {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:229` `async fn lookup_mcp_tool_metadata(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:258` `fn build_mcp_tool_approval_question(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:305` `fn parse_mcp_tool_approval_response(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:334` `fn requires_mcp_tool_approval(annotations: &ToolAnnotations) -> bool {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:339` `async fn notify_mcp_tool_call_skip(`
- `use` `codex-rs/core/src/mcp_tool_call.rs:364` `use super::*;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:365` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:367` `fn annotations(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:382` `fn approval_required_when_read_only_false_and_destructive() {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:388` `fn approval_required_when_read_only_false_and_open_world() {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:394` `fn approval_not_required_when_read_only_true() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use tracing::error;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::mcp::CODEX_APPS_MCP_SERVER_NAME;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::McpInvocation;`
- `use crate::protocol::McpToolCallBeginEvent;`
- `use crate::protocol::McpToolCallEndEvent;`
- `use codex_protocol::mcp::CallToolResult;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use codex_protocol::request_user_input::RequestUserInputQuestionOption;`
- `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use rmcp::model::ToolAnnotations;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
