# `codex-rs/cloud-requirements/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17464`
- sha256: `bdd2eb1e24518abdbd97e5cc82641dee25055a6322aa96440df9222cd885e383`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-requirements/src/lib.rs` (read)

### Outputs / Side Effects
- performs network I/O
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn cloud_requirements_loader(`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-requirements/src/lib.rs:11` `use async_trait::async_trait;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:12` `use codex_backend_client::Client as BackendClient;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:13` `use codex_core::AuthManager;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:14` `use codex_core::auth::CodexAuth;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:15` `use codex_core::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:16` `use codex_core::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:17` `use codex_core::util::backoff;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:18` `use codex_protocol::account::PlanType;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:19` `use std::sync::Arc;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:20` `use std::time::Duration;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:21` `use std::time::Instant;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:22` `use tokio::time::sleep;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:23` `use tokio::time::timeout;`
- `const` `codex-rs/cloud-requirements/src/lib.rs:25` `const CLOUD_REQUIREMENTS_TIMEOUT: Duration = Duration::from_secs(15);`
- `const` `codex-rs/cloud-requirements/src/lib.rs:26` `const CLOUD_REQUIREMENTS_MAX_ATTEMPTS: usize = 5;`
- `enum` `codex-rs/cloud-requirements/src/lib.rs:29` `enum FetchCloudRequirementsStatus {`
- `trait` `codex-rs/cloud-requirements/src/lib.rs:36` `trait RequirementsFetcher: Send + Sync {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:40` `async fn fetch_requirements(`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:46` `struct BackendRequirementsFetcher {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:50` `impl BackendRequirementsFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:51` `fn new(base_url: String) -> Self {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:57` `impl RequirementsFetcher for BackendRequirementsFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:58` `async fn fetch_requirements(`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:88` `struct CloudRequirementsService {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:94` `impl CloudRequirementsService {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:95` `fn new(`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:107` `async fn fetch_with_timeout(&self) -> Option<ConfigRequirementsToml> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:137` `async fn fetch(&self) -> Option<ConfigRequirementsToml> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:151` `async fn fetch_with_retries(&self, auth: &CodexAuth) -> Option<ConfigRequirementsToml> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:186` `pub fn cloud_requirements_loader(`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:204` `fn parse_cloud_requirements(`
- `use` `codex-rs/cloud-requirements/src/lib.rs:221` `use super::*;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:222` `use base64::Engine;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:223` `use base64::engine::general_purpose::URL_SAFE_NO_PAD;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:224` `use codex_core::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:225` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:226` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:227` `use serde_json::json;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:228` `use std::collections::VecDeque;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:229` `use std::future::pending;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:230` `use std::path::Path;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:231` `use std::sync::atomic::AtomicUsize;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:232` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:233` `use tempfile::tempdir;`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:235` `fn write_auth_json(codex_home: &Path, value: serde_json::Value) -> std::io::Result<()> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:240` `fn auth_manager_with_api_key() -> Arc<AuthManager> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:255` `fn auth_manager_with_plan(plan_type: &str) -> Arc<AuthManager> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:289` `fn parse_for_fetch(contents: Option<&str>) -> Option<ConfigRequirementsToml> {`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:293` `struct StaticFetcher {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:298` `impl RequirementsFetcher for StaticFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:299` `async fn fetch_requirements(`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:307` `struct PendingFetcher;`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:310` `impl RequirementsFetcher for PendingFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:311` `async fn fetch_requirements(`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:320` `struct SequenceFetcher {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:326` `impl SequenceFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:327` `fn new(responses: Vec<Result<Option<String>, FetchCloudRequirementsStatus>>) -> Self {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:336` `impl RequirementsFetcher for SequenceFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:337` `async fn fetch_requirements(`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:348` `async fn fetch_cloud_requirements_skips_non_chatgpt_auth() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:360` `async fn fetch_cloud_requirements_skips_non_business_or_enterprise_plan() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:371` `async fn fetch_cloud_requirements_allows_business_plan() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:394` `async fn fetch_cloud_requirements_handles_missing_contents() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:400` `async fn fetch_cloud_requirements_handles_empty_contents() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:406` `async fn fetch_cloud_requirements_handles_invalid_toml() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:412` `async fn fetch_cloud_requirements_ignores_empty_requirements() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:418` `async fn fetch_cloud_requirements_parses_valid_toml() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:436` `async fn fetch_cloud_requirements_times_out() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:451` `async fn fetch_cloud_requirements_retries_until_success() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:482` `async fn fetch_cloud_requirements_none_is_success_without_retry() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:498` `async fn fetch_cloud_requirements_stops_after_max_retries() {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use codex_backend_client::Client as BackendClient;`
- `use codex_core::AuthManager;`
- `use codex_core::auth::CodexAuth;`
- `use codex_core::config_loader::CloudRequirementsLoader;`
- `use codex_core::config_loader::ConfigRequirementsToml;`
- `use codex_core::util::backoff;`
- `use codex_protocol::account::PlanType;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use tokio::time::sleep;`
- `use tokio::time::timeout;`
- `use super::*;`
- `use base64::Engine;`
- `use base64::engine::general_purpose::URL_SAFE_NO_PAD;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_protocol::protocol::AskForApproval;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
