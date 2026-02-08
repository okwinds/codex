# `codex-rs/codex-api/src/requests/responses.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8092`
- sha256: `91f4506900aa0d61da6221f2da49a727afb8d5dfd1df567a7511b82910e91475`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/requests/responses.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum Compression {`
- `pub struct ResponsesRequest {`
- `pub struct ResponsesRequestBuilder<'a> {`
- `pub fn new(model: &'a str, instructions: &'a str, input: &'a [ResponseItem]) -> Self {`
- `pub fn tools(mut self, tools: &'a [Value]) -> Self {`
- `pub fn parallel_tool_calls(mut self, enabled: bool) -> Self {`
- `pub fn reasoning(mut self, reasoning: Option<Reasoning>) -> Self {`
- `pub fn include(mut self, include: Vec<String>) -> Self {`
- `pub fn prompt_cache_key(mut self, key: Option<String>) -> Self {`
- `pub fn text(mut self, text: Option<TextControls>) -> Self {`
- `pub fn conversation(mut self, conversation_id: Option<String>) -> Self {`
- `pub fn session_source(mut self, source: Option<SessionSource>) -> Self {`
- `pub fn store_override(mut self, store: Option<bool>) -> Self {`
- `pub fn extra_headers(mut self, headers: HeaderMap) -> Self {`
- `pub fn compression(mut self, compression: Compression) -> Self {`
- `pub fn build(self, provider: &Provider) -> Result<ResponsesRequest, ApiError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/requests/responses.rs:1` `use crate::common::Reasoning;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:2` `use crate::common::ResponsesApiRequest;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:3` `use crate::common::TextControls;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:4` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:5` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:6` `use crate::requests::headers::build_conversation_headers;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:7` `use crate::requests::headers::insert_header;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:8` `use crate::requests::headers::subagent_header;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:9` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:10` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:11` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:12` `use serde_json::Value;`
- `enum` `codex-rs/codex-api/src/requests/responses.rs:15` `pub enum Compression {`
- `struct` `codex-rs/codex-api/src/requests/responses.rs:22` `pub struct ResponsesRequest {`
- `struct` `codex-rs/codex-api/src/requests/responses.rs:29` `pub struct ResponsesRequestBuilder<'a> {`
- `impl` `codex-rs/codex-api/src/requests/responses.rs:46` `impl<'a> ResponsesRequestBuilder<'a> {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:47` `pub fn new(model: &'a str, instructions: &'a str, input: &'a [ResponseItem]) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:56` `pub fn tools(mut self, tools: &'a [Value]) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:61` `pub fn parallel_tool_calls(mut self, enabled: bool) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:66` `pub fn reasoning(mut self, reasoning: Option<Reasoning>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:71` `pub fn include(mut self, include: Vec<String>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:76` `pub fn prompt_cache_key(mut self, key: Option<String>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:81` `pub fn text(mut self, text: Option<TextControls>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:86` `pub fn conversation(mut self, conversation_id: Option<String>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:91` `pub fn session_source(mut self, source: Option<SessionSource>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:96` `pub fn store_override(mut self, store: Option<bool>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:101` `pub fn extra_headers(mut self, headers: HeaderMap) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:106` `pub fn compression(mut self, compression: Compression) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:111` `pub fn build(self, provider: &Provider) -> Result<ResponsesRequest, ApiError> {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:163` `fn attach_item_ids(payload_json: &mut Value, original_items: &[ResponseItem]) {`
- `use` `codex-rs/codex-api/src/requests/responses.rs:192` `use super::*;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:193` `use crate::provider::RetryConfig;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:194` `use crate::provider::WireApi;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:195` `use codex_protocol::protocol::SubAgentSource;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:196` `use http::HeaderValue;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:197` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/codex-api/src/requests/responses.rs:198` `use std::time::Duration;`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:200` `fn provider(name: &str, base_url: &str) -> Provider {`
- `fn` `codex-rs/codex-api/src/requests/responses.rs:219` `fn azure_default_store_attaches_ids_and_headers() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::common::Reasoning;`
- `use crate::common::ResponsesApiRequest;`
- `use crate::common::TextControls;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::requests::headers::build_conversation_headers;`
- `use crate::requests::headers::insert_header;`
- `use crate::requests::headers::subagent_header;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::SessionSource;`
- `use http::HeaderMap;`
- `use serde_json::Value;`
- `use super::*;`
- `use crate::provider::RetryConfig;`
- `use crate::provider::WireApi;`
- `use codex_protocol::protocol::SubAgentSource;`
- `use http::HeaderValue;`
- `use pretty_assertions::assert_eq;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
