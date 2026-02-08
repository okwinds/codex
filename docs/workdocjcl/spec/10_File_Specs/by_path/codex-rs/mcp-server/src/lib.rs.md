# `codex-rs/mcp-server/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5764`
- sha256: `37e73c307c9c6a8ed66b702c837a74dfafcf38cac595d602981de8f8b912ed39`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/mcp-server/src/lib.rs:4` `use std::io::ErrorKind;`
- `use` `codex-rs/mcp-server/src/lib.rs:5` `use std::io::Result as IoResult;`
- `use` `codex-rs/mcp-server/src/lib.rs:6` `use std::path::PathBuf;`
- `use` `codex-rs/mcp-server/src/lib.rs:8` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/mcp-server/src/lib.rs:9` `use codex_core::config::Config;`
- `use` `codex-rs/mcp-server/src/lib.rs:11` `use rmcp::model::ClientNotification;`
- `use` `codex-rs/mcp-server/src/lib.rs:12` `use rmcp::model::ClientRequest;`
- `use` `codex-rs/mcp-server/src/lib.rs:13` `use rmcp::model::JsonRpcMessage;`
- `use` `codex-rs/mcp-server/src/lib.rs:14` `use serde_json::Value;`
- `use` `codex-rs/mcp-server/src/lib.rs:15` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/mcp-server/src/lib.rs:16` `use tokio::io::AsyncWriteExt;`
- `use` `codex-rs/mcp-server/src/lib.rs:17` `use tokio::io::BufReader;`
- `use` `codex-rs/mcp-server/src/lib.rs:18` `use tokio::io::{self};`
- `use` `codex-rs/mcp-server/src/lib.rs:19` `use tokio::sync::mpsc;`
- `use` `codex-rs/mcp-server/src/lib.rs:20` `use tracing::debug;`
- `use` `codex-rs/mcp-server/src/lib.rs:21` `use tracing::error;`
- `use` `codex-rs/mcp-server/src/lib.rs:22` `use tracing::info;`
- `use` `codex-rs/mcp-server/src/lib.rs:23` `use tracing_subscriber::EnvFilter;`
- `mod` `codex-rs/mcp-server/src/lib.rs:25` `mod codex_tool_config;`
- `mod` `codex-rs/mcp-server/src/lib.rs:26` `mod codex_tool_runner;`
- `mod` `codex-rs/mcp-server/src/lib.rs:27` `mod exec_approval;`
- `mod` `codex-rs/mcp-server/src/lib.rs:29` `mod outgoing_message;`
- `mod` `codex-rs/mcp-server/src/lib.rs:30` `mod patch_approval;`
- `use` `codex-rs/mcp-server/src/lib.rs:32` `use crate::message_processor::MessageProcessor;`
- `use` `codex-rs/mcp-server/src/lib.rs:33` `use crate::outgoing_message::OutgoingJsonRpcMessage;`
- `use` `codex-rs/mcp-server/src/lib.rs:34` `use crate::outgoing_message::OutgoingMessage;`
- `use` `codex-rs/mcp-server/src/lib.rs:35` `use crate::outgoing_message::OutgoingMessageSender;`
- `const` `codex-rs/mcp-server/src/lib.rs:47` `const CHANNEL_CAPACITY: usize = 128;`
- `type` `codex-rs/mcp-server/src/lib.rs:49` `type IncomingMessage = JsonRpcMessage<ClientRequest, Value, ClientNotification>;`
- `fn` `codex-rs/mcp-server/src/lib.rs:51` `pub async fn run_main(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::ErrorKind;`
- `use std::io::Result as IoResult;`
- `use std::path::PathBuf;`
- `use codex_common::CliConfigOverrides;`
- `use codex_core::config::Config;`
- `use rmcp::model::ClientNotification;`
- `use rmcp::model::ClientRequest;`
- `use rmcp::model::JsonRpcMessage;`
- `use serde_json::Value;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::io::AsyncWriteExt;`
- `use tokio::io::BufReader;`
- `use tokio::io::{self};`
- `use tokio::sync::mpsc;`
- `use tracing::debug;`
- `use tracing::error;`
- `use tracing::info;`
- `use tracing_subscriber::EnvFilter;`
- `use crate::message_processor::MessageProcessor;`
- `use crate::outgoing_message::OutgoingJsonRpcMessage;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
