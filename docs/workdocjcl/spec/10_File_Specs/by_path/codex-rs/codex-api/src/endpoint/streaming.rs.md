# `codex-rs/codex-api/src/endpoint/streaming.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2717`
- sha256: `287201a49b59f57d0638538b1cceacb984adc0b6617300596673efc3aed9c9c0`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/streaming.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:2` `use crate::auth::add_auth_headers;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:3` `use crate::common::ResponseStream;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:4` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:5` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:6` `use crate::telemetry::SseTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:7` `use crate::telemetry::run_with_request_telemetry;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:8` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:9` `use codex_client::RequestCompression;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:10` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:11` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:12` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:13` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:14` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:15` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:16` `use std::sync::OnceLock;`
- `use` `codex-rs/codex-api/src/endpoint/streaming.rs:17` `use std::time::Duration;`
- `type` `codex-rs/codex-api/src/endpoint/streaming.rs:27` `type StreamSpawner = fn(`
- `impl` `codex-rs/codex-api/src/endpoint/streaming.rs:34` `impl<T: HttpTransport, A: AuthProvider> StreamingClient<T, A> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::auth::add_auth_headers;`
- `use crate::common::ResponseStream;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::telemetry::SseTelemetry;`
- `use crate::telemetry::run_with_request_telemetry;`
- `use codex_client::HttpTransport;`
- `use codex_client::RequestCompression;`
- `use codex_client::RequestTelemetry;`
- `use codex_client::StreamResponse;`
- `use http::HeaderMap;`
- `use http::Method;`
- `use serde_json::Value;`
- `use std::sync::Arc;`
- `use std::sync::OnceLock;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
