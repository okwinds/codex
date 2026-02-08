# `codex-rs/codex-api/src/telemetry.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2687`
- sha256: `dca14047de75c7f5d7af761d6e69bc0352efd5ae40d98ed54b5b6ed42ce600a9`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/telemetry.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub trait SseTelemetry: Send + Sync {`
- `pub trait WebsocketTelemetry: Send + Sync {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/telemetry.rs:1` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/telemetry.rs:2` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/telemetry.rs:3` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/telemetry.rs:4` `use codex_client::Response;`
- `use` `codex-rs/codex-api/src/telemetry.rs:5` `use codex_client::RetryPolicy;`
- `use` `codex-rs/codex-api/src/telemetry.rs:6` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/telemetry.rs:7` `use codex_client::TransportError;`
- `use` `codex-rs/codex-api/src/telemetry.rs:8` `use codex_client::run_with_retry;`
- `use` `codex-rs/codex-api/src/telemetry.rs:9` `use http::StatusCode;`
- `use` `codex-rs/codex-api/src/telemetry.rs:10` `use std::future::Future;`
- `use` `codex-rs/codex-api/src/telemetry.rs:11` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/telemetry.rs:12` `use std::time::Duration;`
- `use` `codex-rs/codex-api/src/telemetry.rs:13` `use tokio::time::Instant;`
- `use` `codex-rs/codex-api/src/telemetry.rs:14` `use tokio_tungstenite::tungstenite::Error;`
- `use` `codex-rs/codex-api/src/telemetry.rs:15` `use tokio_tungstenite::tungstenite::Message;`
- `trait` `codex-rs/codex-api/src/telemetry.rs:18` `pub trait SseTelemetry: Send + Sync {`
- `fn` `codex-rs/codex-api/src/telemetry.rs:19` `fn on_sse_poll(`
- `trait` `codex-rs/codex-api/src/telemetry.rs:35` `pub trait WebsocketTelemetry: Send + Sync {`
- `fn` `codex-rs/codex-api/src/telemetry.rs:36` `fn on_ws_request(&self, duration: Duration, error: Option<&ApiError>);`
- `fn` `codex-rs/codex-api/src/telemetry.rs:38` `fn on_ws_event(`
- `fn` `codex-rs/codex-api/src/telemetry.rs:46` `fn status(&self) -> StatusCode;`
- `fn` `codex-rs/codex-api/src/telemetry.rs:49` `fn http_status(err: &TransportError) -> Option<StatusCode> {`
- `impl` `codex-rs/codex-api/src/telemetry.rs:56` `impl WithStatus for Response {`
- `fn` `codex-rs/codex-api/src/telemetry.rs:57` `fn status(&self) -> StatusCode {`
- `impl` `codex-rs/codex-api/src/telemetry.rs:62` `impl WithStatus for StreamResponse {`
- `fn` `codex-rs/codex-api/src/telemetry.rs:63` `fn status(&self) -> StatusCode {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::ApiError;`
- `use codex_client::Request;`
- `use codex_client::RequestTelemetry;`
- `use codex_client::Response;`
- `use codex_client::RetryPolicy;`
- `use codex_client::StreamResponse;`
- `use codex_client::TransportError;`
- `use codex_client::run_with_retry;`
- `use http::StatusCode;`
- `use std::future::Future;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use tokio::time::Instant;`
- `use tokio_tungstenite::tungstenite::Error;`
- `use tokio_tungstenite::tungstenite::Message;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
