# `codex-rs/mcp-server/src/codex_tool_runner.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15646`
- sha256: `80ce2eae67216343af06e124416858e16c011c54757a9a61525c17cd9922c021`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/codex_tool_runner.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:5` `use std::collections::HashMap;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:6` `use std::sync::Arc;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:8` `use crate::exec_approval::handle_exec_approval_request;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:9` `use crate::outgoing_message::OutgoingMessageSender;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:10` `use crate::outgoing_message::OutgoingNotificationMeta;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:11` `use crate::patch_approval::handle_patch_approval_request;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:12` `use codex_core::CodexThread;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:13` `use codex_core::NewThread;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:14` `use codex_core::ThreadManager;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:15` `use codex_core::config::Config as CodexConfig;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:16` `use codex_core::protocol::AgentMessageEvent;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:17` `use codex_core::protocol::ApplyPatchApprovalRequestEvent;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:18` `use codex_core::protocol::Event;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:19` `use codex_core::protocol::EventMsg;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:20` `use codex_core::protocol::ExecApprovalRequestEvent;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:21` `use codex_core::protocol::Op;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:22` `use codex_core::protocol::Submission;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:23` `use codex_core::protocol::TurnCompleteEvent;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:24` `use codex_protocol::ThreadId;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:25` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:26` `use rmcp::model::CallToolResult;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:27` `use rmcp::model::Content;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:28` `use rmcp::model::RequestId;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:29` `use serde_json::json;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:30` `use tokio::sync::Mutex;`
- `fn` `codex-rs/mcp-server/src/codex_tool_runner.rs:59` `pub async fn run_codex_tool_session(`
- `fn` `codex-rs/mcp-server/src/codex_tool_runner.rs:143` `pub async fn run_codex_tool_session_reply(`
- `fn` `codex-rs/mcp-server/src/codex_tool_runner.rs:191` `async fn run_codex_tool_session_inner(`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:390` `use super::*;`
- `use` `codex-rs/mcp-server/src/codex_tool_runner.rs:391` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/mcp-server/src/codex_tool_runner.rs:394` `fn call_tool_result_includes_thread_id_in_structured_content() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
- `use crate::exec_approval::handle_exec_approval_request;`
- `use crate::outgoing_message::OutgoingMessageSender;`
- `use crate::outgoing_message::OutgoingNotificationMeta;`
- `use crate::patch_approval::handle_patch_approval_request;`
- `use codex_core::CodexThread;`
- `use codex_core::NewThread;`
- `use codex_core::ThreadManager;`
- `use codex_core::config::Config as CodexConfig;`
- `use codex_core::protocol::AgentMessageEvent;`
- `use codex_core::protocol::ApplyPatchApprovalRequestEvent;`
- `use codex_core::protocol::Event;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecApprovalRequestEvent;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::Submission;`
- `use codex_core::protocol::TurnCompleteEvent;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::user_input::UserInput;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
