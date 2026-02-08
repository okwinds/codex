# `codex-rs/core/src/client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `50051`
- sha256: `c5b80a67d68d429befb27c97a21c866a829229b2c8a94040e1d5cd0b9ee84032`
- generated_utc: `2026-02-08T10:45:26Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/client.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses

## Public Surface (auto)
- `pub struct ModelClient {`
- `pub struct ModelClientSession {`
- `pub fn new(`
- `pub fn new_session(&self) -> ModelClientSession {`
- `pub fn pre_establish_connection(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/client.rs:30` `use std::sync::Arc;`
- `use` `codex-rs/core/src/client.rs:31` `use std::sync::Mutex;`
- `use` `codex-rs/core/src/client.rs:32` `use std::sync::OnceLock;`
- `use` `codex-rs/core/src/client.rs:33` `use std::sync::atomic::AtomicBool;`
- `use` `codex-rs/core/src/client.rs:34` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/core/src/client.rs:36` `use crate::api_bridge::CoreAuthProvider;`
- `use` `codex-rs/core/src/client.rs:37` `use crate::api_bridge::auth_provider_from_auth;`
- `use` `codex-rs/core/src/client.rs:38` `use crate::api_bridge::map_api_error;`
- `use` `codex-rs/core/src/client.rs:39` `use crate::auth::UnauthorizedRecovery;`
- `use` `codex-rs/core/src/client.rs:40` `use codex_api::CompactClient as ApiCompactClient;`
- `use` `codex-rs/core/src/client.rs:41` `use codex_api::CompactionInput as ApiCompactionInput;`
- `use` `codex-rs/core/src/client.rs:42` `use codex_api::MemoriesClient as ApiMemoriesClient;`
- `use` `codex-rs/core/src/client.rs:43` `use codex_api::MemoryTrace as ApiMemoryTrace;`
- `use` `codex-rs/core/src/client.rs:44` `use codex_api::MemoryTraceSummarizeInput as ApiMemoryTraceSummarizeInput;`
- `use` `codex-rs/core/src/client.rs:45` `use codex_api::MemoryTraceSummaryOutput as ApiMemoryTraceSummaryOutput;`
- `use` `codex-rs/core/src/client.rs:46` `use codex_api::Prompt as ApiPrompt;`
- `use` `codex-rs/core/src/client.rs:47` `use codex_api::RequestTelemetry;`
- `use` `codex-rs/core/src/client.rs:48` `use codex_api::ReqwestTransport;`
- `use` `codex-rs/core/src/client.rs:49` `use codex_api::ResponseAppendWsRequest;`
- `use` `codex-rs/core/src/client.rs:50` `use codex_api::ResponseCreateWsRequest;`
- `use` `codex-rs/core/src/client.rs:51` `use codex_api::ResponsesClient as ApiResponsesClient;`
- `use` `codex-rs/core/src/client.rs:52` `use codex_api::ResponsesOptions as ApiResponsesOptions;`
- `use` `codex-rs/core/src/client.rs:53` `use codex_api::ResponsesWebsocketClient as ApiWebSocketResponsesClient;`
- `use` `codex-rs/core/src/client.rs:54` `use codex_api::ResponsesWebsocketConnection as ApiWebSocketConnection;`
- `use` `codex-rs/core/src/client.rs:55` `use codex_api::SseTelemetry;`
- `use` `codex-rs/core/src/client.rs:56` `use codex_api::TransportError;`
- `use` `codex-rs/core/src/client.rs:57` `use codex_api::WebsocketTelemetry;`
- `use` `codex-rs/core/src/client.rs:58` `use codex_api::build_conversation_headers;`
- `use` `codex-rs/core/src/client.rs:59` `use codex_api::common::Reasoning;`
- `use` `codex-rs/core/src/client.rs:60` `use codex_api::common::ResponsesWsRequest;`
- `use` `codex-rs/core/src/client.rs:61` `use codex_api::create_text_param_for_request;`
- `use` `codex-rs/core/src/client.rs:62` `use codex_api::error::ApiError;`
- `use` `codex-rs/core/src/client.rs:63` `use codex_api::requests::responses::Compression;`
- `use` `codex-rs/core/src/client.rs:64` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/client.rs:66` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/client.rs:67` `use codex_protocol::config_types::ReasoningSummary as ReasoningSummaryConfig;`
- `use` `codex-rs/core/src/client.rs:68` `use codex_protocol::config_types::Verbosity as VerbosityConfig;`
- `use` `codex-rs/core/src/client.rs:69` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/client.rs:70` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/client.rs:71` `use codex_protocol::openai_models::ReasoningEffort as ReasoningEffortConfig;`
- `use` `codex-rs/core/src/client.rs:72` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/client.rs:73` `use eventsource_stream::Event;`
- `use` `codex-rs/core/src/client.rs:74` `use eventsource_stream::EventStreamError;`
- `use` `codex-rs/core/src/client.rs:75` `use futures::StreamExt;`
- `use` `codex-rs/core/src/client.rs:76` `use futures::future::BoxFuture;`
- `use` `codex-rs/core/src/client.rs:77` `use http::HeaderMap as ApiHeaderMap;`
- `use` `codex-rs/core/src/client.rs:78` `use http::HeaderValue;`
- `use` `codex-rs/core/src/client.rs:79` `use http::StatusCode as HttpStatusCode;`
- `use` `codex-rs/core/src/client.rs:80` `use reqwest::StatusCode;`
- `use` `codex-rs/core/src/client.rs:81` `use serde_json::Value;`
- `use` `codex-rs/core/src/client.rs:82` `use std::time::Duration;`
- `use` `codex-rs/core/src/client.rs:83` `use tokio::sync::mpsc;`
- `use` `codex-rs/core/src/client.rs:84` `use tokio::sync::oneshot;`
- `use` `codex-rs/core/src/client.rs:85` `use tokio::sync::oneshot::error::TryRecvError;`
- `use` `codex-rs/core/src/client.rs:86` `use tokio::task::JoinHandle;`
- `use` `codex-rs/core/src/client.rs:87` `use tokio_tungstenite::tungstenite::Error;`
- `use` `codex-rs/core/src/client.rs:88` `use tokio_tungstenite::tungstenite::Message;`
- `use` `codex-rs/core/src/client.rs:89` `use tracing::warn;`
- `use` `codex-rs/core/src/client.rs:91` `use crate::AuthManager;`
- `use` `codex-rs/core/src/client.rs:92` `use crate::auth::CodexAuth;`
- `use` `codex-rs/core/src/client.rs:93` `use crate::auth::RefreshTokenError;`
- `use` `codex-rs/core/src/client.rs:94` `use crate::client_common::Prompt;`
- `use` `codex-rs/core/src/client.rs:95` `use crate::client_common::ResponseEvent;`
- `use` `codex-rs/core/src/client.rs:96` `use crate::client_common::ResponseStream;`
- `use` `codex-rs/core/src/client.rs:97` `use crate::default_client::build_reqwest_client;`
- `use` `codex-rs/core/src/client.rs:98` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/client.rs:99` `use crate::error::Result;`
- `use` `codex-rs/core/src/client.rs:100` `use crate::flags::CODEX_RS_SSE_FIXTURE;`
- `use` `codex-rs/core/src/client.rs:101` `use crate::model_provider_info::ModelProviderInfo;`
- `use` `codex-rs/core/src/client.rs:102` `use crate::model_provider_info::WireApi;`
- `use` `codex-rs/core/src/client.rs:103` `use crate::tools::spec::create_tools_json_for_responses_api;`
- `const` `codex-rs/core/src/client.rs:105` `pub const OPENAI_BETA_HEADER: &str = "OpenAI-Beta";`
- `const` `codex-rs/core/src/client.rs:106` `pub const OPENAI_BETA_RESPONSES_WEBSOCKETS: &str = "responses_websockets=2026-02-04";`
- `const` `codex-rs/core/src/client.rs:107` `pub const X_CODEX_TURN_STATE_HEADER: &str = "x-codex-turn-state";`
- `const` `codex-rs/core/src/client.rs:108` `pub const X_CODEX_TURN_METADATA_HEADER: &str = "x-codex-turn-metadata";`
- `const` `codex-rs/core/src/client.rs:109` `pub const X_RESPONSESAPI_INCLUDE_TIMING_METRICS_HEADER: &str =`
- `const` `codex-rs/core/src/client.rs:111` `const RESPONSES_WEBSOCKETS_V2_BETA_HEADER_VALUE: &str = "responses_websockets=2026-02-06";`
- `struct` `codex-rs/core/src/client.rs:113` `struct PreconnectedWebSocket {`
- `type` `codex-rs/core/src/client.rs:118` `type PreconnectTask = JoinHandle<Option<PreconnectedWebSocket>>;`
- `struct` `codex-rs/core/src/client.rs:123` `struct ModelClientState {`
- `impl` `codex-rs/core/src/client.rs:139` `impl std::fmt::Debug for ModelClientState {`
- `fn` `codex-rs/core/src/client.rs:140` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/client.rs:170` `struct CurrentClientSetup {`
- `struct` `codex-rs/core/src/client.rs:189` `pub struct ModelClient {`
- `struct` `codex-rs/core/src/client.rs:209` `pub struct ModelClientSession {`
- `enum` `codex-rs/core/src/client.rs:228` `enum WebsocketStreamOutcome {`
- `impl` `codex-rs/core/src/client.rs:233` `impl ModelClient {`
- `fn` `codex-rs/core/src/client.rs:239` `pub fn new(`
- `fn` `codex-rs/core/src/client.rs:274` `pub fn new_session(&self) -> ModelClientSession {`
- `fn` `codex-rs/core/src/client.rs:291` `pub fn pre_establish_connection(`
- `fn` `codex-rs/core/src/client.rs:321` `async fn preconnect(`
- `fn` `codex-rs/core/src/client.rs:365` `pub async fn compact_conversation_history(`
- `fn` `codex-rs/core/src/client.rs:401` `pub async fn summarize_memory_traces(`
- `fn` `codex-rs/core/src/client.rs:434` `fn build_subagent_headers(&self) -> ApiHeaderMap {`
- `fn` `codex-rs/core/src/client.rs:451` `fn build_request_telemetry(otel_manager: &OtelManager) -> Arc<dyn RequestTelemetry> {`
- `fn` `codex-rs/core/src/client.rs:461` `fn responses_websocket_enabled(&self) -> bool {`
- `fn` `codex-rs/core/src/client.rs:465` `fn responses_websockets_v2_enabled(&self) -> bool {`
- `fn` `codex-rs/core/src/client.rs:472` `fn disable_websockets(&self) -> bool {`
- `fn` `codex-rs/core/src/client.rs:480` `async fn current_client_setup(&self) -> Result<CurrentClientSetup> {`
- `fn` `codex-rs/core/src/client.rs:501` `async fn connect_websocket(`
- `fn` `codex-rs/core/src/client.rs:520` `fn build_websocket_headers(`
- `fn` `codex-rs/core/src/client.rs:553` `fn take_preconnected_task(&self) -> Option<PreconnectTask> {`
- `fn` `codex-rs/core/src/client.rs:562` `fn set_preconnected_task(&self, task: Option<PreconnectTask>) {`
- `impl` `codex-rs/core/src/client.rs:575` `impl ModelClientSession {`
- `fn` `codex-rs/core/src/client.rs:576` `fn activate_http_fallback(&self, websocket_enabled: bool) -> bool {`
- `fn` `codex-rs/core/src/client.rs:585` `fn build_responses_request(prompt: &Prompt) -> Result<ApiPrompt> {`
- `fn` `codex-rs/core/src/client.rs:596` `fn build_responses_options(`
- `fn` `codex-rs/core/src/client.rs:663` `fn get_incremental_items(&self, input_items: &[ResponseItem]) -> Option<Vec<ResponseItem>> {`
- `fn` `codex-rs/core/src/client.rs:678` `fn refresh_websocket_last_response_id(&mut self) {`
- `fn` `codex-rs/core/src/client.rs:694` `fn websocket_previous_response_id(&mut self) -> Option<String> {`
- `fn` `codex-rs/core/src/client.rs:701` `fn prepare_websocket_create_request(`
- `fn` `codex-rs/core/src/client.rs:738` `fn prepare_websocket_request(`
- `fn` `codex-rs/core/src/client.rs:782` `async fn websocket_connection(`
- `fn` `codex-rs/core/src/client.rs:842` `fn responses_request_compression(&self, auth: Option<&crate::auth::CodexAuth>) -> Compression {`
- `fn` `codex-rs/core/src/client.rs:858` `async fn stream_responses_api(`
- `fn` `codex-rs/core/src/client.rs:926` `async fn stream_responses_websocket(`
- `fn` `codex-rs/core/src/client.rs:1013` `fn build_streaming_telemetry(`
- `fn` `codex-rs/core/src/client.rs:1023` `fn build_websocket_telemetry(otel_manager: &OtelManager) -> Arc<dyn WebsocketTelemetry> {`
- `fn` `codex-rs/core/src/client.rs:1036` `pub async fn stream(`
- `fn` `codex-rs/core/src/client.rs:1110` `fn build_api_prompt(prompt: &Prompt, instructions: String, tools_json: Vec<Value>) -> ApiPrompt {`
- `fn` `codex-rs/core/src/client.rs:1124` `fn parse_turn_metadata_header(turn_metadata_header: Option<&str>) -> Option<HeaderValue> {`
- `fn` `codex-rs/core/src/client.rs:1135` `fn build_responses_headers(`
- `fn` `codex-rs/core/src/client.rs:1223` `async fn handle_unauthorized(`
- `struct` `codex-rs/core/src/client.rs:1240` `struct ApiTelemetry {`
- `impl` `codex-rs/core/src/client.rs:1244` `impl ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:1245` `fn new(otel_manager: OtelManager) -> Self {`
- `impl` `codex-rs/core/src/client.rs:1250` `impl RequestTelemetry for ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:1251` `fn on_request(`
- `impl` `codex-rs/core/src/client.rs:1268` `impl SseTelemetry for ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:1269` `fn on_sse_poll(`
- `impl` `codex-rs/core/src/client.rs:1281` `impl WebsocketTelemetry for ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:1282` `fn on_ws_request(&self, duration: Duration, error: Option<&ApiError>) {`
- `fn` `codex-rs/core/src/client.rs:1288` `fn on_ws_event(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use std::sync::OnceLock;`
- `use std::sync::atomic::AtomicBool;`
- `use std::sync::atomic::Ordering;`
- `use crate::api_bridge::CoreAuthProvider;`
- `use crate::api_bridge::auth_provider_from_auth;`
- `use crate::api_bridge::map_api_error;`
- `use crate::auth::UnauthorizedRecovery;`
- `use codex_api::CompactClient as ApiCompactClient;`
- `use codex_api::CompactionInput as ApiCompactionInput;`
- `use codex_api::MemoriesClient as ApiMemoriesClient;`
- `use codex_api::MemoryTrace as ApiMemoryTrace;`
- `use codex_api::MemoryTraceSummarizeInput as ApiMemoryTraceSummarizeInput;`
- `use codex_api::MemoryTraceSummaryOutput as ApiMemoryTraceSummaryOutput;`
- `use codex_api::Prompt as ApiPrompt;`
- `use codex_api::RequestTelemetry;`
- `use codex_api::ReqwestTransport;`
- `use codex_api::ResponseAppendWsRequest;`
- `use codex_api::ResponseCreateWsRequest;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
