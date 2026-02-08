# `codex-rs/core/src/error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `36764`
- sha256: `5c3a69e880f983e20c01d72458d5b79862bfa90b860870b8a9975946dbb37a8f`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `const` `codex-rs/core/src/error.rs:292` `const CLOUDFLARE_BLOCKED_MESSAGE: &str =`
- `impl` `codex-rs/core/src/error.rs:295` `impl UnexpectedResponseError {`
- `fn` `codex-rs/core/src/error.rs:296` `fn friendly_message(&self) -> Option<String> {`
- `impl` `codex-rs/core/src/error.rs:318` `impl std::fmt::Display for UnexpectedResponseError {`
- `fn` `codex-rs/core/src/error.rs:319` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/error.rs:339` `pub struct RetryLimitReachedError {`
- `impl` `codex-rs/core/src/error.rs:344` `impl std::fmt::Display for RetryLimitReachedError {`
- `fn` `codex-rs/core/src/error.rs:345` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/error.rs:359` `pub struct UsageLimitReachedError {`
- `impl` `codex-rs/core/src/error.rs:366` `impl std::fmt::Display for UsageLimitReachedError {`
- `fn` `codex-rs/core/src/error.rs:367` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `struct` `codex-rs/core/src/error.rs:413` `pub struct ModelCapError {`
- `impl` `codex-rs/core/src/error.rs:418` `impl std::fmt::Display for ModelCapError {`
- `fn` `codex-rs/core/src/error.rs:419` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/core/src/error.rs:436` `fn retry_suffix(resets_at: Option<&DateTime<Utc>>) -> String {`
- `fn` `codex-rs/core/src/error.rs:445` `fn retry_suffix_after_or(resets_at: Option<&DateTime<Utc>>) -> String {`
- `fn` `codex-rs/core/src/error.rs:454` `fn format_retry_timestamp(resets_at: &DateTime<Utc>) -> String {`
- `fn` `codex-rs/core/src/error.rs:467` `fn format_duration_short(seconds: u64) -> String {`
- `fn` `codex-rs/core/src/error.rs:479` `fn day_suffix(day: u32) -> &'static str {`
- `static` `codex-rs/core/src/error.rs:493` `static NOW_OVERRIDE: std::cell::RefCell<Option<DateTime<Utc>>> =`
- `fn` `codex-rs/core/src/error.rs:497` `fn now_for_retry() -> DateTime<Utc> {`
- `struct` `codex-rs/core/src/error.rs:508` `pub struct EnvVarError {`
- `impl` `codex-rs/core/src/error.rs:517` `impl std::fmt::Display for EnvVarError {`
- `fn` `codex-rs/core/src/error.rs:518` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `impl` `codex-rs/core/src/error.rs:527` `impl CodexErr {`
- `fn` `codex-rs/core/src/error.rs:536` `pub fn to_codex_protocol_error(&self) -> CodexErrorInfo {`
- `fn` `codex-rs/core/src/error.rs:567` `pub fn to_error_event(&self, message_prefix: Option<String>) -> ErrorEvent {`
- `fn` `codex-rs/core/src/error.rs:579` `pub fn http_status_code_value(&self) -> Option<u16> {`
- `fn` `codex-rs/core/src/error.rs:591` `pub fn get_error_message_ui(e: &CodexErr) -> String {`
- `use` `codex-rs/core/src/error.rs:629` `use super::*;`
- `use` `codex-rs/core/src/error.rs:630` `use crate::exec::StreamOutput;`
- `use` `codex-rs/core/src/error.rs:631` `use chrono::DateTime;`
- `use` `codex-rs/core/src/error.rs:632` `use chrono::Duration as ChronoDuration;`
- `use` `codex-rs/core/src/error.rs:633` `use chrono::TimeZone;`
- `use` `codex-rs/core/src/error.rs:634` `use chrono::Utc;`
- `use` `codex-rs/core/src/error.rs:635` `use codex_protocol::protocol::RateLimitWindow;`
- `use` `codex-rs/core/src/error.rs:636` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/error.rs:637` `use reqwest::Response;`
- `use` `codex-rs/core/src/error.rs:638` `use reqwest::ResponseBuilderExt;`
- `use` `codex-rs/core/src/error.rs:639` `use reqwest::StatusCode;`
- `use` `codex-rs/core/src/error.rs:640` `use reqwest::Url;`
- `fn` `codex-rs/core/src/error.rs:642` `fn rate_limit_snapshot() -> RateLimitSnapshot {`
- `fn` `codex-rs/core/src/error.rs:677` `fn usage_limit_reached_error_formats_plus_plan() {`
- `fn` `codex-rs/core/src/error.rs:691` `fn model_cap_error_formats_message() {`
- `fn` `codex-rs/core/src/error.rs:703` `fn model_cap_error_formats_message_without_reset() {`
- `fn` `codex-rs/core/src/error.rs:715` `fn model_cap_error_maps_to_protocol() {`
- `fn` `codex-rs/core/src/error.rs:730` `fn sandbox_denied_uses_aggregated_output_when_stderr_empty() {`
- `fn` `codex-rs/core/src/error.rs:746` `fn sandbox_denied_reports_both_streams_when_available() {`
- `fn` `codex-rs/core/src/error.rs:762` `fn sandbox_denied_reports_stdout_when_no_stderr() {`
- `fn` `codex-rs/core/src/error.rs:778` `fn to_error_event_handles_response_stream_failed() {`
- `fn` `codex-rs/core/src/error.rs:805` `fn sandbox_denied_reports_exit_code_when_no_output_available() {`
- `fn` `codex-rs/core/src/error.rs:824` `fn usage_limit_reached_error_formats_free_plan() {`
- `fn` `codex-rs/core/src/error.rs:838` `fn usage_limit_reached_error_formats_go_plan() {`
- `fn` `codex-rs/core/src/error.rs:852` `fn usage_limit_reached_error_formats_default_when_none() {`
- `fn` `codex-rs/core/src/error.rs:866` `fn usage_limit_reached_error_formats_team_plan() {`
- `fn` `codex-rs/core/src/error.rs:885` `fn usage_limit_reached_error_formats_business_plan_without_reset() {`
- `fn` `codex-rs/core/src/error.rs:899` `fn usage_limit_reached_error_formats_default_for_other_plans() {`
- `fn` `codex-rs/core/src/error.rs:913` `fn usage_limit_reached_error_formats_pro_plan_with_reset() {`
- `fn` `codex-rs/core/src/error.rs:932` `fn usage_limit_reached_includes_minutes_when_available() {`
- `fn` `codex-rs/core/src/error.rs:949` `fn unexpected_status_cloudflare_html_is_simplified() {`
- `fn` `codex-rs/core/src/error.rs:968` `fn unexpected_status_non_html_is_unchanged() {`
- `fn` `codex-rs/core/src/error.rs:984` `fn usage_limit_reached_includes_hours_and_minutes() {`
- `fn` `codex-rs/core/src/error.rs:1003` `fn usage_limit_reached_includes_days_hours_minutes() {`
- `fn` `codex-rs/core/src/error.rs:1021` `fn usage_limit_reached_less_than_minute() {`
- `fn` `codex-rs/core/src/error.rs:1038` `fn usage_limit_reached_with_promo_message() {`

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
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
