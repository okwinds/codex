# `codex-rs/cloud-tasks/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `116174`
- sha256: `ebceeb2b0d54c6505c0739b4a1e47a4d3a16553f198be7dbd7176c5e7a6149d1`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/lib.rs` (read)
- env: `CODEX_CLOUD_TASKS_BASE_URL`, `CODEX_CLOUD_TASKS_FORCE_INTERNAL`, `CODEX_CLOUD_TASKS_MODE`

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/cloud-tasks/src/lib.rs:1` `mod app;`
- `mod` `codex-rs/cloud-tasks/src/lib.rs:2` `mod cli;`
- `mod` `codex-rs/cloud-tasks/src/lib.rs:3` `pub mod env_detect;`
- `mod` `codex-rs/cloud-tasks/src/lib.rs:4` `mod new_task;`
- `mod` `codex-rs/cloud-tasks/src/lib.rs:5` `pub mod scrollable_diff;`
- `mod` `codex-rs/cloud-tasks/src/lib.rs:6` `mod ui;`
- `mod` `codex-rs/cloud-tasks/src/lib.rs:7` `pub mod util;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:10` `use anyhow::anyhow;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:11` `use chrono::Utc;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:12` `use codex_cloud_tasks_client::TaskStatus;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:13` `use owo_colors::OwoColorize;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:14` `use owo_colors::Stream;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:15` `use std::cmp::Ordering;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:16` `use std::io::IsTerminal;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:17` `use std::io::Read;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:18` `use std::path::PathBuf;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:19` `use std::sync::Arc;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:20` `use std::time::Duration;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:21` `use std::time::Instant;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:22` `use supports_color::Stream as SupportStream;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:23` `use tokio::sync::mpsc::UnboundedSender;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:24` `use tracing::info;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:25` `use tracing_subscriber::EnvFilter;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:26` `use util::append_error_log;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:27` `use util::format_relative_time;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:28` `use util::set_user_agent_suffix;`
- `struct` `codex-rs/cloud-tasks/src/lib.rs:30` `struct ApplyJob {`
- `struct` `codex-rs/cloud-tasks/src/lib.rs:35` `struct BackendContext {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:40` `async fn init_backend(user_agent_suffix: &str) -> anyhow::Result<BackendContext> {`
- `trait` `codex-rs/cloud-tasks/src/lib.rs:111` `trait GitInfoProvider {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:112` `async fn default_branch_name(&self, path: &std::path::Path) -> Option<String>;`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:114` `async fn current_branch_name(&self, path: &std::path::Path) -> Option<String>;`
- `struct` `codex-rs/cloud-tasks/src/lib.rs:117` `struct RealGitInfo;`
- `impl` `codex-rs/cloud-tasks/src/lib.rs:120` `impl GitInfoProvider for RealGitInfo {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:121` `async fn default_branch_name(&self, path: &std::path::Path) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:125` `async fn current_branch_name(&self, path: &std::path::Path) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:130` `async fn resolve_git_ref(branch_override: Option<&String>) -> String {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:134` `async fn resolve_git_ref_with_git_info(`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:158` `async fn run_exec_command(args: crate::cli::ExecCommand) -> anyhow::Result<()> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:183` `async fn resolve_environment_id(ctx: &BackendContext, requested: &str) -> anyhow::Result<String> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:228` `fn resolve_query_input(query_arg: Option<String>) -> anyhow::Result<String> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:255` `fn parse_task_id(raw: &str) -> anyhow::Result<codex_cloud_tasks_client::TaskId> {`
- `struct` `codex-rs/cloud-tasks/src/lib.rs:277` `struct AttemptDiffData {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:283` `fn cmp_attempt(lhs: &AttemptDiffData, rhs: &AttemptDiffData) -> Ordering {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:297` `async fn collect_attempt_diffs(`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:340` `fn select_attempt(`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:360` `fn task_status_label(status: &TaskStatus) -> &'static str {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:369` `fn summary_line(summary: &codex_cloud_tasks_client::DiffSummary, colorize: bool) -> String {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:408` `fn format_task_status_lines(`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:475` `fn format_task_list_lines(`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:494` `async fn run_status_command(args: crate::cli::StatusCommand) -> anyhow::Result<()> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:510` `async fn run_list_command(args: crate::cli::ListCommand) -> anyhow::Result<()> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:577` `async fn run_diff_command(args: crate::cli::DiffCommand) -> anyhow::Result<()> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:586` `async fn run_apply_command(args: crate::cli::ApplyCommand) -> anyhow::Result<()> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:607` `fn level_from_status(status: codex_cloud_tasks_client::ApplyStatus) -> app::ApplyResultLevel {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:615` `fn spawn_preflight(`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:677` `fn spawn_apply(`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:732` `pub async fn run_main(cli: Cli, _codex_linux_sandbox_exe: Option<PathBuf>) -> anyhow::Result<()> {`
- `use` `codex-rs/cloud-tasks/src/lib.rs:761` `use crossterm::ExecutableCommand;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:762` `use crossterm::event::DisableBracketedPaste;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:763` `use crossterm::event::EnableBracketedPaste;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:764` `use crossterm::event::KeyboardEnhancementFlags;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:765` `use crossterm::event::PopKeyboardEnhancementFlags;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:766` `use crossterm::event::PushKeyboardEnhancementFlags;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:767` `use crossterm::terminal::EnterAlternateScreen;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:768` `use crossterm::terminal::LeaveAlternateScreen;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:769` `use crossterm::terminal::disable_raw_mode;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:770` `use crossterm::terminal::enable_raw_mode;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:771` `use ratatui::Terminal;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:772` `use ratatui::backend::CrosstermBackend;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:814` `use crossterm::event::Event;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:815` `use crossterm::event::EventStream;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:816` `use crossterm::event::KeyCode;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:817` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:818` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:819` `use tokio_stream::StreamExt;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:823` `use tokio::sync::mpsc::unbounded_channel;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:871` `use std::time::Instant;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:872` `use tokio::time::Instant as TokioInstant;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:873` `use tokio::time::sleep_until;`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2013` `fn conversation_lines(prompt: Option<String>, messages: &[String]) -> Vec<String> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2041` `fn pretty_lines_from_error(raw: &str) -> Vec<String> {`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2121` `use super::*;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2122` `use crate::resolve_git_ref_with_git_info;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2123` `use codex_cloud_tasks_client::DiffSummary;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2124` `use codex_cloud_tasks_client::MockClient;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2125` `use codex_cloud_tasks_client::TaskId;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2126` `use codex_cloud_tasks_client::TaskStatus;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2127` `use codex_cloud_tasks_client::TaskSummary;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2128` `use codex_tui::ComposerAction;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2129` `use codex_tui::ComposerInput;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2130` `use crossterm::event::KeyCode;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2131` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2132` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2133` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2134` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/cloud-tasks/src/lib.rs:2135` `use ratatui::layout::Rect;`
- `struct` `codex-rs/cloud-tasks/src/lib.rs:2137` `struct StubGitInfo {`
- `impl` `codex-rs/cloud-tasks/src/lib.rs:2142` `impl StubGitInfo {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2143` `fn new(default_branch: Option<String>, current_branch: Option<String>) -> Self {`
- `impl` `codex-rs/cloud-tasks/src/lib.rs:2152` `impl super::GitInfoProvider for StubGitInfo {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2153` `async fn default_branch_name(&self, _path: &std::path::Path) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2157` `async fn current_branch_name(&self, _path: &std::path::Path) -> Option<String> {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2163` `async fn branch_override_is_used_when_provided() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2174` `async fn trims_override_whitespace() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2185` `async fn prefers_current_branch_when_available() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2199` `async fn falls_back_to_current_branch_when_default_is_missing() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2210` `async fn falls_back_to_main_when_no_git_info_is_available() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2217` `fn format_task_status_lines_with_diff_and_label() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2246` `fn format_task_status_lines_without_diff_falls_back() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2271` `fn format_task_list_lines_formats_urls() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2319` `async fn collect_attempt_diffs_includes_sibling_attempts() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2333` `fn select_attempt_validates_bounds() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2345` `fn parse_task_id_from_url_and_raw() {`
- `fn` `codex-rs/cloud-tasks/src/lib.rs:2356` `fn composer_input_renders_typed_characters() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::anyhow;`
- `use chrono::Utc;`
- `use codex_cloud_tasks_client::TaskStatus;`
- `use owo_colors::OwoColorize;`
- `use owo_colors::Stream;`
- `use std::cmp::Ordering;`
- `use std::io::IsTerminal;`
- `use std::io::Read;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use supports_color::Stream as SupportStream;`
- `use tokio::sync::mpsc::UnboundedSender;`
- `use tracing::info;`
- `use tracing_subscriber::EnvFilter;`
- `use util::append_error_log;`
- `use util::format_relative_time;`
- `use util::set_user_agent_suffix;`
- `use crossterm::ExecutableCommand;`
### Referenced env vars
- `CODEX_CLOUD_TASKS_BASE_URL`
- `CODEX_CLOUD_TASKS_FORCE_INTERNAL`
- `CODEX_CLOUD_TASKS_MODE`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
