# `codex-rs/core/src/models_manager/manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `29247`
- sha256: `6d76bae986c0aea7d9f0f9264c0204ebcb8436b3d2634790c4d969277545e1f0`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/models_manager/manager.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum RefreshStrategy {`
- `pub struct ModelsManager {`
- `pub fn new(codex_home: PathBuf, auth_manager: Arc<AuthManager>) -> Self {`
- `pub fn list_collaboration_modes(&self) -> Vec<CollaborationModeMask> {`
- `pub fn try_list_models(&self, config: &Config) -> Result<Vec<ModelPreset>, TryLockError> {`
- `pub fn with_provider(`
- `pub fn get_model_offline(model: Option<&str>) -> String {`
- `pub fn construct_model_info_offline(model: &str, config: &Config) -> ModelInfo {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/models_manager/manager.rs:1` `use super::cache::ModelsCacheManager;`
- `use` `codex-rs/core/src/models_manager/manager.rs:2` `use crate::api_bridge::auth_provider_from_auth;`
- `use` `codex-rs/core/src/models_manager/manager.rs:3` `use crate::api_bridge::map_api_error;`
- `use` `codex-rs/core/src/models_manager/manager.rs:4` `use crate::auth::AuthManager;`
- `use` `codex-rs/core/src/models_manager/manager.rs:5` `use crate::auth::AuthMode;`
- `use` `codex-rs/core/src/models_manager/manager.rs:6` `use crate::config::Config;`
- `use` `codex-rs/core/src/models_manager/manager.rs:7` `use crate::default_client::build_reqwest_client;`
- `use` `codex-rs/core/src/models_manager/manager.rs:8` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/models_manager/manager.rs:9` `use crate::error::Result as CoreResult;`
- `use` `codex-rs/core/src/models_manager/manager.rs:10` `use crate::features::Feature;`
- `use` `codex-rs/core/src/models_manager/manager.rs:11` `use crate::model_provider_info::ModelProviderInfo;`
- `use` `codex-rs/core/src/models_manager/manager.rs:12` `use crate::models_manager::collaboration_mode_presets::builtin_collaboration_mode_presets;`
- `use` `codex-rs/core/src/models_manager/manager.rs:13` `use crate::models_manager::model_info;`
- `use` `codex-rs/core/src/models_manager/manager.rs:14` `use crate::models_manager::model_presets::builtin_model_presets;`
- `use` `codex-rs/core/src/models_manager/manager.rs:15` `use codex_api::ModelsClient;`
- `use` `codex-rs/core/src/models_manager/manager.rs:16` `use codex_api::ReqwestTransport;`
- `use` `codex-rs/core/src/models_manager/manager.rs:17` `use codex_protocol::config_types::CollaborationModeMask;`
- `use` `codex-rs/core/src/models_manager/manager.rs:18` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/models_manager/manager.rs:19` `use codex_protocol::openai_models::ModelPreset;`
- `use` `codex-rs/core/src/models_manager/manager.rs:20` `use codex_protocol::openai_models::ModelsResponse;`
- `use` `codex-rs/core/src/models_manager/manager.rs:21` `use http::HeaderMap;`
- `use` `codex-rs/core/src/models_manager/manager.rs:22` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/models_manager/manager.rs:23` `use std::sync::Arc;`
- `use` `codex-rs/core/src/models_manager/manager.rs:24` `use std::time::Duration;`
- `use` `codex-rs/core/src/models_manager/manager.rs:25` `use tokio::sync::RwLock;`
- `use` `codex-rs/core/src/models_manager/manager.rs:26` `use tokio::sync::TryLockError;`
- `use` `codex-rs/core/src/models_manager/manager.rs:27` `use tokio::time::timeout;`
- `use` `codex-rs/core/src/models_manager/manager.rs:28` `use tracing::error;`
- `const` `codex-rs/core/src/models_manager/manager.rs:30` `const MODEL_CACHE_FILE: &str = "models_cache.json";`
- `const` `codex-rs/core/src/models_manager/manager.rs:31` `const DEFAULT_MODEL_CACHE_TTL: Duration = Duration::from_secs(300);`
- `const` `codex-rs/core/src/models_manager/manager.rs:32` `const MODELS_REFRESH_TIMEOUT: Duration = Duration::from_secs(5);`
- `enum` `codex-rs/core/src/models_manager/manager.rs:36` `pub enum RefreshStrategy {`
- `struct` `codex-rs/core/src/models_manager/manager.rs:47` `pub struct ModelsManager {`
- `impl` `codex-rs/core/src/models_manager/manager.rs:56` `impl ModelsManager {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:60` `pub fn new(codex_home: PathBuf, auth_manager: Arc<AuthManager>) -> Self {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:76` `pub async fn list_models(`
- `fn` `codex-rs/core/src/models_manager/manager.rs:94` `pub fn list_collaboration_modes(&self) -> Vec<CollaborationModeMask> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:101` `pub fn try_list_models(&self, config: &Config) -> Result<Vec<ModelPreset>, TryLockError> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:111` `pub async fn get_default_model(`
- `fn` `codex-rs/core/src/models_manager/manager.rs:138` `pub async fn get_model_info(&self, model: &str, config: &Config) -> ModelInfo {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:172` `async fn refresh_available_models(`
- `fn` `codex-rs/core/src/models_manager/manager.rs:203` `async fn fetch_and_update_models(&self) -> CoreResult<()> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:230` `async fn get_etag(&self) -> Option<String> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:235` `async fn apply_remote_models(&self, models: Vec<ModelInfo>) {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:250` `fn load_remote_models_from_file() -> Result<Vec<ModelInfo>, std::io::Error> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:257` `async fn try_load_cache(&self) -> bool {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:272` `fn build_available_models(&self, mut remote_models: Vec<ModelInfo>) -> Vec<ModelPreset> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:296` `async fn get_remote_models(&self, config: &Config) -> Vec<ModelInfo> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:304` `fn try_get_remote_models(&self, config: &Config) -> Result<Vec<ModelInfo>, TryLockError> {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:314` `pub fn with_provider(`
- `fn` `codex-rs/core/src/models_manager/manager.rs:333` `pub fn get_model_offline(model: Option<&str>) -> String {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:348` `pub fn construct_model_info_offline(model: &str, config: &Config) -> ModelInfo {`
- `use` `codex-rs/core/src/models_manager/manager.rs:355` `use super::*;`
- `use` `codex-rs/core/src/models_manager/manager.rs:356` `use crate::CodexAuth;`
- `use` `codex-rs/core/src/models_manager/manager.rs:357` `use crate::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/core/src/models_manager/manager.rs:358` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/models_manager/manager.rs:359` `use crate::features::Feature;`
- `use` `codex-rs/core/src/models_manager/manager.rs:360` `use crate::model_provider_info::WireApi;`
- `use` `codex-rs/core/src/models_manager/manager.rs:361` `use chrono::Utc;`
- `use` `codex-rs/core/src/models_manager/manager.rs:362` `use codex_protocol::openai_models::ModelsResponse;`
- `use` `codex-rs/core/src/models_manager/manager.rs:363` `use core_test_support::responses::mount_models_once;`
- `use` `codex-rs/core/src/models_manager/manager.rs:364` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/models_manager/manager.rs:365` `use serde_json::json;`
- `use` `codex-rs/core/src/models_manager/manager.rs:366` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/models_manager/manager.rs:367` `use wiremock::MockServer;`
- `fn` `codex-rs/core/src/models_manager/manager.rs:369` `fn remote_model(slug: &str, display: &str, priority: i32) -> ModelInfo {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:373` `fn remote_model_with_visibility(`
- `fn` `codex-rs/core/src/models_manager/manager.rs:404` `fn assert_models_contain(actual: &[ModelInfo], expected: &[ModelInfo]) {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:414` `fn provider_for(base_url: String) -> ModelProviderInfo {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:434` `async fn refresh_available_models_sorts_by_priority() {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:491` `async fn refresh_available_models_uses_cache_when_fresh() {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:538` `async fn refresh_available_models_refetches_when_cache_stale() {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:607` `async fn refresh_available_models_refetches_when_version_mismatch() {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:676` `async fn refresh_available_models_drops_removed_remote_models() {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:745` `fn build_available_models_picks_default_after_hiding_hidden_models() {`
- `fn` `codex-rs/core/src/models_manager/manager.rs:767` `fn bundled_models_json_roundtrips() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::cache::ModelsCacheManager;`
- `use crate::api_bridge::auth_provider_from_auth;`
- `use crate::api_bridge::map_api_error;`
- `use crate::auth::AuthManager;`
- `use crate::auth::AuthMode;`
- `use crate::config::Config;`
- `use crate::default_client::build_reqwest_client;`
- `use crate::error::CodexErr;`
- `use crate::error::Result as CoreResult;`
- `use crate::features::Feature;`
- `use crate::model_provider_info::ModelProviderInfo;`
- `use crate::models_manager::collaboration_mode_presets::builtin_collaboration_mode_presets;`
- `use crate::models_manager::model_info;`
- `use crate::models_manager::model_presets::builtin_model_presets;`
- `use codex_api::ModelsClient;`
- `use codex_api::ReqwestTransport;`
- `use codex_protocol::config_types::CollaborationModeMask;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelPreset;`
- `use codex_protocol::openai_models::ModelsResponse;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
