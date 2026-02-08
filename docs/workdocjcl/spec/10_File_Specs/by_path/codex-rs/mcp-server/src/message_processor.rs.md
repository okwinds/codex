# `codex-rs/mcp-server/src/message_processor.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `21348`
- sha256: `cd020080b99ebf86f3d1b183e91cbca2b6b6aadcc2573e23534d4f6269f1ebdf`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/message_processor.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/message_processor.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:4` `use codex_core::AuthManager;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:5` `use codex_core::ThreadManager;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:6` `use codex_core::config::Config;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:7` `use codex_core::default_client::USER_AGENT_SUFFIX;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:8` `use codex_core::default_client::get_codex_user_agent;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:9` `use codex_core::protocol::Submission;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:10` `use codex_protocol::ThreadId;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:11` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:12` `use rmcp::model::CallToolRequestParam;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:13` `use rmcp::model::CallToolResult;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:14` `use rmcp::model::ClientNotification;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:15` `use rmcp::model::ClientRequest;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:16` `use rmcp::model::ErrorCode;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:17` `use rmcp::model::ErrorData;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:18` `use rmcp::model::Implementation;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:19` `use rmcp::model::InitializeResult;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:20` `use rmcp::model::JsonRpcError;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:21` `use rmcp::model::JsonRpcNotification;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:22` `use rmcp::model::JsonRpcRequest;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:23` `use rmcp::model::JsonRpcResponse;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:24` `use rmcp::model::RequestId;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:25` `use rmcp::model::ServerCapabilities;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:26` `use rmcp::model::ToolsCapability;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:27` `use serde_json::json;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:28` `use std::sync::Arc;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:29` `use tokio::sync::Mutex;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:30` `use tokio::task;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:32` `use crate::codex_tool_config::CodexToolCallParam;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:33` `use crate::codex_tool_config::CodexToolCallReplyParam;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:34` `use crate::codex_tool_config::create_tool_for_codex_tool_call_param;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:35` `use crate::codex_tool_config::create_tool_for_codex_tool_call_reply_param;`
- `use` `codex-rs/mcp-server/src/message_processor.rs:36` `use crate::outgoing_message::OutgoingMessageSender;`
- `impl` `codex-rs/mcp-server/src/message_processor.rs:46` `impl MessageProcessor {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:167` `async fn handle_initialize(`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:254` `async fn handle_ping(&self, id: RequestId) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:259` `fn handle_list_resources(&self, params: Option<rmcp::model::PaginatedRequestParam>) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:263` `fn handle_list_resource_templates(&self, params: Option<rmcp::model::PaginatedRequestParam>) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:267` `fn handle_read_resource(&self, params: rmcp::model::ReadResourceRequestParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:271` `fn handle_subscribe(&self, params: rmcp::model::SubscribeRequestParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:275` `fn handle_unsubscribe(&self, params: rmcp::model::UnsubscribeRequestParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:279` `fn handle_list_prompts(&self, params: Option<rmcp::model::PaginatedRequestParam>) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:283` `fn handle_get_prompt(&self, params: rmcp::model::GetPromptRequestParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:287` `async fn handle_list_tools(`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:305` `async fn handle_call_tool(&self, id: RequestId, params: CallToolRequestParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:327` `async fn handle_tool_call_codex(`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:401` `async fn handle_tool_call_codex_session_reply(`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:499` `fn handle_set_level(&self, params: rmcp::model::SetLevelRequestParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:503` `fn handle_complete(&self, params: rmcp::model::CompleteRequestParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:511` `async fn handle_cancelled_notification(&self, params: rmcp::model::CancelledNotificationParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:556` `fn handle_progress_notification(&self, params: rmcp::model::ProgressNotificationParam) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:560` `fn handle_roots_list_changed(&self) {`
- `fn` `codex-rs/mcp-server/src/message_processor.rs:564` `fn handle_initialized_notification(&self) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use codex_core::AuthManager;`
- `use codex_core::ThreadManager;`
- `use codex_core::config::Config;`
- `use codex_core::default_client::USER_AGENT_SUFFIX;`
- `use codex_core::default_client::get_codex_user_agent;`
- `use codex_core::protocol::Submission;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::SessionSource;`
- `use rmcp::model::CallToolRequestParam;`
- `use rmcp::model::CallToolResult;`
- `use rmcp::model::ClientNotification;`
- `use rmcp::model::ClientRequest;`
- `use rmcp::model::ErrorCode;`
- `use rmcp::model::ErrorData;`
- `use rmcp::model::Implementation;`
- `use rmcp::model::InitializeResult;`
- `use rmcp::model::JsonRpcError;`
- `use rmcp::model::JsonRpcNotification;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
