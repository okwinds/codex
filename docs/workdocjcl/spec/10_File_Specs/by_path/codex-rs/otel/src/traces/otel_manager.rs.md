# `codex-rs/otel/src/traces/otel_manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `26658`
- sha256: `0915e322538658aed6db748ec1df1432a05d8a14f18ca0281e6030958824eb63`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/traces/otel_manager.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub fn new(`
- `pub fn apply_traceparent_parent(&self, span: &Span) {`
- `pub fn record_responses(&self, handle_responses_span: &Span, event: &ResponseEvent) {`
- `pub fn conversation_starts(`
- `pub fn record_api_request(`
- `pub fn record_websocket_request(&self, duration: Duration, error: Option<&str>) {`
- `pub fn record_websocket_event(`
- `pub fn sse_event_completed(`
- `pub fn user_prompt(&self, items: &[UserInput]) {`
- `pub fn tool_decision(`
- `pub fn log_tool_failed(&self, tool_name: &str, error: &str) {`
- `pub fn tool_result(`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/traces/otel_manager.rs:1` `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:2` `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:3` `use crate::metrics::names::SSE_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:4` `use crate::metrics::names::SSE_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:5` `use crate::metrics::names::TOOL_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:6` `use crate::metrics::names::TOOL_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:7` `use crate::metrics::names::WEBSOCKET_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:8` `use crate::metrics::names::WEBSOCKET_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:9` `use crate::metrics::names::WEBSOCKET_REQUEST_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:10` `use crate::metrics::names::WEBSOCKET_REQUEST_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:11` `use crate::otel_provider::traceparent_context_from_env;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:12` `use chrono::SecondsFormat;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:13` `use chrono::Utc;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:14` `use codex_api::ApiError;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:15` `use codex_api::ResponseEvent;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:16` `use codex_app_server_protocol::AuthMode;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:17` `use codex_protocol::ThreadId;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:18` `use codex_protocol::config_types::ReasoningSummary;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:19` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:20` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:21` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:22` `use codex_protocol::protocol::ReviewDecision;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:23` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:24` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:25` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:26` `use eventsource_stream::Event as StreamEvent;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:27` `use eventsource_stream::EventStreamError as StreamError;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:28` `use reqwest::Error;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:29` `use reqwest::Response;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:30` `use std::borrow::Cow;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:31` `use std::fmt::Display;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:32` `use std::future::Future;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:33` `use std::time::Duration;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:34` `use std::time::Instant;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:35` `use tokio::time::error::Elapsed;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:36` `use tracing::Span;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:37` `use tracing_opentelemetry::OpenTelemetrySpanExt;`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:43` `const SSE_UNKNOWN_KIND: &str = "unknown";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:44` `const WEBSOCKET_UNKNOWN_KIND: &str = "unknown";`
- `impl` `codex-rs/otel/src/traces/otel_manager.rs:46` `impl OtelManager {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:48` `pub fn new(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:77` `pub fn apply_traceparent_parent(&self, span: &Span) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:83` `pub fn record_responses(&self, handle_responses_span: &Span, event: &ResponseEvent) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:104` `pub fn conversation_starts(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:158` `pub fn record_api_request(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:199` `pub fn record_websocket_request(&self, duration: Duration, error: Option<&str>) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:229` `pub fn record_websocket_event(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:374` `fn sse_event(&self, kind: &str, duration: Duration) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:473` `pub fn sse_event_completed(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:502` `pub fn user_prompt(&self, items: &[UserInput]) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:534` `pub fn tool_decision(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:593` `pub fn log_tool_failed(&self, tool_name: &str, error: &str) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:613` `pub fn tool_result(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:654` `fn responses_type(event: &ResponseEvent) -> String {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:672` `fn responses_item_type(item: &ResponseItem) -> String {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:689` `fn timestamp() -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use crate::metrics::names::SSE_EVENT_COUNT_METRIC;`
- `use crate::metrics::names::SSE_EVENT_DURATION_METRIC;`
- `use crate::metrics::names::TOOL_CALL_COUNT_METRIC;`
- `use crate::metrics::names::TOOL_CALL_DURATION_METRIC;`
- `use crate::metrics::names::WEBSOCKET_EVENT_COUNT_METRIC;`
- `use crate::metrics::names::WEBSOCKET_EVENT_DURATION_METRIC;`
- `use crate::metrics::names::WEBSOCKET_REQUEST_COUNT_METRIC;`
- `use crate::metrics::names::WEBSOCKET_REQUEST_DURATION_METRIC;`
- `use crate::otel_provider::traceparent_context_from_env;`
- `use chrono::SecondsFormat;`
- `use chrono::Utc;`
- `use codex_api::ApiError;`
- `use codex_api::ResponseEvent;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::openai_models::ReasoningEffort;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
