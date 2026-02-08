# `codex-rs/codex-api/src/endpoint/models.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8299`
- sha256: `e47fa5fe2a29cc219a80a33753e1620beb509043750a78a181cd51da265d5fb0`
- generated_utc: `2026-02-08T10:45:16Z`

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
- `pub fn with_telemetry(self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/models.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:2` `use crate::endpoint::session::EndpointSession;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:3` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:4` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:5` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:6` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:7` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:8` `use codex_protocol::openai_models::ModelsResponse;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:9` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:10` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:11` `use http::header::ETAG;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:12` `use std::sync::Arc;`
- `struct` `codex-rs/codex-api/src/endpoint/models.rs:14` `pub struct ModelsClient<T: HttpTransport, A: AuthProvider> {`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:18` `impl<T: HttpTransport, A: AuthProvider> ModelsClient<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:19` `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:25` `pub fn with_telemetry(self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:31` `fn path() -> &'static str {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:35` `fn append_client_version_query(req: &mut codex_client::Request, client_version: &str) {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:40` `pub async fn list_models(`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:72` `use super::*;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:73` `use crate::provider::RetryConfig;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:74` `use async_trait::async_trait;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:75` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:76` `use codex_client::Response;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:77` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:78` `use codex_client::TransportError;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:79` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:80` `use http::StatusCode;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:81` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:82` `use serde_json::json;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:83` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:84` `use std::sync::Mutex;`
- `use` `codex-rs/codex-api/src/endpoint/models.rs:85` `use std::time::Duration;`
- `struct` `codex-rs/codex-api/src/endpoint/models.rs:88` `struct CapturingTransport {`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:94` `impl Default for CapturingTransport {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:95` `fn default() -> Self {`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:105` `impl HttpTransport for CapturingTransport {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:106` `async fn execute(&self, req: Request) -> Result<Response, TransportError> {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:120` `async fn stream(&self, _req: Request) -> Result<StreamResponse, TransportError> {`
- `struct` `codex-rs/codex-api/src/endpoint/models.rs:126` `struct DummyAuth;`
- `impl` `codex-rs/codex-api/src/endpoint/models.rs:128` `impl AuthProvider for DummyAuth {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:129` `fn bearer_token(&self) -> Option<String> {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:134` `fn provider(base_url: &str) -> Provider {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:152` `async fn appends_client_version_query() {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:189` `async fn parses_models_response() {`
- `fn` `codex-rs/codex-api/src/endpoint/models.rs:242` `async fn list_models_includes_etag() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::endpoint::session::EndpointSession;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
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
- `use async_trait::async_trait;`
- `use codex_client::Request;`
- `use codex_client::Response;`
- `use codex_client::StreamResponse;`
- `use codex_client::TransportError;`
- `use http::HeaderMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
