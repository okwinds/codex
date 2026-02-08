# `codex-rs/core/src/mcp/auth.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3330`
- sha256: `d58d2f05c5e0ac984adff5b68edefc26cf82f71e70400b69e3e5246d22f3acb3`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/mcp/auth.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct McpOAuthLoginConfig {`
- `pub enum McpOAuthLoginSupport {`
- `pub struct McpAuthStatusEntry {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/mcp/auth.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/mcp/auth.rs:3` `use anyhow::Result;`
- `use` `codex-rs/core/src/mcp/auth.rs:4` `use codex_protocol::protocol::McpAuthStatus;`
- `use` `codex-rs/core/src/mcp/auth.rs:5` `use codex_rmcp_client::OAuthCredentialsStoreMode;`
- `use` `codex-rs/core/src/mcp/auth.rs:6` `use codex_rmcp_client::determine_streamable_http_auth_status;`
- `use` `codex-rs/core/src/mcp/auth.rs:7` `use codex_rmcp_client::supports_oauth_login;`
- `use` `codex-rs/core/src/mcp/auth.rs:8` `use futures::future::join_all;`
- `use` `codex-rs/core/src/mcp/auth.rs:9` `use tracing::warn;`
- `use` `codex-rs/core/src/mcp/auth.rs:11` `use crate::config::types::McpServerConfig;`
- `use` `codex-rs/core/src/mcp/auth.rs:12` `use crate::config::types::McpServerTransportConfig;`
- `struct` `codex-rs/core/src/mcp/auth.rs:15` `pub struct McpOAuthLoginConfig {`
- `enum` `codex-rs/core/src/mcp/auth.rs:22` `pub enum McpOAuthLoginSupport {`
- `fn` `codex-rs/core/src/mcp/auth.rs:28` `pub async fn oauth_login_support(transport: &McpServerTransportConfig) -> McpOAuthLoginSupport {`
- `struct` `codex-rs/core/src/mcp/auth.rs:55` `pub struct McpAuthStatusEntry {`
- `fn` `codex-rs/core/src/mcp/auth.rs:89` `async fn compute_auth_status(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use anyhow::Result;`
- `use codex_protocol::protocol::McpAuthStatus;`
- `use codex_rmcp_client::OAuthCredentialsStoreMode;`
- `use codex_rmcp_client::determine_streamable_http_auth_status;`
- `use codex_rmcp_client::supports_oauth_login;`
- `use futures::future::join_all;`
- `use tracing::warn;`
- `use crate::config::types::McpServerConfig;`
- `use crate::config::types::McpServerTransportConfig;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
