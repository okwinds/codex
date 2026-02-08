# `codex-rs/core/src/connectors.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7687`
- sha256: `bcc561220dd6439a19762566321f2295c30518fb0d7360398c21143b0c719c76`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/connectors.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn connector_display_label(connector: &AppInfo) -> String {`
- `pub fn connector_mention_slug(connector: &AppInfo) -> String {`
- `pub fn merge_connectors(`
- `pub fn connector_install_url(name: &str, connector_id: &str) -> String {`
- `pub fn connector_name_slug(name: &str) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/connectors.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/connectors.rs:2` `use std::env;`
- `use` `codex-rs/core/src/connectors.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/connectors.rs:5` `use async_channel::unbounded;`
- `use` `codex-rs/core/src/connectors.rs:7` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/connectors.rs:8` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/connectors.rs:10` `use crate::AuthManager;`
- `use` `codex-rs/core/src/connectors.rs:11` `use crate::SandboxState;`
- `use` `codex-rs/core/src/connectors.rs:12` `use crate::config::Config;`
- `use` `codex-rs/core/src/connectors.rs:13` `use crate::features::Feature;`
- `use` `codex-rs/core/src/connectors.rs:14` `use crate::mcp::CODEX_APPS_MCP_SERVER_NAME;`
- `use` `codex-rs/core/src/connectors.rs:15` `use crate::mcp::auth::compute_auth_statuses;`
- `use` `codex-rs/core/src/connectors.rs:16` `use crate::mcp::with_codex_apps_mcp;`
- `use` `codex-rs/core/src/connectors.rs:17` `use crate::mcp_connection_manager::DEFAULT_STARTUP_TIMEOUT;`
- `use` `codex-rs/core/src/connectors.rs:18` `use crate::mcp_connection_manager::McpConnectionManager;`
- `fn` `codex-rs/core/src/connectors.rs:20` `pub async fn list_accessible_connectors_from_mcp_tools(`
- `fn` `codex-rs/core/src/connectors.rs:73` `fn auth_manager_from_config(config: &Config) -> std::sync::Arc<AuthManager> {`
- `fn` `codex-rs/core/src/connectors.rs:81` `pub fn connector_display_label(connector: &AppInfo) -> String {`
- `fn` `codex-rs/core/src/connectors.rs:85` `pub fn connector_mention_slug(connector: &AppInfo) -> String {`
- `fn` `codex-rs/core/src/connectors.rs:103` `pub fn merge_connectors(`
- `fn` `codex-rs/core/src/connectors.rs:194` `fn normalize_connector_value(value: Option<&str>) -> Option<String> {`
- `fn` `codex-rs/core/src/connectors.rs:201` `pub fn connector_install_url(name: &str, connector_id: &str) -> String {`
- `fn` `codex-rs/core/src/connectors.rs:206` `pub fn connector_name_slug(name: &str) -> String {`
- `fn` `codex-rs/core/src/connectors.rs:223` `fn format_connector_label(name: &str, _id: &str) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::env;`
- `use std::path::PathBuf;`
- `use async_channel::unbounded;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use tokio_util::sync::CancellationToken;`
- `use crate::AuthManager;`
- `use crate::SandboxState;`
- `use crate::config::Config;`
- `use crate::features::Feature;`
- `use crate::mcp::CODEX_APPS_MCP_SERVER_NAME;`
- `use crate::mcp::auth::compute_auth_statuses;`
- `use crate::mcp::with_codex_apps_mcp;`
- `use crate::mcp_connection_manager::DEFAULT_STARTUP_TIMEOUT;`
- `use crate::mcp_connection_manager::McpConnectionManager;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
