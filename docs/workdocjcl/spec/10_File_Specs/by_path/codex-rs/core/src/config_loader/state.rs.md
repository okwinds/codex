# `codex-rs/core/src/config_loader/state.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10378`
- sha256: `0e4cc7a66bcd80ceb5d763d9b27d0fb27a370ea3098ac790a2c4a29241734749`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/state.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct LoaderOverrides {`
- `pub struct ConfigLayerEntry {`
- `pub fn new(name: ConfigLayerSource, config: TomlValue) -> Self {`
- `pub fn new_disabled(`
- `pub fn is_disabled(&self) -> bool {`
- `pub fn metadata(&self) -> ConfigLayerMetadata {`
- `pub fn as_layer(&self) -> ConfigLayer {`
- `pub fn config_folder(&self) -> Option<AbsolutePathBuf> {`
- `pub enum ConfigLayerStackOrdering {`
- `pub struct ConfigLayerStack {`
- `pub fn new(`
- `pub fn get_user_layer(&self) -> Option<&ConfigLayerEntry> {`
- `pub fn requirements(&self) -> &ConfigRequirements {`
- `pub fn requirements_toml(&self) -> &ConfigRequirementsToml {`
- `pub fn with_user_config(&self, config_toml: &AbsolutePathBuf, user_config: TomlValue) -> Self {`
- `pub fn effective_config(&self) -> TomlValue {`
- `pub fn origins(&self) -> HashMap<String, ConfigLayerMetadata> {`
- `pub fn layers_high_to_low(&self) -> Vec<&ConfigLayerEntry> {`
- `pub fn get_layers(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/state.rs:1` `use crate::config_loader::ConfigRequirements;`
- `use` `codex-rs/core/src/config_loader/state.rs:2` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/config_loader/state.rs:4` `use super::fingerprint::record_origins;`
- `use` `codex-rs/core/src/config_loader/state.rs:5` `use super::fingerprint::version_for_toml;`
- `use` `codex-rs/core/src/config_loader/state.rs:6` `use super::merge::merge_toml_values;`
- `use` `codex-rs/core/src/config_loader/state.rs:7` `use codex_app_server_protocol::ConfigLayer;`
- `use` `codex-rs/core/src/config_loader/state.rs:8` `use codex_app_server_protocol::ConfigLayerMetadata;`
- `use` `codex-rs/core/src/config_loader/state.rs:9` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/config_loader/state.rs:10` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/state.rs:11` `use serde_json::Value as JsonValue;`
- `use` `codex-rs/core/src/config_loader/state.rs:12` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/config_loader/state.rs:13` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/config_loader/state.rs:14` `use toml::Value as TomlValue;`
- `struct` `codex-rs/core/src/config_loader/state.rs:18` `pub struct LoaderOverrides {`
- `struct` `codex-rs/core/src/config_loader/state.rs:27` `pub struct ConfigLayerEntry {`
- `impl` `codex-rs/core/src/config_loader/state.rs:34` `impl ConfigLayerEntry {`
- `fn` `codex-rs/core/src/config_loader/state.rs:35` `pub fn new(name: ConfigLayerSource, config: TomlValue) -> Self {`
- `fn` `codex-rs/core/src/config_loader/state.rs:45` `pub fn new_disabled(`
- `fn` `codex-rs/core/src/config_loader/state.rs:59` `pub fn is_disabled(&self) -> bool {`
- `fn` `codex-rs/core/src/config_loader/state.rs:63` `pub fn metadata(&self) -> ConfigLayerMetadata {`
- `fn` `codex-rs/core/src/config_loader/state.rs:70` `pub fn as_layer(&self) -> ConfigLayer {`
- `fn` `codex-rs/core/src/config_loader/state.rs:80` `pub fn config_folder(&self) -> Option<AbsolutePathBuf> {`
- `enum` `codex-rs/core/src/config_loader/state.rs:94` `pub enum ConfigLayerStackOrdering {`
- `struct` `codex-rs/core/src/config_loader/state.rs:100` `pub struct ConfigLayerStack {`
- `impl` `codex-rs/core/src/config_loader/state.rs:118` `impl ConfigLayerStack {`
- `fn` `codex-rs/core/src/config_loader/state.rs:119` `pub fn new(`
- `fn` `codex-rs/core/src/config_loader/state.rs:134` `pub fn get_user_layer(&self) -> Option<&ConfigLayerEntry> {`
- `fn` `codex-rs/core/src/config_loader/state.rs:139` `pub fn requirements(&self) -> &ConfigRequirements {`
- `fn` `codex-rs/core/src/config_loader/state.rs:143` `pub fn requirements_toml(&self) -> &ConfigRequirementsToml {`
- `fn` `codex-rs/core/src/config_loader/state.rs:151` `pub fn with_user_config(&self, config_toml: &AbsolutePathBuf, user_config: TomlValue) -> Self {`
- `fn` `codex-rs/core/src/config_loader/state.rs:194` `pub fn effective_config(&self) -> TomlValue {`
- `fn` `codex-rs/core/src/config_loader/state.rs:202` `pub fn origins(&self) -> HashMap<String, ConfigLayerMetadata> {`
- `fn` `codex-rs/core/src/config_loader/state.rs:215` `pub fn layers_high_to_low(&self) -> Vec<&ConfigLayerEntry> {`
- `fn` `codex-rs/core/src/config_loader/state.rs:221` `pub fn get_layers(`
- `fn` `codex-rs/core/src/config_loader/state.rs:240` `fn verify_layer_ordering(layers: &[ConfigLayerEntry]) -> std::io::Result<Option<usize>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config_loader::ConfigRequirements;`
- `use crate::config_loader::ConfigRequirementsToml;`
- `use super::fingerprint::record_origins;`
- `use super::fingerprint::version_for_toml;`
- `use super::merge::merge_toml_values;`
- `use codex_app_server_protocol::ConfigLayer;`
- `use codex_app_server_protocol::ConfigLayerMetadata;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use serde_json::Value as JsonValue;`
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use toml::Value as TomlValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
