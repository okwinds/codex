# `codex-rs/codex-api/src/endpoint/memories.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3107`
- sha256: `b0457c3e75574574bf6fe72b74836ad46205a2c9e40621d67d3383a4b3384f09`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/memories.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct MemoriesClient<T: HttpTransport, A: AuthProvider> {`
- `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `pub fn with_telemetry(self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:2` `use crate::common::MemoryTraceSummarizeInput;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:3` `use crate::common::MemoryTraceSummaryOutput;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:4` `use crate::endpoint::session::EndpointSession;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:5` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:6` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:7` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:8` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:9` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:10` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:11` `use serde::Deserialize;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:12` `use serde_json::to_value;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:13` `use std::sync::Arc;`
- `struct` `codex-rs/codex-api/src/endpoint/memories.rs:15` `pub struct MemoriesClient<T: HttpTransport, A: AuthProvider> {`
- `impl` `codex-rs/codex-api/src/endpoint/memories.rs:19` `impl<T: HttpTransport, A: AuthProvider> MemoriesClient<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:20` `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:26` `pub fn with_telemetry(self, request: Option<Arc<dyn RequestTelemetry>>) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:32` `fn path() -> &'static str {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:36` `pub async fn trace_summarize(`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:50` `pub async fn trace_summarize_input(`
- `struct` `codex-rs/codex-api/src/endpoint/memories.rs:65` `struct TraceSummarizeResponse {`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:71` `use super::*;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:72` `use async_trait::async_trait;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:73` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:74` `use codex_client::Response;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:75` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/endpoint/memories.rs:76` `use codex_client::TransportError;`
- `struct` `codex-rs/codex-api/src/endpoint/memories.rs:79` `struct DummyTransport;`
- `impl` `codex-rs/codex-api/src/endpoint/memories.rs:82` `impl HttpTransport for DummyTransport {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:83` `async fn execute(&self, _req: Request) -> Result<Response, TransportError> {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:87` `async fn stream(&self, _req: Request) -> Result<StreamResponse, TransportError> {`
- `struct` `codex-rs/codex-api/src/endpoint/memories.rs:93` `struct DummyAuth;`
- `impl` `codex-rs/codex-api/src/endpoint/memories.rs:95` `impl AuthProvider for DummyAuth {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:96` `fn bearer_token(&self) -> Option<String> {`
- `fn` `codex-rs/codex-api/src/endpoint/memories.rs:102` `fn path_is_memories_trace_summarize() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::common::MemoryTraceSummarizeInput;`
- `use crate::common::MemoryTraceSummaryOutput;`
- `use crate::endpoint::session::EndpointSession;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use codex_client::HttpTransport;`
- `use codex_client::RequestTelemetry;`
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
