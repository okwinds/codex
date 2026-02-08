# `codex-rs/rmcp-client/src/oauth.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `31529`
- sha256: `76e4197369f0b6122c62d6c4ed3e55deeb46fefd29dec9028cc6a8dd44ccdfef`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/oauth.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct StoredOAuthTokens {`
- `pub enum OAuthCredentialsStoreMode {`
- `pub struct WrappedOAuthTokenResponse(pub OAuthTokenResponse);`
- `pub fn save_oauth_tokens(`
- `pub fn delete_oauth_tokens(`

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/oauth.rs:19` `use anyhow::Context;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:20` `use anyhow::Error;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:21` `use anyhow::Result;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:22` `use oauth2::AccessToken;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:23` `use oauth2::EmptyExtraTokenFields;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:24` `use oauth2::RefreshToken;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:25` `use oauth2::Scope;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:26` `use oauth2::TokenResponse;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:27` `use oauth2::basic::BasicTokenType;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:28` `use rmcp::transport::auth::OAuthTokenResponse;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:29` `use schemars::JsonSchema;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:30` `use serde::Deserialize;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:31` `use serde::Serialize;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:32` `use serde_json::Value;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:33` `use serde_json::map::Map as JsonMap;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:34` `use sha2::Digest;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:35` `use sha2::Sha256;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:36` `use std::collections::BTreeMap;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:37` `use std::fs;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:38` `use std::io::ErrorKind;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:39` `use std::path::PathBuf;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:40` `use std::sync::Arc;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:41` `use std::time::Duration;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:42` `use std::time::SystemTime;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:43` `use std::time::UNIX_EPOCH;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:44` `use tracing::warn;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:46` `use codex_keyring_store::DefaultKeyringStore;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:47` `use codex_keyring_store::KeyringStore;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:48` `use rmcp::transport::auth::AuthorizationManager;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:49` `use tokio::sync::Mutex;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:51` `use codex_utils_home_dir::find_codex_home;`
- `const` `codex-rs/rmcp-client/src/oauth.rs:53` `const KEYRING_SERVICE: &str = "Codex MCP Credentials";`
- `const` `codex-rs/rmcp-client/src/oauth.rs:54` `const REFRESH_SKEW_MILLIS: u64 = 30_000;`
- `struct` `codex-rs/rmcp-client/src/oauth.rs:57` `pub struct StoredOAuthTokens {`
- `enum` `codex-rs/rmcp-client/src/oauth.rs:69` `pub enum OAuthCredentialsStoreMode {`
- `struct` `codex-rs/rmcp-client/src/oauth.rs:83` `pub struct WrappedOAuthTokenResponse(pub OAuthTokenResponse);`
- `impl` `codex-rs/rmcp-client/src/oauth.rs:85` `impl PartialEq for WrappedOAuthTokenResponse {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:86` `fn eq(&self, other: &Self) -> bool {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:120` `fn refresh_expires_in_from_timestamp(tokens: &mut StoredOAuthTokens) {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:170` `pub fn save_oauth_tokens(`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:231` `pub fn delete_oauth_tokens(`
- `struct` `codex-rs/rmcp-client/src/oauth.rs:272` `struct OAuthPersistorInner {`
- `impl` `codex-rs/rmcp-client/src/oauth.rs:280` `impl OAuthPersistor {`
- `const` `codex-rs/rmcp-client/src/oauth.rs:378` `const FALLBACK_FILENAME: &str = ".credentials.json";`
- `const` `codex-rs/rmcp-client/src/oauth.rs:379` `const MCP_SERVER_TYPE: &str = "http";`
- `type` `codex-rs/rmcp-client/src/oauth.rs:381` `type FallbackFile = BTreeMap<String, FallbackTokenEntry>;`
- `struct` `codex-rs/rmcp-client/src/oauth.rs:384` `struct FallbackTokenEntry {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:397` `fn load_oauth_tokens_from_file(server_name: &str, url: &str) -> Result<Option<StoredOAuthTokens>> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:440` `fn save_oauth_tokens_to_file(tokens: &StoredOAuthTokens) -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:469` `fn delete_oauth_tokens_from_file(key: &str) -> Result<bool> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:498` `fn expires_in_from_timestamp(expires_at: u64) -> Option<u64> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:511` `fn token_needs_refresh(expires_at: Option<u64>) -> bool {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:524` `fn compute_store_key(server_name: &str, server_url: &str) -> Result<String> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:537` `fn fallback_file_path() -> Result<PathBuf> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:543` `fn read_fallback_file() -> Result<Option<FallbackFile>> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:565` `fn write_fallback_file(store: &FallbackFile) -> Result<()> {`
- `use` `codex-rs/rmcp-client/src/oauth.rs:584` `use std::os::unix::fs::PermissionsExt;`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:592` `fn sha_256_prefix(value: &Value) -> Result<String> {`
- `use` `codex-rs/rmcp-client/src/oauth.rs:605` `use super::*;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:606` `use anyhow::Result;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:607` `use keyring::Error as KeyringError;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:608` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:609` `use std::sync::Mutex;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:610` `use std::sync::MutexGuard;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:611` `use std::sync::OnceLock;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:612` `use std::sync::PoisonError;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:613` `use tempfile::tempdir;`
- `use` `codex-rs/rmcp-client/src/oauth.rs:615` `use codex_keyring_store::tests::MockKeyringStore;`
- `struct` `codex-rs/rmcp-client/src/oauth.rs:617` `struct TempCodexHome {`
- `impl` `codex-rs/rmcp-client/src/oauth.rs:622` `impl TempCodexHome {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:623` `fn new() -> Self {`
- `static` `codex-rs/rmcp-client/src/oauth.rs:624` `static LOCK: OnceLock<Mutex<()>> = OnceLock::new();`
- `impl` `codex-rs/rmcp-client/src/oauth.rs:640` `impl Drop for TempCodexHome {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:641` `fn drop(&mut self) {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:649` `fn load_oauth_tokens_reads_from_keyring_when_available() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:666` `fn load_oauth_tokens_falls_back_when_missing_in_keyring() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:685` `fn load_oauth_tokens_falls_back_when_keyring_errors() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:706` `fn save_oauth_tokens_prefers_keyring_when_available() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:728` `fn save_oauth_tokens_writes_fallback_when_keyring_fails() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:758` `fn delete_oauth_tokens_removes_all_storage() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:780` `fn delete_oauth_tokens_file_mode_removes_keyring_only_entry() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:802` `fn delete_oauth_tokens_propagates_keyring_errors() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:822` `fn refresh_expires_in_from_timestamp_restores_future_durations() {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:842` `fn refresh_expires_in_from_timestamp_clears_expired_tokens() {`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:858` `fn assert_tokens_match_without_expiry(`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:872` `fn assert_token_response_match_without_expiry(`
- `fn` `codex-rs/rmcp-client/src/oauth.rs:899` `fn sample_tokens() -> StoredOAuthTokens {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Error;`
- `use anyhow::Result;`
- `use oauth2::AccessToken;`
- `use oauth2::EmptyExtraTokenFields;`
- `use oauth2::RefreshToken;`
- `use oauth2::Scope;`
- `use oauth2::TokenResponse;`
- `use oauth2::basic::BasicTokenType;`
- `use rmcp::transport::auth::OAuthTokenResponse;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use serde_json::map::Map as JsonMap;`
- `use sha2::Digest;`
- `use sha2::Sha256;`
- `use std::collections::BTreeMap;`
- `use std::fs;`
- `use std::io::ErrorKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
