# `codex-rs/cloud-tasks/src/util.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4813`
- sha256: `146d375e6056d3b0d5db31ecc01505815681af2daafadd748405cba1a1a36719`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/util.rs` (read)

### Outputs / Side Effects
- performs network I/O
- writes to filesystem

## Public Surface (auto)
- `pub fn set_user_agent_suffix(suffix: &str) {`
- `pub fn append_error_log(message: impl AsRef<str>) {`
- `pub fn normalize_base_url(input: &str) -> String {`
- `pub fn extract_chatgpt_account_id(token: &str) -> Option<String> {`
- `pub fn task_url(base_url: &str, task_id: &str) -> String {`
- `pub fn format_relative_time(reference: DateTime<Utc>, ts: DateTime<Utc>) -> String {`
- `pub fn format_relative_time_now(ts: DateTime<Utc>) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks/src/util.rs:1` `use base64::Engine as _;`
- `use` `codex-rs/cloud-tasks/src/util.rs:2` `use chrono::DateTime;`
- `use` `codex-rs/cloud-tasks/src/util.rs:3` `use chrono::Local;`
- `use` `codex-rs/cloud-tasks/src/util.rs:4` `use chrono::Utc;`
- `use` `codex-rs/cloud-tasks/src/util.rs:5` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/cloud-tasks/src/util.rs:7` `use codex_core::config::Config;`
- `use` `codex-rs/cloud-tasks/src/util.rs:8` `use codex_login::AuthManager;`
- `fn` `codex-rs/cloud-tasks/src/util.rs:10` `pub fn set_user_agent_suffix(suffix: &str) {`
- `fn` `codex-rs/cloud-tasks/src/util.rs:16` `pub fn append_error_log(message: impl AsRef<str>) {`
- `use` `codex-rs/cloud-tasks/src/util.rs:23` `use std::io::Write as _;`
- `fn` `codex-rs/cloud-tasks/src/util.rs:31` `pub fn normalize_base_url(input: &str) -> String {`
- `fn` `codex-rs/cloud-tasks/src/util.rs:46` `pub fn extract_chatgpt_account_id(token: &str) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks/src/util.rs:62` `pub async fn load_auth_manager() -> Option<AuthManager> {`
- `fn` `codex-rs/cloud-tasks/src/util.rs:74` `pub async fn build_chatgpt_headers() -> HeaderMap {`
- `use` `codex-rs/cloud-tasks/src/util.rs:75` `use reqwest::header::AUTHORIZATION;`
- `use` `codex-rs/cloud-tasks/src/util.rs:76` `use reqwest::header::HeaderName;`
- `use` `codex-rs/cloud-tasks/src/util.rs:77` `use reqwest::header::HeaderValue;`
- `use` `codex-rs/cloud-tasks/src/util.rs:78` `use reqwest::header::USER_AGENT;`
- `fn` `codex-rs/cloud-tasks/src/util.rs:109` `pub fn task_url(base_url: &str, task_id: &str) -> String {`
- `fn` `codex-rs/cloud-tasks/src/util.rs:123` `pub fn format_relative_time(reference: DateTime<Utc>, ts: DateTime<Utc>) -> String {`
- `fn` `codex-rs/cloud-tasks/src/util.rs:143` `pub fn format_relative_time_now(ts: DateTime<Utc>) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use base64::Engine as _;`
- `use chrono::DateTime;`
- `use chrono::Local;`
- `use chrono::Utc;`
- `use reqwest::header::HeaderMap;`
- `use codex_core::config::Config;`
- `use codex_login::AuthManager;`
- `use std::io::Write as _;`
- `use reqwest::header::AUTHORIZATION;`
- `use reqwest::header::HeaderName;`
- `use reqwest::header::HeaderValue;`
- `use reqwest::header::USER_AGENT;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
