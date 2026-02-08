# `codex-rs/core/src/mcp/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13417`
- sha256: `882cbf254e2558b9dc7ea5fa57a00ac0beddede0ff213d94dd62eced6459ce89`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/mcp/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn split_qualified_tool_name(qualified_name: &str) -> Option<(String, String)> {`
- `pub fn group_tools_by_server(`

## Definitions (auto, per-file)
- `mod` `codex-rs/core/src/mcp/mod.rs:1` `pub mod auth;`
- `mod` `codex-rs/core/src/mcp/mod.rs:2` `mod skill_dependencies;`
- `use` `codex-rs/core/src/mcp/mod.rs:5` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/mcp/mod.rs:6` `use std::env;`
- `use` `codex-rs/core/src/mcp/mod.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/mcp/mod.rs:8` `use std::time::Duration;`
- `use` `codex-rs/core/src/mcp/mod.rs:10` `use async_channel::unbounded;`
- `use` `codex-rs/core/src/mcp/mod.rs:11` `use codex_protocol::mcp::Resource;`
- `use` `codex-rs/core/src/mcp/mod.rs:12` `use codex_protocol::mcp::ResourceTemplate;`
- `use` `codex-rs/core/src/mcp/mod.rs:13` `use codex_protocol::mcp::Tool;`
- `use` `codex-rs/core/src/mcp/mod.rs:14` `use codex_protocol::protocol::McpListToolsResponseEvent;`
- `use` `codex-rs/core/src/mcp/mod.rs:15` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/mcp/mod.rs:16` `use serde_json::Value;`
- `use` `codex-rs/core/src/mcp/mod.rs:17` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/mcp/mod.rs:19` `use crate::AuthManager;`
- `use` `codex-rs/core/src/mcp/mod.rs:20` `use crate::CodexAuth;`
- `use` `codex-rs/core/src/mcp/mod.rs:21` `use crate::config::Config;`
- `use` `codex-rs/core/src/mcp/mod.rs:22` `use crate::config::types::McpServerConfig;`
- `use` `codex-rs/core/src/mcp/mod.rs:23` `use crate::config::types::McpServerTransportConfig;`
- `use` `codex-rs/core/src/mcp/mod.rs:24` `use crate::features::Feature;`
- `use` `codex-rs/core/src/mcp/mod.rs:25` `use crate::mcp::auth::compute_auth_statuses;`
- `use` `codex-rs/core/src/mcp/mod.rs:26` `use crate::mcp_connection_manager::McpConnectionManager;`
- `use` `codex-rs/core/src/mcp/mod.rs:27` `use crate::mcp_connection_manager::SandboxState;`
- `const` `codex-rs/core/src/mcp/mod.rs:29` `const MCP_TOOL_NAME_PREFIX: &str = "mcp";`
- `const` `codex-rs/core/src/mcp/mod.rs:30` `const MCP_TOOL_NAME_DELIMITER: &str = "__";`
- `const` `codex-rs/core/src/mcp/mod.rs:32` `const CODEX_CONNECTORS_TOKEN_ENV_VAR: &str = "CODEX_CONNECTORS_TOKEN";`
- `fn` `codex-rs/core/src/mcp/mod.rs:34` `fn codex_apps_mcp_bearer_token_env_var() -> Option<String> {`
- `fn` `codex-rs/core/src/mcp/mod.rs:43` `fn codex_apps_mcp_bearer_token(auth: Option<&CodexAuth>) -> Option<String> {`
- `fn` `codex-rs/core/src/mcp/mod.rs:53` `fn codex_apps_mcp_http_headers(auth: Option<&CodexAuth>) -> Option<HashMap<String, String>> {`
- `fn` `codex-rs/core/src/mcp/mod.rs:68` `fn codex_apps_mcp_url(base_url: &str) -> String {`
- `fn` `codex-rs/core/src/mcp/mod.rs:85` `fn codex_apps_mcp_server_config(config: &Config, auth: Option<&CodexAuth>) -> McpServerConfig {`
- `fn` `codex-rs/core/src/mcp/mod.rs:141` `pub async fn collect_mcp_snapshot(config: &Config) -> McpListToolsResponseEvent {`
- `fn` `codex-rs/core/src/mcp/mod.rs:193` `pub fn split_qualified_tool_name(qualified_name: &str) -> Option<(String, String)> {`
- `fn` `codex-rs/core/src/mcp/mod.rs:207` `pub fn group_tools_by_server(`
- `use` `codex-rs/core/src/mcp/mod.rs:335` `use super::*;`
- `use` `codex-rs/core/src/mcp/mod.rs:336` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/mcp/mod.rs:338` `fn make_tool(name: &str) -> Tool {`
- `fn` `codex-rs/core/src/mcp/mod.rs:352` `fn split_qualified_tool_name_returns_server_and_tool() {`
- `fn` `codex-rs/core/src/mcp/mod.rs:360` `fn split_qualified_tool_name_rejects_invalid_names() {`
- `fn` `codex-rs/core/src/mcp/mod.rs:366` `fn group_tools_by_server_strips_prefix_and_groups() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::env;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use async_channel::unbounded;`
- `use codex_protocol::mcp::Resource;`
- `use codex_protocol::mcp::ResourceTemplate;`
- `use codex_protocol::mcp::Tool;`
- `use codex_protocol::protocol::McpListToolsResponseEvent;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use serde_json::Value;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::AuthManager;`
- `use crate::CodexAuth;`
- `use crate::config::Config;`
- `use crate::config::types::McpServerConfig;`
- `use crate::config::types::McpServerTransportConfig;`
- `use crate::features::Feature;`
- `use crate::mcp::auth::compute_auth_statuses;`
- `use crate::mcp_connection_manager::McpConnectionManager;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
