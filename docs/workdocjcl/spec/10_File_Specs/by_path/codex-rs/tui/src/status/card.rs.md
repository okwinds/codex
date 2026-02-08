# `codex-rs/tui/src/status/card.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `20086`
- sha256: `f13dd4a6636db45f0a3dabac8e45ad6002b65b042e8e7ab306cb4013266556a6`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/status/card.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/status/card.rs:1` `use crate::history_cell::CompositeHistoryCell;`
- `use` `codex-rs/tui/src/status/card.rs:2` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/status/card.rs:3` `use crate::history_cell::PlainHistoryCell;`
- `use` `codex-rs/tui/src/status/card.rs:4` `use crate::history_cell::with_border_with_inner_width;`
- `use` `codex-rs/tui/src/status/card.rs:5` `use crate::version::CODEX_CLI_VERSION;`
- `use` `codex-rs/tui/src/status/card.rs:6` `use chrono::DateTime;`
- `use` `codex-rs/tui/src/status/card.rs:7` `use chrono::Local;`
- `use` `codex-rs/tui/src/status/card.rs:8` `use codex_common::summarize_sandbox_policy;`
- `use` `codex-rs/tui/src/status/card.rs:9` `use codex_core::WireApi;`
- `use` `codex-rs/tui/src/status/card.rs:10` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/status/card.rs:11` `use codex_core::protocol::NetworkAccess;`
- `use` `codex-rs/tui/src/status/card.rs:12` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/tui/src/status/card.rs:13` `use codex_core::protocol::TokenUsage;`
- `use` `codex-rs/tui/src/status/card.rs:14` `use codex_core::protocol::TokenUsageInfo;`
- `use` `codex-rs/tui/src/status/card.rs:15` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/status/card.rs:16` `use codex_protocol::account::PlanType;`
- `use` `codex-rs/tui/src/status/card.rs:17` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/tui/src/status/card.rs:18` `use ratatui::prelude::*;`
- `use` `codex-rs/tui/src/status/card.rs:19` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/status/card.rs:20` `use std::collections::BTreeSet;`
- `use` `codex-rs/tui/src/status/card.rs:21` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/status/card.rs:22` `use url::Url;`
- `use` `codex-rs/tui/src/status/card.rs:24` `use super::account::StatusAccountDisplay;`
- `use` `codex-rs/tui/src/status/card.rs:25` `use super::format::FieldFormatter;`
- `use` `codex-rs/tui/src/status/card.rs:26` `use super::format::line_display_width;`
- `use` `codex-rs/tui/src/status/card.rs:27` `use super::format::push_label;`
- `use` `codex-rs/tui/src/status/card.rs:28` `use super::format::truncate_line_to_width;`
- `use` `codex-rs/tui/src/status/card.rs:29` `use super::helpers::compose_account_display;`
- `use` `codex-rs/tui/src/status/card.rs:30` `use super::helpers::compose_agents_summary;`
- `use` `codex-rs/tui/src/status/card.rs:31` `use super::helpers::compose_model_display;`
- `use` `codex-rs/tui/src/status/card.rs:32` `use super::helpers::format_directory_display;`
- `use` `codex-rs/tui/src/status/card.rs:33` `use super::helpers::format_tokens_compact;`
- `use` `codex-rs/tui/src/status/card.rs:34` `use super::rate_limits::RateLimitSnapshotDisplay;`
- `use` `codex-rs/tui/src/status/card.rs:35` `use super::rate_limits::StatusRateLimitData;`
- `use` `codex-rs/tui/src/status/card.rs:36` `use super::rate_limits::StatusRateLimitRow;`
- `use` `codex-rs/tui/src/status/card.rs:37` `use super::rate_limits::StatusRateLimitValue;`
- `use` `codex-rs/tui/src/status/card.rs:38` `use super::rate_limits::compose_rate_limit_data;`
- `use` `codex-rs/tui/src/status/card.rs:39` `use super::rate_limits::format_status_limit_summary;`
- `use` `codex-rs/tui/src/status/card.rs:40` `use super::rate_limits::render_status_limit_progress_bar;`
- `use` `codex-rs/tui/src/status/card.rs:41` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/status/card.rs:42` `use crate::wrapping::word_wrap_lines;`
- `use` `codex-rs/tui/src/status/card.rs:43` `use codex_core::AuthManager;`
- `struct` `codex-rs/tui/src/status/card.rs:46` `struct StatusContextWindowData {`
- `struct` `codex-rs/tui/src/status/card.rs:61` `struct StatusHistoryCell {`
- `impl` `codex-rs/tui/src/status/card.rs:114` `impl StatusHistoryCell {`
- `fn` `codex-rs/tui/src/status/card.rs:116` `fn new(`
- `fn` `codex-rs/tui/src/status/card.rs:212` `fn token_usage_spans(&self) -> Vec<Span<'static>> {`
- `fn` `codex-rs/tui/src/status/card.rs:230` `fn context_window_spans(&self) -> Option<Vec<Span<'static>>> {`
- `fn` `codex-rs/tui/src/status/card.rs:246` `fn rate_limit_lines(`
- `fn` `codex-rs/tui/src/status/card.rs:276` `fn rate_limit_row_lines(`
- `fn` `codex-rs/tui/src/status/card.rs:329` `fn collect_rate_limit_labels(&self, seen: &mut BTreeSet<String>, labels: &mut Vec<String>) {`
- `impl` `codex-rs/tui/src/status/card.rs:351` `impl HistoryCell for StatusHistoryCell {`
- `fn` `codex-rs/tui/src/status/card.rs:352` `fn display_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/status/card.rs:492` `fn format_model_provider(config: &Config) -> Option<String> {`
- `fn` `codex-rs/tui/src/status/card.rs:512` `fn sanitize_base_url(raw: &str) -> Option<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::history_cell::CompositeHistoryCell;`
- `use crate::history_cell::HistoryCell;`
- `use crate::history_cell::PlainHistoryCell;`
- `use crate::history_cell::with_border_with_inner_width;`
- `use crate::version::CODEX_CLI_VERSION;`
- `use chrono::DateTime;`
- `use chrono::Local;`
- `use codex_common::summarize_sandbox_policy;`
- `use codex_core::WireApi;`
- `use codex_core::config::Config;`
- `use codex_core::protocol::NetworkAccess;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::TokenUsage;`
- `use codex_core::protocol::TokenUsageInfo;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::account::PlanType;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use ratatui::prelude::*;`
- `use ratatui::style::Stylize;`
- `use std::collections::BTreeSet;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
