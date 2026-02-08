# `codex-rs/core/src/exec_policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `48391`
- sha256: `0aa22da87b77e13b2ab0788ee314be575c60b3c3954897cb78bb0d07ffd249d9`
- generated_utc: `2026-02-08T10:45:32Z`

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
- `use` `codex-rs/core/src/exec_policy.rs:28` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/exec_policy.rs:29` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/exec_policy.rs:30` `use shlex::try_join as shlex_try_join;`
- `const` `codex-rs/core/src/exec_policy.rs:32` `const PROMPT_CONFLICT_REASON: &str =`
- `const` `codex-rs/core/src/exec_policy.rs:34` `const RULES_DIR_NAME: &str = "rules";`
- `const` `codex-rs/core/src/exec_policy.rs:35` `const RULE_EXTENSION: &str = "rules";`
- `const` `codex-rs/core/src/exec_policy.rs:36` `const DEFAULT_POLICY_FILE: &str = "default.rules";`
- `fn` `codex-rs/core/src/exec_policy.rs:38` `fn is_policy_match(rule_match: &RuleMatch) -> bool {`
- `enum` `codex-rs/core/src/exec_policy.rs:46` `pub enum ExecPolicyError {`
- `enum` `codex-rs/core/src/exec_policy.rs:67` `pub enum ExecPolicyUpdateError {`
- `impl` `codex-rs/core/src/exec_policy.rs:93` `impl ExecPolicyManager {`
- `impl` `codex-rs/core/src/exec_policy.rs:197` `impl Default for ExecPolicyManager {`
- `fn` `codex-rs/core/src/exec_policy.rs:198` `fn default() -> Self {`
- `fn` `codex-rs/core/src/exec_policy.rs:203` `pub async fn check_execpolicy_for_warnings(`
- `fn` `codex-rs/core/src/exec_policy.rs:210` `async fn load_exec_policy_with_warning(`
- `fn` `codex-rs/core/src/exec_policy.rs:220` `pub async fn load_exec_policy(config_stack: &ConfigLayerStack) -> Result<Policy, ExecPolicyError> {`
- `fn` `codex-rs/core/src/exec_policy.rs:270` `pub fn render_decision_for_unmatched_command(`
- `fn` `codex-rs/core/src/exec_policy.rs:333` `fn default_policy_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/core/src/exec_policy.rs:347` `fn try_derive_execpolicy_amendment_for_prompt_rules(`
- `fn` `codex-rs/core/src/exec_policy.rs:371` `fn try_derive_execpolicy_amendment_for_allow_rules(`
- `fn` `codex-rs/core/src/exec_policy.rs:389` `fn derive_requested_execpolicy_amendment(`
- `fn` `codex-rs/core/src/exec_policy.rs:409` `fn derive_prompt_reason(command_args: &[String], evaluation: &Evaluation) -> Option<String> {`
- `fn` `codex-rs/core/src/exec_policy.rs:437` `fn render_shlex_command(args: &[String]) -> String {`
- `fn` `codex-rs/core/src/exec_policy.rs:444` `fn derive_forbidden_reason(command_args: &[String], evaluation: &Evaluation) -> String {`
- `fn` `codex-rs/core/src/exec_policy.rs:473` `async fn collect_policy_files(dir: impl AsRef<Path>) -> Result<Vec<PathBuf>, ExecPolicyError> {`
- `use` `codex-rs/core/src/exec_policy.rs:527` `use super::*;`
- `use` `codex-rs/core/src/exec_policy.rs:528` `use crate::config_loader::ConfigLayerEntry;`
- `use` `codex-rs/core/src/exec_policy.rs:529` `use crate::config_loader::ConfigLayerStack;`
- `use` `codex-rs/core/src/exec_policy.rs:530` `use crate::config_loader::ConfigRequirements;`
- `use` `codex-rs/core/src/exec_policy.rs:531` `use crate::config_loader::ConfigRequirementsToml;`
- `use` `codex-rs/core/src/exec_policy.rs:532` `use crate::features::Feature;`
- `use` `codex-rs/core/src/exec_policy.rs:533` `use crate::features::Features;`
- `use` `codex-rs/core/src/exec_policy.rs:534` `use codex_app_server_protocol::ConfigLayerSource;`
- `use` `codex-rs/core/src/exec_policy.rs:535` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/exec_policy.rs:536` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/exec_policy.rs:537` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/exec_policy.rs:538` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/exec_policy.rs:539` `use std::fs;`
- `use` `codex-rs/core/src/exec_policy.rs:540` `use std::path::Path;`
- `use` `codex-rs/core/src/exec_policy.rs:541` `use std::sync::Arc;`
- `use` `codex-rs/core/src/exec_policy.rs:542` `use tempfile::tempdir;`
- `use` `codex-rs/core/src/exec_policy.rs:543` `use toml::Value as TomlValue;`
- `fn` `codex-rs/core/src/exec_policy.rs:545` `fn config_stack_for_dot_codex_folder(dot_codex_folder: &Path) -> ConfigLayerStack {`
- `fn` `codex-rs/core/src/exec_policy.rs:561` `async fn returns_empty_policy_when_no_policy_files_exist() {`
- `fn` `codex-rs/core/src/exec_policy.rs:585` `async fn collect_policy_files_returns_empty_when_dir_missing() {`
- `fn` `codex-rs/core/src/exec_policy.rs:597` `async fn loads_policies_from_policy_subdirectory() {`
- `fn` `codex-rs/core/src/exec_policy.rs:626` `async fn ignores_policies_outside_policy_dir() {`
- `fn` `codex-rs/core/src/exec_policy.rs:652` `async fn ignores_rules_from_untrusted_project_layers() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/exec_policy.rs:691` `async fn loads_policies_from_multiple_config_layers() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/exec_policy.rs:760` `async fn evaluates_bash_lc_inner_commands() {`
- `fn` `codex-rs/core/src/exec_policy.rs:796` `async fn justification_is_included_in_forbidden_exec_approval_requirement() {`
- `fn` `codex-rs/core/src/exec_policy.rs:834` `async fn exec_approval_requirement_prefers_execpolicy_match() {`
- `fn` `codex-rs/core/src/exec_policy.rs:864` `async fn exec_approval_requirement_respects_approval_policy() {`
- `fn` `codex-rs/core/src/exec_policy.rs:893` `async fn exec_approval_requirement_falls_back_to_heuristics() {`
- `fn` `codex-rs/core/src/exec_policy.rs:917` `async fn request_rule_uses_prefix_rule() {`
- `fn` `codex-rs/core/src/exec_policy.rs:950` `async fn heuristics_apply_when_other_commands_match_policy() {`
- `fn` `codex-rs/core/src/exec_policy.rs:983` `async fn append_execpolicy_amendment_updates_policy_and_file() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1016` `async fn append_execpolicy_amendment_rejects_empty_prefix() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1034` `async fn proposed_execpolicy_amendment_is_present_for_single_command_without_policy_match() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1058` `async fn proposed_execpolicy_amendment_is_omitted_when_policy_prompts() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1088` `async fn proposed_execpolicy_amendment_is_present_for_multi_command_scripts() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1118` `async fn proposed_execpolicy_amendment_uses_first_no_match_in_multi_command_scripts() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1152` `async fn proposed_execpolicy_amendment_is_present_when_heuristics_allow() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1176` `async fn proposed_execpolicy_amendment_is_suppressed_when_policy_matches_allow() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1206` `async fn dangerous_git_push_requires_approval_in_danger_full_access() {`
- `fn` `codex-rs/core/src/exec_policy.rs:1228` `fn vec_str(items: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/core/src/exec_policy.rs:1235` `async fn verify_approval_requirement_for_unsafe_powershell_command() {`

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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
