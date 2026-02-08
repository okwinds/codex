# `codex-rs/core/src/exec_env.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11113`
- sha256: `e3e744df0905e28920f6725780735ab794bb6d6b83bdadddf16509f1f14b8b2b`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/exec_env.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn create_env(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/exec_env.rs:1` `use crate::config::types::EnvironmentVariablePattern;`
- `use` `codex-rs/core/src/exec_env.rs:2` `use crate::config::types::ShellEnvironmentPolicy;`
- `use` `codex-rs/core/src/exec_env.rs:3` `use crate::config::types::ShellEnvironmentPolicyInherit;`
- `use` `codex-rs/core/src/exec_env.rs:4` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/exec_env.rs:5` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/exec_env.rs:6` `use std::collections::HashSet;`
- `const` `codex-rs/core/src/exec_env.rs:8` `pub const CODEX_THREAD_ID_ENV_VAR: &str = "CODEX_THREAD_ID";`
- `fn` `codex-rs/core/src/exec_env.rs:20` `pub fn create_env(`
- `const` `codex-rs/core/src/exec_env.rs:41` `const CORE_VARS: &[&str] = &[`
- `use` `codex-rs/core/src/exec_env.rs:98` `use super::*;`
- `use` `codex-rs/core/src/exec_env.rs:99` `use crate::config::types::ShellEnvironmentPolicyInherit;`
- `use` `codex-rs/core/src/exec_env.rs:100` `use maplit::hashmap;`
- `fn` `codex-rs/core/src/exec_env.rs:102` `fn make_vars(pairs: &[(&str, &str)]) -> Vec<(String, String)> {`
- `fn` `codex-rs/core/src/exec_env.rs:110` `fn test_core_inherit_defaults_keep_sensitive_vars() {`
- `fn` `codex-rs/core/src/exec_env.rs:134` `fn test_core_inherit_with_default_excludes_enabled() {`
- `fn` `codex-rs/core/src/exec_env.rs:159` `fn test_include_only() {`
- `fn` `codex-rs/core/src/exec_env.rs:181` `fn test_set_overrides() {`
- `fn` `codex-rs/core/src/exec_env.rs:203` `fn populate_env_inserts_thread_id() {`
- `fn` `codex-rs/core/src/exec_env.rs:218` `fn populate_env_omits_thread_id_when_missing() {`
- `fn` `codex-rs/core/src/exec_env.rs:231` `fn test_inherit_all() {`
- `fn` `codex-rs/core/src/exec_env.rs:248` `fn test_inherit_all_with_default_excludes() {`
- `fn` `codex-rs/core/src/exec_env.rs:268` `fn test_core_inherit_respects_case_insensitive_names_on_windows() {`
- `fn` `codex-rs/core/src/exec_env.rs:293` `fn test_inherit_none() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::types::EnvironmentVariablePattern;`
- `use crate::config::types::ShellEnvironmentPolicy;`
- `use crate::config::types::ShellEnvironmentPolicyInherit;`
- `use codex_protocol::ThreadId;`
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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
