# `codex-rs/apply-patch/src/invocation.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `27852`
- sha256: `1386140e24bbf17996dab3a87f857bee0257c6896c8edf31f8360b34712edd68`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/apply-patch/src/invocation.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum MaybeApplyPatch {`
- `pub enum ExtractHeredocError {`
- `pub fn maybe_parse_apply_patch(argv: &[String]) -> MaybeApplyPatch {`
- `pub fn maybe_parse_apply_patch_verified(argv: &[String], cwd: &Path) -> MaybeApplyPatchVerified {`

## Definitions (auto, per-file)
- `use` `codex-rs/apply-patch/src/invocation.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/apply-patch/src/invocation.rs:2` `use std::path::Path;`
- `use` `codex-rs/apply-patch/src/invocation.rs:3` `use std::sync::LazyLock;`
- `use` `codex-rs/apply-patch/src/invocation.rs:5` `use tree_sitter::Parser;`
- `use` `codex-rs/apply-patch/src/invocation.rs:6` `use tree_sitter::Query;`
- `use` `codex-rs/apply-patch/src/invocation.rs:7` `use tree_sitter::QueryCursor;`
- `use` `codex-rs/apply-patch/src/invocation.rs:8` `use tree_sitter::StreamingIterator;`
- `use` `codex-rs/apply-patch/src/invocation.rs:9` `use tree_sitter_bash::LANGUAGE as BASH;`
- `use` `codex-rs/apply-patch/src/invocation.rs:11` `use crate::ApplyPatchAction;`
- `use` `codex-rs/apply-patch/src/invocation.rs:12` `use crate::ApplyPatchArgs;`
- `use` `codex-rs/apply-patch/src/invocation.rs:13` `use crate::ApplyPatchError;`
- `use` `codex-rs/apply-patch/src/invocation.rs:14` `use crate::ApplyPatchFileChange;`
- `use` `codex-rs/apply-patch/src/invocation.rs:15` `use crate::ApplyPatchFileUpdate;`
- `use` `codex-rs/apply-patch/src/invocation.rs:16` `use crate::IoError;`
- `use` `codex-rs/apply-patch/src/invocation.rs:17` `use crate::MaybeApplyPatchVerified;`
- `use` `codex-rs/apply-patch/src/invocation.rs:18` `use crate::parser::Hunk;`
- `use` `codex-rs/apply-patch/src/invocation.rs:19` `use crate::parser::ParseError;`
- `use` `codex-rs/apply-patch/src/invocation.rs:20` `use crate::parser::parse_patch;`
- `use` `codex-rs/apply-patch/src/invocation.rs:21` `use crate::unified_diff_from_chunks;`
- `use` `codex-rs/apply-patch/src/invocation.rs:22` `use std::str::Utf8Error;`
- `use` `codex-rs/apply-patch/src/invocation.rs:23` `use tree_sitter::LanguageError;`
- `const` `codex-rs/apply-patch/src/invocation.rs:25` `const APPLY_PATCH_COMMANDS: [&str; 2] = ["apply_patch", "applypatch"];`
- `enum` `codex-rs/apply-patch/src/invocation.rs:28` `enum ApplyPatchShell {`
- `enum` `codex-rs/apply-patch/src/invocation.rs:35` `pub enum MaybeApplyPatch {`
- `enum` `codex-rs/apply-patch/src/invocation.rs:43` `pub enum ExtractHeredocError {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:51` `fn classify_shell_name(shell: &str) -> Option<String> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:58` `fn classify_shell(shell: &str, flag: &str) -> Option<ApplyPatchShell> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:69` `fn can_skip_flag(shell: &str, flag: &str) -> bool {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:75` `fn parse_shell_script(argv: &[String]) -> Option<(ApplyPatchShell, &str)> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:91` `fn extract_apply_patch_from_shell(`
- `fn` `codex-rs/apply-patch/src/invocation.rs:103` `pub fn maybe_parse_apply_patch(argv: &[String]) -> MaybeApplyPatch {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:132` `pub fn maybe_parse_apply_patch_verified(argv: &[String], cwd: &Path) -> MaybeApplyPatchVerified {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:239` `fn extract_apply_patch_from_bash(`
- `static` `codex-rs/apply-patch/src/invocation.rs:263` `static APPLY_PATCH_QUERY: LazyLock<Query> = LazyLock::new(|| {`
- `use` `codex-rs/apply-patch/src/invocation.rs:373` `use super::*;`
- `use` `codex-rs/apply-patch/src/invocation.rs:374` `use assert_matches::assert_matches;`
- `use` `codex-rs/apply-patch/src/invocation.rs:375` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/apply-patch/src/invocation.rs:376` `use std::fs;`
- `use` `codex-rs/apply-patch/src/invocation.rs:377` `use std::path::PathBuf;`
- `use` `codex-rs/apply-patch/src/invocation.rs:378` `use std::string::ToString;`
- `use` `codex-rs/apply-patch/src/invocation.rs:379` `use tempfile::tempdir;`
- `fn` `codex-rs/apply-patch/src/invocation.rs:382` `fn wrap_patch(body: &str) -> String {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:386` `fn strs_to_strings(strs: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:391` `fn args_bash(script: &str) -> Vec<String> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:395` `fn args_powershell(script: &str) -> Vec<String> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:399` `fn args_powershell_no_profile(script: &str) -> Vec<String> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:403` `fn args_pwsh(script: &str) -> Vec<String> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:407` `fn args_cmd(script: &str) -> Vec<String> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:411` `fn heredoc_script(prefix: &str) -> String {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:417` `fn heredoc_script_ps(prefix: &str, suffix: &str) -> String {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:423` `fn expected_single_add() -> Vec<Hunk> {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:430` `fn assert_match_args(args: Vec<String>, expected_workdir: Option<&str>) {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:440` `fn assert_match(script: &str, expected_workdir: Option<&str>) {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:445` `fn assert_not_match(script: &str) {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:454` `fn test_implicit_patch_single_arg_is_error() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:465` `fn test_implicit_patch_bash_script_is_error() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:476` `fn test_literal() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:501` `fn test_literal_applypatch() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:526` `fn test_heredoc() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:531` `fn test_heredoc_non_login_shell() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:538` `fn test_heredoc_applypatch() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:566` `fn test_powershell_heredoc() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:571` `fn test_powershell_heredoc_no_profile() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:576` `fn test_pwsh_heredoc() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:582` `fn test_cmd_heredoc_with_cd() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:588` `fn test_heredoc_with_leading_cd() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:593` `fn test_cd_with_semicolon_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:598` `fn test_cd_or_apply_patch_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:603` `fn test_cd_pipe_apply_patch_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:608` `fn test_cd_single_quoted_path_with_spaces() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:613` `fn test_cd_double_quoted_path_with_spaces() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:618` `fn test_echo_and_apply_patch_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:623` `fn test_apply_patch_with_arg_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:629` `fn test_double_cd_then_apply_patch_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:634` `fn test_cd_two_args_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:639` `fn test_cd_then_apply_patch_then_extra_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:645` `fn test_echo_then_cd_and_apply_patch_is_ignored() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:651` `fn test_unified_diff_last_line_replacement() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:688` `fn test_unified_diff_insert_at_eof() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:722` `fn test_apply_patch_should_resolve_absolute_paths_in_cwd() {`
- `fn` `codex-rs/apply-patch/src/invocation.rs:768` `fn test_apply_patch_resolves_move_path_with_effective_cwd() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use std::sync::LazyLock;`
- `use tree_sitter::Parser;`
- `use tree_sitter::Query;`
- `use tree_sitter::QueryCursor;`
- `use tree_sitter::StreamingIterator;`
- `use tree_sitter_bash::LANGUAGE as BASH;`
- `use crate::ApplyPatchAction;`
- `use crate::ApplyPatchArgs;`
- `use crate::ApplyPatchError;`
- `use crate::ApplyPatchFileChange;`
- `use crate::ApplyPatchFileUpdate;`
- `use crate::IoError;`
- `use crate::MaybeApplyPatchVerified;`
- `use crate::parser::Hunk;`
- `use crate::parser::ParseError;`
- `use crate::parser::parse_patch;`
- `use crate::unified_diff_from_chunks;`
- `use std::str::Utf8Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
