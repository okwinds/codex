# `codex-rs/backend-client/src/client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13722`
- sha256: `b2e7f380231e1df66621cc5fd0920908cd826835d0098986188e0506b6bdb698`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/backend-client/src/client.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub enum PathStyle {`
- `pub fn from_base_url(base_url: &str) -> Self {`
- `pub struct Client {`
- `pub fn new(base_url: impl Into<String>) -> Result<Self> {`
- `pub fn from_auth(base_url: impl Into<String>, auth: &CodexAuth) -> Result<Self> {`
- `pub fn with_bearer_token(mut self, token: impl Into<String>) -> Self {`
- `pub fn with_user_agent(mut self, ua: impl Into<String>) -> Self {`
- `pub fn with_chatgpt_account_id(mut self, account_id: impl Into<String>) -> Self {`
- `pub fn with_path_style(mut self, style: PathStyle) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/backend-client/src/client.rs:1` `use crate::types::CodeTaskDetailsResponse;`
- `use` `codex-rs/backend-client/src/client.rs:2` `use crate::types::ConfigFileResponse;`
- `use` `codex-rs/backend-client/src/client.rs:3` `use crate::types::CreditStatusDetails;`
- `use` `codex-rs/backend-client/src/client.rs:4` `use crate::types::PaginatedListTaskListItem;`
- `use` `codex-rs/backend-client/src/client.rs:5` `use crate::types::RateLimitStatusPayload;`
- `use` `codex-rs/backend-client/src/client.rs:6` `use crate::types::RateLimitWindowSnapshot;`
- `use` `codex-rs/backend-client/src/client.rs:7` `use crate::types::TurnAttemptsSiblingTurnsResponse;`
- `use` `codex-rs/backend-client/src/client.rs:8` `use anyhow::Result;`
- `use` `codex-rs/backend-client/src/client.rs:9` `use codex_core::auth::CodexAuth;`
- `use` `codex-rs/backend-client/src/client.rs:10` `use codex_core::default_client::get_codex_user_agent;`
- `use` `codex-rs/backend-client/src/client.rs:11` `use codex_protocol::account::PlanType as AccountPlanType;`
- `use` `codex-rs/backend-client/src/client.rs:12` `use codex_protocol::protocol::CreditsSnapshot;`
- `use` `codex-rs/backend-client/src/client.rs:13` `use codex_protocol::protocol::RateLimitSnapshot;`
- `use` `codex-rs/backend-client/src/client.rs:14` `use codex_protocol::protocol::RateLimitWindow;`
- `use` `codex-rs/backend-client/src/client.rs:15` `use reqwest::header::AUTHORIZATION;`
- `use` `codex-rs/backend-client/src/client.rs:16` `use reqwest::header::CONTENT_TYPE;`
- `use` `codex-rs/backend-client/src/client.rs:17` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/backend-client/src/client.rs:18` `use reqwest::header::HeaderName;`
- `use` `codex-rs/backend-client/src/client.rs:19` `use reqwest::header::HeaderValue;`
- `use` `codex-rs/backend-client/src/client.rs:20` `use reqwest::header::USER_AGENT;`
- `use` `codex-rs/backend-client/src/client.rs:21` `use serde::de::DeserializeOwned;`
- `enum` `codex-rs/backend-client/src/client.rs:24` `pub enum PathStyle {`
- `impl` `codex-rs/backend-client/src/client.rs:31` `impl PathStyle {`
- `fn` `codex-rs/backend-client/src/client.rs:32` `pub fn from_base_url(base_url: &str) -> Self {`
- `struct` `codex-rs/backend-client/src/client.rs:42` `pub struct Client {`
- `impl` `codex-rs/backend-client/src/client.rs:51` `impl Client {`
- `fn` `codex-rs/backend-client/src/client.rs:52` `pub fn new(base_url: impl Into<String>) -> Result<Self> {`
- `fn` `codex-rs/backend-client/src/client.rs:77` `pub fn from_auth(base_url: impl Into<String>, auth: &CodexAuth) -> Result<Self> {`
- `fn` `codex-rs/backend-client/src/client.rs:88` `pub fn with_bearer_token(mut self, token: impl Into<String>) -> Self {`
- `fn` `codex-rs/backend-client/src/client.rs:93` `pub fn with_user_agent(mut self, ua: impl Into<String>) -> Self {`
- `fn` `codex-rs/backend-client/src/client.rs:100` `pub fn with_chatgpt_account_id(mut self, account_id: impl Into<String>) -> Self {`
- `fn` `codex-rs/backend-client/src/client.rs:105` `pub fn with_path_style(mut self, style: PathStyle) -> Self {`
- `fn` `codex-rs/backend-client/src/client.rs:110` `fn headers(&self) -> HeaderMap {`
- `fn` `codex-rs/backend-client/src/client.rs:132` `async fn exec_request(`
- `fn` `codex-rs/backend-client/src/client.rs:162` `pub async fn get_rate_limits(&self) -> Result<RateLimitSnapshot> {`
- `fn` `codex-rs/backend-client/src/client.rs:173` `pub async fn list_tasks(`
- `fn` `codex-rs/backend-client/src/client.rs:209` `pub async fn get_task_details(&self, task_id: &str) -> Result<CodeTaskDetailsResponse> {`
- `fn` `codex-rs/backend-client/src/client.rs:214` `pub async fn get_task_details_with_body(`
- `fn` `codex-rs/backend-client/src/client.rs:228` `pub async fn list_sibling_turns(`
- `fn` `codex-rs/backend-client/src/client.rs:252` `pub async fn get_config_requirements_file(&self) -> Result<ConfigFileResponse> {`
- `fn` `codex-rs/backend-client/src/client.rs:264` `pub async fn create_task(&self, request_body: serde_json::Value) -> Result<String> {`
- `fn` `codex-rs/backend-client/src/client.rs:298` `fn rate_limit_snapshot_from_payload(payload: RateLimitStatusPayload) -> RateLimitSnapshot {`
- `fn` `codex-rs/backend-client/src/client.rs:320` `fn map_rate_limit_window(`
- `fn` `codex-rs/backend-client/src/client.rs:338` `fn map_credits(credits: Option<Option<Box<CreditStatusDetails>>>) -> Option<CreditsSnapshot> {`
- `fn` `codex-rs/backend-client/src/client.rs:351` `fn map_plan_type(plan_type: crate::types::PlanType) -> AccountPlanType {`
- `fn` `codex-rs/backend-client/src/client.rs:368` `fn window_minutes_from_seconds(seconds: i32) -> Option<i64> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::types::CodeTaskDetailsResponse;`
- `use crate::types::ConfigFileResponse;`
- `use crate::types::CreditStatusDetails;`
- `use crate::types::PaginatedListTaskListItem;`
- `use crate::types::RateLimitStatusPayload;`
- `use crate::types::RateLimitWindowSnapshot;`
- `use crate::types::TurnAttemptsSiblingTurnsResponse;`
- `use anyhow::Result;`
- `use codex_core::auth::CodexAuth;`
- `use codex_core::default_client::get_codex_user_agent;`
- `use codex_protocol::account::PlanType as AccountPlanType;`
- `use codex_protocol::protocol::CreditsSnapshot;`
- `use codex_protocol::protocol::RateLimitSnapshot;`
- `use codex_protocol::protocol::RateLimitWindow;`
- `use reqwest::header::AUTHORIZATION;`
- `use reqwest::header::CONTENT_TYPE;`
- `use reqwest::header::HeaderMap;`
- `use reqwest::header::HeaderName;`
- `use reqwest::header::HeaderValue;`
- `use reqwest::header::USER_AGENT;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
