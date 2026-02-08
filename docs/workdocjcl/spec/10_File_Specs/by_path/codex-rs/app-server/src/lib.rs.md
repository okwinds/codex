# `codex-rs/app-server/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15363`
- sha256: `20f7cd3b3a4a9eaa1567a485b555ae0a1f8ab0e5a487a6540283c305e4362e31`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/lib.rs:3` `use codex_cloud_requirements::cloud_requirements_loader;`
- `use` `codex-rs/app-server/src/lib.rs:4` `use codex_common::CliConfigOverrides;`
- `use` `codex-rs/app-server/src/lib.rs:5` `use codex_core::AuthManager;`
- `use` `codex-rs/app-server/src/lib.rs:6` `use codex_core::config::Config;`
- `use` `codex-rs/app-server/src/lib.rs:7` `use codex_core::config::ConfigBuilder;`
- `use` `codex-rs/app-server/src/lib.rs:8` `use codex_core::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/app-server/src/lib.rs:9` `use codex_core::config_loader::ConfigLayerStackOrdering;`
- `use` `codex-rs/app-server/src/lib.rs:10` `use codex_core::config_loader::LoaderOverrides;`
- `use` `codex-rs/app-server/src/lib.rs:11` `use std::io::ErrorKind;`
- `use` `codex-rs/app-server/src/lib.rs:12` `use std::io::Result as IoResult;`
- `use` `codex-rs/app-server/src/lib.rs:13` `use std::path::PathBuf;`
- `use` `codex-rs/app-server/src/lib.rs:15` `use crate::message_processor::MessageProcessor;`
- `use` `codex-rs/app-server/src/lib.rs:16` `use crate::message_processor::MessageProcessorArgs;`
- `use` `codex-rs/app-server/src/lib.rs:17` `use crate::outgoing_message::OutgoingMessage;`
- `use` `codex-rs/app-server/src/lib.rs:18` `use crate::outgoing_message::OutgoingMessageSender;`
- `use` `codex-rs/app-server/src/lib.rs:19` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/app-server/src/lib.rs:20` `use codex_app_server_protocol::ConfigWarningNotification;`
- `use` `codex-rs/app-server/src/lib.rs:21` `use codex_app_server_protocol::JSONRPCMessage;`
- `use` `codex-rs/app-server/src/lib.rs:22` `use codex_app_server_protocol::TextPosition as AppTextPosition;`
- `use` `codex-rs/app-server/src/lib.rs:23` `use codex_app_server_protocol::TextRange as AppTextRange;`
- `use` `codex-rs/app-server/src/lib.rs:24` `use codex_core::ExecPolicyError;`
- `use` `codex-rs/app-server/src/lib.rs:25` `use codex_core::check_execpolicy_for_warnings;`
- `use` `codex-rs/app-server/src/lib.rs:26` `use codex_core::config_loader::ConfigLoadError;`
- `use` `codex-rs/app-server/src/lib.rs:27` `use codex_core::config_loader::TextRange as CoreTextRange;`
- `use` `codex-rs/app-server/src/lib.rs:28` `use codex_feedback::CodexFeedback;`
- `use` `codex-rs/app-server/src/lib.rs:29` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/app-server/src/lib.rs:30` `use tokio::io::AsyncWriteExt;`
- `use` `codex-rs/app-server/src/lib.rs:31` `use tokio::io::BufReader;`
- `use` `codex-rs/app-server/src/lib.rs:32` `use tokio::io::{self};`
- `use` `codex-rs/app-server/src/lib.rs:33` `use tokio::sync::mpsc;`
- `use` `codex-rs/app-server/src/lib.rs:34` `use toml::Value as TomlValue;`
- `use` `codex-rs/app-server/src/lib.rs:35` `use tracing::debug;`
- `use` `codex-rs/app-server/src/lib.rs:36` `use tracing::error;`
- `use` `codex-rs/app-server/src/lib.rs:37` `use tracing::info;`
- `use` `codex-rs/app-server/src/lib.rs:38` `use tracing::warn;`
- `use` `codex-rs/app-server/src/lib.rs:39` `use tracing_subscriber::EnvFilter;`
- `use` `codex-rs/app-server/src/lib.rs:40` `use tracing_subscriber::Layer;`
- `use` `codex-rs/app-server/src/lib.rs:41` `use tracing_subscriber::layer::SubscriberExt;`
- `use` `codex-rs/app-server/src/lib.rs:42` `use tracing_subscriber::util::SubscriberInitExt;`
- `mod` `codex-rs/app-server/src/lib.rs:44` `mod bespoke_event_handling;`
- `mod` `codex-rs/app-server/src/lib.rs:45` `mod codex_message_processor;`
- `mod` `codex-rs/app-server/src/lib.rs:46` `mod config_api;`
- `mod` `codex-rs/app-server/src/lib.rs:47` `mod dynamic_tools;`
- `mod` `codex-rs/app-server/src/lib.rs:48` `mod error_code;`
- `mod` `codex-rs/app-server/src/lib.rs:49` `mod filters;`
- `mod` `codex-rs/app-server/src/lib.rs:50` `mod fuzzy_file_search;`
- `mod` `codex-rs/app-server/src/lib.rs:51` `mod message_processor;`
- `mod` `codex-rs/app-server/src/lib.rs:52` `mod models;`
- `mod` `codex-rs/app-server/src/lib.rs:53` `mod outgoing_message;`
- `const` `codex-rs/app-server/src/lib.rs:58` `const CHANNEL_CAPACITY: usize = 128;`
- `fn` `codex-rs/app-server/src/lib.rs:60` `fn config_warning_from_error(`
- `fn` `codex-rs/app-server/src/lib.rs:76` `fn config_error_location(err: &std::io::Error) -> Option<(String, AppTextRange)> {`
- `fn` `codex-rs/app-server/src/lib.rs:88` `fn exec_policy_warning_location(err: &ExecPolicyError) -> (Option<String>, Option<AppTextRange>) {`
- `fn` `codex-rs/app-server/src/lib.rs:110` `fn app_text_range(range: &CoreTextRange) -> AppTextRange {`
- `fn` `codex-rs/app-server/src/lib.rs:123` `fn project_config_warning(config: &Config) -> Option<ConfigWarningNotification> {`
- `fn` `codex-rs/app-server/src/lib.rs:170` `pub async fn run_main(`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_cloud_requirements::cloud_requirements_loader;`
- `use codex_common::CliConfigOverrides;`
- `use codex_core::AuthManager;`
- `use codex_core::config::Config;`
- `use codex_core::config::ConfigBuilder;`
- `use codex_core::config_loader::CloudRequirementsLoader;`
- `use codex_core::config_loader::ConfigLayerStackOrdering;`
- `use codex_core::config_loader::LoaderOverrides;`
- `use std::io::ErrorKind;`
- `use std::io::Result as IoResult;`
- `use std::path::PathBuf;`
- `use crate::message_processor::MessageProcessor;`
- `use crate::message_processor::MessageProcessorArgs;`
- `use crate::outgoing_message::OutgoingMessage;`
- `use crate::outgoing_message::OutgoingMessageSender;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_app_server_protocol::ConfigWarningNotification;`
- `use codex_app_server_protocol::JSONRPCMessage;`
- `use codex_app_server_protocol::TextPosition as AppTextPosition;`
- `use codex_app_server_protocol::TextRange as AppTextRange;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
