# `codex-rs/codex-api/src/requests/chat.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `18468`
- sha256: `c1467f2d9c0365b357bae48039031da378ad942f5374ac3c9287e25ac690e39a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/requests/chat.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ChatRequest {`
- `pub struct ChatRequestBuilder<'a> {`
- `pub fn new(`
- `pub fn conversation_id(mut self, id: Option<String>) -> Self {`
- `pub fn session_source(mut self, source: Option<SessionSource>) -> Self {`
- `pub fn build(self, _provider: &Provider) -> Result<ChatRequest, ApiError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/requests/chat.rs:1` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:2` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:3` `use crate::requests::headers::build_conversation_headers;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:4` `use crate::requests::headers::insert_header;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:5` `use crate::requests::headers::subagent_header;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:6` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:7` `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:8` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:9` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:10` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:11` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:12` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:13` `use serde_json::json;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:14` `use std::collections::HashMap;`
- `struct` `codex-rs/codex-api/src/requests/chat.rs:17` `pub struct ChatRequest {`
- `struct` `codex-rs/codex-api/src/requests/chat.rs:22` `pub struct ChatRequestBuilder<'a> {`
- `impl` `codex-rs/codex-api/src/requests/chat.rs:31` `impl<'a> ChatRequestBuilder<'a> {`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:32` `pub fn new(`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:48` `pub fn conversation_id(mut self, id: Option<String>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:53` `pub fn session_source(mut self, source: Option<SessionSource>) -> Self {`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:58` `pub fn build(self, _provider: &Provider) -> Result<ChatRequest, ApiError> {`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:313` `fn push_tool_call_message(messages: &mut Vec<Value>, tool_call: Value, reasoning: Option<&str>) {`
- `use` `codex-rs/codex-api/src/requests/chat.rs:353` `use super::*;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:354` `use crate::provider::RetryConfig;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:355` `use crate::provider::WireApi;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:356` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:357` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:358` `use codex_protocol::protocol::SubAgentSource;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:359` `use http::HeaderValue;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:360` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/codex-api/src/requests/chat.rs:361` `use std::time::Duration;`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:363` `fn provider() -> Provider {`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:382` `fn attaches_conversation_and_subagent_headers() {`
- `fn` `codex-rs/codex-api/src/requests/chat.rs:409` `fn groups_consecutive_tool_calls_into_a_single_assistant_message() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::requests::headers::build_conversation_headers;`
- `use crate::requests::headers::insert_header;`
- `use crate::requests::headers::subagent_header;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use codex_protocol::models::ReasoningItemContent;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::SessionSource;`
- `use http::HeaderMap;`
- `use serde_json::Value;`
- `use serde_json::json;`
- `use std::collections::HashMap;`
- `use super::*;`
- `use crate::provider::RetryConfig;`
- `use crate::provider::WireApi;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::protocol::SubAgentSource;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
