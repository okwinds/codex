# `codex-rs/tui/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `41624`
- sha256: `55545744fcddefdb762c6c2b8934175528d135616a7a70163e892a8284f47d3f`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/lib.rs` (read)

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub enum LoginStatus {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/lib.rs:6` `use additional_dirs::add_dir_warning_message;`
- `use` `codex-rs/tui/src/lib.rs:7` `use app::App;`
- `use` `codex-rs/tui/src/lib.rs:10` `use codex_cloud_requirements::cloud_requirements_loader;`
- `use` `codex-rs/tui/src/lib.rs:11` `use codex_common::oss::ensure_oss_provider_ready;`
- `use` `codex-rs/tui/src/lib.rs:12` `use codex_common::oss::get_default_model_for_oss_provider;`
- `use` `codex-rs/tui/src/lib.rs:13` `use codex_core::AuthManager;`
- `use` `codex-rs/tui/src/lib.rs:14` `use codex_core::CodexAuth;`
- `use` `codex-rs/tui/src/lib.rs:15` `use codex_core::INTERACTIVE_SESSION_SOURCES;`
- `use` `codex-rs/tui/src/lib.rs:16` `use codex_core::RolloutRecorder;`
- `use` `codex-rs/tui/src/lib.rs:17` `use codex_core::ThreadSortKey;`
- `use` `codex-rs/tui/src/lib.rs:18` `use codex_core::auth::AuthMode;`
- `use` `codex-rs/tui/src/lib.rs:19` `use codex_core::auth::enforce_login_restrictions;`
- `use` `codex-rs/tui/src/lib.rs:20` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/lib.rs:21` `use codex_core::config::ConfigBuilder;`
- `use` `codex-rs/tui/src/lib.rs:22` `use codex_core::config::ConfigOverrides;`
- `use` `codex-rs/tui/src/lib.rs:23` `use codex_core::config::find_codex_home;`
- `use` `codex-rs/tui/src/lib.rs:24` `use codex_core::config::load_config_as_toml_with_cli_overrides;`
- `use` `codex-rs/tui/src/lib.rs:25` `use codex_core::config::resolve_oss_provider;`
- `use` `codex-rs/tui/src/lib.rs:26` `use codex_core::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/tui/src/lib.rs:27` `use codex_core::config_loader::ConfigLoadError;`
- `use` `codex-rs/tui/src/lib.rs:28` `use codex_core::config_loader::format_config_error_with_source;`
- `use` `codex-rs/tui/src/lib.rs:29` `use codex_core::default_client::set_default_client_residency_requirement;`
- `use` `codex-rs/tui/src/lib.rs:30` `use codex_core::find_thread_path_by_id_str;`
- `use` `codex-rs/tui/src/lib.rs:31` `use codex_core::find_thread_path_by_name_str;`
- `use` `codex-rs/tui/src/lib.rs:32` `use codex_core::path_utils;`
- `use` `codex-rs/tui/src/lib.rs:33` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/tui/src/lib.rs:34` `use codex_core::read_session_meta_line;`
- `use` `codex-rs/tui/src/lib.rs:35` `use codex_core::terminal::Multiplexer;`
- `use` `codex-rs/tui/src/lib.rs:36` `use codex_core::windows_sandbox::WindowsSandboxLevelExt;`
- `use` `codex-rs/tui/src/lib.rs:37` `use codex_protocol::config_types::AltScreenMode;`
- `use` `codex-rs/tui/src/lib.rs:38` `use codex_protocol::config_types::SandboxMode;`
- `use` `codex-rs/tui/src/lib.rs:39` `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use` `codex-rs/tui/src/lib.rs:40` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/tui/src/lib.rs:41` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/tui/src/lib.rs:42` `use codex_state::log_db;`
- `use` `codex-rs/tui/src/lib.rs:43` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/tui/src/lib.rs:44` `use cwd_prompt::CwdPromptAction;`
- `use` `codex-rs/tui/src/lib.rs:45` `use cwd_prompt::CwdSelection;`
- `use` `codex-rs/tui/src/lib.rs:46` `use std::fs::OpenOptions;`
- `use` `codex-rs/tui/src/lib.rs:47` `use std::path::Path;`
- `use` `codex-rs/tui/src/lib.rs:48` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/lib.rs:49` `use tracing::error;`
- `use` `codex-rs/tui/src/lib.rs:50` `use tracing_appender::non_blocking;`
- `use` `codex-rs/tui/src/lib.rs:51` `use tracing_subscriber::EnvFilter;`
- `use` `codex-rs/tui/src/lib.rs:52` `use tracing_subscriber::prelude::*;`
- `use` `codex-rs/tui/src/lib.rs:53` `use uuid::Uuid;`
- `mod` `codex-rs/tui/src/lib.rs:55` `mod additional_dirs;`
- `mod` `codex-rs/tui/src/lib.rs:56` `mod app;`
- `mod` `codex-rs/tui/src/lib.rs:57` `mod app_backtrack;`
- `mod` `codex-rs/tui/src/lib.rs:58` `mod app_event;`
- `mod` `codex-rs/tui/src/lib.rs:59` `mod app_event_sender;`
- `mod` `codex-rs/tui/src/lib.rs:60` `mod ascii_animation;`
- `mod` `codex-rs/tui/src/lib.rs:61` `mod bottom_pane;`
- `mod` `codex-rs/tui/src/lib.rs:62` `mod chatwidget;`
- `mod` `codex-rs/tui/src/lib.rs:63` `mod cli;`
- `mod` `codex-rs/tui/src/lib.rs:64` `mod clipboard_paste;`
- `mod` `codex-rs/tui/src/lib.rs:65` `mod collab;`
- `mod` `codex-rs/tui/src/lib.rs:66` `mod collaboration_modes;`
- `mod` `codex-rs/tui/src/lib.rs:67` `mod color;`
- `mod` `codex-rs/tui/src/lib.rs:68` `pub mod custom_terminal;`
- `mod` `codex-rs/tui/src/lib.rs:69` `mod cwd_prompt;`
- `mod` `codex-rs/tui/src/lib.rs:70` `mod debug_config;`
- `mod` `codex-rs/tui/src/lib.rs:71` `mod diff_render;`
- `mod` `codex-rs/tui/src/lib.rs:72` `mod exec_cell;`
- `mod` `codex-rs/tui/src/lib.rs:73` `mod exec_command;`
- `mod` `codex-rs/tui/src/lib.rs:74` `mod external_editor;`
- `mod` `codex-rs/tui/src/lib.rs:75` `mod file_search;`
- `mod` `codex-rs/tui/src/lib.rs:76` `mod frames;`
- `mod` `codex-rs/tui/src/lib.rs:77` `mod get_git_diff;`
- `mod` `codex-rs/tui/src/lib.rs:78` `mod history_cell;`
- `mod` `codex-rs/tui/src/lib.rs:79` `pub mod insert_history;`
- `mod` `codex-rs/tui/src/lib.rs:80` `mod key_hint;`
- `mod` `codex-rs/tui/src/lib.rs:81` `pub mod live_wrap;`
- `mod` `codex-rs/tui/src/lib.rs:82` `mod markdown;`
- `mod` `codex-rs/tui/src/lib.rs:83` `mod markdown_render;`
- `mod` `codex-rs/tui/src/lib.rs:84` `mod markdown_stream;`
- `mod` `codex-rs/tui/src/lib.rs:85` `mod mention_codec;`
- `mod` `codex-rs/tui/src/lib.rs:86` `mod model_migration;`
- `mod` `codex-rs/tui/src/lib.rs:87` `mod notifications;`
- `mod` `codex-rs/tui/src/lib.rs:88` `pub mod onboarding;`
- `mod` `codex-rs/tui/src/lib.rs:89` `mod oss_selection;`
- `mod` `codex-rs/tui/src/lib.rs:90` `mod pager_overlay;`
- `mod` `codex-rs/tui/src/lib.rs:91` `pub mod public_widgets;`
- `mod` `codex-rs/tui/src/lib.rs:92` `mod render;`
- `mod` `codex-rs/tui/src/lib.rs:93` `mod resume_picker;`
- `mod` `codex-rs/tui/src/lib.rs:94` `mod selection_list;`
- `mod` `codex-rs/tui/src/lib.rs:95` `mod session_log;`
- `mod` `codex-rs/tui/src/lib.rs:96` `mod shimmer;`
- `mod` `codex-rs/tui/src/lib.rs:97` `mod skills_helpers;`
- `mod` `codex-rs/tui/src/lib.rs:98` `mod slash_command;`
- `mod` `codex-rs/tui/src/lib.rs:99` `mod status;`
- `mod` `codex-rs/tui/src/lib.rs:100` `mod status_indicator_widget;`
- `mod` `codex-rs/tui/src/lib.rs:101` `mod streaming;`
- `mod` `codex-rs/tui/src/lib.rs:102` `mod style;`
- `mod` `codex-rs/tui/src/lib.rs:103` `mod terminal_palette;`
- `mod` `codex-rs/tui/src/lib.rs:104` `mod text_formatting;`
- `mod` `codex-rs/tui/src/lib.rs:105` `mod tooltips;`
- `mod` `codex-rs/tui/src/lib.rs:106` `mod tui;`
- `mod` `codex-rs/tui/src/lib.rs:107` `mod ui_consts;`
- `mod` `codex-rs/tui/src/lib.rs:108` `pub mod update_action;`
- `mod` `codex-rs/tui/src/lib.rs:109` `mod update_prompt;`
- `mod` `codex-rs/tui/src/lib.rs:110` `mod updates;`
- `mod` `codex-rs/tui/src/lib.rs:111` `mod version;`
- `mod` `codex-rs/tui/src/lib.rs:113` `mod wrapping;`
- `mod` `codex-rs/tui/src/lib.rs:116` `pub mod test_backend;`
- `use` `codex-rs/tui/src/lib.rs:118` `use crate::onboarding::onboarding_screen::OnboardingScreenArgs;`
- `use` `codex-rs/tui/src/lib.rs:119` `use crate::onboarding::onboarding_screen::run_onboarding_app;`
- `use` `codex-rs/tui/src/lib.rs:120` `use crate::tui::Tui;`
- `fn` `codex-rs/tui/src/lib.rs:127` `pub async fn run_main(`
- `use` `codex-rs/tui/src/lib.rs:315` `use std::os::unix::fs::OpenOptionsExt;`
- `fn` `codex-rs/tui/src/lib.rs:412` `async fn run_ratatui_app(`
- `use` `codex-rs/tui/src/lib.rs:440` `use crate::update_prompt::UpdatePromptOutcome;`
- `fn` `codex-rs/tui/src/lib.rs:742` `async fn parse_latest_turn_context_cwd(path: &Path) -> Option<PathBuf> {`
- `fn` `codex-rs/tui/src/lib.rs:794` `fn restore() {`
- `fn` `codex-rs/tui/src/lib.rs:818` `fn determine_alt_screen_mode(no_alt_screen: bool, tui_alternate_screen: AltScreenMode) -> bool {`
- `enum` `codex-rs/tui/src/lib.rs:834` `pub enum LoginStatus {`
- `fn` `codex-rs/tui/src/lib.rs:839` `fn get_login_status(config: &Config) -> LoginStatus {`
- `fn` `codex-rs/tui/src/lib.rs:857` `async fn load_config_or_exit(`
- `fn` `codex-rs/tui/src/lib.rs:866` `async fn load_config_or_exit_with_fallback_cwd(`
- `fn` `codex-rs/tui/src/lib.rs:892` `fn should_show_trust_screen(config: &Config) -> bool {`
- `fn` `codex-rs/tui/src/lib.rs:907` `fn should_show_onboarding(`
- `fn` `codex-rs/tui/src/lib.rs:919` `fn should_show_login_screen(login_status: LoginStatus, config: &Config) -> bool {`
- `use` `codex-rs/tui/src/lib.rs:931` `use super::*;`
- `use` `codex-rs/tui/src/lib.rs:932` `use codex_core::config::ConfigBuilder;`
- `use` `codex-rs/tui/src/lib.rs:933` `use codex_core::config::ConfigOverrides;`
- `use` `codex-rs/tui/src/lib.rs:934` `use codex_core::config::ProjectConfig;`
- `use` `codex-rs/tui/src/lib.rs:935` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/tui/src/lib.rs:936` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/tui/src/lib.rs:937` `use codex_protocol::protocol::RolloutLine;`
- `use` `codex-rs/tui/src/lib.rs:938` `use codex_protocol::protocol::SessionMeta;`
- `use` `codex-rs/tui/src/lib.rs:939` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/tui/src/lib.rs:940` `use codex_protocol::protocol::TurnContextItem;`
- `use` `codex-rs/tui/src/lib.rs:941` `use serial_test::serial;`
- `use` `codex-rs/tui/src/lib.rs:942` `use tempfile::TempDir;`
- `fn` `codex-rs/tui/src/lib.rs:944` `async fn build_config(temp_dir: &TempDir) -> std::io::Result<Config> {`
- `fn` `codex-rs/tui/src/lib.rs:953` `async fn windows_skips_trust_prompt_without_sandbox() -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/lib.rs:976` `async fn windows_shows_trust_prompt_with_sandbox() -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/lib.rs:998` `async fn untrusted_project_skips_trust_prompt() -> std::io::Result<()> {`
- `use` `codex-rs/tui/src/lib.rs:999` `use codex_protocol::config_types::TrustLevel;`
- `fn` `codex-rs/tui/src/lib.rs:1015` `fn build_turn_context(config: &Config, cwd: PathBuf) -> TurnContextItem {`
- `fn` `codex-rs/tui/src/lib.rs:1037` `async fn read_session_cwd_prefers_latest_turn_context() -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/lib.rs:1069` `async fn should_prompt_when_meta_matches_current_but_latest_turn_differs() -> std::io::Result<()>`
- `fn` `codex-rs/tui/src/lib.rs:1110` `async fn config_rebuild_changes_trust_defaults_with_cwd() -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/lib.rs:1162` `async fn read_session_cwd_falls_back_to_session_meta() -> std::io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use additional_dirs::add_dir_warning_message;`
- `use app::App;`
- `use codex_cloud_requirements::cloud_requirements_loader;`
- `use codex_common::oss::ensure_oss_provider_ready;`
- `use codex_common::oss::get_default_model_for_oss_provider;`
- `use codex_core::AuthManager;`
- `use codex_core::CodexAuth;`
- `use codex_core::INTERACTIVE_SESSION_SOURCES;`
- `use codex_core::RolloutRecorder;`
- `use codex_core::ThreadSortKey;`
- `use codex_core::auth::AuthMode;`
- `use codex_core::auth::enforce_login_restrictions;`
- `use codex_core::config::Config;`
- `use codex_core::config::ConfigBuilder;`
- `use codex_core::config::ConfigOverrides;`
- `use codex_core::config::find_codex_home;`
- `use codex_core::config::load_config_as_toml_with_cli_overrides;`
- `use codex_core::config::resolve_oss_provider;`
- `use codex_core::config_loader::CloudRequirementsLoader;`
- `use codex_core::config_loader::ConfigLoadError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
