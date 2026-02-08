# `codex-rs/core/src/config/edit.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `57410`
- sha256: `9e02658371d6f1c1395160f27bd4ccdaccf4d8ed046353b908689ecd2e2fd672`
- generated_utc: `2026-02-08T10:45:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config/edit.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum ConfigEdit {`
- `pub fn status_line_items_edit(items: &[String]) -> ConfigEdit {`
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
- `fn` `codex-rs/core/src/config/edit.rs:58` `pub fn status_line_items_edit(items: &[String]) -> ConfigEdit {`
- `use` `codex-rs/core/src/config/edit.rs:78` `use crate::config::types::McpServerConfig;`
- `use` `codex-rs/core/src/config/edit.rs:79` `use crate::config::types::McpServerTransportConfig;`
- `use` `codex-rs/core/src/config/edit.rs:80` `use toml_edit::Array as TomlArray;`
- `use` `codex-rs/core/src/config/edit.rs:81` `use toml_edit::InlineTable;`
- `use` `codex-rs/core/src/config/edit.rs:82` `use toml_edit::Item as TomlItem;`
- `use` `codex-rs/core/src/config/edit.rs:83` `use toml_edit::Table as TomlTable;`
- `use` `codex-rs/core/src/config/edit.rs:84` `use toml_edit::value;`
- `fn` `codex-rs/core/src/config/edit.rs:118` `fn serialize_mcp_server_table(config: &McpServerConfig) -> TomlTable {`
- `fn` `codex-rs/core/src/config/edit.rs:222` `fn table_from_inline(inline: &InlineTable) -> TomlTable {`
- `struct` `codex-rs/core/src/config/edit.rs:265` `struct ConfigDocument {`
- `enum` `codex-rs/core/src/config/edit.rs:271` `enum Scope {`
- `enum` `codex-rs/core/src/config/edit.rs:277` `enum TraversalMode {`
- `impl` `codex-rs/core/src/config/edit.rs:282` `impl ConfigDocument {`
- `fn` `codex-rs/core/src/config/edit.rs:283` `fn new(doc: DocumentMut, profile: Option<String>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:287` `fn apply(&mut self, edit: &ConfigEdit) -> anyhow::Result<bool> {`
- `fn` `codex-rs/core/src/config/edit.rs:356` `fn write_profile_value(&mut self, segments: &[&str], value: Option<TomlItem>) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:363` `fn write_value(&mut self, scope: Scope, segments: &[&str], value: TomlItem) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:368` `fn clear(&mut self, scope: Scope, segments: &[&str]) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:373` `fn clear_owned(&mut self, segments: &[String]) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:377` `fn replace_mcp_servers(&mut self, servers: &BTreeMap<String, McpServerConfig>) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:430` `fn set_skill_config(&mut self, path: &Path, enabled: bool) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:537` `fn scoped_segments(&self, scope: Scope, segments: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/config/edit.rs:557` `fn insert(&mut self, segments: &[String], value: TomlItem) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:574` `fn remove(&mut self, segments: &[String]) -> bool {`
- `fn` `codex-rs/core/src/config/edit.rs:586` `fn descend(&mut self, segments: &[String], mode: TraversalMode) -> Option<&mut TomlTable> {`
- `fn` `codex-rs/core/src/config/edit.rs:612` `fn preserve_decor(existing: &TomlItem, replacement: &mut TomlItem) {`
- `fn` `codex-rs/core/src/config/edit.rs:644` `fn normalize_skill_config_path(path: &Path) -> String {`
- `fn` `codex-rs/core/src/config/edit.rs:652` `pub fn apply_blocking(`
- `fn` `codex-rs/core/src/config/edit.rs:706` `pub async fn apply(`
- `struct` `codex-rs/core/src/config/edit.rs:720` `pub struct ConfigEditsBuilder {`
- `impl` `codex-rs/core/src/config/edit.rs:726` `impl ConfigEditsBuilder {`
- `fn` `codex-rs/core/src/config/edit.rs:727` `pub fn new(codex_home: &Path) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:735` `pub fn with_profile(mut self, profile: Option<&str>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:740` `pub fn set_model(mut self, model: Option<&str>, effort: Option<ReasoningEffort>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:748` `pub fn set_personality(mut self, personality: Option<Personality>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:754` `pub fn set_hide_full_access_warning(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:760` `pub fn set_hide_world_writable_warning(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:766` `pub fn set_hide_rate_limit_model_nudge(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:772` `pub fn set_hide_model_migration_prompt(mut self, model: &str, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:781` `pub fn record_model_migration_seen(mut self, from: &str, to: &str) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:789` `pub fn set_windows_wsl_setup_acknowledged(mut self, acknowledged: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:795` `pub fn replace_mcp_servers(mut self, servers: &BTreeMap<String, McpServerConfig>) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:814` `pub fn set_feature_enabled(mut self, key: &str, enabled: bool) -> Self {`
- `fn` `codex-rs/core/src/config/edit.rs:831` `pub fn apply_blocking(self) -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config/edit.rs:836` `pub async fn apply(self) -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config/edit.rs:847` `use super::*;`
- `use` `codex-rs/core/src/config/edit.rs:848` `use crate::config::types::McpServerTransportConfig;`
- `use` `codex-rs/core/src/config/edit.rs:849` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/config/edit.rs:850` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config/edit.rs:852` `use std::os::unix::fs::symlink;`
- `use` `codex-rs/core/src/config/edit.rs:853` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/config/edit.rs:854` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/config/edit.rs:857` `fn blocking_set_model_top_level() {`
- `fn` `codex-rs/core/src/config/edit.rs:880` `fn builder_with_edits_applies_custom_paths() {`
- `fn` `codex-rs/core/src/config/edit.rs:898` `fn set_skill_config_writes_disabled_entry() {`
- `fn` `codex-rs/core/src/config/edit.rs:920` `fn set_skill_config_removes_entry_when_enabled() {`
- `fn` `codex-rs/core/src/config/edit.rs:946` `fn blocking_set_model_preserves_inline_table_contents() {`
- `fn` `codex-rs/core/src/config/edit.rs:994` `fn blocking_set_model_writes_through_symlink_chain() {`
- `fn` `codex-rs/core/src/config/edit.rs:1027` `fn blocking_set_model_replaces_symlink_on_cycle() {`
- `fn` `codex-rs/core/src/config/edit.rs:1058` `fn batch_write_table_upsert_preserves_inline_comments() {`
- `fn` `codex-rs/core/src/config/edit.rs:1120` `fn blocking_clear_model_removes_inline_table_entry() {`
- `fn` `codex-rs/core/src/config/edit.rs:1155` `fn blocking_set_model_scopes_to_active_profile() {`
- `fn` `codex-rs/core/src/config/edit.rs:1190` `fn blocking_set_model_with_explicit_profile() {`
- `fn` `codex-rs/core/src/config/edit.rs:1220` `fn blocking_set_hide_full_access_warning_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1254` `fn blocking_set_hide_rate_limit_model_nudge_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1282` `fn blocking_set_hide_gpt5_1_migration_prompt_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1312` `fn blocking_set_hide_gpt_5_1_codex_max_migration_prompt_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1342` `fn blocking_record_model_migration_seen_preserves_table() {`
- `fn` `codex-rs/core/src/config/edit.rs:1374` `fn blocking_replace_mcp_servers_round_trips() {`
- `fn` `codex-rs/core/src/config/edit.rs:1464` `fn blocking_replace_mcp_servers_preserves_inline_comments() {`
- `fn` `codex-rs/core/src/config/edit.rs:1511` `fn blocking_replace_mcp_servers_preserves_inline_comment_suffix() {`
- `fn` `codex-rs/core/src/config/edit.rs:1556` `fn blocking_replace_mcp_servers_preserves_inline_comment_after_removing_keys() {`
- `fn` `codex-rs/core/src/config/edit.rs:1601` `fn blocking_replace_mcp_servers_preserves_inline_comment_prefix_on_update() {`
- `fn` `codex-rs/core/src/config/edit.rs:1648` `fn blocking_clear_path_noop_when_missing() {`
- `fn` `codex-rs/core/src/config/edit.rs:1668` `fn blocking_set_path_updates_notifications() {`
- `fn` `codex-rs/core/src/config/edit.rs:1694` `async fn async_builder_set_model_persists() {`
- `fn` `codex-rs/core/src/config/edit.rs:1713` `fn blocking_builder_set_model_round_trips_back_and_forth() {`
- `fn` `codex-rs/core/src/config/edit.rs:1747` `async fn blocking_set_asynchronous_helpers_available() {`
- `fn` `codex-rs/core/src/config/edit.rs:1768` `fn replace_mcp_servers_blocking_clears_table_when_empty() {`

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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
