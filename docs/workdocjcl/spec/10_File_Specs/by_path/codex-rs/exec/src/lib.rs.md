# `codex-rs/exec/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `32485`
- sha256: `319437004cd80870f103f62feff0e66971c923094a1e62e0a834457cbd2a353a`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/exec/src/lib.rs:7` `mod cli;`
- `mod` `codex-rs/exec/src/lib.rs:8` `mod event_processor;`
- `mod` `codex-rs/exec/src/lib.rs:9` `mod event_processor_with_human_output;`
- `mod` `codex-rs/exec/src/lib.rs:10` `pub mod event_processor_with_jsonl_output;`
- `mod` `codex-rs/exec/src/lib.rs:11` `pub mod exec_events;`
- `use` `codex-rs/exec/src/lib.rs:16` `use codex_cloud_requirements::cloud_requirements_loader;`
- `use` `codex-rs/exec/src/lib.rs:17` `use codex_common::oss::ensure_oss_provider_ready;`
- `use` `codex-rs/exec/src/lib.rs:18` `use codex_common::oss::get_default_model_for_oss_provider;`
- `use` `codex-rs/exec/src/lib.rs:19` `use codex_common::oss::ollama_chat_deprecation_notice;`
- `use` `codex-rs/exec/src/lib.rs:20` `use codex_core::AuthManager;`
- `use` `codex-rs/exec/src/lib.rs:21` `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use` `codex-rs/exec/src/lib.rs:22` `use codex_core::NewThread;`
- `use` `codex-rs/exec/src/lib.rs:23` `use codex_core::OLLAMA_CHAT_PROVIDER_ID;`
- `use` `codex-rs/exec/src/lib.rs:24` `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use` `codex-rs/exec/src/lib.rs:25` `use codex_core::ThreadManager;`
- `use` `codex-rs/exec/src/lib.rs:26` `use codex_core::auth::enforce_login_restrictions;`
- `use` `codex-rs/exec/src/lib.rs:27` `use codex_core::config::Config;`
- `use` `codex-rs/exec/src/lib.rs:28` `use codex_core::config::ConfigBuilder;`
- `use` `codex-rs/exec/src/lib.rs:29` `use codex_core::config::ConfigOverrides;`
- `use` `codex-rs/exec/src/lib.rs:30` `use codex_core::config::find_codex_home;`
- `use` `codex-rs/exec/src/lib.rs:31` `use codex_core::config::load_config_as_toml_with_cli_overrides;`
- `use` `codex-rs/exec/src/lib.rs:32` `use codex_core::config::resolve_oss_provider;`
- `use` `codex-rs/exec/src/lib.rs:33` `use codex_core::config_loader::ConfigLoadError;`
- `use` `codex-rs/exec/src/lib.rs:34` `use codex_core::config_loader::format_config_error_with_source;`
- `use` `codex-rs/exec/src/lib.rs:35` `use codex_core::git_info::get_git_repo_root;`
- `use` `codex-rs/exec/src/lib.rs:36` `use codex_core::models_manager::manager::RefreshStrategy;`
- `use` `codex-rs/exec/src/lib.rs:37` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/exec/src/lib.rs:38` `use codex_core::protocol::Event;`
- `use` `codex-rs/exec/src/lib.rs:39` `use codex_core::protocol::EventMsg;`
- `use` `codex-rs/exec/src/lib.rs:40` `use codex_core::protocol::Op;`
- `use` `codex-rs/exec/src/lib.rs:41` `use codex_core::protocol::ReviewRequest;`
- `use` `codex-rs/exec/src/lib.rs:42` `use codex_core::protocol::ReviewTarget;`
- `use` `codex-rs/exec/src/lib.rs:43` `use codex_core::protocol::SessionSource;`
- `use` `codex-rs/exec/src/lib.rs:44` `use codex_protocol::approvals::ElicitationAction;`
- `use` `codex-rs/exec/src/lib.rs:45` `use codex_protocol::config_types::SandboxMode;`
- `use` `codex-rs/exec/src/lib.rs:46` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/exec/src/lib.rs:47` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/exec/src/lib.rs:48` `use event_processor_with_human_output::EventProcessorWithHumanOutput;`
- `use` `codex-rs/exec/src/lib.rs:49` `use event_processor_with_jsonl_output::EventProcessorWithJsonOutput;`
- `use` `codex-rs/exec/src/lib.rs:50` `use serde_json::Value;`
- `use` `codex-rs/exec/src/lib.rs:51` `use std::collections::HashSet;`
- `use` `codex-rs/exec/src/lib.rs:52` `use std::io::IsTerminal;`
- `use` `codex-rs/exec/src/lib.rs:53` `use std::io::Read;`
- `use` `codex-rs/exec/src/lib.rs:54` `use std::path::PathBuf;`
- `use` `codex-rs/exec/src/lib.rs:55` `use std::sync::Arc;`
- `use` `codex-rs/exec/src/lib.rs:56` `use supports_color::Stream;`
- `use` `codex-rs/exec/src/lib.rs:57` `use tokio::sync::Mutex;`
- `use` `codex-rs/exec/src/lib.rs:58` `use tracing::debug;`
- `use` `codex-rs/exec/src/lib.rs:59` `use tracing::error;`
- `use` `codex-rs/exec/src/lib.rs:60` `use tracing::info;`
- `use` `codex-rs/exec/src/lib.rs:61` `use tracing::warn;`
- `use` `codex-rs/exec/src/lib.rs:62` `use tracing_subscriber::EnvFilter;`
- `use` `codex-rs/exec/src/lib.rs:63` `use tracing_subscriber::prelude::*;`
- `use` `codex-rs/exec/src/lib.rs:64` `use uuid::Uuid;`
- `use` `codex-rs/exec/src/lib.rs:66` `use crate::cli::Command as ExecCommand;`
- `use` `codex-rs/exec/src/lib.rs:67` `use crate::event_processor::CodexStatus;`
- `use` `codex-rs/exec/src/lib.rs:68` `use crate::event_processor::EventProcessor;`
- `use` `codex-rs/exec/src/lib.rs:69` `use codex_core::default_client::set_default_client_residency_requirement;`
- `use` `codex-rs/exec/src/lib.rs:70` `use codex_core::default_client::set_default_originator;`
- `use` `codex-rs/exec/src/lib.rs:71` `use codex_core::find_thread_path_by_id_str;`
- `use` `codex-rs/exec/src/lib.rs:72` `use codex_core::find_thread_path_by_name_str;`
- `enum` `codex-rs/exec/src/lib.rs:74` `enum InitialOperation {`
- `struct` `codex-rs/exec/src/lib.rs:85` `struct ThreadEventEnvelope {`
- `fn` `codex-rs/exec/src/lib.rs:91` `pub async fn run_main(cli: Cli, codex_linux_sandbox_exe: Option<PathBuf>) -> anyhow::Result<()> {`
- `fn` `codex-rs/exec/src/lib.rs:577` `fn spawn_thread_listener(`
- `fn` `codex-rs/exec/src/lib.rs:613` `async fn resolve_resume_path(`
- `fn` `codex-rs/exec/src/lib.rs:655` `fn load_output_schema(path: Option<PathBuf>) -> Option<Value> {`
- `enum` `codex-rs/exec/src/lib.rs:682` `enum PromptDecodeError {`
- `impl` `codex-rs/exec/src/lib.rs:688` `impl std::fmt::Display for PromptDecodeError {`
- `fn` `codex-rs/exec/src/lib.rs:689` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/exec/src/lib.rs:707` `fn decode_prompt_bytes(input: &[u8]) -> Result<String, PromptDecodeError> {`
- `fn` `codex-rs/exec/src/lib.rs:737` `fn decode_utf16(`
- `fn` `codex-rs/exec/src/lib.rs:754` `fn resolve_prompt(prompt_arg: Option<String>) -> String {`
- `fn` `codex-rs/exec/src/lib.rs:794` `fn build_review_request(args: ReviewArgs) -> anyhow::Result<ReviewRequest> {`
- `use` `codex-rs/exec/src/lib.rs:826` `use super::*;`
- `use` `codex-rs/exec/src/lib.rs:827` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/exec/src/lib.rs:830` `fn builds_uncommitted_review_request() {`
- `fn` `codex-rs/exec/src/lib.rs:849` `fn builds_commit_review_request_with_title() {`
- `fn` `codex-rs/exec/src/lib.rs:871` `fn builds_custom_review_request_trims_prompt() {`
- `fn` `codex-rs/exec/src/lib.rs:892` `fn decode_prompt_bytes_strips_utf8_bom() {`
- `fn` `codex-rs/exec/src/lib.rs:901` `fn decode_prompt_bytes_decodes_utf16le_bom() {`
- `fn` `codex-rs/exec/src/lib.rs:911` `fn decode_prompt_bytes_decodes_utf16be_bom() {`
- `fn` `codex-rs/exec/src/lib.rs:921` `fn decode_prompt_bytes_rejects_utf32le_bom() {`
- `fn` `codex-rs/exec/src/lib.rs:939` `fn decode_prompt_bytes_rejects_utf32be_bom() {`
- `fn` `codex-rs/exec/src/lib.rs:957` `fn decode_prompt_bytes_rejects_invalid_utf8() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_cloud_requirements::cloud_requirements_loader;`
- `use codex_common::oss::ensure_oss_provider_ready;`
- `use codex_common::oss::get_default_model_for_oss_provider;`
- `use codex_common::oss::ollama_chat_deprecation_notice;`
- `use codex_core::AuthManager;`
- `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use codex_core::NewThread;`
- `use codex_core::OLLAMA_CHAT_PROVIDER_ID;`
- `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use codex_core::ThreadManager;`
- `use codex_core::auth::enforce_login_restrictions;`
- `use codex_core::config::Config;`
- `use codex_core::config::ConfigBuilder;`
- `use codex_core::config::ConfigOverrides;`
- `use codex_core::config::find_codex_home;`
- `use codex_core::config::load_config_as_toml_with_cli_overrides;`
- `use codex_core::config::resolve_oss_provider;`
- `use codex_core::config_loader::ConfigLoadError;`
- `use codex_core::config_loader::format_config_error_with_source;`
- `use codex_core::git_info::get_git_repo_root;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
