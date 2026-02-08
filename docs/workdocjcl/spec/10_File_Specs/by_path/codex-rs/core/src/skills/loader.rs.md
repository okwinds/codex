# `codex-rs/core/src/skills/loader.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `72888`
- sha256: `81b29034491483adc8e801aae967f2e468bcda0cc590d1053295925b4fa2f08a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/skills/loader.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn load_skills(config: &Config) -> SkillLoadOutcome {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/skills/loader.rs:1` `use crate::config::Config;`
- `use` `codex-rs/core/src/skills/loader.rs:2` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/skills/loader.rs:3` `use crate::config_loader::ConfigLayerStackOrdering;`
- `use` `codex-rs/core/src/skills/loader.rs:4` `use crate::config_loader::default_project_root_markers;`
- `use` `codex-rs/core/src/skills/loader.rs:5` `use crate::config_loader::merge_toml_values;`
- `use` `codex-rs/core/src/skills/loader.rs:6` `use crate::config_loader::project_root_markers_from_config;`
- `use` `codex-rs/core/src/skills/loader.rs:7` `use crate::skills::model::SkillDependencies;`
- `use` `codex-rs/core/src/skills/loader.rs:8` `use crate::skills::model::SkillError;`
- `use` `codex-rs/core/src/skills/loader.rs:9` `use crate::skills::model::SkillInterface;`
- `use` `codex-rs/core/src/skills/loader.rs:10` `use crate::skills::model::SkillLoadOutcome;`
- `use` `codex-rs/core/src/skills/loader.rs:11` `use crate::skills::model::SkillMetadata;`
- `use` `codex-rs/core/src/skills/loader.rs:12` `use crate::skills::model::SkillToolDependency;`
- `use` `codex-rs/core/src/skills/loader.rs:13` `use crate::skills::system::system_cache_root_dir;`
- `use` `codex-rs/core/src/skills/loader.rs:14` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/skills/loader.rs:15` `use codex_protocol::protocol::SkillScope;`
- `use` `codex-rs/core/src/skills/loader.rs:16` `use dirs::home_dir;`
- `use` `codex-rs/core/src/skills/loader.rs:17` `use dunce::canonicalize as canonicalize_path;`
- `use` `codex-rs/core/src/skills/loader.rs:18` `use serde::Deserialize;`
- `use` `codex-rs/core/src/skills/loader.rs:19` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/skills/loader.rs:20` `use std::collections::VecDeque;`
- `use` `codex-rs/core/src/skills/loader.rs:21` `use std::error::Error;`
- `use` `codex-rs/core/src/skills/loader.rs:22` `use std::fmt;`
- `use` `codex-rs/core/src/skills/loader.rs:23` `use std::fs;`
- `use` `codex-rs/core/src/skills/loader.rs:24` `use std::path::Component;`
- `use` `codex-rs/core/src/skills/loader.rs:25` `use std::path::Path;`
- `use` `codex-rs/core/src/skills/loader.rs:26` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/skills/loader.rs:27` `use toml::Value as TomlValue;`
- `use` `codex-rs/core/src/skills/loader.rs:28` `use tracing::error;`
- `struct` `codex-rs/core/src/skills/loader.rs:31` `struct SkillFrontmatter {`
- `struct` `codex-rs/core/src/skills/loader.rs:39` `struct SkillFrontmatterMetadata {`
- `struct` `codex-rs/core/src/skills/loader.rs:45` `struct SkillMetadataFile {`
- `struct` `codex-rs/core/src/skills/loader.rs:53` `struct Interface {`
- `struct` `codex-rs/core/src/skills/loader.rs:63` `struct Dependencies {`
- `struct` `codex-rs/core/src/skills/loader.rs:69` `struct DependencyTool {`
- `const` `codex-rs/core/src/skills/loader.rs:79` `const SKILLS_FILENAME: &str = "SKILL.md";`
- `const` `codex-rs/core/src/skills/loader.rs:80` `const AGENTS_DIR_NAME: &str = ".agents";`
- `const` `codex-rs/core/src/skills/loader.rs:81` `const SKILLS_METADATA_DIR: &str = "agents";`
- `const` `codex-rs/core/src/skills/loader.rs:82` `const SKILLS_METADATA_FILENAME: &str = "openai.yaml";`
- `const` `codex-rs/core/src/skills/loader.rs:83` `const SKILLS_DIR_NAME: &str = "skills";`
- `const` `codex-rs/core/src/skills/loader.rs:84` `const MAX_NAME_LEN: usize = 64;`
- `const` `codex-rs/core/src/skills/loader.rs:85` `const MAX_DESCRIPTION_LEN: usize = 1024;`
- `const` `codex-rs/core/src/skills/loader.rs:86` `const MAX_SHORT_DESCRIPTION_LEN: usize = MAX_DESCRIPTION_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:87` `const MAX_DEFAULT_PROMPT_LEN: usize = MAX_DESCRIPTION_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:88` `const MAX_DEPENDENCY_TYPE_LEN: usize = MAX_NAME_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:89` `const MAX_DEPENDENCY_TRANSPORT_LEN: usize = MAX_NAME_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:90` `const MAX_DEPENDENCY_VALUE_LEN: usize = MAX_DESCRIPTION_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:91` `const MAX_DEPENDENCY_DESCRIPTION_LEN: usize = MAX_DESCRIPTION_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:92` `const MAX_DEPENDENCY_COMMAND_LEN: usize = MAX_DESCRIPTION_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:93` `const MAX_DEPENDENCY_URL_LEN: usize = MAX_DESCRIPTION_LEN;`
- `const` `codex-rs/core/src/skills/loader.rs:95` `const MAX_SCAN_DEPTH: usize = 6;`
- `const` `codex-rs/core/src/skills/loader.rs:96` `const MAX_SKILLS_DIRS_PER_ROOT: usize = 2000;`
- `enum` `codex-rs/core/src/skills/loader.rs:99` `enum SkillParseError {`
- `impl` `codex-rs/core/src/skills/loader.rs:107` `impl fmt::Display for SkillParseError {`
- `fn` `codex-rs/core/src/skills/loader.rs:108` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `fn` `codex-rs/core/src/skills/loader.rs:125` `pub fn load_skills(config: &Config) -> SkillLoadOutcome {`
- `fn` `codex-rs/core/src/skills/loader.rs:148` `fn scope_rank(scope: SkillScope) -> u8 {`
- `fn` `codex-rs/core/src/skills/loader.rs:168` `fn skill_roots_from_layer_stack_inner(`
- `fn` `codex-rs/core/src/skills/loader.rs:229` `fn skill_roots(config: &Config) -> Vec<SkillRoot> {`
- `fn` `codex-rs/core/src/skills/loader.rs:251` `fn dedupe_skill_roots_by_path(roots: &mut Vec<SkillRoot>) {`
- `fn` `codex-rs/core/src/skills/loader.rs:256` `fn repo_agents_skill_roots(config_layer_stack: &ConfigLayerStack, cwd: &Path) -> Vec<SkillRoot> {`
- `fn` `codex-rs/core/src/skills/loader.rs:273` `fn project_root_markers_from_stack(config_layer_stack: &ConfigLayerStack) -> Vec<String> {`
- `fn` `codex-rs/core/src/skills/loader.rs:294` `fn find_project_root(cwd: &Path, project_root_markers: &[String]) -> PathBuf {`
- `fn` `codex-rs/core/src/skills/loader.rs:311` `fn dirs_between_project_root_and_cwd(cwd: &Path, project_root: &Path) -> Vec<PathBuf> {`
- `fn` `codex-rs/core/src/skills/loader.rs:329` `fn discover_skills_under_root(root: &Path, scope: SkillScope, outcome: &mut SkillLoadOutcome) {`
- `fn` `codex-rs/core/src/skills/loader.rs:338` `fn enqueue_dir(`
- `fn` `codex-rs/core/src/skills/loader.rs:468` `fn parse_skill_file(path: &Path, scope: SkillScope) -> Result<SkillMetadata, SkillParseError> {`
- `fn` `codex-rs/core/src/skills/loader.rs:509` `fn load_skill_metadata(skill_path: &Path) -> (Option<SkillInterface>, Option<SkillDependencies>) {`
- `fn` `codex-rs/core/src/skills/loader.rs:551` `fn resolve_interface(interface: Option<Interface>, skill_dir: &Path) -> Option<SkillInterface> {`
- `fn` `codex-rs/core/src/skills/loader.rs:582` `fn resolve_dependencies(dependencies: Option<Dependencies>) -> Option<SkillDependencies> {`
- `fn` `codex-rs/core/src/skills/loader.rs:596` `fn resolve_dependency_tool(tool: DependencyTool) -> Option<SkillToolDependency> {`
- `fn` `codex-rs/core/src/skills/loader.rs:634` `fn resolve_asset_path(`
- `fn` `codex-rs/core/src/skills/loader.rs:682` `fn sanitize_single_line(raw: &str) -> String {`
- `fn` `codex-rs/core/src/skills/loader.rs:686` `fn validate_len(`
- `fn` `codex-rs/core/src/skills/loader.rs:703` `fn resolve_str(value: Option<String>, max_len: usize, field: &'static str) -> Option<String> {`
- `fn` `codex-rs/core/src/skills/loader.rs:717` `fn resolve_required_str(`
- `fn` `codex-rs/core/src/skills/loader.rs:729` `fn resolve_color_str(value: Option<String>, field: &'static str) -> Option<String> {`
- `fn` `codex-rs/core/src/skills/loader.rs:745` `fn extract_frontmatter(contents: &str) -> Option<String> {`
- `use` `codex-rs/core/src/skills/loader.rs:770` `use super::*;`
- `use` `codex-rs/core/src/skills/loader.rs:771` `use crate::config::CONFIG_TOML_FILE;`
- `use` `codex-rs/core/src/skills/loader.rs:772` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/skills/loader.rs:773` `use crate::config::ConfigOverrides;`
- `use` `codex-rs/core/src/skills/loader.rs:774` `use crate::config::ConfigToml;`
- `use` `codex-rs/core/src/skills/loader.rs:775` `use crate::config::ProjectConfig;`
- `use` `codex-rs/core/src/skills/loader.rs:776` `use crate::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/core/src/skills/loader.rs:777` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/skills/loader.rs:778` `use crate::config_loader::ConfigRequirements;`
- `use` `codex-rs/core/src/skills/loader.rs:779` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/skills/loader.rs:780` `use codex_protocol::config_types::TrustLevel;`
- `use` `codex-rs/core/src/skills/loader.rs:781` `use codex_protocol::protocol::SkillScope;`
- `use` `codex-rs/core/src/skills/loader.rs:782` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/skills/loader.rs:783` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/skills/loader.rs:784` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/skills/loader.rs:785` `use std::path::Path;`
- `use` `codex-rs/core/src/skills/loader.rs:786` `use tempfile::TempDir;`
- `use` `codex-rs/core/src/skills/loader.rs:787` `use toml::Value as TomlValue;`
- `const` `codex-rs/core/src/skills/loader.rs:789` `const REPO_ROOT_CONFIG_DIR_NAME: &str = ".codex";`
- `fn` `codex-rs/core/src/skills/loader.rs:791` `async fn make_config(codex_home: &TempDir) -> Config {`
- `fn` `codex-rs/core/src/skills/loader.rs:795` `async fn make_config_for_cwd(codex_home: &TempDir, cwd: PathBuf) -> Config {`
- `fn` `codex-rs/core/src/skills/loader.rs:830` `fn mark_as_git_repo(dir: &Path) {`
- `fn` `codex-rs/core/src/skills/loader.rs:836` `fn normalized(path: &Path) -> PathBuf {`
- `fn` `codex-rs/core/src/skills/loader.rs:841` `fn skill_roots_from_layer_stack_maps_user_to_user_and_system_cache_and_system_to_admin()`
- `fn` `codex-rs/core/src/skills/loader.rs:896` `fn skill_roots_from_layer_stack_includes_disabled_project_layers() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/skills/loader.rs:954` `fn loads_skills_from_home_agents_dir_for_user_scope() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/skills/loader.rs:1002` `fn write_skill(codex_home: &TempDir, dir: &str, name: &str, description: &str) -> PathBuf {`
- `fn` `codex-rs/core/src/skills/loader.rs:1006` `fn write_system_skill(`
- `fn` `codex-rs/core/src/skills/loader.rs:1020` `fn write_skill_at(root: &Path, dir: &str, name: &str, description: &str) -> PathBuf {`
- `fn` `codex-rs/core/src/skills/loader.rs:1032` `fn write_skill_metadata_at(skill_dir: &Path, contents: &str) -> PathBuf {`
- `fn` `codex-rs/core/src/skills/loader.rs:1043` `fn write_skill_interface_at(skill_dir: &Path, contents: &str) -> PathBuf {`
- `fn` `codex-rs/core/src/skills/loader.rs:1048` `async fn loads_skill_dependencies_metadata_from_yaml() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1147` `async fn loads_skill_interface_metadata_from_yaml() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1201` `async fn accepts_icon_paths_under_assets_dir() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1250` `async fn ignores_invalid_brand_color() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1289` `async fn ignores_default_prompt_over_max_length() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1341` `async fn drops_interface_when_icons_are_invalid() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1381` `fn symlink_dir(target: &Path, link: &Path) {`
- `fn` `codex-rs/core/src/skills/loader.rs:1386` `fn symlink_file(target: &Path, link: &Path) {`
- `fn` `codex-rs/core/src/skills/loader.rs:1392` `async fn loads_skills_via_symlinked_subdir_for_user_scope() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1425` `async fn ignores_symlinked_skill_file_for_user_scope() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1449` `async fn does_not_loop_on_symlink_cycle_for_user_scope() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1484` `fn loads_skills_via_symlinked_subdir_for_admin_scope() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1519` `async fn loads_skills_via_symlinked_subdir_for_repo_scope() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1558` `async fn system_scope_ignores_symlinked_subdir() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1580` `async fn respects_max_scan_depth_for_user_scope() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1619` `async fn loads_valid_skill() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1645` `async fn loads_short_description_from_metadata() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1675` `async fn enforces_short_description_length_limits() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1699` `async fn skips_hidden_and_invalid() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1727` `async fn enforces_length_limits() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1753` `async fn loads_skills_from_repo_root() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1786` `async fn loads_skills_from_agents_dir_without_codex_dir() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1820` `async fn loads_skills_from_all_codex_dirs_under_project_root() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1882` `async fn loads_skills_from_codex_dir_when_not_git_repo() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1919` `async fn deduplicates_by_path_preferring_first_root() {`
- `fn` `codex-rs/core/src/skills/loader.rs:1955` `async fn keeps_duplicate_names_from_repo_and_user() {`
- `fn` `codex-rs/core/src/skills/loader.rs:2005` `async fn keeps_duplicate_names_from_nested_codex_dirs() {`
- `fn` `codex-rs/core/src/skills/loader.rs:2077` `async fn repo_skills_search_does_not_escape_repo_root() {`
- `fn` `codex-rs/core/src/skills/loader.rs:2106` `async fn loads_skills_when_cwd_is_file_in_repo() {`
- `fn` `codex-rs/core/src/skills/loader.rs:2146` `async fn non_git_repo_skills_search_does_not_walk_parents() {`
- `fn` `codex-rs/core/src/skills/loader.rs:2174` `async fn loads_skills_from_system_cache_when_present() {`
- `fn` `codex-rs/core/src/skills/loader.rs:2203` `async fn skill_roots_include_admin_with_lowest_priority_on_unix() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::Config;`
- `use crate::config_loader::ConfigLayerStack;`
- `use crate::config_loader::ConfigLayerStackOrdering;`
- `use crate::config_loader::default_project_root_markers;`
- `use crate::config_loader::merge_toml_values;`
- `use crate::config_loader::project_root_markers_from_config;`
- `use crate::skills::model::SkillDependencies;`
- `use crate::skills::model::SkillError;`
- `use crate::skills::model::SkillInterface;`
- `use crate::skills::model::SkillLoadOutcome;`
- `use crate::skills::model::SkillMetadata;`
- `use crate::skills::model::SkillToolDependency;`
- `use crate::skills::system::system_cache_root_dir;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_protocol::protocol::SkillScope;`
- `use dirs::home_dir;`
- `use dunce::canonicalize as canonicalize_path;`
- `use serde::Deserialize;`
- `use std::collections::HashSet;`
- `use std::collections::VecDeque;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
