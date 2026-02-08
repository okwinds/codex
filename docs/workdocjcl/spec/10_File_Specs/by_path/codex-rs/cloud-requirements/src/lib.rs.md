# `codex-rs/cloud-requirements/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11863`
- sha256: `d8884331891fbeb861b941d6fadaab1ced23d0e9a38a6b9d47a406721d731329`
- generated_utc: `2026-02-03T16:08:28Z`

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
- `use` `codex-rs/cloud-requirements/src/lib.rs:17` `use codex_protocol::account::PlanType;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:18` `use std::sync::Arc;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:19` `use std::time::Duration;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:20` `use std::time::Instant;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:21` `use tokio::time::timeout;`
- `const` `codex-rs/cloud-requirements/src/lib.rs:24` `const CLOUD_REQUIREMENTS_TIMEOUT: Duration = Duration::from_secs(5);`
- `trait` `codex-rs/cloud-requirements/src/lib.rs:27` `trait RequirementsFetcher: Send + Sync {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:32` `async fn fetch_requirements(&self, auth: &CodexAuth) -> Option<String>;`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:35` `struct BackendRequirementsFetcher {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:39` `impl BackendRequirementsFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:40` `fn new(base_url: String) -> Self {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:46` `impl RequirementsFetcher for BackendRequirementsFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:47` `async fn fetch_requirements(&self, auth: &CodexAuth) -> Option<String> {`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:72` `struct CloudRequirementsService {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:78` `impl CloudRequirementsService {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:79` `fn new(`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:91` `async fn fetch_with_timeout(&self) -> Option<ConfigRequirementsToml> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:121` `async fn fetch(&self) -> Option<ConfigRequirementsToml> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:140` `pub fn cloud_requirements_loader(`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:158` `fn parse_cloud_requirements(`
- `use` `codex-rs/cloud-requirements/src/lib.rs:175` `use super::*;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:176` `use base64::Engine;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:177` `use base64::engine::general_purpose::URL_SAFE_NO_PAD;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:178` `use codex_core::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:179` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:180` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:181` `use serde_json::json;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:182` `use std::future::pending;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:183` `use std::path::Path;`
- `use` `codex-rs/cloud-requirements/src/lib.rs:184` `use tempfile::tempdir;`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:186` `fn write_auth_json(codex_home: &Path, value: serde_json::Value) -> std::io::Result<()> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:191` `fn auth_manager_with_api_key() -> Arc<AuthManager> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:206` `fn auth_manager_with_plan(plan_type: &str) -> Arc<AuthManager> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:240` `fn parse_for_fetch(contents: Option<&str>) -> Option<ConfigRequirementsToml> {`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:244` `struct StaticFetcher {`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:249` `impl RequirementsFetcher for StaticFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:250` `async fn fetch_requirements(&self, _auth: &CodexAuth) -> Option<String> {`
- `struct` `codex-rs/cloud-requirements/src/lib.rs:255` `struct PendingFetcher;`
- `impl` `codex-rs/cloud-requirements/src/lib.rs:258` `impl RequirementsFetcher for PendingFetcher {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:259` `async fn fetch_requirements(&self, _auth: &CodexAuth) -> Option<String> {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:266` `async fn fetch_cloud_requirements_skips_non_chatgpt_auth() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:278` `async fn fetch_cloud_requirements_skips_non_business_or_enterprise_plan() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:289` `async fn fetch_cloud_requirements_allows_business_plan() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:310` `async fn fetch_cloud_requirements_handles_missing_contents() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:316` `async fn fetch_cloud_requirements_handles_empty_contents() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:322` `async fn fetch_cloud_requirements_handles_invalid_toml() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:328` `async fn fetch_cloud_requirements_ignores_empty_requirements() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:334` `async fn fetch_cloud_requirements_parses_valid_toml() {`
- `fn` `codex-rs/cloud-requirements/src/lib.rs:350` `async fn fetch_cloud_requirements_times_out() {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use codex_backend_client::Client as BackendClient;`
- `use codex_core::AuthManager;`
- `use codex_core::auth::CodexAuth;`
- `use codex_core::config_loader::CloudRequirementsLoader;`
- `use codex_core::config_loader::ConfigRequirementsToml;`
- `use codex_protocol::account::PlanType;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use tokio::time::timeout;`
- `use super::*;`
- `use base64::Engine;`
- `use base64::engine::general_purpose::URL_SAFE_NO_PAD;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_protocol::protocol::AskForApproval;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::json;`
- `use std::future::pending;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
