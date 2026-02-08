# `codex-rs/cli/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `46110`
- sha256: `0b88c6f634eb8292c2dcbf41db4be1cd119b5613a1839112f372549b1796914c`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Rust CLI multitool entrypoint: parses args, routes to subcommands, defaults to launching TUI when no subcommand is provided.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/src/main.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- `fn main() -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/cli/src/main.rs:1` `use clap::Args;`
- `use` `codex-rs/cli/src/main.rs:2` `use clap::CommandFactory;`
- `use` `codex-rs/cli/src/main.rs:3` `use clap::Parser;`
- `use` `codex-rs/cli/src/main.rs:4` `use clap_complete::Shell;`
- `use` `codex-rs/cli/src/main.rs:5` `use clap_complete::generate;`
- `use` `codex-rs/cli/src/main.rs:6` `use codex_arg0::arg0_dispatch_or_else;`
- `use` `codex-rs/cli/src/main.rs:7` `use codex_chatgpt::apply_command::ApplyCommand;`
- `use` `codex-rs/cli/src/main.rs:8` `use codex_chatgpt::apply_command::run_apply_command;`
- `use` `codex-rs/cli/src/main.rs:9` `use codex_cli::LandlockCommand;`
- `use` `codex-rs/cli/src/main.rs:10` `use codex_cli::SeatbeltCommand;`
- `use` `codex-rs/cli/src/main.rs:11` `use codex_cli::WindowsCommand;`
- `use` `codex-rs/cli/src/main.rs:12` `use codex_cli::login::read_api_key_from_stdin;`
- `use` `codex-rs/cli/src/main.rs:13` `use codex_cli::login::run_login_status;`
- `use` `codex-rs/cli/src/main.rs:14` `use codex_cli::login::run_login_with_api_key;`
- `use` `codex-rs/cli/src/main.rs:15` `use codex_cli::login::run_login_with_chatgpt;`
- `use` `codex-rs/cli/src/main.rs:16` `use codex_cli::login::run_login_with_device_code;`
- `use` `codex-rs/cli/src/main.rs:17` `use codex_cli::login::run_logout;`
- `use` `codex-rs/cli/src/main.rs:18` `use codex_cloud_tasks::Cli as CloudTasksCli;`
- `use` `codex-rs/cli/src/main.rs:19` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/cli/src/main.rs:20` `use codex_exec::Cli as ExecCli;`
- `use` `codex-rs/cli/src/main.rs:21` `use codex_exec::Command as ExecCommand;`
- `use` `codex-rs/cli/src/main.rs:22` `use codex_exec::ReviewArgs;`
- `use` `codex-rs/cli/src/main.rs:23` `use codex_execpolicy::ExecPolicyCheckCommand;`
- `use` `codex-rs/cli/src/main.rs:24` `use codex_responses_api_proxy::Args as ResponsesApiProxyArgs;`
- `use` `codex-rs/cli/src/main.rs:25` `use codex_tui::AppExitInfo;`
- `use` `codex-rs/cli/src/main.rs:26` `use codex_tui::Cli as TuiCli;`
- `use` `codex-rs/cli/src/main.rs:27` `use codex_tui::ExitReason;`
- `use` `codex-rs/cli/src/main.rs:28` `use codex_tui::update_action::UpdateAction;`
- `use` `codex-rs/cli/src/main.rs:29` `use owo_colors::OwoColorize;`
- `use` `codex-rs/cli/src/main.rs:30` `use std::io::IsTerminal;`
- `use` `codex-rs/cli/src/main.rs:31` `use std::path::PathBuf;`
- `use` `codex-rs/cli/src/main.rs:32` `use supports_color::Stream;`
- `mod` `codex-rs/cli/src/main.rs:35` `mod app_cmd;`
- `mod` `codex-rs/cli/src/main.rs:37` `mod desktop_app;`
- `mod` `codex-rs/cli/src/main.rs:38` `mod mcp_cmd;`
- `mod` `codex-rs/cli/src/main.rs:40` `mod wsl_paths;`
- `use` `codex-rs/cli/src/main.rs:42` `use crate::mcp_cmd::McpCli;`
- `use` `codex-rs/cli/src/main.rs:44` `use codex_core::config::Config;`
- `use` `codex-rs/cli/src/main.rs:45` `use codex_core::config::ConfigOverrides;`
- `use` `codex-rs/cli/src/main.rs:46` `use codex_core::config::edit::ConfigEditsBuilder;`
- `use` `codex-rs/cli/src/main.rs:47` `use codex_core::config::find_codex_home;`
- `use` `codex-rs/cli/src/main.rs:48` `use codex_core::features::Stage;`
- `use` `codex-rs/cli/src/main.rs:49` `use codex_core::features::is_known_feature_key;`
- `use` `codex-rs/cli/src/main.rs:50` `use codex_core::terminal::TerminalName;`
- `struct` `codex-rs/cli/src/main.rs:67` `struct MultitoolCli {`
- `enum` `codex-rs/cli/src/main.rs:82` `enum Subcommand {`
- `struct` `codex-rs/cli/src/main.rs:147` `struct CompletionCommand {`
- `struct` `codex-rs/cli/src/main.rs:154` `struct ResumeCommand {`
- `struct` `codex-rs/cli/src/main.rs:173` `struct ForkCommand {`
- `struct` `codex-rs/cli/src/main.rs:192` `struct SandboxArgs {`
- `enum` `codex-rs/cli/src/main.rs:198` `enum SandboxCommand {`
- `struct` `codex-rs/cli/src/main.rs:212` `struct ExecpolicyCommand {`
- `enum` `codex-rs/cli/src/main.rs:218` `enum ExecpolicySubcommand {`
- `struct` `codex-rs/cli/src/main.rs:225` `struct LoginCommand {`
- `enum` `codex-rs/cli/src/main.rs:260` `enum LoginSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:266` `struct LogoutCommand {`
- `struct` `codex-rs/cli/src/main.rs:272` `struct AppServerCommand {`
- `enum` `codex-rs/cli/src/main.rs:297` `enum AppServerSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:306` `struct GenerateTsCommand {`
- `struct` `codex-rs/cli/src/main.rs:321` `struct GenerateJsonSchemaCommand {`
- `struct` `codex-rs/cli/src/main.rs:332` `struct StdioToUdsCommand {`
- `fn` `codex-rs/cli/src/main.rs:338` `fn format_exit_messages(exit_info: AppExitInfo, color_enabled: bool) -> Vec<String> {`
- `fn` `codex-rs/cli/src/main.rs:370` `fn handle_app_exit(exit_info: AppExitInfo) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:391` `fn run_update_action(action: UpdateAction) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:424` `fn run_execpolicycheck(cmd: ExecPolicyCheckCommand) -> anyhow::Result<()> {`
- `struct` `codex-rs/cli/src/main.rs:429` `struct FeatureToggles {`
- `impl` `codex-rs/cli/src/main.rs:439` `impl FeatureToggles {`
- `fn` `codex-rs/cli/src/main.rs:440` `fn to_overrides(&self) -> anyhow::Result<Vec<String>> {`
- `fn` `codex-rs/cli/src/main.rs:453` `fn validate_feature(feature: &str) -> anyhow::Result<()> {`
- `struct` `codex-rs/cli/src/main.rs:463` `struct FeaturesCli {`
- `enum` `codex-rs/cli/src/main.rs:469` `enum FeaturesSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:479` `struct FeatureSetArgs {`
- `fn` `codex-rs/cli/src/main.rs:484` `fn stage_str(stage: codex_core::features::Stage) -> &'static str {`
- `use` `codex-rs/cli/src/main.rs:485` `use codex_core::features::Stage;`
- `fn` `codex-rs/cli/src/main.rs:495` `fn main() -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:502` `async fn cli_main(codex_linux_sandbox_exe: Option<PathBuf>) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:769` `async fn enable_feature_in_config(interactive: &TuiCli, feature: &str) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:782` `async fn disable_feature_in_config(interactive: &TuiCli, feature: &str) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:794` `fn maybe_print_under_development_feature_warning(`
- `fn` `codex-rs/cli/src/main.rs:822` `fn prepend_config_flags(`
- `fn` `codex-rs/cli/src/main.rs:831` `async fn run_interactive_tui(`
- `fn` `codex-rs/cli/src/main.rs:861` `fn confirm(prompt: &str) -> std::io::Result<bool> {`
- `fn` `codex-rs/cli/src/main.rs:871` `fn finalize_resume_interactive(`
- `fn` `codex-rs/cli/src/main.rs:897` `fn finalize_fork_interactive(`
- `fn` `codex-rs/cli/src/main.rs:925` `fn merge_interactive_cli_flags(interactive: &mut TuiCli, subcommand_cli: TuiCli) {`
- `fn` `codex-rs/cli/src/main.rs:970` `fn print_completion(cmd: CompletionCommand) {`
- `use` `codex-rs/cli/src/main.rs:978` `use super::*;`
- `use` `codex-rs/cli/src/main.rs:979` `use assert_matches::assert_matches;`
- `use` `codex-rs/cli/src/main.rs:980` `use codex_core::protocol::TokenUsage;`
- `use` `codex-rs/cli/src/main.rs:981` `use codex_protocol::ThreadId;`
- `use` `codex-rs/cli/src/main.rs:982` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/cli/src/main.rs:984` `fn finalize_resume_from_args(args: &[&str]) -> TuiCli {`
- `fn` `codex-rs/cli/src/main.rs:1013` `fn finalize_fork_from_args(args: &[&str]) -> TuiCli {`
- `fn` `codex-rs/cli/src/main.rs:1036` `fn exec_resume_last_accepts_prompt_positional() {`
- `fn` `codex-rs/cli/src/main.rs:1053` `fn app_server_from_args(args: &[&str]) -> AppServerCommand {`
- `fn` `codex-rs/cli/src/main.rs:1061` `fn sample_exit_info(conversation_id: Option<&str>, thread_name: Option<&str>) -> AppExitInfo {`
- `fn` `codex-rs/cli/src/main.rs:1079` `fn format_exit_messages_skips_zero_usage() {`
- `fn` `codex-rs/cli/src/main.rs:1092` `fn format_exit_messages_includes_resume_hint_without_color() {`
- `fn` `codex-rs/cli/src/main.rs:1106` `fn format_exit_messages_applies_color_when_enabled() {`
- `fn` `codex-rs/cli/src/main.rs:1114` `fn format_exit_messages_prefers_thread_name() {`
- `fn` `codex-rs/cli/src/main.rs:1130` `fn resume_model_flag_applies_when_no_root_flags() {`
- `fn` `codex-rs/cli/src/main.rs:1141` `fn resume_picker_logic_none_and_not_last() {`
- `fn` `codex-rs/cli/src/main.rs:1150` `fn resume_picker_logic_last() {`
- `fn` `codex-rs/cli/src/main.rs:1159` `fn resume_picker_logic_with_session_id() {`
- `fn` `codex-rs/cli/src/main.rs:1168` `fn resume_all_flag_sets_show_all() {`
- `fn` `codex-rs/cli/src/main.rs:1175` `fn resume_merges_option_flags_and_full_auto() {`
- `fn` `codex-rs/cli/src/main.rs:1232` `fn resume_merges_dangerously_bypass_flag() {`
- `fn` `codex-rs/cli/src/main.rs:1248` `fn fork_picker_logic_none_and_not_last() {`
- `fn` `codex-rs/cli/src/main.rs:1257` `fn fork_picker_logic_last() {`
- `fn` `codex-rs/cli/src/main.rs:1266` `fn fork_picker_logic_with_session_id() {`
- `fn` `codex-rs/cli/src/main.rs:1275` `fn fork_all_flag_sets_show_all() {`
- `fn` `codex-rs/cli/src/main.rs:1282` `fn app_server_analytics_default_disabled_without_flag() {`
- `fn` `codex-rs/cli/src/main.rs:1288` `fn app_server_analytics_default_enabled_with_flag() {`
- `fn` `codex-rs/cli/src/main.rs:1295` `fn features_enable_parses_feature_name() {`
- `fn` `codex-rs/cli/src/main.rs:1308` `fn features_disable_parses_feature_name() {`
- `fn` `codex-rs/cli/src/main.rs:1321` `fn feature_toggles_known_features_generate_overrides() {`
- `fn` `codex-rs/cli/src/main.rs:1337` `fn feature_toggles_unknown_feature_errors() {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::Args;`
- `use clap::CommandFactory;`
- `use clap::Parser;`
- `use clap_complete::Shell;`
- `use clap_complete::generate;`
- `use codex_arg0::arg0_dispatch_or_else;`
- `use codex_chatgpt::apply_command::ApplyCommand;`
- `use codex_chatgpt::apply_command::run_apply_command;`
- `use codex_cli::LandlockCommand;`
- `use codex_cli::SeatbeltCommand;`
- `use codex_cli::WindowsCommand;`
- `use codex_cli::login::read_api_key_from_stdin;`
- `use codex_cli::login::run_login_status;`
- `use codex_cli::login::run_login_with_api_key;`
- `use codex_cli::login::run_login_with_chatgpt;`
- `use codex_cli::login::run_login_with_device_code;`
- `use codex_cli::login::run_logout;`
- `use codex_cloud_tasks::Cli as CloudTasksCli;`
- `use codex_common::CliConfigOverrides;`
- `use codex_exec::Cli as ExecCli;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/03_API/CLI.md`
