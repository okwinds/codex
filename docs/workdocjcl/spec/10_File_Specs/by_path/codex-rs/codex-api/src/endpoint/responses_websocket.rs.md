# `codex-rs/codex-api/src/endpoint/responses_websocket.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10812`
- sha256: `f1aa42e7f8bb35f04a78f0ddd8d5457a84c94acf3704bc1839a7969789ea1c5f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/responses_websocket.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct ResponsesWebsocketConnection {`
- `pub struct ResponsesWebsocketClient<A: AuthProvider> {`
- `pub fn new(provider: Provider, auth: A) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:2` `use crate::common::ResponseEvent;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:3` `use crate::common::ResponseStream;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:4` `use crate::common::ResponsesWsRequest;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:5` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:6` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:7` `use crate::sse::responses::ResponsesStreamEvent;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:8` `use crate::sse::responses::process_responses_event;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:9` `use crate::telemetry::WebsocketTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:10` `use codex_client::TransportError;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:11` `use futures::SinkExt;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:12` `use futures::StreamExt;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:13` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:14` `use http::HeaderValue;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:15` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:16` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:17` `use std::sync::OnceLock;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:18` `use std::time::Duration;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:19` `use tokio::net::TcpStream;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:20` `use tokio::sync::Mutex;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:21` `use tokio::sync::mpsc;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:22` `use tokio::time::Instant;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:23` `use tokio_tungstenite::MaybeTlsStream;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:24` `use tokio_tungstenite::WebSocketStream;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:25` `use tokio_tungstenite::tungstenite::Error as WsError;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:26` `use tokio_tungstenite::tungstenite::Message;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:27` `use tokio_tungstenite::tungstenite::client::IntoClientRequest;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:28` `use tracing::debug;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:29` `use tracing::error;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:30` `use tracing::info;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:31` `use tracing::trace;`
- `use` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:32` `use url::Url;`
- `type` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:34` `type WsStream = WebSocketStream<MaybeTlsStream<TcpStream>>;`
- `const` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:35` `const X_CODEX_TURN_STATE_HEADER: &str = "x-codex-turn-state";`
- `const` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:36` `const X_REASONING_INCLUDED_HEADER: &str = "x-reasoning-included";`
- `struct` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:38` `pub struct ResponsesWebsocketConnection {`
- `impl` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:46` `impl ResponsesWebsocketConnection {`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:47` `fn new(`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:61` `pub async fn is_closed(&self) -> bool {`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:65` `pub async fn stream_request(`
- `struct` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:114` `pub struct ResponsesWebsocketClient<A: AuthProvider> {`
- `impl` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:119` `impl<A: AuthProvider> ResponsesWebsocketClient<A> {`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:120` `pub fn new(provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:124` `pub async fn connect(`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:151` `fn apply_auth_headers(headers: &mut HeaderMap, auth: &impl AuthProvider) {`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:164` `async fn connect_websocket(`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:205` `fn map_ws_error(err: WsError, url: &Url) -> ApiError {`
- `fn` `codex-rs/codex-api/src/endpoint/responses_websocket.rs:229` `async fn run_websocket_response_stream(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::common::ResponseEvent;`
- `use crate::common::ResponseStream;`
- `use crate::common::ResponsesWsRequest;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::sse::responses::ResponsesStreamEvent;`
- `use crate::sse::responses::process_responses_event;`
- `use crate::telemetry::WebsocketTelemetry;`
- `use codex_client::TransportError;`
- `use futures::SinkExt;`
- `use futures::StreamExt;`
- `use http::HeaderMap;`
- `use http::HeaderValue;`
- `use serde_json::Value;`
- `use std::sync::Arc;`
- `use std::sync::OnceLock;`
- `use std::time::Duration;`
- `use tokio::net::TcpStream;`
- `use tokio::sync::Mutex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
