# `codex-rs/codex-api/src/endpoint/models.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8616`
- sha256: `d2bcb6a7bac5af22bad3ab30b34bbe1043707416e24ef9a0c3a41ca556140221`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/models.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ModelsClient<T: HttpTransport, A: AuthProvider> {`
- `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `pub fn with_telemetry(mut self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/models.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:2` `use crate::auth::add_auth_headers;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:3` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:4` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:5` `use crate::telemetry::run_with_request_telemetry;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:6` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:7` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:8` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:9` `use codex_protocol::openai_models::ModelsResponse;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:10` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:11` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:12` `use http::header::ETAG;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:13` `use std::sync::Arc;`
- `struct` `codex-rs/codex-api/src/endpoint/models.rs:15` `pub struct ModelsClient<T: HttpTransport, A: AuthProvider> {`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:22` `impl<T: HttpTransport, A: AuthProvider> ModelsClient<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:23` `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:32` `pub fn with_telemetry(mut self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:37` `fn path(&self) -> &'static str {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:41` `pub async fn list_models(`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:84` `use super::*;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:85` `use crate::provider::RetryConfig;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:86` `use crate::provider::WireApi;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:87` `use async_trait::async_trait;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:88` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:89` `use codex_client::Response;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:90` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:91` `use codex_client::TransportError;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:92` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:93` `use http::StatusCode;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:94` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:95` `use serde_json::json;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:96` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:97` `use std::sync::Mutex;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:98` `use std::time::Duration;`
- `struct` `codex-rs/codex-api/src/endpoint/models.rs:101` `struct CapturingTransport {`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:107` `impl Default for CapturingTransport {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:108` `fn default() -> Self {`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:118` `impl HttpTransport for CapturingTransport {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:119` `async fn execute(&self, req: Request) -> Result<Response, TransportError> {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:133` `async fn stream(&self, _req: Request) -> Result<StreamResponse, TransportError> {`
- `struct` `codex-rs/codex-api/src/endpoint/models.rs:139` `struct DummyAuth;`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:141` `impl AuthProvider for DummyAuth {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:142` `fn bearer_token(&self) -> Option<String> {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:147` `fn provider(base_url: &str) -> Provider {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:166` `async fn appends_client_version_query() {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:203` `async fn parses_models_response() {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:256` `async fn list_models_includes_etag() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::auth::add_auth_headers;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::telemetry::run_with_request_telemetry;`
- `use codex_client::HttpTransport;`
- `use codex_client::RequestTelemetry;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelsResponse;`
- `use http::HeaderMap;`
- `use http::Method;`
- `use http::header::ETAG;`
- `use std::sync::Arc;`
- `use super::*;`
- `use crate::provider::RetryConfig;`
- `use crate::provider::WireApi;`
- `use async_trait::async_trait;`
- `use codex_client::Request;`
- `use codex_client::Response;`
- `use codex_client::StreamResponse;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
