# `codex-rs/core/src/mcp_connection_manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `49658`
- sha256: `ab003aec646f8c3ae3ca8cd5f2609e15a46a0126e937365172b53eb0acff5839`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/mcp_connection_manager.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct SandboxState {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/mcp_connection_manager.rs:9` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:10` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:11` `use std::env;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:12` `use std::ffi::OsString;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:13` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:14` `use std::sync::Arc;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:15` `use std::sync::LazyLock;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:16` `use std::sync::Mutex as StdMutex;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:17` `use std::time::Duration;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:18` `use std::time::Instant;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:20` `use crate::mcp::CODEX_APPS_MCP_SERVER_NAME;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:21` `use crate::mcp::auth::McpAuthStatusEntry;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:22` `use anyhow::Context;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:23` `use anyhow::Result;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:24` `use anyhow::anyhow;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:25` `use async_channel::Sender;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:26` `use codex_async_utils::CancelErr;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:27` `use codex_async_utils::OrCancelExt;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:28` `use codex_protocol::approvals::ElicitationRequestEvent;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:29` `use codex_protocol::mcp::CallToolResult;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:30` `use codex_protocol::mcp::RequestId as ProtocolRequestId;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:31` `use codex_protocol::protocol::Event;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:32` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:33` `use codex_protocol::protocol::McpStartupCompleteEvent;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:34` `use codex_protocol::protocol::McpStartupFailure;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:35` `use codex_protocol::protocol::McpStartupStatus;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:36` `use codex_protocol::protocol::McpStartupUpdateEvent;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:37` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:38` `use codex_rmcp_client::ElicitationResponse;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:39` `use codex_rmcp_client::OAuthCredentialsStoreMode;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:40` `use codex_rmcp_client::RmcpClient;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:41` `use codex_rmcp_client::SendElicitation;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:42` `use futures::future::BoxFuture;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:43` `use futures::future::FutureExt;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:44` `use futures::future::Shared;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:45` `use rmcp::model::ClientCapabilities;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:46` `use rmcp::model::ElicitationCapability;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:47` `use rmcp::model::Implementation;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:48` `use rmcp::model::InitializeRequestParam;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:49` `use rmcp::model::ListResourceTemplatesResult;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:50` `use rmcp::model::ListResourcesResult;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:51` `use rmcp::model::PaginatedRequestParam;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:52` `use rmcp::model::ProtocolVersion;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:53` `use rmcp::model::ReadResourceRequestParam;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:54` `use rmcp::model::ReadResourceResult;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:55` `use rmcp::model::RequestId;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:56` `use rmcp::model::Resource;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:57` `use rmcp::model::ResourceTemplate;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:58` `use rmcp::model::Tool;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:60` `use serde::Deserialize;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:61` `use serde::Serialize;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:62` `use sha1::Digest;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:63` `use sha1::Sha1;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:64` `use tokio::sync::Mutex;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:65` `use tokio::sync::oneshot;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:66` `use tokio::task::JoinSet;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:67` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:68` `use tracing::instrument;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:69` `use tracing::warn;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:71` `use crate::codex::INITIAL_SUBMIT_ID;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:72` `use crate::config::types::McpServerConfig;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:73` `use crate::config::types::McpServerTransportConfig;`
- `const` `codex-rs/core/src/mcp_connection_manager.rs:80` `const MCP_TOOL_NAME_DELIMITER: &str = "__";`
- `const` `codex-rs/core/src/mcp_connection_manager.rs:81` `const MAX_TOOL_NAME_LENGTH: usize = 64;`
- `const` `codex-rs/core/src/mcp_connection_manager.rs:84` `pub const DEFAULT_STARTUP_TIMEOUT: Duration = Duration::from_secs(10);`
- `const` `codex-rs/core/src/mcp_connection_manager.rs:87` `const DEFAULT_TOOL_TIMEOUT: Duration = Duration::from_secs(60);`
- `const` `codex-rs/core/src/mcp_connection_manager.rs:89` `const CODEX_APPS_TOOLS_CACHE_TTL: Duration = Duration::from_secs(3600);`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:94` `fn sanitize_responses_api_tool_name(name: &str) -> String {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:111` `fn sha1_hex(s: &str) -> String {`
- `struct` `codex-rs/core/src/mcp_connection_manager.rs:170` `struct CachedCodexAppsTools {`
- `static` `codex-rs/core/src/mcp_connection_manager.rs:175` `static CODEX_APPS_TOOLS_CACHE: LazyLock<StdMutex<Option<CachedCodexAppsTools>>> =`
- `type` `codex-rs/core/src/mcp_connection_manager.rs:178` `type ResponderMap = HashMap<(String, RequestId), oneshot::Sender<ElicitationResponse>>;`
- `struct` `codex-rs/core/src/mcp_connection_manager.rs:181` `struct ElicitationRequestManager {`
- `impl` `codex-rs/core/src/mcp_connection_manager.rs:185` `impl ElicitationRequestManager {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:186` `async fn resolve(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:201` `fn make_sender(&self, server_name: String, tx_event: Sender<Event>) -> SendElicitation {`
- `struct` `codex-rs/core/src/mcp_connection_manager.rs:239` `struct ManagedClient {`
- `impl` `codex-rs/core/src/mcp_connection_manager.rs:247` `impl ManagedClient {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:249` `async fn notify_sandbox_state_change(&self, sandbox_state: &SandboxState) -> Result<()> {`
- `struct` `codex-rs/core/src/mcp_connection_manager.rs:266` `struct AsyncManagedClient {`
- `impl` `codex-rs/core/src/mcp_connection_manager.rs:270` `impl AsyncManagedClient {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:271` `fn new(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:308` `async fn client(&self) -> Result<ManagedClient, StartupOutcomeError> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:312` `async fn notify_sandbox_state_change(&self, sandbox_state: &SandboxState) -> Result<()> {`
- `const` `codex-rs/core/src/mcp_connection_manager.rs:318` `pub const MCP_SANDBOX_STATE_CAPABILITY: &str = "codex/sandbox-state";`
- `const` `codex-rs/core/src/mcp_connection_manager.rs:322` `pub const MCP_SANDBOX_STATE_METHOD: &str = "codex/sandbox-state/update";`
- `struct` `codex-rs/core/src/mcp_connection_manager.rs:326` `pub struct SandboxState {`
- `impl` `codex-rs/core/src/mcp_connection_manager.rs:341` `impl McpConnectionManager {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:342` `pub async fn initialize(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:446` `async fn client_by_name(&self, name: &str) -> Result<ManagedClient> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:455` `pub async fn resolve_elicitation(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:505` `pub async fn list_all_tools(&self) -> HashMap<String, ToolInfo> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:536` `pub async fn list_all_resources(&self) -> HashMap<String, Vec<Resource>> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:601` `pub async fn list_all_resource_templates(&self) -> HashMap<String, Vec<ResourceTemplate>> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:669` `pub async fn call_tool(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:706` `pub async fn list_resources(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:722` `pub async fn list_resource_templates(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:738` `pub async fn read_resource(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:754` `pub async fn parse_tool_name(&self, tool_name: &str) -> Option<(String, String)> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:761` `pub async fn notify_sandbox_state_change(&self, sandbox_state: &SandboxState) -> Result<()> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:790` `async fn emit_update(`
- `impl` `codex-rs/core/src/mcp_connection_manager.rs:811` `impl ToolFilter {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:812` `fn from_config(cfg: &McpServerConfig) -> Self {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:826` `fn allows(&self, tool_name: &str) -> bool {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:837` `fn filter_tools(tools: Vec<ToolInfo>, filter: ToolFilter) -> Vec<ToolInfo> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:844` `fn normalize_codex_apps_tool_title(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:870` `fn resolve_bearer_token(`
- `enum` `codex-rs/core/src/mcp_connection_manager.rs:898` `enum StartupOutcomeError {`
- `impl` `codex-rs/core/src/mcp_connection_manager.rs:907` `impl From<anyhow::Error> for StartupOutcomeError {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:908` `fn from(error: anyhow::Error) -> Self {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:915` `async fn start_server_task(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:974` `async fn make_rmcp_client(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1018` `async fn list_tools_for_client(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1036` `fn read_cached_codex_apps_tools() -> Option<Vec<ToolInfo>> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1052` `fn write_cached_codex_apps_tools(tools: &[ToolInfo]) {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1062` `async fn list_tools_for_client_uncached(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1092` `fn validate_mcp_server_name(server_name: &str) -> Result<()> {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1103` `fn mcp_init_error_display(`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1142` `fn is_mcp_client_auth_required_error(error: &StartupOutcomeError) -> bool {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1149` `fn is_mcp_client_startup_timeout_error(error: &StartupOutcomeError) -> bool {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1159` `fn startup_outcome_error_message(error: StartupOutcomeError) -> String {`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:1171` `use super::*;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:1172` `use codex_protocol::protocol::McpAuthStatus;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:1173` `use rmcp::model::JsonObject;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:1174` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/mcp_connection_manager.rs:1175` `use std::sync::Arc;`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1177` `fn create_test_tool(server_name: &str, tool_name: &str) -> ToolInfo {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1197` `fn test_qualify_tools_short_non_duplicated_names() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1211` `fn test_qualify_tools_duplicated_names_skipped() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1225` `fn test_qualify_tools_long_names_same_server() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1260` `fn test_qualify_tools_sanitizes_invalid_characters() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1282` `fn tool_filter_allows_by_default() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1289` `fn tool_filter_applies_enabled_list() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1300` `fn tool_filter_applies_disabled_list() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1311` `fn tool_filter_applies_enabled_then_disabled() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1323` `fn filter_tools_applies_per_server_filters() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1349` `fn mcp_init_error_display_prompts_for_github_pat() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1382` `fn mcp_init_error_display_prompts_for_login_when_auth_required() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1396` `fn mcp_init_error_display_reports_generic_errors() {`
- `fn` `codex-rs/core/src/mcp_connection_manager.rs:1427` `fn mcp_init_error_display_includes_startup_timeout_hint() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::env;`
- `use std::ffi::OsString;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::LazyLock;`
- `use std::sync::Mutex as StdMutex;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use crate::mcp::CODEX_APPS_MCP_SERVER_NAME;`
- `use crate::mcp::auth::McpAuthStatusEntry;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use async_channel::Sender;`
- `use codex_async_utils::CancelErr;`
- `use codex_async_utils::OrCancelExt;`
- `use codex_protocol::approvals::ElicitationRequestEvent;`
- `use codex_protocol::mcp::CallToolResult;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
