# `codex-rs/otel/src/traces/otel_manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `31567`
- sha256: `5d0f506e22e756c85a4dfb8e5fc7059a323fa1401f29eff48fe5246fe1c8ec48`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `pub fn tool_result_with_tags(`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/traces/otel_manager.rs:1` `use crate::TelemetryAuthMode;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:2` `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:3` `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:4` `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TBT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:5` `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TTFT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:6` `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TBT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:7` `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TTFT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:8` `use crate::metrics::names::RESPONSES_API_INFERENCE_TIME_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:9` `use crate::metrics::names::RESPONSES_API_OVERHEAD_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:10` `use crate::metrics::names::SSE_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:11` `use crate::metrics::names::SSE_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:12` `use crate::metrics::names::TOOL_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:13` `use crate::metrics::names::TOOL_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:14` `use crate::metrics::names::WEBSOCKET_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:15` `use crate::metrics::names::WEBSOCKET_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:16` `use crate::metrics::names::WEBSOCKET_REQUEST_COUNT_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:17` `use crate::metrics::names::WEBSOCKET_REQUEST_DURATION_METRIC;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:18` `use crate::otel_provider::traceparent_context_from_env;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:19` `use chrono::SecondsFormat;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:20` `use chrono::Utc;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:21` `use codex_api::ApiError;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:22` `use codex_api::ResponseEvent;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:23` `use codex_protocol::ThreadId;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:24` `use codex_protocol::config_types::ReasoningSummary;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:25` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:26` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:27` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:28` `use codex_protocol::protocol::ReviewDecision;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:29` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:30` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:31` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:32` `use eventsource_stream::Event as StreamEvent;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:33` `use eventsource_stream::EventStreamError as StreamError;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:34` `use reqwest::Error;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:35` `use reqwest::Response;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:36` `use std::borrow::Cow;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:37` `use std::fmt::Display;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:38` `use std::future::Future;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:39` `use std::time::Duration;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:40` `use std::time::Instant;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:41` `use tokio::time::error::Elapsed;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:42` `use tracing::Span;`
- `use` `codex-rs/otel/src/traces/otel_manager.rs:43` `use tracing_opentelemetry::OpenTelemetrySpanExt;`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:49` `const SSE_UNKNOWN_KIND: &str = "unknown";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:50` `const WEBSOCKET_UNKNOWN_KIND: &str = "unknown";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:51` `const RESPONSES_WEBSOCKET_TIMING_KIND: &str = "responsesapi.websocket_timing";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:52` `const RESPONSES_WEBSOCKET_TIMING_METRICS_FIELD: &str = "timing_metrics";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:53` `const RESPONSES_API_OVERHEAD_FIELD: &str = "responses_duration_excl_engine_and_client_tool_time_ms";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:54` `const RESPONSES_API_INFERENCE_FIELD: &str = "engine_service_total_ms";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:55` `const RESPONSES_API_ENGINE_IAPI_TTFT_FIELD: &str = "engine_iapi_ttft_total_ms";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:56` `const RESPONSES_API_ENGINE_SERVICE_TTFT_FIELD: &str = "engine_service_ttft_total_ms";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:57` `const RESPONSES_API_ENGINE_IAPI_TBT_FIELD: &str = "engine_iapi_tbt_across_engine_calls_ms";`
- `const` `codex-rs/otel/src/traces/otel_manager.rs:58` `const RESPONSES_API_ENGINE_SERVICE_TBT_FIELD: &str = "engine_service_tbt_across_engine_calls_ms";`
- `impl` `codex-rs/otel/src/traces/otel_manager.rs:60` `impl OtelManager {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:62` `pub fn new(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:93` `pub fn apply_traceparent_parent(&self, span: &Span) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:99` `pub fn record_responses(&self, handle_responses_span: &Span, event: &ResponseEvent) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:120` `pub fn conversation_starts(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:175` `pub fn record_api_request(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:217` `pub fn record_websocket_request(&self, duration: Duration, error: Option<&str>) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:248` `pub fn record_websocket_event(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:397` `fn sse_event(&self, kind: &str, duration: Duration) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:500` `pub fn sse_event_completed(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:530` `pub fn user_prompt(&self, items: &[UserInput]) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:563` `pub fn tool_decision(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:625` `pub fn log_tool_failed(&self, tool_name: &str, error: &str) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:647` `pub fn tool_result_with_tags(`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:686` `fn record_responses_websocket_timing_metrics(&self, value: &serde_json::Value) {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:738` `fn responses_type(event: &ResponseEvent) -> String {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:756` `fn responses_item_type(item: &ResponseItem) -> String {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:773` `fn timestamp() -> String {`
- `fn` `codex-rs/otel/src/traces/otel_manager.rs:777` `fn duration_from_ms_value(value: Option<&serde_json::Value>) -> Option<Duration> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::TelemetryAuthMode;`
- `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TBT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TTFT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TBT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TTFT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_INFERENCE_TIME_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_OVERHEAD_DURATION_METRIC;`
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
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
