# `codex-rs/core/src/mcp_tool_call.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15236`
- sha256: `7957bfac25aeb73907cc91ff75223df87db558532abd3466bc98b16a8b4292ca`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `use` `codex-rs/core/src/mcp_tool_call.rs:14` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:15` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:16` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:17` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:18` `use codex_protocol::protocol::ReviewDecision;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:19` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:20` `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:21` `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:22` `use codex_protocol::request_user_input::RequestUserInputQuestionOption;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:23` `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:24` `use rmcp::model::ToolAnnotations;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:25` `use serde::Serialize;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:26` `use std::sync::Arc;`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:163` `async fn notify_mcp_tool_call_event(sess: &Session, turn_context: &TurnContext, event: EventMsg) {`
- `enum` `codex-rs/core/src/mcp_tool_call.rs:168` `enum McpToolApprovalDecision {`
- `struct` `codex-rs/core/src/mcp_tool_call.rs:175` `struct McpToolApprovalMetadata {`
- `const` `codex-rs/core/src/mcp_tool_call.rs:182` `const MCP_TOOL_APPROVAL_QUESTION_ID_PREFIX: &str = "mcp_tool_call_approval";`
- `const` `codex-rs/core/src/mcp_tool_call.rs:183` `const MCP_TOOL_APPROVAL_ACCEPT: &str = "Approve Once";`
- `const` `codex-rs/core/src/mcp_tool_call.rs:184` `const MCP_TOOL_APPROVAL_ACCEPT_AND_REMEMBER: &str = "Approve this Session";`
- `const` `codex-rs/core/src/mcp_tool_call.rs:185` `const MCP_TOOL_APPROVAL_DECLINE: &str = "Deny";`
- `const` `codex-rs/core/src/mcp_tool_call.rs:186` `const MCP_TOOL_APPROVAL_CANCEL: &str = "Cancel";`
- `struct` `codex-rs/core/src/mcp_tool_call.rs:189` `struct McpToolApprovalKey {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:195` `async fn maybe_request_mcp_tool_approval(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:251` `fn is_full_access_mode(turn_context: &TurnContext) -> bool {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:259` `async fn lookup_mcp_tool_metadata(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:289` `fn build_mcp_tool_approval_question(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:345` `fn parse_mcp_tool_approval_response(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:379` `async fn mcp_tool_approval_is_remembered(sess: &Session, key: &McpToolApprovalKey) -> bool {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:384` `async fn remember_mcp_tool_approval(sess: &Session, key: McpToolApprovalKey) {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:389` `fn requires_mcp_tool_approval(annotations: &ToolAnnotations) -> bool {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:394` `async fn notify_mcp_tool_call_skip(`
- `use` `codex-rs/core/src/mcp_tool_call.rs:419` `use super::*;`
- `use` `codex-rs/core/src/mcp_tool_call.rs:420` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:422` `fn annotations(`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:437` `fn approval_required_when_read_only_false_and_destructive() {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:443` `fn approval_required_when_read_only_false_and_open_world() {`
- `fn` `codex-rs/core/src/mcp_tool_call.rs:449` `fn approval_not_required_when_read_only_true() {`

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
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::models::ResponseInputItem;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::ReviewDecision;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use codex_protocol::request_user_input::RequestUserInputQuestionOption;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
