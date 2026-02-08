# `codex-rs/app-server/src/transport.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15271`
- sha256: `930d2b71b1cc9a6e73e86f7eed47947ef085f2e9a8a3a1ef72dfe775982ecdfc`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/transport.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- `pub enum AppServerTransport {`
- `pub enum AppServerTransportParseError {`
- `pub fn from_listen_url(listen_url: &str) -> Result<Self, AppServerTransportParseError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/transport.rs:1` `use crate::message_processor::ConnectionSessionState;`
- `use` `codex-rs/app-server/src/transport.rs:2` `use crate::outgoing_message::ConnectionId;`
- `use` `codex-rs/app-server/src/transport.rs:3` `use crate::outgoing_message::OutgoingEnvelope;`
- `use` `codex-rs/app-server/src/transport.rs:4` `use crate::outgoing_message::OutgoingMessage;`
- `use` `codex-rs/app-server/src/transport.rs:5` `use codex_app_server_protocol::JSONRPCMessage;`
- `use` `codex-rs/app-server/src/transport.rs:6` `use futures::SinkExt;`
- `use` `codex-rs/app-server/src/transport.rs:7` `use futures::StreamExt;`
- `use` `codex-rs/app-server/src/transport.rs:8` `use owo_colors::OwoColorize;`
- `use` `codex-rs/app-server/src/transport.rs:9` `use owo_colors::Stream;`
- `use` `codex-rs/app-server/src/transport.rs:10` `use owo_colors::Style;`
- `use` `codex-rs/app-server/src/transport.rs:11` `use std::collections::HashMap;`
- `use` `codex-rs/app-server/src/transport.rs:12` `use std::io::ErrorKind;`
- `use` `codex-rs/app-server/src/transport.rs:13` `use std::io::Result as IoResult;`
- `use` `codex-rs/app-server/src/transport.rs:14` `use std::net::SocketAddr;`
- `use` `codex-rs/app-server/src/transport.rs:15` `use std::str::FromStr;`
- `use` `codex-rs/app-server/src/transport.rs:16` `use std::sync::Arc;`
- `use` `codex-rs/app-server/src/transport.rs:17` `use std::sync::atomic::AtomicU64;`
- `use` `codex-rs/app-server/src/transport.rs:18` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/app-server/src/transport.rs:19` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/app-server/src/transport.rs:20` `use tokio::io::AsyncWriteExt;`
- `use` `codex-rs/app-server/src/transport.rs:21` `use tokio::io::BufReader;`
- `use` `codex-rs/app-server/src/transport.rs:22` `use tokio::io::{self};`
- `use` `codex-rs/app-server/src/transport.rs:23` `use tokio::net::TcpListener;`
- `use` `codex-rs/app-server/src/transport.rs:24` `use tokio::net::TcpStream;`
- `use` `codex-rs/app-server/src/transport.rs:25` `use tokio::sync::mpsc;`
- `use` `codex-rs/app-server/src/transport.rs:26` `use tokio::task::JoinHandle;`
- `use` `codex-rs/app-server/src/transport.rs:27` `use tokio_tungstenite::accept_async;`
- `use` `codex-rs/app-server/src/transport.rs:28` `use tokio_tungstenite::tungstenite::Message as WebSocketMessage;`
- `use` `codex-rs/app-server/src/transport.rs:29` `use tracing::debug;`
- `use` `codex-rs/app-server/src/transport.rs:30` `use tracing::error;`
- `use` `codex-rs/app-server/src/transport.rs:31` `use tracing::info;`
- `use` `codex-rs/app-server/src/transport.rs:32` `use tracing::warn;`
- `fn` `codex-rs/app-server/src/transport.rs:39` `fn colorize(text: &str, style: Style) -> String {`
- `fn` `codex-rs/app-server/src/transport.rs:45` `fn print_websocket_startup_banner(addr: SocketAddr) {`
- `fn` `codex-rs/app-server/src/transport.rs:64` `fn print_websocket_connection(peer_addr: SocketAddr) {`
- `enum` `codex-rs/app-server/src/transport.rs:70` `pub enum AppServerTransport {`
- `enum` `codex-rs/app-server/src/transport.rs:76` `pub enum AppServerTransportParseError {`
- `impl` `codex-rs/app-server/src/transport.rs:81` `impl std::fmt::Display for AppServerTransportParseError {`
- `fn` `codex-rs/app-server/src/transport.rs:82` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `impl` `codex-rs/app-server/src/transport.rs:98` `impl AppServerTransport {`
- `const` `codex-rs/app-server/src/transport.rs:99` `pub const DEFAULT_LISTEN_URL: &'static str = "stdio://";`
- `fn` `codex-rs/app-server/src/transport.rs:101` `pub fn from_listen_url(listen_url: &str) -> Result<Self, AppServerTransportParseError> {`
- `impl` `codex-rs/app-server/src/transport.rs:119` `impl FromStr for AppServerTransport {`
- `type` `codex-rs/app-server/src/transport.rs:120` `type Err = AppServerTransportParseError;`
- `fn` `codex-rs/app-server/src/transport.rs:122` `fn from_str(s: &str) -> Result<Self, Self::Err> {`
- `impl` `codex-rs/app-server/src/transport.rs:147` `impl ConnectionState {`
- `fn` `codex-rs/app-server/src/transport.rs:256` `async fn run_websocket_connection(`
- `fn` `codex-rs/app-server/src/transport.rs:327` `async fn forward_incoming_message(`
- `fn` `codex-rs/app-server/src/transport.rs:347` `fn serialize_outgoing_message(outgoing_message: OutgoingMessage) -> Option<String> {`
- `use` `codex-rs/app-server/src/transport.rs:418` `use super::*;`
- `use` `codex-rs/app-server/src/transport.rs:419` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/app-server/src/transport.rs:422` `fn app_server_transport_parses_stdio_listen_url() {`
- `fn` `codex-rs/app-server/src/transport.rs:429` `fn app_server_transport_parses_websocket_listen_url() {`
- `fn` `codex-rs/app-server/src/transport.rs:441` `fn app_server_transport_rejects_invalid_websocket_listen_url() {`
- `fn` `codex-rs/app-server/src/transport.rs:451` `fn app_server_transport_rejects_unsupported_listen_url() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::message_processor::ConnectionSessionState;`
- `use crate::outgoing_message::ConnectionId;`
- `use crate::outgoing_message::OutgoingEnvelope;`
- `use crate::outgoing_message::OutgoingMessage;`
- `use codex_app_server_protocol::JSONRPCMessage;`
- `use futures::SinkExt;`
- `use futures::StreamExt;`
- `use owo_colors::OwoColorize;`
- `use owo_colors::Stream;`
- `use owo_colors::Style;`
- `use std::collections::HashMap;`
- `use std::io::ErrorKind;`
- `use std::io::Result as IoResult;`
- `use std::net::SocketAddr;`
- `use std::str::FromStr;`
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicU64;`
- `use std::sync::atomic::Ordering;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::io::AsyncWriteExt;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
