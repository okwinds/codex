# `codex-rs/rmcp-client/src/perform_oauth_login.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11637`
- sha256: `1e0b1c55a3785ad2db976d5903acccb3d35708cff72473962b23450af14e1f04`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/perform_oauth_login.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct OauthLoginHandle {`
- `pub fn authorization_url(&self) -> &str {`
- `pub fn into_parts(self) -> (String, oneshot::Receiver<Result<()>>) {`

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:2` `use std::string::String;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:4` `use std::time::Duration;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:6` `use anyhow::Context;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:7` `use anyhow::Result;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:8` `use anyhow::anyhow;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:9` `use anyhow::bail;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:10` `use reqwest::ClientBuilder;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:11` `use rmcp::transport::auth::OAuthState;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:12` `use tiny_http::Response;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:13` `use tiny_http::Server;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:14` `use tokio::sync::oneshot;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:15` `use tokio::time::timeout;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:16` `use urlencoding::decode;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:18` `use crate::OAuthCredentialsStoreMode;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:19` `use crate::StoredOAuthTokens;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:20` `use crate::WrappedOAuthTokenResponse;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:21` `use crate::oauth::compute_expires_at_millis;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:22` `use crate::save_oauth_tokens;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:23` `use crate::utils::apply_default_headers;`
- `use` `codex-rs/rmcp-client/src/perform_oauth_login.rs:24` `use crate::utils::build_default_headers;`
- `struct` `codex-rs/rmcp-client/src/perform_oauth_login.rs:26` `struct OauthHeaders {`
- `struct` `codex-rs/rmcp-client/src/perform_oauth_login.rs:31` `struct CallbackServerGuard {`
- `impl` `codex-rs/rmcp-client/src/perform_oauth_login.rs:35` `impl Drop for CallbackServerGuard {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:36` `fn drop(&mut self) {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:41` `pub async fn perform_oauth_login(`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:70` `pub async fn perform_oauth_login_return_url(`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:102` `fn spawn_callback_server(server: Arc<Server>, tx: oneshot::Sender<(String, String)>) {`
- `struct` `codex-rs/rmcp-client/src/perform_oauth_login.rs:138` `struct OauthCallbackResult {`
- `enum` `codex-rs/rmcp-client/src/perform_oauth_login.rs:143` `enum CallbackOutcome {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:149` `fn parse_oauth_callback(path: &str) -> CallbackOutcome {`
- `struct` `codex-rs/rmcp-client/src/perform_oauth_login.rs:188` `pub struct OauthLoginHandle {`
- `impl` `codex-rs/rmcp-client/src/perform_oauth_login.rs:193` `impl OauthLoginHandle {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:194` `fn new(authorization_url: String, completion: oneshot::Receiver<Result<()>>) -> Self {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:201` `pub fn authorization_url(&self) -> &str {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:205` `pub fn into_parts(self) -> (String, oneshot::Receiver<Result<()>>) {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:209` `pub async fn wait(self) -> Result<()> {`
- `struct` `codex-rs/rmcp-client/src/perform_oauth_login.rs:216` `struct OauthLoginFlow {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:228` `fn resolve_callback_port(callback_port: Option<u16>) -> Result<Option<u16>> {`
- `impl` `codex-rs/rmcp-client/src/perform_oauth_login.rs:241` `impl OauthLoginFlow {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:243` `async fn new(`
- `const` `codex-rs/rmcp-client/src/perform_oauth_login.rs:253` `const DEFAULT_OAUTH_TIMEOUT_SECS: i64 = 300;`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:313` `fn authorization_url(&self) -> String {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:317` `async fn finish(mut self) -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/perform_oauth_login.rs:367` `fn spawn(self) -> oneshot::Receiver<Result<()>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::string::String;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use anyhow::bail;`
- `use reqwest::ClientBuilder;`
- `use rmcp::transport::auth::OAuthState;`
- `use tiny_http::Response;`
- `use tiny_http::Server;`
- `use tokio::sync::oneshot;`
- `use tokio::time::timeout;`
- `use urlencoding::decode;`
- `use crate::OAuthCredentialsStoreMode;`
- `use crate::StoredOAuthTokens;`
- `use crate::WrappedOAuthTokenResponse;`
- `use crate::oauth::compute_expires_at_millis;`
- `use crate::save_oauth_tokens;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
