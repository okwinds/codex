# `codex-rs/tui/src/status/tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `28900`
- sha256: `cd0b7994e757a928e0ee8ac401d838ca775ff4cf30c69d643f3b646e88c4f409`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/status/tests.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/status/tests.rs:1` `use super::new_status_output;`
- `use` `codex-rs/tui/src/status/tests.rs:2` `use super::rate_limit_snapshot_display;`
- `use` `codex-rs/tui/src/status/tests.rs:3` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/status/tests.rs:4` `use chrono::Duration as ChronoDuration;`
- `use` `codex-rs/tui/src/status/tests.rs:5` `use chrono::TimeZone;`
- `use` `codex-rs/tui/src/status/tests.rs:6` `use chrono::Utc;`
- `use` `codex-rs/tui/src/status/tests.rs:7` `use codex_core::AuthManager;`
- `use` `codex-rs/tui/src/status/tests.rs:8` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/status/tests.rs:9` `use codex_core::config::ConfigBuilder;`
- `use` `codex-rs/tui/src/status/tests.rs:10` `use codex_core::models_manager::manager::ModelsManager;`
- `use` `codex-rs/tui/src/status/tests.rs:11` `use codex_core::protocol::CreditsSnapshot;`
- `use` `codex-rs/tui/src/status/tests.rs:12` `use codex_core::protocol::RateLimitSnapshot;`
- `use` `codex-rs/tui/src/status/tests.rs:13` `use codex_core::protocol::RateLimitWindow;`
- `use` `codex-rs/tui/src/status/tests.rs:14` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/tui/src/status/tests.rs:15` `use codex_core::protocol::TokenUsage;`
- `use` `codex-rs/tui/src/status/tests.rs:16` `use codex_core::protocol::TokenUsageInfo;`
- `use` `codex-rs/tui/src/status/tests.rs:17` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/status/tests.rs:18` `use codex_protocol::config_types::ReasoningSummary;`
- `use` `codex-rs/tui/src/status/tests.rs:19` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/tui/src/status/tests.rs:20` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/status/tests.rs:21` `use ratatui::prelude::*;`
- `use` `codex-rs/tui/src/status/tests.rs:22` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/status/tests.rs:23` `use tempfile::TempDir;`
- `fn` `codex-rs/tui/src/status/tests.rs:25` `async fn test_config(temp_home: &TempDir) -> Config {`
- `fn` `codex-rs/tui/src/status/tests.rs:33` `fn test_auth_manager(config: &Config) -> AuthManager {`
- `fn` `codex-rs/tui/src/status/tests.rs:41` `fn token_info_for(model_slug: &str, config: &Config, usage: &TokenUsage) -> TokenUsageInfo {`
- `fn` `codex-rs/tui/src/status/tests.rs:51` `fn render_lines(lines: &[Line<'static>]) -> Vec<String> {`
- `fn` `codex-rs/tui/src/status/tests.rs:63` `fn sanitize_directory(lines: Vec<String>) -> Vec<String> {`
- `fn` `codex-rs/tui/src/status/tests.rs:86` `fn reset_at_from(captured_at: &chrono::DateTime<chrono::Local>, seconds: i64) -> i64 {`
- `fn` `codex-rs/tui/src/status/tests.rs:93` `async fn status_snapshot_includes_reasoning_details() {`
- `fn` `codex-rs/tui/src/status/tests.rs:170` `async fn status_snapshot_includes_forked_from() {`
- `fn` `codex-rs/tui/src/status/tests.rs:224` `async fn status_snapshot_includes_monthly_limit() {`
- `fn` `codex-rs/tui/src/status/tests.rs:284` `async fn status_snapshot_shows_unlimited_credits() {`
- `fn` `codex-rs/tui/src/status/tests.rs:331` `async fn status_snapshot_shows_positive_credits() {`
- `fn` `codex-rs/tui/src/status/tests.rs:378` `async fn status_snapshot_hides_zero_credits() {`
- `fn` `codex-rs/tui/src/status/tests.rs:423` `async fn status_snapshot_hides_when_has_no_credits_flag() {`
- `fn` `codex-rs/tui/src/status/tests.rs:468` `async fn status_card_token_usage_excludes_cached_tokens() {`
- `fn` `codex-rs/tui/src/status/tests.rs:514` `async fn status_snapshot_truncates_in_narrow_terminal() {`
- `fn` `codex-rs/tui/src/status/tests.rs:577` `async fn status_snapshot_shows_missing_limits_message() {`
- `fn` `codex-rs/tui/src/status/tests.rs:625` `async fn status_snapshot_includes_credits_and_limits() {`
- `fn` `codex-rs/tui/src/status/tests.rs:692` `async fn status_snapshot_shows_empty_limits_message() {`
- `fn` `codex-rs/tui/src/status/tests.rs:747` `async fn status_snapshot_shows_stale_limits_message() {`
- `fn` `codex-rs/tui/src/status/tests.rs:811` `async fn status_snapshot_cached_limits_hide_credits_without_flag() {`
- `fn` `codex-rs/tui/src/status/tests.rs:879` `async fn status_context_window_uses_last_usage() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::new_status_output;`
- `use super::rate_limit_snapshot_display;`
- `use crate::history_cell::HistoryCell;`
- `use chrono::Duration as ChronoDuration;`
- `use chrono::TimeZone;`
- `use chrono::Utc;`
- `use codex_core::AuthManager;`
- `use codex_core::config::Config;`
- `use codex_core::config::ConfigBuilder;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_core::protocol::CreditsSnapshot;`
- `use codex_core::protocol::RateLimitSnapshot;`
- `use codex_core::protocol::RateLimitWindow;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::TokenUsage;`
- `use codex_core::protocol::TokenUsageInfo;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use insta::assert_snapshot;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
