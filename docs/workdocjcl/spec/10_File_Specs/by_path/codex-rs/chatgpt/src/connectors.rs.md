# `codex-rs/chatgpt/src/connectors.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9766`
- sha256: `4644ac39209807a6ed02d5ab56876a2a8754d387d121b129008fa563f0020d9c`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/chatgpt/src/connectors.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/chatgpt/src/connectors.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/chatgpt/src/connectors.rs:3` `use codex_core::config::Config;`
- `use` `codex-rs/chatgpt/src/connectors.rs:4` `use codex_core::features::Feature;`
- `use` `codex-rs/chatgpt/src/connectors.rs:5` `use serde::Deserialize;`
- `use` `codex-rs/chatgpt/src/connectors.rs:6` `use std::time::Duration;`
- `use` `codex-rs/chatgpt/src/connectors.rs:8` `use crate::chatgpt_client::chatgpt_get_request_with_timeout;`
- `use` `codex-rs/chatgpt/src/connectors.rs:9` `use crate::chatgpt_token::get_chatgpt_token_data;`
- `use` `codex-rs/chatgpt/src/connectors.rs:10` `use crate::chatgpt_token::init_chatgpt_token_from_auth;`
- `use` `codex-rs/chatgpt/src/connectors.rs:14` `use codex_core::connectors::connector_install_url;`
- `use` `codex-rs/chatgpt/src/connectors.rs:16` `use codex_core::connectors::merge_connectors;`
- `struct` `codex-rs/chatgpt/src/connectors.rs:19` `struct DirectoryListResponse {`
- `struct` `codex-rs/chatgpt/src/connectors.rs:26` `struct DirectoryApp {`
- `const` `codex-rs/chatgpt/src/connectors.rs:39` `const DIRECTORY_CONNECTORS_TIMEOUT: Duration = Duration::from_secs(60);`
- `fn` `codex-rs/chatgpt/src/connectors.rs:41` `pub async fn list_connectors(config: &Config) -> anyhow::Result<Vec<AppInfo>> {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:55` `pub async fn list_all_connectors(config: &Config) -> anyhow::Result<Vec<AppInfo>> {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:90` `async fn list_directory_connectors(config: &Config) -> anyhow::Result<Vec<DirectoryApp>> {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:121` `async fn list_workspace_connectors(config: &Config) -> anyhow::Result<Vec<DirectoryApp>> {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:138` `fn merge_directory_apps(apps: Vec<DirectoryApp>) -> Vec<DirectoryApp> {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:150` `fn merge_directory_app(existing: &mut DirectoryApp, incoming: DirectoryApp) {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:190` `fn is_hidden_directory_app(app: &DirectoryApp) -> bool {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:194` `fn directory_app_to_app_info(app: DirectoryApp) -> AppInfo {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:207` `fn normalize_connector_name(name: &str, connector_id: &str) -> String {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:216` `fn normalize_connector_value(value: Option<&str>) -> Option<String> {`
- `const` `codex-rs/chatgpt/src/connectors.rs:223` `const ALLOWED_APPS_SDK_APPS: &[&str] = &["asdk_app_69781557cc1481919cf5e9824fa2e792"];`
- `const` `codex-rs/chatgpt/src/connectors.rs:224` `const DISALLOWED_CONNECTOR_IDS: &[&str] = &[`
- `const` `codex-rs/chatgpt/src/connectors.rs:229` `const DISALLOWED_CONNECTOR_PREFIX: &str = "connector_openai_";`
- `fn` `codex-rs/chatgpt/src/connectors.rs:231` `fn filter_disallowed_connectors(connectors: Vec<AppInfo>) -> Vec<AppInfo> {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:239` `fn is_connector_allowed(connector: &AppInfo) -> bool {`
- `use` `codex-rs/chatgpt/src/connectors.rs:254` `use super::*;`
- `use` `codex-rs/chatgpt/src/connectors.rs:255` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/chatgpt/src/connectors.rs:257` `fn app(id: &str) -> AppInfo {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:271` `fn filters_internal_asdk_connectors() {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:277` `fn allows_whitelisted_asdk_connectors() {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:292` `fn filters_openai_connectors() {`
- `fn` `codex-rs/chatgpt/src/connectors.rs:302` `fn filters_disallowed_connector_ids() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use codex_core::config::Config;`
- `use codex_core::features::Feature;`
- `use serde::Deserialize;`
- `use std::time::Duration;`
- `use crate::chatgpt_client::chatgpt_get_request_with_timeout;`
- `use crate::chatgpt_token::get_chatgpt_token_data;`
- `use crate::chatgpt_token::init_chatgpt_token_from_auth;`
- `use codex_core::connectors::connector_install_url;`
- `use codex_core::connectors::merge_connectors;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
