# `codex-rs/core/src/skills/manager.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7392`
- sha256: `0aeb7d244626392853f2a426b10cdceb82eb27549c2776d3958666f53dac48b8`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/manager.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct SkillsManager {`
- `pub fn new(codex_home: PathBuf) -> Self {`
- `pub fn skills_for_config(&self, config: &Config) -> SkillLoadOutcome {`
- `pub fn clear_cache(&self) {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/manager.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/skills/manager.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/skills/manager.rs:3` `use std::path::Path;`
- `use` `codex-rs/core/src/skills/manager.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/skills/manager.rs:5` `use std::sync::RwLock;`
- `use` `codex-rs/core/src/skills/manager.rs:7` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/skills/manager.rs:8` `use toml::Value as TomlValue;`
- `use` `codex-rs/core/src/skills/manager.rs:9` `use tracing::info;`
- `use` `codex-rs/core/src/skills/manager.rs:10` `use tracing::warn;`
- `use` `codex-rs/core/src/skills/manager.rs:12` `use crate::config::Config;`
- `use` `codex-rs/core/src/skills/manager.rs:13` `use crate::config::types::SkillsConfig;`
- `use` `codex-rs/core/src/skills/manager.rs:14` `use crate::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/core/src/skills/manager.rs:15` `use crate::config_loader::LoaderOverrides;`
- `use` `codex-rs/core/src/skills/manager.rs:16` `use crate::config_loader::load_config_layers_state;`
- `use` `codex-rs/core/src/skills/manager.rs:17` `use crate::skills::SkillLoadOutcome;`
- `use` `codex-rs/core/src/skills/manager.rs:18` `use crate::skills::loader::load_skills_from_roots;`
- `use` `codex-rs/core/src/skills/manager.rs:19` `use crate::skills::loader::skill_roots_from_layer_stack_with_agents;`
- `use` `codex-rs/core/src/skills/manager.rs:20` `use crate::skills::system::install_system_skills;`
- `struct` `codex-rs/core/src/skills/manager.rs:22` `pub struct SkillsManager {`
- `impl` `codex-rs/core/src/skills/manager.rs:27` `impl SkillsManager {`
- `fn` `codex-rs/core/src/skills/manager.rs:28` `pub fn new(codex_home: PathBuf) -> Self {`
- `fn` `codex-rs/core/src/skills/manager.rs:41` `pub fn skills_for_config(&self, config: &Config) -> SkillLoadOutcome {`
- `fn` `codex-rs/core/src/skills/manager.rs:63` `pub async fn skills_for_cwd(&self, cwd: &Path, force_reload: bool) -> SkillLoadOutcome {`
- `fn` `codex-rs/core/src/skills/manager.rs:118` `pub fn clear_cache(&self) {`
- `fn` `codex-rs/core/src/skills/manager.rs:129` `fn disabled_paths_from_stack(`
- `fn` `codex-rs/core/src/skills/manager.rs:163` `fn normalize_override_path(path: &Path) -> PathBuf {`
- `use` `codex-rs/core/src/skills/manager.rs:169` `use super::*;`
- `use` `codex-rs/core/src/skills/manager.rs:170` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/skills/manager.rs:171` `use crate::config::ConfigOverrides;`
- `use` `codex-rs/core/src/skills/manager.rs:172` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/skills/manager.rs:173` `use std::fs;`
- `use` `codex-rs/core/src/skills/manager.rs:174` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/skills/manager.rs:176` `fn write_user_skill(codex_home: &TempDir, dir: &str, name: &str, description: &str) {`
- `fn` `codex-rs/core/src/skills/manager.rs:184` `async fn skills_for_config_seeds_cache_by_cwd() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::RwLock;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use toml::Value as TomlValue;`
- `use tracing::info;`
- `use tracing::warn;`
- `use crate::config::Config;`
- `use crate::config::types::SkillsConfig;`
- `use crate::config_loader::CloudRequirementsLoader;`
- `use crate::config_loader::LoaderOverrides;`
- `use crate::config_loader::load_config_layers_state;`
- `use crate::skills::SkillLoadOutcome;`
- `use crate::skills::loader::load_skills_from_roots;`
- `use crate::skills::loader::skill_roots_from_layer_stack_with_agents;`
- `use crate::skills::system::install_system_skills;`
- `use super::*;`
- `use crate::config::ConfigBuilder;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
