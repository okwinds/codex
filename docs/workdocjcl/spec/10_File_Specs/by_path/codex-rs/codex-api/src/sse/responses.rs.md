# `codex-rs/codex-api/src/sse/responses.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `31159`
- sha256: `1aaff9dea2c84707a77d9b83030bdafce00fb0742597de3610d6d750a5510ffe`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `enum` `codex-rs/codex-api/src/sse/responses.rs:169` `pub enum ResponsesEventError {`
- `impl` `codex-rs/codex-api/src/sse/responses.rs:173` `impl ResponsesEventError {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:174` `pub fn into_api_error(self) -> ApiError {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:181` `pub fn process_responses_event(`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:312` `pub async fn process_sse(`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:377` `fn try_parse_retry_after(err: &Error) -> Option<Duration> {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:403` `fn is_context_window_error(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:407` `fn is_quota_exceeded_error(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:411` `fn is_usage_not_included(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:415` `fn is_invalid_prompt_error(error: &Error) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:419` `fn rate_limit_regex() -> &'static regex_lite::Regex {`
- `static` `codex-rs/codex-api/src/sse/responses.rs:420` `static RE: std::sync::OnceLock<regex_lite::Regex> = std::sync::OnceLock::new();`
- `use` `codex-rs/codex-api/src/sse/responses.rs:429` `use super::*;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:430` `use assert_matches::assert_matches;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:431` `use bytes::Bytes;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:432` `use codex_protocol::models::MessagePhase;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:433` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:434` `use futures::stream;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:435` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:436` `use serde_json::json;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:437` `use tokio::sync::mpsc;`
- `use` `codex-rs/codex-api/src/sse/responses.rs:438` `use tokio_test::io::Builder as IoBuilder;`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:440` `async fn collect_events(chunks: &[&[u8]]) -> Vec<Result<ResponseEvent, ApiError>> {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:459` `async fn run_sse(events: Vec<serde_json::Value>) -> Vec<ResponseEvent> {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:485` `fn idle_timeout() -> Duration {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:490` `async fn parses_items_and_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:554` `async fn error_when_missing_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:582` `async fn response_done_emits_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:616` `async fn response_done_without_payload_emits_completed() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:641` `async fn emits_completed_without_stream_end() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:679` `async fn error_when_error_event() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:701` `async fn context_window_error_is_fatal() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:714` `async fn context_window_error_with_newline_is_fatal() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:727` `async fn quota_exceeded_error_is_fatal() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:740` `async fn invalid_prompt_without_type_is_invalid_request() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:761` `async fn table_driven_event_kinds() {`
- `struct` `codex-rs/codex-api/src/sse/responses.rs:762` `struct TestCase {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:769` `fn is_created(ev: &ResponseEvent) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:772` `fn is_output(ev: &ResponseEvent) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:775` `fn is_completed(ev: &ResponseEvent) -> bool {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:839` `fn test_try_parse_retry_after() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:853` `fn test_try_parse_retry_after_no_delay() {`
- `fn` `codex-rs/codex-api/src/sse/responses.rs:866` `fn test_try_parse_retry_after_azure() {`

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
