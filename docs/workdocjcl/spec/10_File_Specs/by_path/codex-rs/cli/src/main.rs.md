# `codex-rs/cli/src/main.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `48861`
- sha256: `9f8a41abff99ba8a6c3c1700cb75d6b72505cd74c5c78d03d433912f9d78f223`
- generated_utc: `2026-02-08T10:45:16Z`

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
- `struct` `codex-rs/cli/src/main.rs:149` `struct CompletionCommand {`
- `struct` `codex-rs/cli/src/main.rs:156` `struct DebugCommand {`
- `enum` `codex-rs/cli/src/main.rs:162` `enum DebugSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:168` `struct DebugAppServerCommand {`
- `enum` `codex-rs/cli/src/main.rs:174` `enum DebugAppServerSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:180` `struct DebugAppServerSendMessageV2Command {`
- `struct` `codex-rs/cli/src/main.rs:186` `struct ResumeCommand {`
- `struct` `codex-rs/cli/src/main.rs:205` `struct ForkCommand {`
- `struct` `codex-rs/cli/src/main.rs:224` `struct SandboxArgs {`
- `enum` `codex-rs/cli/src/main.rs:230` `enum SandboxCommand {`
- `struct` `codex-rs/cli/src/main.rs:244` `struct ExecpolicyCommand {`
- `enum` `codex-rs/cli/src/main.rs:250` `enum ExecpolicySubcommand {`
- `struct` `codex-rs/cli/src/main.rs:257` `struct LoginCommand {`
- `enum` `codex-rs/cli/src/main.rs:292` `enum LoginSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:298` `struct LogoutCommand {`
- `struct` `codex-rs/cli/src/main.rs:304` `struct AppServerCommand {`
- `enum` `codex-rs/cli/src/main.rs:338` `enum AppServerSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:347` `struct GenerateTsCommand {`
- `struct` `codex-rs/cli/src/main.rs:362` `struct GenerateJsonSchemaCommand {`
- `struct` `codex-rs/cli/src/main.rs:373` `struct StdioToUdsCommand {`
- `fn` `codex-rs/cli/src/main.rs:379` `fn format_exit_messages(exit_info: AppExitInfo, color_enabled: bool) -> Vec<String> {`
- `fn` `codex-rs/cli/src/main.rs:411` `fn handle_app_exit(exit_info: AppExitInfo) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:432` `fn run_update_action(action: UpdateAction) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:465` `fn run_execpolicycheck(cmd: ExecPolicyCheckCommand) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:469` `fn run_debug_app_server_command(cmd: DebugAppServerCommand) -> anyhow::Result<()> {`
- `struct` `codex-rs/cli/src/main.rs:479` `struct FeatureToggles {`
- `impl` `codex-rs/cli/src/main.rs:489` `impl FeatureToggles {`
- `fn` `codex-rs/cli/src/main.rs:490` `fn to_overrides(&self) -> anyhow::Result<Vec<String>> {`
- `fn` `codex-rs/cli/src/main.rs:503` `fn validate_feature(feature: &str) -> anyhow::Result<()> {`
- `struct` `codex-rs/cli/src/main.rs:513` `struct FeaturesCli {`
- `enum` `codex-rs/cli/src/main.rs:519` `enum FeaturesSubcommand {`
- `struct` `codex-rs/cli/src/main.rs:529` `struct FeatureSetArgs {`
- `fn` `codex-rs/cli/src/main.rs:534` `fn stage_str(stage: codex_core::features::Stage) -> &'static str {`
- `use` `codex-rs/cli/src/main.rs:535` `use codex_core::features::Stage;`
- `fn` `codex-rs/cli/src/main.rs:545` `fn main() -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:552` `async fn cli_main(codex_linux_sandbox_exe: Option<PathBuf>) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:826` `async fn enable_feature_in_config(interactive: &TuiCli, feature: &str) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:839` `async fn disable_feature_in_config(interactive: &TuiCli, feature: &str) -> anyhow::Result<()> {`
- `fn` `codex-rs/cli/src/main.rs:851` `fn maybe_print_under_development_feature_warning(`
- `fn` `codex-rs/cli/src/main.rs:879` `fn prepend_config_flags(`
- `fn` `codex-rs/cli/src/main.rs:888` `async fn run_interactive_tui(`
- `fn` `codex-rs/cli/src/main.rs:918` `fn confirm(prompt: &str) -> std::io::Result<bool> {`
- `fn` `codex-rs/cli/src/main.rs:928` `fn finalize_resume_interactive(`
- `fn` `codex-rs/cli/src/main.rs:954` `fn finalize_fork_interactive(`
- `fn` `codex-rs/cli/src/main.rs:982` `fn merge_interactive_cli_flags(interactive: &mut TuiCli, subcommand_cli: TuiCli) {`
- `fn` `codex-rs/cli/src/main.rs:1027` `fn print_completion(cmd: CompletionCommand) {`
- `use` `codex-rs/cli/src/main.rs:1035` `use super::*;`
- `use` `codex-rs/cli/src/main.rs:1036` `use assert_matches::assert_matches;`
- `use` `codex-rs/cli/src/main.rs:1037` `use codex_core::protocol::TokenUsage;`
- `use` `codex-rs/cli/src/main.rs:1038` `use codex_protocol::ThreadId;`
- `use` `codex-rs/cli/src/main.rs:1039` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/cli/src/main.rs:1041` `fn finalize_resume_from_args(args: &[&str]) -> TuiCli {`
- `fn` `codex-rs/cli/src/main.rs:1070` `fn finalize_fork_from_args(args: &[&str]) -> TuiCli {`
- `fn` `codex-rs/cli/src/main.rs:1093` `fn exec_resume_last_accepts_prompt_positional() {`
- `fn` `codex-rs/cli/src/main.rs:1110` `fn app_server_from_args(args: &[&str]) -> AppServerCommand {`
- `fn` `codex-rs/cli/src/main.rs:1118` `fn sample_exit_info(conversation_id: Option<&str>, thread_name: Option<&str>) -> AppExitInfo {`
- `fn` `codex-rs/cli/src/main.rs:1136` `fn format_exit_messages_skips_zero_usage() {`
- `fn` `codex-rs/cli/src/main.rs:1149` `fn format_exit_messages_includes_resume_hint_without_color() {`
- `fn` `codex-rs/cli/src/main.rs:1163` `fn format_exit_messages_applies_color_when_enabled() {`
- `fn` `codex-rs/cli/src/main.rs:1171` `fn format_exit_messages_prefers_thread_name() {`
- `fn` `codex-rs/cli/src/main.rs:1187` `fn resume_model_flag_applies_when_no_root_flags() {`
- `fn` `codex-rs/cli/src/main.rs:1198` `fn resume_picker_logic_none_and_not_last() {`
- `fn` `codex-rs/cli/src/main.rs:1207` `fn resume_picker_logic_last() {`
- `fn` `codex-rs/cli/src/main.rs:1216` `fn resume_picker_logic_with_session_id() {`
- `fn` `codex-rs/cli/src/main.rs:1225` `fn resume_all_flag_sets_show_all() {`
- `fn` `codex-rs/cli/src/main.rs:1232` `fn resume_merges_option_flags_and_full_auto() {`
- `fn` `codex-rs/cli/src/main.rs:1289` `fn resume_merges_dangerously_bypass_flag() {`
- `fn` `codex-rs/cli/src/main.rs:1305` `fn fork_picker_logic_none_and_not_last() {`
- `fn` `codex-rs/cli/src/main.rs:1314` `fn fork_picker_logic_last() {`
- `fn` `codex-rs/cli/src/main.rs:1323` `fn fork_picker_logic_with_session_id() {`
- `fn` `codex-rs/cli/src/main.rs:1332` `fn fork_all_flag_sets_show_all() {`
- `fn` `codex-rs/cli/src/main.rs:1339` `fn app_server_analytics_default_disabled_without_flag() {`
- `fn` `codex-rs/cli/src/main.rs:1349` `fn app_server_analytics_default_enabled_with_flag() {`
- `fn` `codex-rs/cli/src/main.rs:1356` `fn app_server_listen_websocket_url_parses() {`
- `fn` `codex-rs/cli/src/main.rs:1369` `fn app_server_listen_stdio_url_parses() {`
- `fn` `codex-rs/cli/src/main.rs:1379` `fn app_server_listen_invalid_url_fails_to_parse() {`
- `fn` `codex-rs/cli/src/main.rs:1386` `fn features_enable_parses_feature_name() {`
- `fn` `codex-rs/cli/src/main.rs:1399` `fn features_disable_parses_feature_name() {`
- `fn` `codex-rs/cli/src/main.rs:1412` `fn feature_toggles_known_features_generate_overrides() {`
- `fn` `codex-rs/cli/src/main.rs:1428` `fn feature_toggles_unknown_feature_errors() {`

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
- `docs/workdocjcl/spec/03_API/CLI.md`
