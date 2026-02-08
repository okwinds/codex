# `codex-rs/rmcp-client/src/rmcp_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `20188`
- sha256: `51a6967a8e2a7f418c3ed8f529bd54902790b60d977e7539850940033a743e6c`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/rmcp_client.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses

## Public Surface (auto)
- `pub struct ToolWithConnectorId {`
- `pub struct ListToolsWithConnectorIdResult {`
- `pub struct RmcpClient {`

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:2` `use std::ffi::OsString;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:3` `use std::io;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:5` `use std::process::Stdio;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:6` `use std::sync::Arc;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:7` `use std::time::Duration;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:9` `use anyhow::Result;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:10` `use anyhow::anyhow;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:11` `use futures::FutureExt;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:12` `use futures::future::BoxFuture;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:13` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:14` `use rmcp::model::CallToolRequestParam;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:15` `use rmcp::model::CallToolResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:16` `use rmcp::model::ClientNotification;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:17` `use rmcp::model::ClientRequest;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:18` `use rmcp::model::CreateElicitationRequestParam;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:19` `use rmcp::model::CreateElicitationResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:20` `use rmcp::model::CustomNotification;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:21` `use rmcp::model::CustomRequest;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:22` `use rmcp::model::Extensions;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:23` `use rmcp::model::InitializeRequestParam;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:24` `use rmcp::model::InitializeResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:25` `use rmcp::model::ListResourceTemplatesResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:26` `use rmcp::model::ListResourcesResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:27` `use rmcp::model::ListToolsResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:28` `use rmcp::model::PaginatedRequestParam;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:29` `use rmcp::model::ReadResourceRequestParam;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:30` `use rmcp::model::ReadResourceResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:31` `use rmcp::model::RequestId;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:32` `use rmcp::model::ServerResult;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:33` `use rmcp::model::Tool;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:34` `use rmcp::service::RoleClient;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:35` `use rmcp::service::RunningService;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:36` `use rmcp::service::{self};`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:37` `use rmcp::transport::StreamableHttpClientTransport;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:38` `use rmcp::transport::auth::AuthClient;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:39` `use rmcp::transport::auth::OAuthState;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:40` `use rmcp::transport::child_process::TokioChildProcess;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:41` `use rmcp::transport::streamable_http_client::StreamableHttpClientTransportConfig;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:42` `use serde_json::Value;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:43` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:44` `use tokio::io::BufReader;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:45` `use tokio::process::Command;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:46` `use tokio::sync::Mutex;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:47` `use tokio::time;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:48` `use tracing::info;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:49` `use tracing::warn;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:51` `use crate::load_oauth_tokens;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:52` `use crate::logging_client_handler::LoggingClientHandler;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:53` `use crate::oauth::OAuthCredentialsStoreMode;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:54` `use crate::oauth::OAuthPersistor;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:55` `use crate::oauth::StoredOAuthTokens;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:56` `use crate::program_resolver;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:57` `use crate::utils::apply_default_headers;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:58` `use crate::utils::build_default_headers;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:59` `use crate::utils::create_env_for_mcp_server;`
- `use` `codex-rs/rmcp-client/src/rmcp_client.rs:60` `use crate::utils::run_with_timeout;`
- `enum` `codex-rs/rmcp-client/src/rmcp_client.rs:62` `enum PendingTransport {`
- `enum` `codex-rs/rmcp-client/src/rmcp_client.rs:76` `enum ClientState {`
- `const` `codex-rs/rmcp-client/src/rmcp_client.rs:88` `const PROCESS_GROUP_TERM_GRACE_PERIOD: Duration = Duration::from_secs(2);`
- `struct` `codex-rs/rmcp-client/src/rmcp_client.rs:91` `struct ProcessGroupGuard {`
- `struct` `codex-rs/rmcp-client/src/rmcp_client.rs:96` `struct ProcessGroupGuard;`
- `impl` `codex-rs/rmcp-client/src/rmcp_client.rs:98` `impl ProcessGroupGuard {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:99` `fn new(process_group_id: u32) -> Self {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:112` `fn maybe_terminate_process_group(&self) {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:135` `fn maybe_terminate_process_group(&self) {}`
- `impl` `codex-rs/rmcp-client/src/rmcp_client.rs:138` `impl Drop for ProcessGroupGuard {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:139` `fn drop(&mut self) {`
- `type` `codex-rs/rmcp-client/src/rmcp_client.rs:146` `pub type Elicitation = CreateElicitationRequestParam;`
- `type` `codex-rs/rmcp-client/src/rmcp_client.rs:147` `pub type ElicitationResponse = CreateElicitationResult;`
- `type` `codex-rs/rmcp-client/src/rmcp_client.rs:150` `pub type SendElicitation = Box<`
- `struct` `codex-rs/rmcp-client/src/rmcp_client.rs:154` `pub struct ToolWithConnectorId {`
- `struct` `codex-rs/rmcp-client/src/rmcp_client.rs:160` `pub struct ListToolsWithConnectorIdResult {`
- `struct` `codex-rs/rmcp-client/src/rmcp_client.rs:167` `pub struct RmcpClient {`
- `impl` `codex-rs/rmcp-client/src/rmcp_client.rs:171` `impl RmcpClient {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:172` `pub async fn new_stdio_client(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:235` `pub async fn new_streamable_http_client(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:290` `pub async fn initialize(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:363` `pub async fn list_tools(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:376` `pub async fn list_tools_with_connector_ids(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:408` `fn meta_string(meta: Option<&rmcp::model::Meta>, key: &str) -> Option<String> {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:416` `pub async fn list_resources(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:430` `pub async fn list_resource_templates(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:444` `pub async fn read_resource(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:457` `pub async fn call_tool(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:484` `pub async fn send_custom_notification(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:500` `pub async fn send_custom_request(`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:514` `async fn service(&self) -> Result<Arc<RunningService<RoleClient, LoggingClientHandler>>> {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:522` `async fn oauth_persistor(&self) -> Option<OAuthPersistor> {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:535` `async fn persist_oauth_tokens(&self) {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:543` `async fn refresh_oauth_if_needed(&self) {`
- `fn` `codex-rs/rmcp-client/src/rmcp_client.rs:552` `async fn create_oauth_transport_and_runtime(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::ffi::OsString;`
- `use std::io;`
- `use std::path::PathBuf;`
- `use std::process::Stdio;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use futures::FutureExt;`
- `use futures::future::BoxFuture;`
- `use reqwest::header::HeaderMap;`
- `use rmcp::model::CallToolRequestParam;`
- `use rmcp::model::CallToolResult;`
- `use rmcp::model::ClientNotification;`
- `use rmcp::model::ClientRequest;`
- `use rmcp::model::CreateElicitationRequestParam;`
- `use rmcp::model::CreateElicitationResult;`
- `use rmcp::model::CustomNotification;`
- `use rmcp::model::CustomRequest;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
