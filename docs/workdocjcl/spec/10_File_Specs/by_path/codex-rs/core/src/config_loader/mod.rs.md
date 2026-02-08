# `codex-rs/core/src/config_loader/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `32571`
- sha256: `9016b84cf08b329e0d450aa4210a76f715948fde388806c64e5c88d31a45d897`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `mod` `codex-rs/core/src/config_loader/mod.rs:1` `mod cloud_requirements;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:2` `mod config_requirements;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:3` `mod diagnostics;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:4` `mod fingerprint;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:5` `mod layer_io;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:7` `mod macos;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:8` `mod merge;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:9` `mod overrides;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:10` `mod requirements_exec_policy;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:11` `mod state;`
- `mod` `codex-rs/core/src/config_loader/mod.rs:14` `mod tests;`
- `use` `codex-rs/core/src/config_loader/mod.rs:16` `use crate::config::CONFIG_TOML_FILE;`
- `use` `codex-rs/core/src/config_loader/mod.rs:17` `use crate::config::ConfigToml;`
- `use` `codex-rs/core/src/config_loader/mod.rs:18` `use crate::config::deserialize_config_toml_with_base;`
- `use` `codex-rs/core/src/config_loader/mod.rs:19` `use crate::config_loader::config_requirements::ConfigRequirementsWithSources;`
- `use` `codex-rs/core/src/config_loader/mod.rs:20` `use crate::config_loader::layer_io::LoadedConfigLayers;`
- `use` `codex-rs/core/src/config_loader/mod.rs:21` `use crate::git_info::resolve_root_git_project_for_trust;`
- `use` `codex-rs/core/src/config_loader/mod.rs:22` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/config_loader/mod.rs:23` `use codex_protocol::config_types::SandboxMode;`
- `use` `codex-rs/core/src/config_loader/mod.rs:24` `use codex_protocol::config_types::TrustLevel;`
- `use` `codex-rs/core/src/config_loader/mod.rs:25` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/config_loader/mod.rs:26` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/mod.rs:27` `use codex_utils_absolute_path::AbsolutePathBufGuard;`
- `use` `codex-rs/core/src/config_loader/mod.rs:28` `use dunce::canonicalize as normalize_path;`
- `use` `codex-rs/core/src/config_loader/mod.rs:29` `use serde::Deserialize;`
- `use` `codex-rs/core/src/config_loader/mod.rs:30` `use std::io;`
- `use` `codex-rs/core/src/config_loader/mod.rs:31` `use std::path::Path;`
- `use` `codex-rs/core/src/config_loader/mod.rs:32` `use toml::Value as TomlValue;`
- `const` `codex-rs/core/src/config_loader/mod.rs:61` `const DEFAULT_REQUIREMENTS_TOML_FILE_UNIX: &str = "/etc/codex/requirements.toml";`
- `const` `codex-rs/core/src/config_loader/mod.rs:66` `pub const SYSTEM_CONFIG_TOML_FILE_UNIX: &str = "/etc/codex/config.toml";`
- `const` `codex-rs/core/src/config_loader/mod.rs:68` `const DEFAULT_PROJECT_ROOT_MARKERS: &[&str] = &[".git"];`
- `fn` `codex-rs/core/src/config_loader/mod.rs:100` `pub async fn load_config_layers_state(`
- `fn` `codex-rs/core/src/config_loader/mod.rs:300` `async fn load_config_toml_for_required_layer(`
- `fn` `codex-rs/core/src/config_loader/mod.rs:339` `async fn load_requirements_toml(`
- `fn` `codex-rs/core/src/config_loader/mod.rs:380` `async fn load_requirements_from_legacy_scheme(`
- `struct` `codex-rs/core/src/config_loader/mod.rs:466` `struct ProjectTrustContext {`
- `struct` `codex-rs/core/src/config_loader/mod.rs:474` `struct ProjectTrustDecision {`
- `impl` `codex-rs/core/src/config_loader/mod.rs:479` `impl ProjectTrustDecision {`
- `fn` `codex-rs/core/src/config_loader/mod.rs:480` `fn is_trusted(&self) -> bool {`
- `impl` `codex-rs/core/src/config_loader/mod.rs:485` `impl ProjectTrustContext {`
- `fn` `codex-rs/core/src/config_loader/mod.rs:486` `fn decision_for_dir(&self, dir: &AbsolutePathBuf) -> ProjectTrustDecision {`
- `fn` `codex-rs/core/src/config_loader/mod.rs:520` `fn disabled_reason_for_dir(&self, dir: &AbsolutePathBuf) -> Option<String> {`
- `fn` `codex-rs/core/src/config_loader/mod.rs:539` `fn project_layer_entry(`
- `fn` `codex-rs/core/src/config_loader/mod.rs:557` `async fn project_trust_context(`
- `fn` `codex-rs/core/src/config_loader/mod.rs:595` `fn resolve_relative_paths_in_config_toml(`
- `fn` `codex-rs/core/src/config_loader/mod.rs:624` `fn copy_shape_from_original(original: &TomlValue, resolved: &TomlValue) -> TomlValue {`
- `fn` `codex-rs/core/src/config_loader/mod.rs:649` `async fn find_project_root(`
- `fn` `codex-rs/core/src/config_loader/mod.rs:673` `async fn load_project_layers(`
- `struct` `codex-rs/core/src/config_loader/mod.rs:783` `struct LegacyManagedConfigToml {`
- `impl` `codex-rs/core/src/config_loader/mod.rs:788` `impl From<LegacyManagedConfigToml> for ConfigRequirementsToml {`
- `fn` `codex-rs/core/src/config_loader/mod.rs:789` `fn from(legacy: LegacyManagedConfigToml) -> Self {`
- `use` `codex-rs/core/src/config_loader/mod.rs:816` `use super::*;`
- `use` `codex-rs/core/src/config_loader/mod.rs:817` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/config_loader/mod.rs:820` `fn ensure_resolve_relative_paths_in_config_toml_preserves_all_fields() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/mod.rs:857` `fn legacy_managed_config_backfill_includes_read_only_sandbox_mode() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::CONFIG_TOML_FILE;`
- `use crate::config::ConfigToml;`
- `use crate::config::deserialize_config_toml_with_base;`
- `use crate::config_loader::config_requirements::ConfigRequirementsWithSources;`
- `use crate::config_loader::layer_io::LoadedConfigLayers;`
- `use crate::git_info::resolve_root_git_project_for_trust;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_protocol::config_types::SandboxMode;`
- `use codex_protocol::config_types::TrustLevel;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use codex_utils_absolute_path::AbsolutePathBufGuard;`
- `use dunce::canonicalize as normalize_path;`
- `use serde::Deserialize;`
- `use std::io;`
- `use std::path::Path;`
- `use toml::Value as TomlValue;`
- `use super::*;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
