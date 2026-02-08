# `codex-rs/core/src/config/edit.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `56646`
- sha256: `364a62cccd007801fe57326b79ed5032949d0dd39cb29fd9e740aa22bebc1862`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config/edit.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum ConfigEdit {`
- `pub fn apply_blocking(`
- `pub struct ConfigEditsBuilder {`
- `pub fn new(codex_home: &Path) -> Self {`
- `pub fn with_profile(mut self, profile: Option<&str>) -> Self {`
- `pub fn set_model(mut self, model: Option<&str>, effort: Option<ReasoningEffort>) -> Self {`
- `pub fn set_personality(mut self, personality: Option<Personality>) -> Self {`
- `pub fn set_hide_full_access_warning(mut self, acknowledged: bool) -> Self {`
- `pub fn set_hide_world_writable_warning(mut self, acknowledged: bool) -> Self {`
- `pub fn set_hide_rate_limit_model_nudge(mut self, acknowledged: bool) -> Self {`
- `pub fn set_hide_model_migration_prompt(mut self, model: &str, acknowledged: bool) -> Self {`
- `pub fn record_model_migration_seen(mut self, from: &str, to: &str) -> Self {`
- `pub fn set_windows_wsl_setup_acknowledged(mut self, acknowledged: bool) -> Self {`
- `pub fn replace_mcp_servers(mut self, servers: &BTreeMap<String, McpServerConfig>) -> Self {`
- `pub fn set_feature_enabled(mut self, key: &str, enabled: bool) -> Self {`
- `pub fn apply_blocking(self) -> anyhow::Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config/edit.rs:1` `use crate::config::CONFIG_TOML_FILE;`
- `use` `codex-rs/core/src/config/edit.rs:2` `use crate::config::types::McpServerConfig;`
- `use` `codex-rs/core/src/config/edit.rs:3` `use crate::config::types::Notice;`
- `use` `codex-rs/core/src/config/edit.rs:4` `use crate::path_utils::resolve_symlink_write_paths;`
- `use` `codex-rs/core/src/config/edit.rs:5` `use crate::path_utils::write_atomically;`
- `use` `codex-rs/core/src/config/edit.rs:6` `use anyhow::Context;`
- `use` `codex-rs/core/src/config/edit.rs:7` `use codex_protocol::config_types::Personality;`
- `use` `codex-rs/core/src/config/edit.rs:8` `use codex_protocol::config_types::TrustLevel;`
- `use` `codex-rs/core/src/config/edit.rs:9` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/config/edit.rs:10` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/config/edit.rs:11` `use std::path::Path;`
- `use` `codex-rs/core/src/config/edit.rs:12` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/config/edit.rs:13` `use tokio::task;`
- `use` `codex-rs/core/src/config/edit.rs:14` `use toml_edit::ArrayOfTables;`
- `use` `codex-rs/core/src/config/edit.rs:15` `use toml_edit::DocumentMut;`
- `use` `codex-rs/core/src/config/edit.rs:16` `use toml_edit::Item as TomlItem;`
- `use` `codex-rs/core/src/config/edit.rs:17` `use toml_edit::Table as TomlTable;`
- `use` `codex-rs/core/src/config/edit.rs:18` `use toml_edit::value;`
- `enum` `codex-rs/core/src/config/edit.rs:22` `pub enum ConfigEdit {`
- `use` `codex-rs/core/src/config/edit.rs:60` `use crate::config::types::McpServerConfig;`
- `use` `codex-rs/core/src/config/edit.rs:61` `use crate::config::types::McpServerTransportConfig;`
- `use` `codex-rs/core/src/config/edit.rs:62` `use toml_edit::Array as TomlArray;`
- `use` `codex-rs/core/src/config/edit.rs:63` `use toml_edit::InlineTable;`
- `use` `codex-rs/core/src/config/edit.rs:64` `use toml_edit::Item as TomlItem;`
- `use` `codex-rs/core/src/config/edit.rs:65` `use toml_edit::Table as TomlTable;`
- `use` `codex-rs/core/src/config/edit.rs:66` `use toml_edit::value;`
- `fn` `codex-rs/core/src/config/edit.rs:100` `fn serialize_mcp_server_table(config: &McpServerConfig) -> TomlTable {`
- `fn` `codex-rs/core/src/config/edit.rs:201` `fn table_from_inline(inline: &InlineTable) -> TomlTable {`
- `struct` `codex-rs/core/src/config/edit.rs:244` `struct ConfigDocument {`
- `enum` `codex-rs/core/src/config/edit.rs:250` `enum Scope {`
- `enum` `codex-rs/core/src/config/edit.rs:256` `enum TraversalMode {`
- `impl` `codex-rs/core/src/config/edit.rs:261` `impl ConfigDocument {`
- `fn` `codex-rs/core/src/config/edit.rs:262` `fn new(doc: DocumentMut, profile: Option<String>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:266` `fn apply(&mut self, edit: &ConfigEdit) -> anyhow::Result<bool> {`
- `fn` `codex-rs/core/src/config/edit.rs:335` `fn write_profile_value(&mut self, segments: &[&str], value: Option<TomlItem>) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:342` `fn write_value(&mut self, scope: Scope, segments: &[&str], value: TomlItem) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:347` `fn clear(&mut self, scope: Scope, segments: &[&str]) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:352` `fn clear_owned(&mut self, segments: &[String]) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:356` `fn replace_mcp_servers(&mut self, servers: &BTreeMap<String, McpServerConfig>) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:409` `fn set_skill_config(&mut self, path: &Path, enabled: bool) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:516` `fn scoped_segments(&self, scope: Scope, segments: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/config/edit.rs:536` `fn insert(&mut self, segments: &[String], value: TomlItem) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:553` `fn remove(&mut self, segments: &[String]) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:565` `fn descend(&mut self, segments: &[String], mode: TraversalMode) -> Option<&mut TomlTable> {`
- `fn` `codex-rs/core/src/config/edit.rs:591` `fn preserve_decor(existing: &TomlItem, replacement: &mut TomlItem) {`
- `fn` `codex-rs/core/src/config/edit.rs:623` `fn normalize_skill_config_path(path: &Path) -> String {`
- `fn` `codex-rs/core/src/config/edit.rs:631` `pub fn apply_blocking(`
- `fn` `codex-rs/core/src/config/edit.rs:685` `pub async fn apply(`
- `struct` `codex-rs/core/src/config/edit.rs:699` `pub struct ConfigEditsBuilder {`
- `impl` `codex-rs/core/src/config/edit.rs:705` `impl ConfigEditsBuilder {`
- `fn` `codex-rs/core/src/config/edit.rs:706` `pub fn new(codex_home: &Path) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:714` `pub fn with_profile(mut self, profile: Option<&str>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:719` `pub fn set_model(mut self, model: Option<&str>, effort: Option<ReasoningEffort>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:727` `pub fn set_personality(mut self, personality: Option<Personality>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:733` `pub fn set_hide_full_access_warning(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:739` `pub fn set_hide_world_writable_warning(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:745` `pub fn set_hide_rate_limit_model_nudge(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:751` `pub fn set_hide_model_migration_prompt(mut self, model: &str, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:760` `pub fn record_model_migration_seen(mut self, from: &str, to: &str) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:768` `pub fn set_windows_wsl_setup_acknowledged(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:774` `pub fn replace_mcp_servers(mut self, servers: &BTreeMap<String, McpServerConfig>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:793` `pub fn set_feature_enabled(mut self, key: &str, enabled: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:810` `pub fn apply_blocking(self) -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config/edit.rs:815` `pub async fn apply(self) -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config/edit.rs:826` `use super::*;`
- `use` `codex-rs/core/src/config/edit.rs:827` `use crate::config::types::McpServerTransportConfig;`
- `use` `codex-rs/core/src/config/edit.rs:828` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/config/edit.rs:829` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config/edit.rs:831` `use std::os::unix::fs::symlink;`
- `use` `codex-rs/core/src/config/edit.rs:832` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/config/edit.rs:833` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/config/edit.rs:836` `fn blocking_set_model_top_level() {`
- `fn` `codex-rs/core/src/config/edit.rs:859` `fn builder_with_edits_applies_custom_paths() {`
- `fn` `codex-rs/core/src/config/edit.rs:877` `fn set_skill_config_writes_disabled_entry() {`
- `fn` `codex-rs/core/src/config/edit.rs:899` `fn set_skill_config_removes_entry_when_enabled() {`
- `fn` `codex-rs/core/src/config/edit.rs:925` `fn blocking_set_model_preserves_inline_table_contents() {`
- `fn` `codex-rs/core/src/config/edit.rs:973` `fn blocking_set_model_writes_through_symlink_chain() {`
- `fn` `codex-rs/core/src/config/edit.rs:1006` `fn blocking_set_model_replaces_symlink_on_cycle() {`
- `fn` `codex-rs/core/src/config/edit.rs:1037` `fn batch_write_table_upsert_preserves_inline_comments() {`
- `fn` `codex-rs/core/src/config/edit.rs:1099` `fn blocking_clear_model_removes_inline_table_entry() {`
- `fn` `codex-rs/core/src/config/edit.rs:1134` `fn blocking_set_model_scopes_to_active_profile() {`
- `fn` `codex-rs/core/src/config/edit.rs:1169` `fn blocking_set_model_with_explicit_profile() {`
- `fn` `codex-rs/core/src/config/edit.rs:1199` `fn blocking_set_hide_full_access_warning_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1233` `fn blocking_set_hide_rate_limit_model_nudge_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1261` `fn blocking_set_hide_gpt5_1_migration_prompt_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1291` `fn blocking_set_hide_gpt_5_1_codex_max_migration_prompt_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1321` `fn blocking_record_model_migration_seen_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1353` `fn blocking_replace_mcp_servers_round_trips() {`
- `fn` `codex-rs/core/src/config/edit.rs:1441` `fn blocking_replace_mcp_servers_preserves_inline_comments() {`
- `fn` `codex-rs/core/src/config/edit.rs:1487` `fn blocking_replace_mcp_servers_preserves_inline_comment_suffix() {`
- `fn` `codex-rs/core/src/config/edit.rs:1531` `fn blocking_replace_mcp_servers_preserves_inline_comment_after_removing_keys() {`
- `fn` `codex-rs/core/src/config/edit.rs:1575` `fn blocking_replace_mcp_servers_preserves_inline_comment_prefix_on_update() {`
- `fn` `codex-rs/core/src/config/edit.rs:1621` `fn blocking_clear_path_noop_when_missing() {`
- `fn` `codex-rs/core/src/config/edit.rs:1641` `fn blocking_set_path_updates_notifications() {`
- `fn` `codex-rs/core/src/config/edit.rs:1667` `async fn async_builder_set_model_persists() {`
- `fn` `codex-rs/core/src/config/edit.rs:1686` `fn blocking_builder_set_model_round_trips_back_and_forth() {`
- `fn` `codex-rs/core/src/config/edit.rs:1720` `async fn blocking_set_asynchronous_helpers_available() {`
- `fn` `codex-rs/core/src/config/edit.rs:1741` `fn replace_mcp_servers_blocking_clears_table_when_empty() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::CONFIG_TOML_FILE;`
- `use crate::config::types::McpServerConfig;`
- `use crate::config::types::Notice;`
- `use crate::path_utils::resolve_symlink_write_paths;`
- `use crate::path_utils::write_atomically;`
- `use anyhow::Context;`
- `use codex_protocol::config_types::Personality;`
- `use codex_protocol::config_types::TrustLevel;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use std::collections::BTreeMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tokio::task;`
- `use toml_edit::ArrayOfTables;`
- `use toml_edit::DocumentMut;`
- `use toml_edit::Item as TomlItem;`
- `use toml_edit::Table as TomlTable;`
- `use toml_edit::value;`
- `use crate::config::types::McpServerConfig;`
- `use crate::config::types::McpServerTransportConfig;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
