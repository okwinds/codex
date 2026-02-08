# `codex-rs/cloud-tasks-client/src/http.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `32703`
- sha256: `223ffa922dadfd482316273bc207c41267b7a4b2b24526614a6f0325ea81e697`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks-client/src/http.rs` (read)
- env: `CODEX_STARTING_DIFF`

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct HttpClient {`
- `pub fn new(base_url: impl Into<String>) -> anyhow::Result<Self> {`
- `pub fn with_bearer_token(mut self, token: impl Into<String>) -> Self {`
- `pub fn with_user_agent(mut self, ua: impl Into<String>) -> Self {`
- `pub fn with_chatgpt_account_id(mut self, account_id: impl Into<String>) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks-client/src/http.rs:1` `use crate::ApplyOutcome;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:2` `use crate::ApplyStatus;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:3` `use crate::AttemptStatus;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:4` `use crate::CloudBackend;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:5` `use crate::CloudTaskError;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:6` `use crate::DiffSummary;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:7` `use crate::Result;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:8` `use crate::TaskId;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:9` `use crate::TaskListPage;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:10` `use crate::TaskStatus;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:11` `use crate::TaskSummary;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:12` `use crate::TurnAttempt;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:13` `use crate::api::TaskText;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:14` `use chrono::DateTime;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:15` `use chrono::Utc;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:17` `use codex_backend_client as backend;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:18` `use codex_backend_client::CodeTaskDetailsResponseExt;`
- `struct` `codex-rs/cloud-tasks-client/src/http.rs:21` `pub struct HttpClient {`
- `impl` `codex-rs/cloud-tasks-client/src/http.rs:26` `impl HttpClient {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:27` `pub fn new(base_url: impl Into<String>) -> anyhow::Result<Self> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:33` `pub fn with_bearer_token(mut self, token: impl Into<String>) -> Self {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:38` `pub fn with_user_agent(mut self, ua: impl Into<String>) -> Self {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:43` `pub fn with_chatgpt_account_id(mut self, account_id: impl Into<String>) -> Self {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:48` `fn tasks_api(&self) -> api::Tasks<'_> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:52` `fn attempts_api(&self) -> api::Attempts<'_> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:56` `fn apply_api(&self) -> api::Apply<'_> {`
- `impl` `codex-rs/cloud-tasks-client/src/http.rs:62` `impl CloudBackend for HttpClient {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:63` `async fn list_tasks(`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:72` `async fn get_task_summary(&self, id: TaskId) -> Result<TaskSummary> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:76` `async fn get_task_diff(&self, id: TaskId) -> Result<Option<String>> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:80` `async fn get_task_messages(&self, id: TaskId) -> Result<Vec<String>> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:84` `async fn get_task_text(&self, id: TaskId) -> Result<TaskText> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:88` `async fn list_sibling_attempts(`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:96` `async fn apply_task(&self, id: TaskId, diff_override: Option<String>) -> Result<ApplyOutcome> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:100` `async fn apply_task_preflight(`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:108` `async fn create_task(`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:123` `use super::*;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:124` `use serde_json::Value;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:125` `use std::cmp::Ordering;`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:126` `use std::collections::HashMap;`
- `impl` `codex-rs/cloud-tasks-client/src/http.rs:133` `impl<'a> Tasks<'a> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:375` `async fn details_with_body(`
- `impl` `codex-rs/cloud-tasks-client/src/http.rs:388` `impl<'a> Attempts<'a> {`
- `impl` `codex-rs/cloud-tasks-client/src/http.rs:416` `impl<'a> Apply<'a> {`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:521` `use std::fmt::Write as _;`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:557` `fn details_path(base_url: &str, id: &str) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:567` `fn extract_assistant_messages_from_body(body: &str) -> Vec<String> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:610` `fn turn_attempt_from_map(turn: &HashMap<String, Value>) -> Option<TurnAttempt> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:627` `fn compare_attempts(a: &TurnAttempt, b: &TurnAttempt) -> Ordering {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:641` `fn extract_diff_from_turn(turn: &HashMap<String, Value>) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:669` `fn extract_assistant_messages_from_turn(turn: &HashMap<String, Value>) -> Vec<String> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:691` `fn attempt_status_from_str(raw: Option<&str>) -> AttemptStatus {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:701` `fn parse_timestamp_value(v: Option<&Value>) -> Option<DateTime<Utc>> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:710` `fn map_task_list_item_to_summary(src: backend::TaskListItem) -> TaskSummary {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:728` `fn map_status(v: Option<&HashMap<String, Value>>) -> TaskStatus {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:757` `fn parse_updated_at(ts: Option<&f64>) -> DateTime<Utc> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:768` `fn env_label_from_status_display(v: Option<&HashMap<String, Value>>) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:775` `fn diff_summary_from_diff(diff: &str) -> DiffSummary {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:803` `fn diff_summary_from_status_display(v: Option<&HashMap<String, Value>>) -> DiffSummary {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:824` `fn latest_turn_timestamp(v: Option<&HashMap<String, Value>>) -> Option<f64> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:835` `fn attempt_total_from_status_display(v: Option<&HashMap<String, Value>>) -> Option<usize> {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:844` `fn is_unified_diff(diff: &str) -> bool {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:854` `fn tail(s: &str, max: usize) -> String {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:862` `fn summarize_patch_for_logging(patch: &str) -> String {`
- `fn` `codex-rs/cloud-tasks-client/src/http.rs:891` `fn append_error_log(message: &str) {`
- `use` `codex-rs/cloud-tasks-client/src/http.rs:898` `use std::io::Write as _;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::ApplyOutcome;`
- `use crate::ApplyStatus;`
- `use crate::AttemptStatus;`
- `use crate::CloudBackend;`
- `use crate::CloudTaskError;`
- `use crate::DiffSummary;`
- `use crate::Result;`
- `use crate::TaskId;`
- `use crate::TaskListPage;`
- `use crate::TaskStatus;`
- `use crate::TaskSummary;`
- `use crate::TurnAttempt;`
- `use crate::api::TaskText;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_backend_client as backend;`
- `use codex_backend_client::CodeTaskDetailsResponseExt;`
- `use super::*;`
- `use serde_json::Value;`
- `use std::cmp::Ordering;`
### Referenced env vars
- `CODEX_STARTING_DIFF`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
