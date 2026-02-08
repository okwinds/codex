# `codex-rs/core/src/client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `34387`
- sha256: `2750fc69ecd69feea31c89bd490825eb58dd40ba5fa70c85b876fe0f5d21f627`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `pub fn new_session(&self, turn_metadata_cwd: Option<PathBuf>) -> ModelClientSession {`
- `pub fn get_model_context_window(&self) -> Option<i64> {`
- `pub fn config(&self) -> Arc<Config> {`
- `pub fn provider(&self) -> &ModelProviderInfo {`
- `pub fn get_provider(&self) -> ModelProviderInfo {`
- `pub fn get_otel_manager(&self) -> OtelManager {`
- `pub fn get_session_source(&self) -> SessionSource {`
- `pub fn get_model(&self) -> String {`
- `pub fn get_model_info(&self) -> ModelInfo {`
- `pub fn get_reasoning_effort(&self) -> Option<ReasoningEffortConfig> {`
- `pub fn get_reasoning_summary(&self) -> ReasoningSummaryConfig {`
- `pub fn get_auth_manager(&self) -> Option<Arc<AuthManager>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/client.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/client.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/client.rs:3` `use std::sync::OnceLock;`
- `use` `codex-rs/core/src/client.rs:4` `use std::sync::RwLock;`
- `use` `codex-rs/core/src/client.rs:6` `use crate::api_bridge::CoreAuthProvider;`
- `use` `codex-rs/core/src/client.rs:7` `use crate::api_bridge::auth_provider_from_auth;`
- `use` `codex-rs/core/src/client.rs:8` `use crate::api_bridge::map_api_error;`
- `use` `codex-rs/core/src/client.rs:9` `use crate::auth::UnauthorizedRecovery;`
- `use` `codex-rs/core/src/client.rs:10` `use crate::turn_metadata::build_turn_metadata_header;`
- `use` `codex-rs/core/src/client.rs:11` `use codex_api::AggregateStreamExt;`
- `use` `codex-rs/core/src/client.rs:12` `use codex_api::ChatClient as ApiChatClient;`
- `use` `codex-rs/core/src/client.rs:13` `use codex_api::CompactClient as ApiCompactClient;`
- `use` `codex-rs/core/src/client.rs:14` `use codex_api::CompactionInput as ApiCompactionInput;`
- `use` `codex-rs/core/src/client.rs:15` `use codex_api::Prompt as ApiPrompt;`
- `use` `codex-rs/core/src/client.rs:16` `use codex_api::RequestTelemetry;`
- `use` `codex-rs/core/src/client.rs:17` `use codex_api::ReqwestTransport;`
- `use` `codex-rs/core/src/client.rs:18` `use codex_api::ResponseAppendWsRequest;`
- `use` `codex-rs/core/src/client.rs:19` `use codex_api::ResponseCreateWsRequest;`
- `use` `codex-rs/core/src/client.rs:20` `use codex_api::ResponseStream as ApiResponseStream;`
- `use` `codex-rs/core/src/client.rs:21` `use codex_api::ResponsesClient as ApiResponsesClient;`
- `use` `codex-rs/core/src/client.rs:22` `use codex_api::ResponsesOptions as ApiResponsesOptions;`
- `use` `codex-rs/core/src/client.rs:23` `use codex_api::ResponsesWebsocketClient as ApiWebSocketResponsesClient;`
- `use` `codex-rs/core/src/client.rs:24` `use codex_api::ResponsesWebsocketConnection as ApiWebSocketConnection;`
- `use` `codex-rs/core/src/client.rs:25` `use codex_api::SseTelemetry;`
- `use` `codex-rs/core/src/client.rs:26` `use codex_api::TransportError;`
- `use` `codex-rs/core/src/client.rs:27` `use codex_api::WebsocketTelemetry;`
- `use` `codex-rs/core/src/client.rs:28` `use codex_api::build_conversation_headers;`
- `use` `codex-rs/core/src/client.rs:29` `use codex_api::common::Reasoning;`
- `use` `codex-rs/core/src/client.rs:30` `use codex_api::common::ResponsesWsRequest;`
- `use` `codex-rs/core/src/client.rs:31` `use codex_api::create_text_param_for_request;`
- `use` `codex-rs/core/src/client.rs:32` `use codex_api::error::ApiError;`
- `use` `codex-rs/core/src/client.rs:33` `use codex_api::requests::responses::Compression;`
- `use` `codex-rs/core/src/client.rs:34` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/client.rs:36` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/client.rs:37` `use codex_protocol::config_types::ReasoningSummary as ReasoningSummaryConfig;`
- `use` `codex-rs/core/src/client.rs:38` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/core/src/client.rs:39` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/client.rs:40` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/client.rs:41` `use codex_protocol::openai_models::ReasoningEffort as ReasoningEffortConfig;`
- `use` `codex-rs/core/src/client.rs:42` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/client.rs:43` `use eventsource_stream::Event;`
- `use` `codex-rs/core/src/client.rs:44` `use eventsource_stream::EventStreamError;`
- `use` `codex-rs/core/src/client.rs:45` `use futures::StreamExt;`
- `use` `codex-rs/core/src/client.rs:46` `use http::HeaderMap as ApiHeaderMap;`
- `use` `codex-rs/core/src/client.rs:47` `use http::HeaderValue;`
- `use` `codex-rs/core/src/client.rs:48` `use http::StatusCode as HttpStatusCode;`
- `use` `codex-rs/core/src/client.rs:49` `use reqwest::StatusCode;`
- `use` `codex-rs/core/src/client.rs:50` `use serde_json::Value;`
- `use` `codex-rs/core/src/client.rs:51` `use std::time::Duration;`
- `use` `codex-rs/core/src/client.rs:52` `use tokio::sync::mpsc;`
- `use` `codex-rs/core/src/client.rs:53` `use tokio_tungstenite::tungstenite::Error;`
- `use` `codex-rs/core/src/client.rs:54` `use tokio_tungstenite::tungstenite::Message;`
- `use` `codex-rs/core/src/client.rs:55` `use tracing::warn;`
- `use` `codex-rs/core/src/client.rs:57` `use crate::AuthManager;`
- `use` `codex-rs/core/src/client.rs:58` `use crate::auth::CodexAuth;`
- `use` `codex-rs/core/src/client.rs:59` `use crate::auth::RefreshTokenError;`
- `use` `codex-rs/core/src/client.rs:60` `use crate::client_common::Prompt;`
- `use` `codex-rs/core/src/client.rs:61` `use crate::client_common::ResponseEvent;`
- `use` `codex-rs/core/src/client.rs:62` `use crate::client_common::ResponseStream;`
- `use` `codex-rs/core/src/client.rs:63` `use crate::config::Config;`
- `use` `codex-rs/core/src/client.rs:64` `use crate::default_client::build_reqwest_client;`
- `use` `codex-rs/core/src/client.rs:65` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/client.rs:66` `use crate::error::Result;`
- `use` `codex-rs/core/src/client.rs:67` `use crate::features::FEATURES;`
- `use` `codex-rs/core/src/client.rs:68` `use crate::features::Feature;`
- `use` `codex-rs/core/src/client.rs:69` `use crate::flags::CODEX_RS_SSE_FIXTURE;`
- `use` `codex-rs/core/src/client.rs:70` `use crate::model_provider_info::ModelProviderInfo;`
- `use` `codex-rs/core/src/client.rs:71` `use crate::model_provider_info::WireApi;`
- `use` `codex-rs/core/src/client.rs:72` `use crate::tools::spec::create_tools_json_for_chat_completions_api;`
- `use` `codex-rs/core/src/client.rs:73` `use crate::tools::spec::create_tools_json_for_responses_api;`
- `use` `codex-rs/core/src/client.rs:74` `use crate::transport_manager::TransportManager;`
- `const` `codex-rs/core/src/client.rs:76` `pub const WEB_SEARCH_ELIGIBLE_HEADER: &str = "x-oai-web-search-eligible";`
- `const` `codex-rs/core/src/client.rs:77` `pub const X_CODEX_TURN_STATE_HEADER: &str = "x-codex-turn-state";`
- `const` `codex-rs/core/src/client.rs:78` `pub const X_CODEX_TURN_METADATA_HEADER: &str = "x-codex-turn-metadata";`
- `struct` `codex-rs/core/src/client.rs:81` `struct TurnMetadataCache {`
- `struct` `codex-rs/core/src/client.rs:87` `struct ModelClientState {`
- `struct` `codex-rs/core/src/client.rs:102` `pub struct ModelClient {`
- `struct` `codex-rs/core/src/client.rs:106` `pub struct ModelClientSession {`
- `impl` `codex-rs/core/src/client.rs:125` `impl ModelClient {`
- `fn` `codex-rs/core/src/client.rs:126` `pub fn new(`
- `fn` `codex-rs/core/src/client.rs:155` `pub fn new_session(&self, turn_metadata_cwd: Option<PathBuf>) -> ModelClientSession {`
- `fn` `codex-rs/core/src/client.rs:168` `fn prewarm_turn_metadata_header(&self, turn_metadata_cwd: Option<PathBuf>) {`
- `impl` `codex-rs/core/src/client.rs:199` `impl ModelClient {`
- `fn` `codex-rs/core/src/client.rs:200` `pub fn get_model_context_window(&self) -> Option<i64> {`
- `fn` `codex-rs/core/src/client.rs:208` `pub fn config(&self) -> Arc<Config> {`
- `fn` `codex-rs/core/src/client.rs:212` `pub fn provider(&self) -> &ModelProviderInfo {`
- `fn` `codex-rs/core/src/client.rs:216` `pub fn get_provider(&self) -> ModelProviderInfo {`
- `fn` `codex-rs/core/src/client.rs:220` `pub fn get_otel_manager(&self) -> OtelManager {`
- `fn` `codex-rs/core/src/client.rs:224` `pub fn get_session_source(&self) -> SessionSource {`
- `fn` `codex-rs/core/src/client.rs:233` `pub fn get_model(&self) -> String {`
- `fn` `codex-rs/core/src/client.rs:237` `pub fn get_model_info(&self) -> ModelInfo {`
- `fn` `codex-rs/core/src/client.rs:242` `pub fn get_reasoning_effort(&self) -> Option<ReasoningEffortConfig> {`
- `fn` `codex-rs/core/src/client.rs:247` `pub fn get_reasoning_summary(&self) -> ReasoningSummaryConfig {`
- `fn` `codex-rs/core/src/client.rs:251` `pub fn get_auth_manager(&self) -> Option<Arc<AuthManager>> {`
- `fn` `codex-rs/core/src/client.rs:259` `pub async fn compact_conversation_history(&self, prompt: &Prompt) -> Result<Vec<ResponseItem>> {`
- `impl` `codex-rs/core/src/client.rs:304` `impl ModelClientSession {`
- `fn` `codex-rs/core/src/client.rs:305` `fn turn_metadata_header(&self) -> Option<HeaderValue> {`
- `fn` `codex-rs/core/src/client.rs:318` `pub async fn stream(&mut self, prompt: &Prompt) -> Result<ResponseStream> {`
- `fn` `codex-rs/core/src/client.rs:368` `fn responses_websocket_enabled(&self) -> bool {`
- `fn` `codex-rs/core/src/client.rs:377` `fn build_responses_request(&self, prompt: &Prompt) -> Result<ApiPrompt> {`
- `fn` `codex-rs/core/src/client.rs:383` `fn build_responses_options(`
- `fn` `codex-rs/core/src/client.rs:447` `fn get_incremental_items(&self, input_items: &[ResponseItem]) -> Option<Vec<ResponseItem>> {`
- `fn` `codex-rs/core/src/client.rs:462` `fn prepare_websocket_request(`
- `fn` `codex-rs/core/src/client.rs:501` `async fn websocket_connection(`
- `fn` `codex-rs/core/src/client.rs:532` `fn responses_request_compression(&self, auth: Option<&crate::auth::CodexAuth>) -> Compression {`
- `fn` `codex-rs/core/src/client.rs:551` `async fn stream_chat_completions(&self, prompt: &Prompt) -> Result<ApiResponseStream> {`
- `fn` `codex-rs/core/src/client.rs:609` `async fn stream_responses_api(&self, prompt: &Prompt) -> Result<ResponseStream> {`
- `fn` `codex-rs/core/src/client.rs:663` `async fn stream_responses_websocket(&mut self, prompt: &Prompt) -> Result<ResponseStream> {`
- `fn` `codex-rs/core/src/client.rs:713` `fn build_streaming_telemetry(&self) -> (Arc<dyn RequestTelemetry>, Arc<dyn SseTelemetry>) {`
- `fn` `codex-rs/core/src/client.rs:721` `fn build_websocket_telemetry(&self) -> Arc<dyn WebsocketTelemetry> {`
- `impl` `codex-rs/core/src/client.rs:728` `impl ModelClient {`
- `fn` `codex-rs/core/src/client.rs:730` `fn build_request_telemetry(&self) -> Arc<dyn RequestTelemetry> {`
- `fn` `codex-rs/core/src/client.rs:738` `fn build_api_prompt(prompt: &Prompt, instructions: String, tools_json: Vec<Value>) -> ApiPrompt {`
- `fn` `codex-rs/core/src/client.rs:748` `fn experimental_feature_headers(config: &Config) -> ApiHeaderMap {`
- `fn` `codex-rs/core/src/client.rs:771` `fn build_responses_headers(`
- `fn` `codex-rs/core/src/client.rs:863` `async fn handle_unauthorized(`
- `fn` `codex-rs/core/src/client.rs:880` `fn map_unauthorized_status(status: StatusCode) -> CodexErr {`
- `struct` `codex-rs/core/src/client.rs:889` `struct ApiTelemetry {`
- `impl` `codex-rs/core/src/client.rs:893` `impl ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:894` `fn new(otel_manager: OtelManager) -> Self {`
- `impl` `codex-rs/core/src/client.rs:899` `impl RequestTelemetry for ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:900` `fn on_request(`
- `impl` `codex-rs/core/src/client.rs:917` `impl SseTelemetry for ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:918` `fn on_sse_poll(`
- `impl` `codex-rs/core/src/client.rs:930` `impl WebsocketTelemetry for ApiTelemetry {`
- `fn` `codex-rs/core/src/client.rs:931` `fn on_ws_request(&self, duration: Duration, error: Option<&ApiError>) {`
- `fn` `codex-rs/core/src/client.rs:937` `fn on_ws_event(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::OnceLock;`
- `use std::sync::RwLock;`
- `use crate::api_bridge::CoreAuthProvider;`
- `use crate::api_bridge::auth_provider_from_auth;`
- `use crate::api_bridge::map_api_error;`
- `use crate::auth::UnauthorizedRecovery;`
- `use crate::turn_metadata::build_turn_metadata_header;`
- `use codex_api::AggregateStreamExt;`
- `use codex_api::ChatClient as ApiChatClient;`
- `use codex_api::CompactClient as ApiCompactClient;`
- `use codex_api::CompactionInput as ApiCompactionInput;`
- `use codex_api::Prompt as ApiPrompt;`
- `use codex_api::RequestTelemetry;`
- `use codex_api::ReqwestTransport;`
- `use codex_api::ResponseAppendWsRequest;`
- `use codex_api::ResponseCreateWsRequest;`
- `use codex_api::ResponseStream as ApiResponseStream;`
- `use codex_api::ResponsesClient as ApiResponsesClient;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
