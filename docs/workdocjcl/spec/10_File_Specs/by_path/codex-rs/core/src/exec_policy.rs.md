# `codex-rs/core/src/exec_policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `51475`
- sha256: `6fd0136ad1f2ef7a418918c548e76178b818288fd744e460fde799ea7cbcabe2`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/exec_policy.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum ExecPolicyError {`
- `pub enum ExecPolicyUpdateError {`
- `pub fn render_decision_for_unmatched_command(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/exec_policy.rs:1` `use std::io::ErrorKind;`
- `use` `codex-rs/core/src/exec_policy.rs:2` `use std::path::Path;`
- `use` `codex-rs/core/src/exec_policy.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/exec_policy.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/core/src/exec_policy.rs:6` `use arc_swap::ArcSwap;`
- `use` `codex-rs/core/src/exec_policy.rs:8` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/exec_policy.rs:9` `use crate::config_loader::ConfigLayerStackOrdering;`
- `use` `codex-rs/core/src/exec_policy.rs:10` `use crate::is_dangerous_command::command_might_be_dangerous;`
- `use` `codex-rs/core/src/exec_policy.rs:11` `use crate::is_safe_command::is_known_safe_command;`
- `use` `codex-rs/core/src/exec_policy.rs:12` `use codex_execpolicy::AmendError;`
- `use` `codex-rs/core/src/exec_policy.rs:13` `use codex_execpolicy::Decision;`
- `use` `codex-rs/core/src/exec_policy.rs:14` `use codex_execpolicy::Error as ExecPolicyRuleError;`
- `use` `codex-rs/core/src/exec_policy.rs:15` `use codex_execpolicy::Evaluation;`
- `use` `codex-rs/core/src/exec_policy.rs:16` `use codex_execpolicy::Policy;`
- `use` `codex-rs/core/src/exec_policy.rs:17` `use codex_execpolicy::PolicyParser;`
- `use` `codex-rs/core/src/exec_policy.rs:18` `use codex_execpolicy::RuleMatch;`
- `use` `codex-rs/core/src/exec_policy.rs:19` `use codex_execpolicy::blocking_append_allow_prefix_rule;`
- `use` `codex-rs/core/src/exec_policy.rs:20` `use codex_protocol::approvals::ExecPolicyAmendment;`
- `use` `codex-rs/core/src/exec_policy.rs:21` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/exec_policy.rs:22` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/exec_policy.rs:23` `use thiserror::Error;`
- `use` `codex-rs/core/src/exec_policy.rs:24` `use tokio::fs;`
- `use` `codex-rs/core/src/exec_policy.rs:25` `use tokio::task::spawn_blocking;`
- `use` `codex-rs/core/src/exec_policy.rs:27` `use crate::bash::parse_shell_lc_plain_commands;`
- `use` `codex-rs/core/src/exec_policy.rs:28` `use crate::features::Feature;`
- `use` `codex-rs/core/src/exec_policy.rs:29` `use crate::features::Features;`
- `use` `codex-rs/core/src/exec_policy.rs:30` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/exec_policy.rs:31` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/exec_policy.rs:32` `use shlex::try_join as shlex_try_join;`
- `const` `codex-rs/core/src/exec_policy.rs:34` `const PROMPT_CONFLICT_REASON: &str =`
- `const` `codex-rs/core/src/exec_policy.rs:36` `const RULES_DIR_NAME: &str = "rules";`
- `const` `codex-rs/core/src/exec_policy.rs:37` `const RULE_EXTENSION: &str = "rules";`
- `const` `codex-rs/core/src/exec_policy.rs:38` `const DEFAULT_POLICY_FILE: &str = "default.rules";`
- `fn` `codex-rs/core/src/exec_policy.rs:40` `fn is_policy_match(rule_match: &RuleMatch) -> bool {`
- `enum` `codex-rs/core/src/exec_policy.rs:48` `pub enum ExecPolicyError {`
- `enum` `codex-rs/core/src/exec_policy.rs:69` `pub enum ExecPolicyUpdateError {`
- `impl` `codex-rs/core/src/exec_policy.rs:99` `impl ExecPolicyManager {`
- `impl` `codex-rs/core/src/exec_policy.rs:217` `impl Default for ExecPolicyManager {`
- `fn` `codex-rs/core/src/exec_policy.rs:218` `fn default() -> Self {`
- `fn` `codex-rs/core/src/exec_policy.rs:223` `pub async fn check_execpolicy_for_warnings(`
- `fn` `codex-rs/core/src/exec_policy.rs:231` `async fn load_exec_policy_for_features_with_warning(`
- `fn` `codex-rs/core/src/exec_policy.rs:246` `pub async fn load_exec_policy(config_stack: &ConfigLayerStack) -> Result<Policy, ExecPolicyError> {`
- `fn` `codex-rs/core/src/exec_policy.rs:298` `pub fn render_decision_for_unmatched_command(`
- `fn` `codex-rs/core/src/exec_policy.rs:361` `fn default_policy_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/core/src/exec_policy.rs:375` `fn try_derive_execpolicy_amendment_for_prompt_rules(`
- `fn` `codex-rs/core/src/exec_policy.rs:399` `fn try_derive_execpolicy_amendment_for_allow_rules(`
- `fn` `codex-rs/core/src/exec_policy.rs:417` `fn derive_requested_execpolicy_amendment(`
- `fn` `codex-rs/core/src/exec_policy.rs:442` `fn derive_prompt_reason(command_args: &[String], evaluation: &Evaluation) -> Option<String> {`
- `fn` `codex-rs/core/src/exec_policy.rs:470` `fn render_shlex_command(args: &[String]) -> String {`
- `fn` `codex-rs/core/src/exec_policy.rs:477` `fn derive_forbidden_reason(command_args: &[String], evaluation: &Evaluation) -> String {`
- `fn` `codex-rs/core/src/exec_policy.rs:506` `async fn collect_policy_files(dir: impl AsRef<Path>) -> Result<Vec<PathBuf>, ExecPolicyError> {`
- `use` `codex-rs/core/src/exec_policy.rs:560` `use super::*;`
- `use` `codex-rs/core/src/exec_policy.rs:561` `use crate::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/core/src/exec_policy.rs:562` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/exec_policy.rs:563` `use crate::config_loader::ConfigRequirements;`
- `use` `codex-rs/core/src/exec_policy.rs:564` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/exec_policy.rs:565` `use crate::features::Feature;`
- `use` `codex-rs/core/src/exec_policy.rs:566` `use crate::features::Features;`
- `use` `codex-rs/core/src/exec_policy.rs:567` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/exec_policy.rs:568` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/exec_policy.rs:569` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/exec_policy.rs:570` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/exec_policy.rs:571` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/exec_policy.rs:572` `use std::fs;`
- `use` `codex-rs/core/src/exec_policy.rs:573` `use std::path::Path;`
- `use` `codex-rs/core/src/exec_policy.rs:574` `use std::sync::Arc;`
- `use` `codex-rs/core/src/exec_policy.rs:575` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/exec_policy.rs:576` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/exec_policy.rs:578` `fn config_stack_for_dot_codex_folder(dot_codex_folder: &Path) -> ConfigLayerStack {`
- `fn` `codex-rs/core/src/exec_policy.rs:594` `async fn returns_empty_policy_when_feature_disabled() {`
- `fn` `codex-rs/core/src/exec_policy.rs:620` `async fn collect_policy_files_returns_empty_when_dir_missing() {`
- `fn` `codex-rs/core/src/exec_policy.rs:632` `async fn loads_policies_from_policy_subdirectory() {`
- `fn` `codex-rs/core/src/exec_policy.rs:661` `async fn ignores_policies_outside_policy_dir() {`
- `fn` `codex-rs/core/src/exec_policy.rs:687` `async fn loads_rules_from_disabled_project_layers() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/exec_policy.rs:728` `async fn loads_policies_from_multiple_config_layers() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/exec_policy.rs:797` `async fn evaluates_bash_lc_inner_commands() {`
- `fn` `codex-rs/core/src/exec_policy.rs:834` `async fn justification_is_included_in_forbidden_exec_approval_requirement() {`
- `fn` `codex-rs/core/src/exec_policy.rs:873` `async fn exec_approval_requirement_prefers_execpolicy_match() {`
- `fn` `codex-rs/core/src/exec_policy.rs:904` `async fn exec_approval_requirement_respects_approval_policy() {`
- `fn` `codex-rs/core/src/exec_policy.rs:934` `async fn exec_approval_requirement_falls_back_to_heuristics() {`
- `fn` `codex-rs/core/src/exec_policy.rs:959` `async fn request_rule_uses_prefix_rule() {`
- `fn` `codex-rs/core/src/exec_policy.rs:993` `async fn heuristics_apply_when_other_commands_match_policy() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1027` `async fn append_execpolicy_amendment_updates_policy_and_file() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1060` `async fn append_execpolicy_amendment_rejects_empty_prefix() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1078` `async fn proposed_execpolicy_amendment_is_present_for_single_command_without_policy_match() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1103` `async fn proposed_execpolicy_amendment_is_disabled_when_execpolicy_feature_disabled() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1131` `async fn proposed_execpolicy_amendment_is_omitted_when_policy_prompts() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1162` `async fn proposed_execpolicy_amendment_is_present_for_multi_command_scripts() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1193` `async fn proposed_execpolicy_amendment_uses_first_no_match_in_multi_command_scripts() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1228` `async fn proposed_execpolicy_amendment_is_present_when_heuristics_allow() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1253` `async fn proposed_execpolicy_amendment_is_suppressed_when_policy_matches_allow() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1284` `async fn dangerous_git_push_requires_approval_in_danger_full_access() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1307` `fn vec_str(items: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/exec_policy.rs:1314` `async fn verify_approval_requirement_for_unsafe_powershell_command() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::ErrorKind;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use arc_swap::ArcSwap;`
- `use crate::config_loader::ConfigLayerStack;`
- `use crate::config_loader::ConfigLayerStackOrdering;`
- `use crate::is_dangerous_command::command_might_be_dangerous;`
- `use crate::is_safe_command::is_known_safe_command;`
- `use codex_execpolicy::AmendError;`
- `use codex_execpolicy::Decision;`
- `use codex_execpolicy::Error as ExecPolicyRuleError;`
- `use codex_execpolicy::Evaluation;`
- `use codex_execpolicy::Policy;`
- `use codex_execpolicy::PolicyParser;`
- `use codex_execpolicy::RuleMatch;`
- `use codex_execpolicy::blocking_append_allow_prefix_rule;`
- `use codex_protocol::approvals::ExecPolicyAmendment;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::SandboxPolicy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
