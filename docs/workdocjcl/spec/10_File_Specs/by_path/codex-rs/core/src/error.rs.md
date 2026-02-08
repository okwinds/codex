# `codex-rs/core/src/error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `40642`
- sha256: `cdd4ee40266ac492acf8ca912d978dc3a88634cc22f003e380bf68622fccb981`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/error.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub enum SandboxErr {`
- `pub enum CodexErr {`
- `pub fn is_retryable(&self) -> bool {`
- `pub struct ConnectionFailedError {`
- `pub struct ResponseStreamFailed {`
- `pub struct RefreshTokenFailedError {`
- `pub fn new(reason: RefreshTokenFailedReason, message: impl Into<String>) -> Self {`
- `pub enum RefreshTokenFailedReason {`
- `pub struct UnexpectedResponseError {`
- `pub struct RetryLimitReachedError {`
- `pub struct UsageLimitReachedError {`
- `pub struct ModelCapError {`
- `pub struct EnvVarError {`
- `pub fn to_codex_protocol_error(&self) -> CodexErrorInfo {`
- `pub fn to_error_event(&self, message_prefix: Option<String>) -> ErrorEvent {`
- `pub fn http_status_code_value(&self) -> Option<u16> {`
- `pub fn get_error_message_ui(e: &CodexErr) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/error.rs:1` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/error.rs:2` `use crate::token_data::KnownPlan;`
- `use` `codex-rs/core/src/error.rs:3` `use crate::token_data::PlanType;`
- `use` `codex-rs/core/src/error.rs:4` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/error.rs:5` `use crate::truncate::truncate_text;`
- `use` `codex-rs/core/src/error.rs:6` `use chrono::DateTime;`
- `use` `codex-rs/core/src/error.rs:7` `use chrono::Datelike;`
- `use` `codex-rs/core/src/error.rs:8` `use chrono::Local;`
- `use` `codex-rs/core/src/error.rs:9` `use chrono::Utc;`
- `use` `codex-rs/core/src/error.rs:10` `use codex_async_utils::CancelErr;`
- `use` `codex-rs/core/src/error.rs:11` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/error.rs:12` `use codex_protocol::protocol::CodexErrorInfo;`
- `use` `codex-rs/core/src/error.rs:13` `use codex_protocol::protocol::ErrorEvent;`
- `use` `codex-rs/core/src/error.rs:14` `use codex_protocol::protocol::RateLimitSnapshot;`
- `use` `codex-rs/core/src/error.rs:15` `use reqwest::StatusCode;`
- `use` `codex-rs/core/src/error.rs:16` `use serde_json;`
- `use` `codex-rs/core/src/error.rs:17` `use std::io;`
- `use` `codex-rs/core/src/error.rs:18` `use std::time::Duration;`
- `use` `codex-rs/core/src/error.rs:19` `use thiserror::Error;`
- `use` `codex-rs/core/src/error.rs:20` `use tokio::task::JoinError;`
- `type` `codex-rs/core/src/error.rs:22` `pub type Result<T> = std::result::Result<T, CodexErr>;`
- `const` `codex-rs/core/src/error.rs:25` `const ERROR_MESSAGE_UI_MAX_BYTES: usize = 2 * 1024; // 2 KiB`
- `enum` `codex-rs/core/src/error.rs:28` `pub enum SandboxErr {`
- `enum` `codex-rs/core/src/error.rs:60` `pub enum CodexErr {`
- `impl` `codex-rs/core/src/error.rs:184` `impl From<CancelErr> for CodexErr {`
- `fn` `codex-rs/core/src/error.rs:185` `fn from(_: CancelErr) -> Self {`
- `impl` `codex-rs/core/src/error.rs:190` `impl CodexErr {`
- `fn` `codex-rs/core/src/error.rs:191` `pub fn is_retryable(&self) -> bool {`
- `struct` `codex-rs/core/src/error.rs:230` `pub struct ConnectionFailedError {`
- `impl` `codex-rs/core/src/error.rs:234` `impl std::fmt::Display for ConnectionFailedError {`
- `fn` `codex-rs/core/src/error.rs:235` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/error.rs:241` `pub struct ResponseStreamFailed {`
- `impl` `codex-rs/core/src/error.rs:246` `impl std::fmt::Display for ResponseStreamFailed {`
- `fn` `codex-rs/core/src/error.rs:247` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/error.rs:262` `pub struct RefreshTokenFailedError {`
- `impl` `codex-rs/core/src/error.rs:267` `impl RefreshTokenFailedError {`
- `fn` `codex-rs/core/src/error.rs:268` `pub fn new(reason: RefreshTokenFailedReason, message: impl Into<String>) -> Self {`
- `enum` `codex-rs/core/src/error.rs:277` `pub enum RefreshTokenFailedReason {`
- `struct` `codex-rs/core/src/error.rs:285` `pub struct UnexpectedResponseError {`
- `const` `codex-rs/core/src/error.rs:293` `const CLOUDFLARE_BLOCKED_MESSAGE: &str =`
- `const` `codex-rs/core/src/error.rs:295` `const UNEXPECTED_RESPONSE_BODY_MAX_BYTES: usize = 1000;`
- `impl` `codex-rs/core/src/error.rs:297` `impl UnexpectedResponseError {`
- `fn` `codex-rs/core/src/error.rs:298` `fn display_body(&self) -> String {`
- `fn` `codex-rs/core/src/error.rs:311` `fn extract_error_message(&self) -> Option<String> {`
- `fn` `codex-rs/core/src/error.rs:325` `fn friendly_message(&self) -> Option<String> {`
- `impl` `codex-rs/core/src/error.rs:350` `impl std::fmt::Display for UnexpectedResponseError {`
- `fn` `codex-rs/core/src/error.rs:351` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/core/src/error.rs:374` `fn truncate_with_ellipsis(text: &str, max_bytes: usize) -> String {`
- `struct` `codex-rs/core/src/error.rs:389` `pub struct RetryLimitReachedError {`
- `impl` `codex-rs/core/src/error.rs:394` `impl std::fmt::Display for RetryLimitReachedError {`
- `fn` `codex-rs/core/src/error.rs:395` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/error.rs:409` `pub struct UsageLimitReachedError {`
- `impl` `codex-rs/core/src/error.rs:416` `impl std::fmt::Display for UsageLimitReachedError {`
- `fn` `codex-rs/core/src/error.rs:417` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/error.rs:463` `pub struct ModelCapError {`
- `impl` `codex-rs/core/src/error.rs:468` `impl std::fmt::Display for ModelCapError {`
- `fn` `codex-rs/core/src/error.rs:469` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/core/src/error.rs:486` `fn retry_suffix(resets_at: Option<&DateTime<Utc>>) -> String {`
- `fn` `codex-rs/core/src/error.rs:495` `fn retry_suffix_after_or(resets_at: Option<&DateTime<Utc>>) -> String {`
- `fn` `codex-rs/core/src/error.rs:504` `fn format_retry_timestamp(resets_at: &DateTime<Utc>) -> String {`
- `fn` `codex-rs/core/src/error.rs:517` `fn format_duration_short(seconds: u64) -> String {`
- `fn` `codex-rs/core/src/error.rs:529` `fn day_suffix(day: u32) -> &'static str {`
- `static` `codex-rs/core/src/error.rs:543` `static NOW_OVERRIDE: std::cell::RefCell<Option<DateTime<Utc>>> =`
- `fn` `codex-rs/core/src/error.rs:547` `fn now_for_retry() -> DateTime<Utc> {`
- `struct` `codex-rs/core/src/error.rs:558` `pub struct EnvVarError {`
- `impl` `codex-rs/core/src/error.rs:567` `impl std::fmt::Display for EnvVarError {`
- `fn` `codex-rs/core/src/error.rs:568` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `impl` `codex-rs/core/src/error.rs:577` `impl CodexErr {`
- `fn` `codex-rs/core/src/error.rs:586` `pub fn to_codex_protocol_error(&self) -> CodexErrorInfo {`
- `fn` `codex-rs/core/src/error.rs:617` `pub fn to_error_event(&self, message_prefix: Option<String>) -> ErrorEvent {`
- `fn` `codex-rs/core/src/error.rs:629` `pub fn http_status_code_value(&self) -> Option<u16> {`
- `fn` `codex-rs/core/src/error.rs:641` `pub fn get_error_message_ui(e: &CodexErr) -> String {`
- `use` `codex-rs/core/src/error.rs:679` `use super::*;`
- `use` `codex-rs/core/src/error.rs:680` `use crate::exec::StreamOutput;`
- `use` `codex-rs/core/src/error.rs:681` `use chrono::DateTime;`
- `use` `codex-rs/core/src/error.rs:682` `use chrono::Duration as ChronoDuration;`
- `use` `codex-rs/core/src/error.rs:683` `use chrono::TimeZone;`
- `use` `codex-rs/core/src/error.rs:684` `use chrono::Utc;`
- `use` `codex-rs/core/src/error.rs:685` `use codex_protocol::protocol::RateLimitWindow;`
- `use` `codex-rs/core/src/error.rs:686` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/error.rs:687` `use reqwest::Response;`
- `use` `codex-rs/core/src/error.rs:688` `use reqwest::ResponseBuilderExt;`
- `use` `codex-rs/core/src/error.rs:689` `use reqwest::StatusCode;`
- `use` `codex-rs/core/src/error.rs:690` `use reqwest::Url;`
- `fn` `codex-rs/core/src/error.rs:692` `fn rate_limit_snapshot() -> RateLimitSnapshot {`
- `fn` `codex-rs/core/src/error.rs:727` `fn usage_limit_reached_error_formats_plus_plan() {`
- `fn` `codex-rs/core/src/error.rs:741` `fn model_cap_error_formats_message() {`
- `fn` `codex-rs/core/src/error.rs:753` `fn model_cap_error_formats_message_without_reset() {`
- `fn` `codex-rs/core/src/error.rs:765` `fn model_cap_error_maps_to_protocol() {`
- `fn` `codex-rs/core/src/error.rs:780` `fn sandbox_denied_uses_aggregated_output_when_stderr_empty() {`
- `fn` `codex-rs/core/src/error.rs:796` `fn sandbox_denied_reports_both_streams_when_available() {`
- `fn` `codex-rs/core/src/error.rs:812` `fn sandbox_denied_reports_stdout_when_no_stderr() {`
- `fn` `codex-rs/core/src/error.rs:828` `fn to_error_event_handles_response_stream_failed() {`
- `fn` `codex-rs/core/src/error.rs:855` `fn sandbox_denied_reports_exit_code_when_no_output_available() {`
- `fn` `codex-rs/core/src/error.rs:874` `fn usage_limit_reached_error_formats_free_plan() {`
- `fn` `codex-rs/core/src/error.rs:888` `fn usage_limit_reached_error_formats_go_plan() {`
- `fn` `codex-rs/core/src/error.rs:902` `fn usage_limit_reached_error_formats_default_when_none() {`
- `fn` `codex-rs/core/src/error.rs:916` `fn usage_limit_reached_error_formats_team_plan() {`
- `fn` `codex-rs/core/src/error.rs:935` `fn usage_limit_reached_error_formats_business_plan_without_reset() {`
- `fn` `codex-rs/core/src/error.rs:949` `fn usage_limit_reached_error_formats_default_for_other_plans() {`
- `fn` `codex-rs/core/src/error.rs:963` `fn usage_limit_reached_error_formats_pro_plan_with_reset() {`
- `fn` `codex-rs/core/src/error.rs:982` `fn usage_limit_reached_includes_minutes_when_available() {`
- `fn` `codex-rs/core/src/error.rs:999` `fn unexpected_status_cloudflare_html_is_simplified() {`
- `fn` `codex-rs/core/src/error.rs:1017` `fn unexpected_status_non_html_is_unchanged() {`
- `fn` `codex-rs/core/src/error.rs:1034` `fn unexpected_status_prefers_error_message_when_present() {`
- `fn` `codex-rs/core/src/error.rs:1053` `fn unexpected_status_truncates_long_body_with_ellipsis() {`
- `fn` `codex-rs/core/src/error.rs:1073` `fn unexpected_status_includes_cf_ray_and_request_id() {`
- `fn` `codex-rs/core/src/error.rs:1091` `fn usage_limit_reached_includes_hours_and_minutes() {`
- `fn` `codex-rs/core/src/error.rs:1110` `fn usage_limit_reached_includes_days_hours_minutes() {`
- `fn` `codex-rs/core/src/error.rs:1128` `fn usage_limit_reached_less_than_minute() {`
- `fn` `codex-rs/core/src/error.rs:1145` `fn usage_limit_reached_with_promo_message() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec::ExecToolCallOutput;`
- `use crate::token_data::KnownPlan;`
- `use crate::token_data::PlanType;`
- `use crate::truncate::TruncationPolicy;`
- `use crate::truncate::truncate_text;`
- `use chrono::DateTime;`
- `use chrono::Datelike;`
- `use chrono::Local;`
- `use chrono::Utc;`
- `use codex_async_utils::CancelErr;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::CodexErrorInfo;`
- `use codex_protocol::protocol::ErrorEvent;`
- `use codex_protocol::protocol::RateLimitSnapshot;`
- `use reqwest::StatusCode;`
- `use serde_json;`
- `use std::io;`
- `use std::time::Duration;`
- `use thiserror::Error;`
- `use tokio::task::JoinError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
