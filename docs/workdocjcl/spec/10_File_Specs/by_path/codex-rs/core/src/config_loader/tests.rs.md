# `codex-rs/core/src/config_loader/tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `50481`
- sha256: `021e04e9b825bcb1f836b2cb4062970e94cbdd6725162823147b84da9841ed85`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/config_loader/tests.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/config_loader/tests.rs:1` `use super::LoaderOverrides;`
- `use` `codex-rs/core/src/config_loader/tests.rs:2` `use super::load_config_layers_state;`
- `use` `codex-rs/core/src/config_loader/tests.rs:3` `use crate::config::CONFIG_TOML_FILE;`
- `use` `codex-rs/core/src/config_loader/tests.rs:4` `use crate::config::ConfigBuilder;`
- `use` `codex-rs/core/src/config_loader/tests.rs:5` `use crate::config::ConfigOverrides;`
- `use` `codex-rs/core/src/config_loader/tests.rs:6` `use crate::config::ConfigToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:7` `use crate::config::ConstraintError;`
- `use` `codex-rs/core/src/config_loader/tests.rs:8` `use crate::config::ProjectConfig;`
- `use` `codex-rs/core/src/config_loader/tests.rs:9` `use crate::config_loader::CloudRequirementsLoader;`
- `use` `codex-rs/core/src/config_loader/tests.rs:10` `use crate::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/core/src/config_loader/tests.rs:11` `use crate::config_loader::ConfigLoadError;`
- `use` `codex-rs/core/src/config_loader/tests.rs:12` `use crate::config_loader::ConfigRequirements;`
- `use` `codex-rs/core/src/config_loader/tests.rs:13` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:14` `use crate::config_loader::config_requirements::ConfigRequirementsWithSources;`
- `use` `codex-rs/core/src/config_loader/tests.rs:15` `use crate::config_loader::config_requirements::RequirementSource;`
- `use` `codex-rs/core/src/config_loader/tests.rs:16` `use crate::config_loader::fingerprint::version_for_toml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:17` `use crate::config_loader::load_requirements_toml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:18` `use codex_protocol::config_types::TrustLevel;`
- `use` `codex-rs/core/src/config_loader/tests.rs:19` `use codex_protocol::config_types::WebSearchMode;`
- `use` `codex-rs/core/src/config_loader/tests.rs:20` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/config_loader/tests.rs:22` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/config_loader/tests.rs:23` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/tests.rs:24` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config_loader/tests.rs:25` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/config_loader/tests.rs:26` `use std::path::Path;`
- `use` `codex-rs/core/src/config_loader/tests.rs:27` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/config_loader/tests.rs:28` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:30` `fn config_error_from_io(err: &std::io::Error) -> &super::ConfigError {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:37` `async fn make_config_for_test(`
- `fn` `codex-rs/core/src/config_loader/tests.rs:61` `async fn cli_overrides_resolve_relative_paths_against_cwd() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:85` `async fn returns_config_error_for_invalid_user_config_toml() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:110` `async fn returns_config_error_for_invalid_managed_config_toml() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:140` `async fn returns_config_error_for_schema_error_in_user_config() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:162` `fn schema_error_points_to_feature_value() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:179` `async fn merges_managed_config_layer_on_top() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:236` `async fn returns_empty_when_all_layers_missing() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:308` `async fn managed_preferences_take_highest_precedence() {`
- `use` `codex-rs/core/src/config_loader/tests.rs:309` `use base64::Engine;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:369` `async fn managed_preferences_requirements_are_applied() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config_loader/tests.rs:370` `use base64::Engine;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:428` `async fn managed_preferences_requirements_take_precedence() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config_loader/tests.rs:429` `use base64::Engine;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:472` `async fn load_requirements_toml_produces_expected_constraints() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:544` `async fn cloud_requirements_take_precedence_over_mdm_requirements() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config_loader/tests.rs:545` `use base64::Engine;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:598` `async fn cloud_requirements_are_not_overwritten_by_system_requirements() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:643` `async fn load_config_layers_includes_cloud_requirements() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:691` `async fn project_layers_prefer_closest_cwd() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:748` `async fn project_paths_resolve_relative_to_dot_codex_and_override_in_order() -> std::io::Result<()>`
- `fn` `codex-rs/core/src/config_loader/tests.rs:798` `async fn cli_override_model_instructions_file_sets_base_instructions() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:834` `async fn project_layer_is_added_when_dot_codex_exists_without_config_toml() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:876` `async fn codex_home_is_not_loaded_as_project_layer_from_home_dir() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:912` `async fn codex_home_within_project_tree_is_not_double_loaded() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:973` `async fn project_layers_disabled_when_untrusted_or_unknown() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1075` `async fn invalid_project_config_ignored_when_untrusted_or_unknown() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1141` `async fn cli_overrides_with_relative_paths_do_not_break_trust_check() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1171` `async fn project_root_markers_supports_alternate_markers() -> std::io::Result<()> {`
- `use` `codex-rs/core/src/config_loader/tests.rs:1235` `use super::super::config_requirements::ConfigRequirementsWithSources;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1236` `use super::super::requirements_exec_policy::RequirementsExecPolicyDecisionToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1237` `use super::super::requirements_exec_policy::RequirementsExecPolicyParseError;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1238` `use super::super::requirements_exec_policy::RequirementsExecPolicyPatternTokenToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1239` `use super::super::requirements_exec_policy::RequirementsExecPolicyPrefixRuleToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1240` `use super::super::requirements_exec_policy::RequirementsExecPolicyToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1241` `use crate::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1242` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1243` `use crate::config_loader::ConfigRequirements;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1244` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1245` `use crate::config_loader::RequirementSource;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1246` `use crate::exec_policy::load_exec_policy;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1247` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1248` `use codex_execpolicy::Decision;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1249` `use codex_execpolicy::Evaluation;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1250` `use codex_execpolicy::RuleMatch;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1251` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1252` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1253` `use std::path::Path;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1254` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1255` `use toml::Value as TomlValue;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1256` `use toml::from_str;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1258` `fn tokens(cmd: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1262` `fn panic_if_called(_: &[String]) -> Decision {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1266` `fn config_stack_for_dot_codex_folder_with_requirements(`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1280` `fn requirements_from_toml(toml_str: &str) -> ConfigRequirements {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1288` `fn parses_single_prefix_rule_from_raw_toml() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1315` `fn parses_multiple_prefix_rules_from_raw_toml() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1359` `fn converts_rules_toml_into_internal_policy_representation() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1385` `fn head_any_of_expands_into_multiple_program_rules() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1421` `fn missing_decision_is_rejected() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1439` `fn allow_decision_is_rejected() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1457` `fn empty_prefix_rules_is_rejected() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1473` `async fn loads_requirements_exec_policy_without_rules_files() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1504` `async fn merges_requirements_exec_policy_with_file_rules() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::LoaderOverrides;`
- `use super::load_config_layers_state;`
- `use crate::config::CONFIG_TOML_FILE;`
- `use crate::config::ConfigBuilder;`
- `use crate::config::ConfigOverrides;`
- `use crate::config::ConfigToml;`
- `use crate::config::ConstraintError;`
- `use crate::config::ProjectConfig;`
- `use crate::config_loader::CloudRequirementsLoader;`
- `use crate::config_loader::ConfigLayerEntry;`
- `use crate::config_loader::ConfigLoadError;`
- `use crate::config_loader::ConfigRequirements;`
- `use crate::config_loader::ConfigRequirementsToml;`
- `use crate::config_loader::config_requirements::ConfigRequirementsWithSources;`
- `use crate::config_loader::config_requirements::RequirementSource;`
- `use crate::config_loader::fingerprint::version_for_toml;`
- `use crate::config_loader::load_requirements_toml;`
- `use codex_protocol::config_types::TrustLevel;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use codex_protocol::protocol::AskForApproval;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
