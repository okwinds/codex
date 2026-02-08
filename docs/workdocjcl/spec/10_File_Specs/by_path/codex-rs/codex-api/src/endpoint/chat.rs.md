# `codex-rs/codex-api/src/endpoint/chat.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10468`
- sha256: `046d5f226a028649259c2430f18c4925dd3dbbc82ae3105a4f34e2237ee13283`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/chat.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ChatClient<T: HttpTransport, A: AuthProvider> {`
- `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `pub fn with_telemetry(`
- `pub enum AggregateMode {`
- `pub struct AggregatedStream {`
- `pub trait AggregateStreamExt {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:1` `use crate::ChatRequest;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:2` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:3` `use crate::common::Prompt as ApiPrompt;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:4` `use crate::common::ResponseEvent;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:5` `use crate::common::ResponseStream;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:6` `use crate::endpoint::streaming::StreamingClient;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:7` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:8` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:9` `use crate::provider::WireApi;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:10` `use crate::sse::chat::spawn_chat_stream;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:11` `use crate::telemetry::SseTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:12` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:13` `use codex_client::RequestCompression;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:14` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:15` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:16` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:17` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:18` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:19` `use futures::Stream;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:20` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:21` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:22` `use std::collections::VecDeque;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:23` `use std::pin::Pin;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:24` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:25` `use std::task::Context;`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:26` `use std::task::Poll;`
- `struct` `codex-rs/codex-api/src/endpoint/chat.rs:28` `pub struct ChatClient<T: HttpTransport, A: AuthProvider> {`
- `impl` `codex-rs/codex-api/src/endpoint/chat.rs:32` `impl<T: HttpTransport, A: AuthProvider> ChatClient<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:33` `pub fn new(transport: T, provider: Provider, auth: A) -> Self {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:39` `pub fn with_telemetry(`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:49` `pub async fn stream_request(&self, request: ChatRequest) -> Result<ResponseStream, ApiError> {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:53` `pub async fn stream_prompt(`
- `use` `codex-rs/codex-api/src/endpoint/chat.rs:60` `use crate::requests::ChatRequestBuilder;`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:71` `fn path(&self) -> &'static str {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:78` `pub async fn stream(`
- `enum` `codex-rs/codex-api/src/endpoint/chat.rs:97` `pub enum AggregateMode {`
- `struct` `codex-rs/codex-api/src/endpoint/chat.rs:103` `pub struct AggregatedStream {`
- `impl` `codex-rs/codex-api/src/endpoint/chat.rs:111` `impl Stream for AggregatedStream {`
- `type` `codex-rs/codex-api/src/endpoint/chat.rs:112` `type Item = Result<ResponseEvent, ApiError>;`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:114` `fn poll_next(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Option<Self::Item>> {`
- `trait` `codex-rs/codex-api/src/endpoint/chat.rs:256` `pub trait AggregateStreamExt {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:257` `fn aggregate(self) -> AggregatedStream;`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:259` `fn streaming_mode(self) -> ResponseStream;`
- `impl` `codex-rs/codex-api/src/endpoint/chat.rs:262` `impl AggregateStreamExt for ResponseStream {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:263` `fn aggregate(self) -> AggregatedStream {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:267` `fn streaming_mode(self) -> ResponseStream {`
- `impl` `codex-rs/codex-api/src/endpoint/chat.rs:272` `impl AggregatedStream {`
- `fn` `codex-rs/codex-api/src/endpoint/chat.rs:273` `fn new(inner: ResponseStream, mode: AggregateMode) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::ChatRequest;`
- `use crate::auth::AuthProvider;`
- `use crate::common::Prompt as ApiPrompt;`
- `use crate::common::ResponseEvent;`
- `use crate::common::ResponseStream;`
- `use crate::endpoint::streaming::StreamingClient;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::provider::WireApi;`
- `use crate::sse::chat::spawn_chat_stream;`
- `use crate::telemetry::SseTelemetry;`
- `use codex_client::HttpTransport;`
- `use codex_client::RequestCompression;`
- `use codex_client::RequestTelemetry;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ReasoningItemContent;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::SessionSource;`
- `use futures::Stream;`
- `use http::HeaderMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
