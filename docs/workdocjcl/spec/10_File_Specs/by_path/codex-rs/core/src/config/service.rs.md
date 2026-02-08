# `codex-rs/core/src/config/service.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `43591`
- sha256: `60d73c7be303d083d0c9344630e445253ecf0d6c785986f680c1bf199ed34434`
- generated_utc: `2026-02-08T10:45:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config/service.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum ConfigServiceError {`
- `pub fn write_error_code(&self) -> Option<ConfigWriteErrorCode> {`
- `pub struct ConfigService {`
- `pub fn new(`
- `pub fn new_with_defaults(codex_home: PathBuf) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config/service.rs:1` `use super::CONFIG_TOML_FILE;`
- `use` `codex-rs/core/src/config/service.rs:2` `use super::ConfigToml;`
- `use` `codex-rs/core/src/config/service.rs:3` `use crate::config::edit::ConfigEdit;`
- `use` `codex-rs/core/src/config/service.rs:4` `use crate::config::edit::ConfigEditsBuilder;`
- `use` `codex-rs/core/src/config/service.rs:5` `use crate::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/core/src/config/service.rs:6` `use crate::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/core/src/config/service.rs:7` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/config/service.rs:8` `use crate::config_loader::ConfigLayerStackOrdering;`
- `use` `codex-rs/core/src/config/service.rs:9` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/config/service.rs:10` `use crate::config_loader::LoaderOverrides;`
- `use` `codex-rs/core/src/config/service.rs:11` `use crate::config_loader::load_config_layers_state;`
- `use` `codex-rs/core/src/config/service.rs:12` `use crate::config_loader::merge_toml_values;`
- `use` `codex-rs/core/src/config/service.rs:13` `use crate::path_utils;`
- `use` `codex-rs/core/src/config/service.rs:14` `use crate::path_utils::SymlinkWritePaths;`
- `use` `codex-rs/core/src/config/service.rs:15` `use crate::path_utils::resolve_symlink_write_paths;`
- `use` `codex-rs/core/src/config/service.rs:16` `use crate::path_utils::write_atomically;`
- `use` `codex-rs/core/src/config/service.rs:17` `use codex_app_server_protocol::Config as ApiConfig;`
- `use` `codex-rs/core/src/config/service.rs:18` `use codex_app_server_protocol::ConfigBatchWriteParams;`
- `use` `codex-rs/core/src/config/service.rs:19` `use codex_app_server_protocol::ConfigLayerMetadata;`
- `use` `codex-rs/core/src/config/service.rs:20` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/config/service.rs:21` `use codex_app_server_protocol::ConfigReadParams;`
- `use` `codex-rs/core/src/config/service.rs:22` `use codex_app_server_protocol::ConfigReadResponse;`
- `use` `codex-rs/core/src/config/service.rs:23` `use codex_app_server_protocol::ConfigValueWriteParams;`
- `use` `codex-rs/core/src/config/service.rs:24` `use codex_app_server_protocol::ConfigWriteErrorCode;`
- `use` `codex-rs/core/src/config/service.rs:25` `use codex_app_server_protocol::ConfigWriteResponse;`
- `use` `codex-rs/core/src/config/service.rs:26` `use codex_app_server_protocol::MergeStrategy;`
- `use` `codex-rs/core/src/config/service.rs:27` `use codex_app_server_protocol::OverriddenMetadata;`
- `use` `codex-rs/core/src/config/service.rs:28` `use codex_app_server_protocol::WriteStatus;`
- `use` `codex-rs/core/src/config/service.rs:29` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config/service.rs:30` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/core/src/config/service.rs:31` `use std::borrow::Cow;`
- `use` `codex-rs/core/src/config/service.rs:32` `use std::path::Path;`
- `use` `codex-rs/core/src/config/service.rs:33` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/config/service.rs:34` `use thiserror::Error;`
- `use` `codex-rs/core/src/config/service.rs:35` `use tokio::task;`
- `use` `codex-rs/core/src/config/service.rs:36` `use toml::Value as TomlValue;`
- `use` `codex-rs/core/src/config/service.rs:37` `use toml_edit::Item as TomlItem;`
- `enum` `codex-rs/core/src/config/service.rs:40` `pub enum ConfigServiceError {`
- `impl` `codex-rs/core/src/config/service.rs:76` `impl ConfigServiceError {`
- `fn` `codex-rs/core/src/config/service.rs:77` `fn write(code: ConfigWriteErrorCode, message: impl Into<String>) -> Self {`
- `fn` `codex-rs/core/src/config/service.rs:84` `fn io(context: &'static str, source: std::io::Error) -> Self {`
- `fn` `codex-rs/core/src/config/service.rs:88` `fn json(context: &'static str, source: serde_json::Error) -> Self {`
- `fn` `codex-rs/core/src/config/service.rs:92` `fn toml(context: &'static str, source: toml::de::Error) -> Self {`
- `fn` `codex-rs/core/src/config/service.rs:96` `fn anyhow(context: &'static str, source: anyhow::Error) -> Self {`
- `fn` `codex-rs/core/src/config/service.rs:100` `pub fn write_error_code(&self) -> Option<ConfigWriteErrorCode> {`
- `struct` `codex-rs/core/src/config/service.rs:109` `pub struct ConfigService {`
- `impl` `codex-rs/core/src/config/service.rs:116` `impl ConfigService {`
- `fn` `codex-rs/core/src/config/service.rs:117` `pub fn new(`
- `fn` `codex-rs/core/src/config/service.rs:131` `pub fn new_with_defaults(codex_home: PathBuf) -> Self {`
- `fn` `codex-rs/core/src/config/service.rs:140` `pub async fn read(`
- `fn` `codex-rs/core/src/config/service.rs:189` `pub async fn read_requirements(`
- `fn` `codex-rs/core/src/config/service.rs:205` `pub async fn write_value(`
- `fn` `codex-rs/core/src/config/service.rs:214` `pub async fn batch_write(`
- `fn` `codex-rs/core/src/config/service.rs:228` `pub async fn load_user_saved_config(`
- `fn` `codex-rs/core/src/config/service.rs:243` `async fn apply_edits(`
- `fn` `codex-rs/core/src/config/service.rs:378` `async fn load_thread_agnostic_config(&self) -> std::io::Result<ConfigLayerStack> {`
- `fn` `codex-rs/core/src/config/service.rs:391` `async fn create_empty_user_layer(`
- `fn` `codex-rs/core/src/config/service.rs:428` `async fn write_empty_user_config(write_path: PathBuf) -> Result<(), ConfigServiceError> {`
- `fn` `codex-rs/core/src/config/service.rs:435` `fn parse_value(value: JsonValue) -> Result<Option<TomlValue>, String> {`
- `fn` `codex-rs/core/src/config/service.rs:445` `fn parse_key_path(path: &str) -> Result<Vec<String>, String> {`
- `enum` `codex-rs/core/src/config/service.rs:456` `enum MergeError {`
- `fn` `codex-rs/core/src/config/service.rs:461` `fn apply_merge(`
- `fn` `codex-rs/core/src/config/service.rs:518` `fn clear_path(root: &mut TomlValue, segments: &[String]) -> Result<bool, MergeError> {`
- `fn` `codex-rs/core/src/config/service.rs:542` `fn toml_value_to_item(value: &TomlValue) -> anyhow::Result<TomlItem> {`
- `fn` `codex-rs/core/src/config/service.rs:556` `fn toml_value_to_value(value: &TomlValue) -> anyhow::Result<toml_edit::Value> {`
- `fn` `codex-rs/core/src/config/service.rs:580` `fn validate_config(value: &TomlValue) -> Result<(), toml::de::Error> {`
- `fn` `codex-rs/core/src/config/service.rs:585` `fn paths_match(expected: impl AsRef<Path>, provided: impl AsRef<Path>) -> bool {`
- `fn` `codex-rs/core/src/config/service.rs:614` `fn override_message(layer: &ConfigLayerSource) -> String {`
- `fn` `codex-rs/core/src/config/service.rs:642` `fn compute_override_metadata(`
- `fn` `codex-rs/core/src/config/service.rs:673` `fn first_overridden_edit(`
- `fn` `codex-rs/core/src/config/service.rs:686` `fn find_effective_layer(`
- `use` `codex-rs/core/src/config/service.rs:701` `use super::*;`
- `use` `codex-rs/core/src/config/service.rs:702` `use anyhow::Result;`
- `use` `codex-rs/core/src/config/service.rs:703` `use codex_app_server_protocol::AppConfig;`
- `use` `codex-rs/core/src/config/service.rs:704` `use codex_app_server_protocol::AppDisabledReason;`
- `use` `codex-rs/core/src/config/service.rs:705` `use codex_app_server_protocol::AppsConfig;`
- `use` `codex-rs/core/src/config/service.rs:706` `use codex_app_server_protocol::AskForApproval;`
- `use` `codex-rs/core/src/config/service.rs:707` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config/service.rs:708` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config/service.rs:709` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/config/service.rs:712` `fn toml_value_to_item_handles_nested_config_tables() {`
- `fn` `codex-rs/core/src/config/service.rs:761` `async fn write_value_preserves_comments_and_order() -> Result<()> {`
- `fn` `codex-rs/core/src/config/service.rs:807` `async fn write_value_supports_nested_app_paths() -> Result<()> {`
- `fn` `codex-rs/core/src/config/service.rs:863` `async fn read_includes_origins_and_layers() {`
- `fn` `codex-rs/core/src/config/service.rs:944` `async fn write_value_reports_override() {`
- `fn` `codex-rs/core/src/config/service.rs:1005` `async fn version_conflict_rejected() {`
- `fn` `codex-rs/core/src/config/service.rs:1029` `async fn write_value_defaults_to_user_config_path() {`
- `fn` `codex-rs/core/src/config/service.rs:1054` `async fn invalid_user_value_rejected_even_if_overridden_by_managed() {`
- `fn` `codex-rs/core/src/config/service.rs:1095` `async fn read_reports_managed_overrides_user_and_session_flags() {`
- `fn` `codex-rs/core/src/config/service.rs:1150` `async fn write_value_reports_managed_override() {`
- `fn` `codex-rs/core/src/config/service.rs:1191` `async fn upsert_merges_tables_replace_overwrites() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::CONFIG_TOML_FILE;`
- `use super::ConfigToml;`
- `use crate::config::edit::ConfigEdit;`
- `use crate::config::edit::ConfigEditsBuilder;`
- `use crate::config_loader::CloudRequirementsLoader;`
- `use crate::config_loader::ConfigLayerEntry;`
- `use crate::config_loader::ConfigLayerStack;`
- `use crate::config_loader::ConfigLayerStackOrdering;`
- `use crate::config_loader::ConfigRequirementsToml;`
- `use crate::config_loader::LoaderOverrides;`
- `use crate::config_loader::load_config_layers_state;`
- `use crate::config_loader::merge_toml_values;`
- `use crate::path_utils;`
- `use crate::path_utils::SymlinkWritePaths;`
- `use crate::path_utils::resolve_symlink_write_paths;`
- `use crate::path_utils::write_atomically;`
- `use codex_app_server_protocol::Config as ApiConfig;`
- `use codex_app_server_protocol::ConfigBatchWriteParams;`
- `use codex_app_server_protocol::ConfigLayerMetadata;`
- `use codex_app_server_protocol::ConfigLayerSource;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
