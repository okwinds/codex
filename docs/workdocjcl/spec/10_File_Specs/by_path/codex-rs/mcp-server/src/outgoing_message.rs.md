# `codex-rs/mcp-server/src/outgoing_message.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17098`
- sha256: `645c0dfd6146823bfdc788b4d11d462d5ca74c7872944757a49902fe152d6df3`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/outgoing_message.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:2` `use std::sync::atomic::AtomicI64;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:3` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:5` `use codex_core::protocol::Event;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:6` `use codex_protocol::ThreadId;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:7` `use rmcp::model::CustomNotification;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:8` `use rmcp::model::CustomRequest;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:9` `use rmcp::model::ErrorData;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:10` `use rmcp::model::JsonRpcError;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:11` `use rmcp::model::JsonRpcMessage;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:12` `use rmcp::model::JsonRpcNotification;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:13` `use rmcp::model::JsonRpcRequest;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:14` `use rmcp::model::JsonRpcResponse;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:15` `use rmcp::model::JsonRpcVersion2_0;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:16` `use rmcp::model::RequestId;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:17` `use serde::Serialize;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:18` `use serde_json::Value;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:19` `use tokio::sync::Mutex;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:20` `use tokio::sync::mpsc;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:21` `use tokio::sync::oneshot;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:22` `use tracing::warn;`
- `impl` `codex-rs/mcp-server/src/outgoing_message.rs:33` `impl OutgoingMessageSender {`
- `impl` `codex-rs/mcp-server/src/outgoing_message.rs:146` `impl From<OutgoingMessage> for OutgoingJsonRpcMessage {`
- `fn` `codex-rs/mcp-server/src/outgoing_message.rs:147` `fn from(val: OutgoingMessage) -> Self {`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:148` `use OutgoingMessage::*;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:231` `use std::path::PathBuf;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:233` `use anyhow::Result;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:234` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:235` `use codex_core::protocol::EventMsg;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:236` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:237` `use codex_core::protocol::SessionConfiguredEvent;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:238` `use codex_protocol::ThreadId;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:239` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:240` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:241` `use serde_json::json;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:242` `use tempfile::NamedTempFile;`
- `use` `codex-rs/mcp-server/src/outgoing_message.rs:244` `use super::*;`
- `fn` `codex-rs/mcp-server/src/outgoing_message.rs:247` `fn outgoing_request_serializes_as_jsonrpc_request() {`
- `fn` `codex-rs/mcp-server/src/outgoing_message.rs:269` `fn outgoing_notification_serializes_as_jsonrpc_notification() {`
- `fn` `codex-rs/mcp-server/src/outgoing_message.rs:289` `async fn test_send_event_as_notification() -> Result<()> {`
- `fn` `codex-rs/mcp-server/src/outgoing_message.rs:332` `async fn test_send_event_as_notification_with_meta() -> Result<()> {`
- `fn` `codex-rs/mcp-server/src/outgoing_message.rs:397` `async fn test_send_event_as_notification_with_meta_and_thread_id() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::sync::atomic::AtomicI64;`
- `use std::sync::atomic::Ordering;`
- `use codex_core::protocol::Event;`
- `use codex_protocol::ThreadId;`
- `use rmcp::model::CustomNotification;`
- `use rmcp::model::CustomRequest;`
- `use rmcp::model::ErrorData;`
- `use rmcp::model::JsonRpcError;`
- `use rmcp::model::JsonRpcMessage;`
- `use rmcp::model::JsonRpcNotification;`
- `use rmcp::model::JsonRpcRequest;`
- `use rmcp::model::JsonRpcResponse;`
- `use rmcp::model::JsonRpcVersion2_0;`
- `use rmcp::model::RequestId;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::mpsc;`
- `use tokio::sync::oneshot;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
