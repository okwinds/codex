# `codex-rs/codex-api/src/endpoint/compact.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4889`
- sha256: `0056800177688b001d8fc9b00c3a1ab206ab1d44e09bec311fe2fbab341790a7`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/compact.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CompactClient<T: HttpTransport, A: AuthProvider> {`
- `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `pub fn with_telemetry(mut self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:2` `use crate::auth::add_auth_headers;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:3` `use crate::common::CompactionInput;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:4` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:5` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:6` `use crate::provider::WireApi;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:7` `use crate::telemetry::run_with_request_telemetry;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:8` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:9` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:10` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:11` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:12` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:13` `use serde::Deserialize;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:14` `use serde_json::to_value;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:15` `use std::sync::Arc;`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:17` `pub struct CompactClient<T: HttpTransport, A: AuthProvider> {`
- `impl` `codex-rs/codex-api/src/endpoint/compact.rs:24` `impl<T: HttpTransport, A: AuthProvider> CompactClient<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:25` `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:34` `pub fn with_telemetry(mut self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:39` `fn path(&self) -> Result<&'static str, ApiError> {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:48` `pub async fn compact(`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:73` `pub async fn compact_input(`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:85` `struct CompactHistoryResponse {`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:91` `use super::*;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:92` `use crate::provider::RetryConfig;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:93` `use async_trait::async_trait;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:94` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:95` `use codex_client::Response;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:96` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:97` `use codex_client::TransportError;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:98` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:99` `use std::time::Duration;`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:102` `struct DummyTransport;`
- `impl` `codex-rs/codex-api/src/endpoint/compact.rs:105` `impl HttpTransport for DummyTransport {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:106` `async fn execute(&self, _req: Request) -> Result<Response, TransportError> {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:110` `async fn stream(&self, _req: Request) -> Result<StreamResponse, TransportError> {`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:116` `struct DummyAuth;`
- `impl` `codex-rs/codex-api/src/endpoint/compact.rs:118` `impl AuthProvider for DummyAuth {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:119` `fn bearer_token(&self) -> Option<String> {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:124` `fn provider(wire: WireApi) -> Provider {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:143` `async fn errors_when_wire_is_chat() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::auth::add_auth_headers;`
- `use crate::common::CompactionInput;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::provider::WireApi;`
- `use crate::telemetry::run_with_request_telemetry;`
- `use codex_client::HttpTransport;`
- `use codex_client::RequestTelemetry;`
- `use codex_protocol::models::ResponseItem;`
- `use http::HeaderMap;`
- `use http::Method;`
- `use serde::Deserialize;`
- `use serde_json::to_value;`
- `use std::sync::Arc;`
- `use super::*;`
- `use crate::provider::RetryConfig;`
- `use async_trait::async_trait;`
- `use codex_client::Request;`
- `use codex_client::Response;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
