# `codex-rs/codex-api/src/endpoint/responses.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4644`
- sha256: `3f54c1d718ef446b312e4f4e31b30ca5fae39c3a04f62e5e120230566c8cfbc0`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/responses.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ResponsesClient<T: HttpTransport, A: AuthProvider> {`
- `pub struct ResponsesOptions {`
- `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `pub fn with_telemetry(`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:2` `use crate::common::Prompt as ApiPrompt;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:3` `use crate::common::Reasoning;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:4` `use crate::common::ResponseStream;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:5` `use crate::common::TextControls;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:6` `use crate::endpoint::session::EndpointSession;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:7` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:8` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:9` `use crate::requests::ResponsesRequest;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:10` `use crate::requests::ResponsesRequestBuilder;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:11` `use crate::requests::responses::Compression;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:12` `use crate::sse::spawn_response_stream;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:13` `use crate::telemetry::SseTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:14` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:15` `use codex_client::RequestCompression;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:16` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:17` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:18` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:19` `use http::HeaderValue;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:20` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:21` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:22` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:23` `use std::sync::OnceLock;`
- `use` `codex-rs/codex-api/src/endpoint/responses.rs:24` `use tracing::instrument;`
- `struct` `codex-rs/codex-api/src/endpoint/responses.rs:26` `pub struct ResponsesClient<T: HttpTransport, A: AuthProvider> {`
- `struct` `codex-rs/codex-api/src/endpoint/responses.rs:32` `pub struct ResponsesOptions {`
- `impl` `codex-rs/codex-api/src/endpoint/responses.rs:45` `impl<T: HttpTransport, A: AuthProvider> ResponsesClient<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/responses.rs:46` `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/responses.rs:53` `pub fn with_telemetry(`
- `fn` `codex-rs/codex-api/src/endpoint/responses.rs:64` `pub async fn stream_request(`
- `fn` `codex-rs/codex-api/src/endpoint/responses.rs:79` `pub async fn stream_prompt(`
- `fn` `codex-rs/codex-api/src/endpoint/responses.rs:115` `fn path() -> &'static str {`
- `fn` `codex-rs/codex-api/src/endpoint/responses.rs:119` `pub async fn stream(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::common::Prompt as ApiPrompt;`
- `use crate::common::Reasoning;`
- `use crate::common::ResponseStream;`
- `use crate::common::TextControls;`
- `use crate::endpoint::session::EndpointSession;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::requests::ResponsesRequest;`
- `use crate::requests::ResponsesRequestBuilder;`
- `use crate::requests::responses::Compression;`
- `use crate::sse::spawn_response_stream;`
- `use crate::telemetry::SseTelemetry;`
- `use codex_client::HttpTransport;`
- `use codex_client::RequestCompression;`
- `use codex_client::RequestTelemetry;`
- `use codex_protocol::protocol::SessionSource;`
- `use http::HeaderMap;`
- `use http::HeaderValue;`
- `use http::Method;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
