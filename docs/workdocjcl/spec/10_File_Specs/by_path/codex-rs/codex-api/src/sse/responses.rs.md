# `codex-rs/codex-api/src/sse/responses.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `31248`
- sha256: `c24a3d885d2ac5df85ae7e15edbe5085322d0089ca44e4ce9cec14b56c03e2fb`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/sse/responses.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn stream_from_fixture(`
- `pub fn spawn_response_stream(`
- `pub struct ResponsesStreamEvent {`
- `pub fn kind(&self) -> &str {`
- `pub enum ResponsesEventError {`
- `pub fn into_api_error(self) -> ApiError {`
- `pub fn process_responses_event(`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/sse/responses.rs:1` `use crate::common::ResponseEvent;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:2` `use crate::common::ResponseStream;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:3` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:4` `use crate::rate_limits::parse_rate_limit;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:5` `use crate::telemetry::SseTelemetry;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:6` `use codex_client::ByteStream;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:7` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:8` `use codex_client::TransportError;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:9` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:10` `use codex_protocol::protocol::TokenUsage;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:11` `use eventsource_stream::Eventsource;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:12` `use futures::StreamExt;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:13` `use futures::TryStreamExt;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:14` `use serde::Deserialize;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:15` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:16` `use std::io::BufRead;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:17` `use std::path::Path;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:18` `use std::sync::Arc;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:19` `use std::sync::OnceLock;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:20` `use std::time::Duration;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:21` `use tokio::sync::mpsc;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:22` `use tokio::time::Instant;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:23` `use tokio::time::timeout;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:24` `use tokio_util::io::ReaderStream;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:25` `use tracing::debug;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:26` `use tracing::trace;`
- `const` `codex-rs/codex-api/src/sse/responses.rs:28` `const X_REASONING_INCLUDED_HEADER: &str = "x-reasoning-included";`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:31` `pub fn stream_from_fixture(`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:51` `pub fn spawn_response_stream(`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:96` `struct Error {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:106` `struct ResponseCompleted {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:113` `struct ResponseDone {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:121` `struct ResponseCompletedUsage {`
- `impl` `codex-rs/codex-api/src/sse/responses.rs:129` `impl From<ResponseCompletedUsage> for TokenUsage {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:130` `fn from(val: ResponseCompletedUsage) -> Self {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:148` `struct ResponseCompletedInputTokensDetails {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:153` `struct ResponseCompletedOutputTokensDetails {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:158` `pub struct ResponsesStreamEvent {`
- `impl` `codex-rs/codex-api/src/sse/responses.rs:168` `impl ResponsesStreamEvent {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:169` `pub fn kind(&self) -> &str {`
- `enum` `codex-rs/codex-api/src/sse/responses.rs:175` `pub enum ResponsesEventError {`
- `impl` `codex-rs/codex-api/src/sse/responses.rs:179` `impl ResponsesEventError {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:180` `pub fn into_api_error(self) -> ApiError {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:187` `pub fn process_responses_event(`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:318` `pub async fn process_sse(`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:383` `fn try_parse_retry_after(err: &Error) -> Option<Duration> {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:409` `fn is_context_window_error(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:413` `fn is_quota_exceeded_error(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:417` `fn is_usage_not_included(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:421` `fn is_invalid_prompt_error(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:425` `fn rate_limit_regex() -> &'static regex_lite::Regex {`
- `static` `codex-rs/codex-api/src/sse/responses.rs:426` `static RE: std::sync::OnceLock<regex_lite::Regex> = std::sync::OnceLock::new();`
- `use` `codex-rs/codex-api/src/sse/responses.rs:435` `use super::*;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:436` `use assert_matches::assert_matches;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:437` `use bytes::Bytes;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:438` `use codex_protocol::models::MessagePhase;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:439` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:440` `use futures::stream;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:441` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:442` `use serde_json::json;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:443` `use tokio::sync::mpsc;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:444` `use tokio_test::io::Builder as IoBuilder;`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:446` `async fn collect_events(chunks: &[&[u8]]) -> Vec<Result<ResponseEvent, ApiError>> {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:465` `async fn run_sse(events: Vec<serde_json::Value>) -> Vec<ResponseEvent> {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:491` `fn idle_timeout() -> Duration {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:496` `async fn parses_items_and_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:560` `async fn error_when_missing_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:588` `async fn response_done_emits_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:622` `async fn response_done_without_payload_emits_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:647` `async fn emits_completed_without_stream_end() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:685` `async fn error_when_error_event() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:707` `async fn context_window_error_is_fatal() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:720` `async fn context_window_error_with_newline_is_fatal() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:733` `async fn quota_exceeded_error_is_fatal() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:746` `async fn invalid_prompt_without_type_is_invalid_request() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:767` `async fn table_driven_event_kinds() {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:768` `struct TestCase {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:775` `fn is_created(ev: &ResponseEvent) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:778` `fn is_output(ev: &ResponseEvent) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:781` `fn is_completed(ev: &ResponseEvent) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:845` `fn test_try_parse_retry_after() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:859` `fn test_try_parse_retry_after_no_delay() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:872` `fn test_try_parse_retry_after_azure() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::common::ResponseEvent;`
- `use crate::common::ResponseStream;`
- `use crate::error::ApiError;`
- `use crate::rate_limits::parse_rate_limit;`
- `use crate::telemetry::SseTelemetry;`
- `use codex_client::ByteStream;`
- `use codex_client::StreamResponse;`
- `use codex_client::TransportError;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::TokenUsage;`
- `use eventsource_stream::Eventsource;`
- `use futures::StreamExt;`
- `use futures::TryStreamExt;`
- `use serde::Deserialize;`
- `use serde_json::Value;`
- `use std::io::BufRead;`
- `use std::path::Path;`
- `use std::sync::Arc;`
- `use std::sync::OnceLock;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
