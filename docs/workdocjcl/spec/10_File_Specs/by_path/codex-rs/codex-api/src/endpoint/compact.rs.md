# `codex-rs/codex-api/src/endpoint/compact.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2951`
- sha256: `e799d85bac39df82d4025a7a0806b042f8a8a31f1c5042c73533b78bc90947d9`
- generated_utc: `2026-02-08T10:45:16Z`

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
- `pub fn with_telemetry(self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:2` `use crate::common::CompactionInput;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:3` `use crate::endpoint::session::EndpointSession;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:4` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:5` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:6` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:7` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:8` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:9` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:10` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:11` `use serde::Deserialize;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:12` `use serde_json::to_value;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:13` `use std::sync::Arc;`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:15` `pub struct CompactClient<T: HttpTransport, A: AuthProvider> {`
- `impl` `codex-rs/codex-api/src/endpoint/compact.rs:19` `impl<T: HttpTransport, A: AuthProvider> CompactClient<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:20` `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:26` `pub fn with_telemetry(self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:32` `fn path() -> &'static str {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:36` `pub async fn compact(`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:50` `pub async fn compact_input(`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:62` `struct CompactHistoryResponse {`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:68` `use super::*;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:69` `use async_trait::async_trait;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:70` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:71` `use codex_client::Response;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:72` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/endpoint/compact.rs:73` `use codex_client::TransportError;`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:76` `struct DummyTransport;`
- `impl` `codex-rs/codex-api/src/endpoint/compact.rs:79` `impl HttpTransport for DummyTransport {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:80` `async fn execute(&self, _req: Request) -> Result<Response, TransportError> {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:84` `async fn stream(&self, _req: Request) -> Result<StreamResponse, TransportError> {`
- `struct` `codex-rs/codex-api/src/endpoint/compact.rs:90` `struct DummyAuth;`
- `impl` `codex-rs/codex-api/src/endpoint/compact.rs:92` `impl AuthProvider for DummyAuth {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:93` `fn bearer_token(&self) -> Option<String> {`
- `fn` `codex-rs/codex-api/src/endpoint/compact.rs:99` `fn path_is_responses_compact() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::common::CompactionInput;`
- `use crate::endpoint::session::EndpointSession;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use codex_client::HttpTransport;`
- `use codex_client::RequestTelemetry;`
- `use codex_protocol::models::ResponseItem;`
- `use http::HeaderMap;`
- `use http::Method;`
- `use serde::Deserialize;`
- `use serde_json::to_value;`
- `use std::sync::Arc;`
- `use super::*;`
- `use async_trait::async_trait;`
- `use codex_client::Request;`
- `use codex_client::Response;`
- `use codex_client::StreamResponse;`
- `use codex_client::TransportError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
