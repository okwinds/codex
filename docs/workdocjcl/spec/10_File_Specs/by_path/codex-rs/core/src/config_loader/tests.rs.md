# `codex-rs/core/src/config_loader/tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `47093`
- sha256: `322805839f679d3889ee60ed6952c404982bf98439d831f6de631304a481d630`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/config_loader/tests.rs:19` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/config_loader/tests.rs:21` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/config_loader/tests.rs:22` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/tests.rs:23` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config_loader/tests.rs:24` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/config_loader/tests.rs:25` `use std::path::Path;`
- `use` `codex-rs/core/src/config_loader/tests.rs:26` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/config_loader/tests.rs:27` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:29` `fn config_error_from_io(err: &std::io::Error) -> &super::ConfigError {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:36` `async fn make_config_for_test(`
- `fn` `codex-rs/core/src/config_loader/tests.rs:60` `async fn returns_config_error_for_invalid_user_config_toml() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:85` `async fn returns_config_error_for_invalid_managed_config_toml() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:115` `async fn returns_config_error_for_schema_error_in_user_config() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:137` `fn schema_error_points_to_feature_value() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:154` `async fn merges_managed_config_layer_on_top() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:211` `async fn returns_empty_when_all_layers_missing() {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:283` `async fn managed_preferences_take_highest_precedence() {`
- `use` `codex-rs/core/src/config_loader/tests.rs:284` `use base64::Engine;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:344` `async fn managed_preferences_requirements_are_applied() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config_loader/tests.rs:345` `use base64::Engine;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:403` `async fn managed_preferences_requirements_take_precedence() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/config_loader/tests.rs:404` `use base64::Engine;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:447` `async fn load_requirements_toml_produces_expected_constraints() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:491` `async fn cloud_requirements_are_not_overwritten_by_system_requirements() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:534` `async fn load_config_layers_includes_cloud_requirements() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:580` `async fn project_layers_prefer_closest_cwd() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:637` `async fn project_paths_resolve_relative_to_dot_codex_and_override_in_order() -> std::io::Result<()>`
- `fn` `codex-rs/core/src/config_loader/tests.rs:687` `async fn cli_override_model_instructions_file_sets_base_instructions() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:723` `async fn project_layer_is_added_when_dot_codex_exists_without_config_toml() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:765` `async fn codex_home_is_not_loaded_as_project_layer_from_home_dir() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:801` `async fn codex_home_within_project_tree_is_not_double_loaded() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:862` `async fn project_layers_disabled_when_untrusted_or_unknown() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:964` `async fn invalid_project_config_ignored_when_untrusted_or_unknown() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1030` `async fn cli_overrides_with_relative_paths_do_not_break_trust_check() -> std::io::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1060` `async fn project_root_markers_supports_alternate_markers() -> std::io::Result<()> {`
- `use` `codex-rs/core/src/config_loader/tests.rs:1124` `use super::super::config_requirements::ConfigRequirementsWithSources;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1125` `use super::super::requirements_exec_policy::RequirementsExecPolicyDecisionToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1126` `use super::super::requirements_exec_policy::RequirementsExecPolicyParseError;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1127` `use super::super::requirements_exec_policy::RequirementsExecPolicyPatternTokenToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1128` `use super::super::requirements_exec_policy::RequirementsExecPolicyPrefixRuleToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1129` `use super::super::requirements_exec_policy::RequirementsExecPolicyToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1130` `use crate::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1131` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1132` `use crate::config_loader::ConfigRequirements;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1133` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1134` `use crate::config_loader::RequirementSource;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1135` `use crate::exec_policy::load_exec_policy;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1136` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1137` `use codex_execpolicy::Decision;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1138` `use codex_execpolicy::Evaluation;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1139` `use codex_execpolicy::RuleMatch;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1140` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1141` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1142` `use std::path::Path;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1143` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1144` `use toml::Value as TomlValue;`
- `use` `codex-rs/core/src/config_loader/tests.rs:1145` `use toml::from_str;`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1147` `fn tokens(cmd: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1151` `fn panic_if_called(_: &[String]) -> Decision {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1155` `fn config_stack_for_dot_codex_folder_with_requirements(`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1169` `fn requirements_from_toml(toml_str: &str) -> ConfigRequirements {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1177` `fn parses_single_prefix_rule_from_raw_toml() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1204` `fn parses_multiple_prefix_rules_from_raw_toml() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1248` `fn converts_rules_toml_into_internal_policy_representation() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1274` `fn head_any_of_expands_into_multiple_program_rules() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1310` `fn missing_decision_is_rejected() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1328` `fn allow_decision_is_rejected() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1346` `fn empty_prefix_rules_is_rejected() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1362` `async fn loads_requirements_exec_policy_without_rules_files() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/config_loader/tests.rs:1393` `async fn merges_requirements_exec_policy_with_file_rules() -> anyhow::Result<()> {`

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
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
