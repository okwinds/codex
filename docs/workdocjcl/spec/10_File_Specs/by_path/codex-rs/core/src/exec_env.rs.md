# `codex-rs/core/src/exec_env.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8492`
- sha256: `40d6cfaa9a6b055089ed79e59e0fc35c21b7ccb4e5f8c10cf6012b53d083ef4e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/exec_env.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn create_env(policy: &ShellEnvironmentPolicy) -> HashMap<String, String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/exec_env.rs:1` `use crate::config::types::EnvironmentVariablePattern;`
- `use` `codex-rs/core/src/exec_env.rs:2` `use crate::config::types::ShellEnvironmentPolicy;`
- `use` `codex-rs/core/src/exec_env.rs:3` `use crate::config::types::ShellEnvironmentPolicyInherit;`
- `use` `codex-rs/core/src/exec_env.rs:4` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/exec_env.rs:5` `use std::collections::HashSet;`
- `fn` `codex-rs/core/src/exec_env.rs:14` `pub fn create_env(policy: &ShellEnvironmentPolicy) -> HashMap<String, String> {`
- `const` `codex-rs/core/src/exec_env.rs:28` `const CORE_VARS: &[&str] = &[`
- `use` `codex-rs/core/src/exec_env.rs:80` `use super::*;`
- `use` `codex-rs/core/src/exec_env.rs:81` `use crate::config::types::ShellEnvironmentPolicyInherit;`
- `use` `codex-rs/core/src/exec_env.rs:82` `use maplit::hashmap;`
- `fn` `codex-rs/core/src/exec_env.rs:84` `fn make_vars(pairs: &[(&str, &str)]) -> Vec<(String, String)> {`
- `fn` `codex-rs/core/src/exec_env.rs:92` `fn test_core_inherit_defaults_keep_sensitive_vars() {`
- `fn` `codex-rs/core/src/exec_env.rs:114` `fn test_core_inherit_with_default_excludes_enabled() {`
- `fn` `codex-rs/core/src/exec_env.rs:137` `fn test_include_only() {`
- `fn` `codex-rs/core/src/exec_env.rs:157` `fn test_set_overrides() {`
- `fn` `codex-rs/core/src/exec_env.rs:177` `fn test_inherit_all() {`
- `fn` `codex-rs/core/src/exec_env.rs:192` `fn test_inherit_all_with_default_excludes() {`
- `fn` `codex-rs/core/src/exec_env.rs:210` `fn test_core_inherit_respects_case_insensitive_names_on_windows() {`
- `fn` `codex-rs/core/src/exec_env.rs:233` `fn test_inherit_none() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::types::EnvironmentVariablePattern;`
- `use crate::config::types::ShellEnvironmentPolicy;`
- `use crate::config::types::ShellEnvironmentPolicyInherit;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use super::*;`
- `use crate::config::types::ShellEnvironmentPolicyInherit;`
- `use maplit::hashmap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
