# `codex-rs/rmcp-client/src/auth_status.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4588`
- sha256: `7b5d92c8671623fce4f38d5224688e18b3f5d9e782273fdd8369bf231ea22758`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/auth_status.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/auth_status.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:2` `use std::time::Duration;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:4` `use anyhow::Error;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:5` `use anyhow::Result;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:6` `use codex_protocol::protocol::McpAuthStatus;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:7` `use reqwest::Client;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:8` `use reqwest::StatusCode;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:9` `use reqwest::Url;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:10` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:11` `use serde::Deserialize;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:12` `use tracing::debug;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:14` `use crate::OAuthCredentialsStoreMode;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:15` `use crate::oauth::has_oauth_tokens;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:16` `use crate::utils::apply_default_headers;`
- `use` `codex-rs/rmcp-client/src/auth_status.rs:17` `use crate::utils::build_default_headers;`
- `const` `codex-rs/rmcp-client/src/auth_status.rs:19` `const DISCOVERY_TIMEOUT: Duration = Duration::from_secs(5);`
- `const` `codex-rs/rmcp-client/src/auth_status.rs:20` `const OAUTH_DISCOVERY_HEADER: &str = "MCP-Protocol-Version";`
- `const` `codex-rs/rmcp-client/src/auth_status.rs:21` `const OAUTH_DISCOVERY_VERSION: &str = "2024-11-05";`
- `fn` `codex-rs/rmcp-client/src/auth_status.rs:24` `pub async fn determine_streamable_http_auth_status(`
- `fn` `codex-rs/rmcp-client/src/auth_status.rs:55` `pub async fn supports_oauth_login(url: &str) -> Result<bool> {`
- `fn` `codex-rs/rmcp-client/src/auth_status.rs:59` `async fn supports_oauth_login_with_headers(url: &str, default_headers: &HeaderMap) -> Result<bool> {`
- `struct` `codex-rs/rmcp-client/src/auth_status.rs:110` `struct OAuthDiscoveryMetadata {`
- `fn` `codex-rs/rmcp-client/src/auth_status.rs:121` `fn discovery_paths(base_path: &str) -> Vec<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::time::Duration;`
- `use anyhow::Error;`
- `use anyhow::Result;`
- `use codex_protocol::protocol::McpAuthStatus;`
- `use reqwest::Client;`
- `use reqwest::StatusCode;`
- `use reqwest::Url;`
- `use reqwest::header::HeaderMap;`
- `use serde::Deserialize;`
- `use tracing::debug;`
- `use crate::OAuthCredentialsStoreMode;`
- `use crate::oauth::has_oauth_tokens;`
- `use crate::utils::apply_default_headers;`
- `use crate::utils::build_default_headers;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
