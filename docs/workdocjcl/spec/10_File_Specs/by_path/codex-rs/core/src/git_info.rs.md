# `codex-rs/core/src/git_info.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `42145`
- sha256: `7942943e4272d689e86c685251dc82dfa47a4994d0d4d40704362b6105ccd4c9`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/git_info.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn get_git_repo_root(base_dir: &Path) -> Option<PathBuf> {`
- `pub struct GitDiffToRemote {`
- `pub struct CommitLogEntry {`
- `pub fn resolve_root_git_project_for_trust(cwd: &Path) -> Option<PathBuf> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/git_info.rs:1` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/git_info.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/core/src/git_info.rs:3` `use std::path::Path;`
- `use` `codex-rs/core/src/git_info.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/git_info.rs:6` `use crate::util::resolve_path;`
- `use` `codex-rs/core/src/git_info.rs:7` `use codex_app_server_protocol::GitSha;`
- `use` `codex-rs/core/src/git_info.rs:8` `use codex_protocol::protocol::GitInfo;`
- `use` `codex-rs/core/src/git_info.rs:9` `use futures::future::join_all;`
- `use` `codex-rs/core/src/git_info.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/core/src/git_info.rs:11` `use serde::Serialize;`
- `use` `codex-rs/core/src/git_info.rs:12` `use tokio::process::Command;`
- `use` `codex-rs/core/src/git_info.rs:13` `use tokio::time::Duration as TokioDuration;`
- `use` `codex-rs/core/src/git_info.rs:14` `use tokio::time::timeout;`
- `fn` `codex-rs/core/src/git_info.rs:28` `pub fn get_git_repo_root(base_dir: &Path) -> Option<PathBuf> {`
- `const` `codex-rs/core/src/git_info.rs:47` `const GIT_COMMAND_TIMEOUT: TokioDuration = TokioDuration::from_secs(5);`
- `struct` `codex-rs/core/src/git_info.rs:50` `pub struct GitDiffToRemote {`
- `fn` `codex-rs/core/src/git_info.rs:59` `pub async fn collect_git_info(cwd: &Path) -> Option<GitInfo> {`
- `fn` `codex-rs/core/src/git_info.rs:114` `pub async fn get_git_remote_urls(cwd: &Path) -> Option<BTreeMap<String, String>> {`
- `fn` `codex-rs/core/src/git_info.rs:127` `pub async fn get_git_remote_urls_assume_git_repo(cwd: &Path) -> Option<BTreeMap<String, String>> {`
- `fn` `codex-rs/core/src/git_info.rs:138` `pub async fn get_head_commit_hash(cwd: &Path) -> Option<String> {`
- `fn` `codex-rs/core/src/git_info.rs:153` `fn parse_git_remote_urls(stdout: &str) -> Option<BTreeMap<String, String>> {`
- `struct` `codex-rs/core/src/git_info.rs:182` `pub struct CommitLogEntry {`
- `fn` `codex-rs/core/src/git_info.rs:193` `pub async fn recent_commits(cwd: &Path, limit: usize) -> Vec<CommitLogEntry> {`
- `fn` `codex-rs/core/src/git_info.rs:240` `pub async fn git_diff_to_remote(cwd: &Path) -> Option<GitDiffToRemote> {`
- `fn` `codex-rs/core/src/git_info.rs:255` `async fn run_git_command_with_timeout(args: &[&str], cwd: &Path) -> Option<std::process::Output> {`
- `fn` `codex-rs/core/src/git_info.rs:266` `async fn get_git_remotes(cwd: &Path) -> Option<Vec<String>> {`
- `fn` `codex-rs/core/src/git_info.rs:289` `async fn get_default_branch(cwd: &Path) -> Option<String> {`
- `fn` `codex-rs/core/src/git_info.rs:340` `pub async fn default_branch_name(cwd: &Path) -> Option<String> {`
- `fn` `codex-rs/core/src/git_info.rs:345` `async fn get_default_branch_local(cwd: &Path) -> Option<String> {`
- `fn` `codex-rs/core/src/git_info.rs:368` `async fn branch_ancestry(cwd: &Path) -> Option<Vec<String>> {`
- `fn` `codex-rs/core/src/git_info.rs:439` `async fn branch_remote_and_distance(`
- `fn` `codex-rs/core/src/git_info.rs:518` `async fn find_closest_sha(cwd: &Path, branches: &[String], remotes: &[String]) -> Option<GitSha> {`
- `fn` `codex-rs/core/src/git_info.rs:542` `async fn diff_against_sha(cwd: &Path, sha: &GitSha) -> Option<String> {`
- `fn` `codex-rs/core/src/git_info.rs:600` `pub fn resolve_root_git_project_for_trust(cwd: &Path) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/git_info.rs:627` `pub async fn local_git_branches(cwd: &Path) -> Vec<String> {`
- `fn` `codex-rs/core/src/git_info.rs:654` `pub async fn current_branch_name(cwd: &Path) -> Option<String> {`
- `use` `codex-rs/core/src/git_info.rs:667` `use super::*;`
- `use` `codex-rs/core/src/git_info.rs:669` `use core_test_support::skip_if_sandbox;`
- `use` `codex-rs/core/src/git_info.rs:670` `use std::fs;`
- `use` `codex-rs/core/src/git_info.rs:671` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/git_info.rs:672` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/git_info.rs:675` `async fn create_test_git_repo(temp_dir: &TempDir) -> PathBuf {`
- `fn` `codex-rs/core/src/git_info.rs:733` `async fn test_recent_commits_non_git_directory_returns_empty() {`
- `fn` `codex-rs/core/src/git_info.rs:740` `async fn test_recent_commits_orders_and_limits() {`
- `use` `codex-rs/core/src/git_info.rs:742` `use tokio::time::Duration;`
- `use` `codex-rs/core/src/git_info.rs:743` `use tokio::time::sleep;`
- `fn` `codex-rs/core/src/git_info.rs:807` `async fn create_test_git_repo_with_remote(temp_dir: &TempDir) -> (PathBuf, String) {`
- `fn` `codex-rs/core/src/git_info.rs:843` `async fn test_collect_git_info_non_git_directory() {`
- `fn` `codex-rs/core/src/git_info.rs:850` `async fn test_collect_git_info_git_repository() {`
- `fn` `codex-rs/core/src/git_info.rs:874` `async fn test_collect_git_info_with_remote() {`
- `fn` `codex-rs/core/src/git_info.rs:913` `async fn test_collect_git_info_detached_head() {`
- `fn` `codex-rs/core/src/git_info.rs:945` `async fn test_collect_git_info_with_branch() {`
- `fn` `codex-rs/core/src/git_info.rs:966` `async fn test_get_git_working_tree_state_clean_repo() {`
- `fn` `codex-rs/core/src/git_info.rs:989` `async fn test_get_git_working_tree_state_with_changes() {`
- `fn` `codex-rs/core/src/git_info.rs:1017` `async fn test_get_git_working_tree_state_branch_fallback() {`
- `fn` `codex-rs/core/src/git_info.rs:1059` `fn resolve_root_git_project_for_trust_returns_none_outside_repo() {`
- `fn` `codex-rs/core/src/git_info.rs:1065` `async fn resolve_root_git_project_for_trust_regular_repo_returns_repo_root() {`
- `fn` `codex-rs/core/src/git_info.rs:1080` `async fn resolve_root_git_project_for_trust_detects_worktree_and_returns_main_root() {`
- `fn` `codex-rs/core/src/git_info.rs:1110` `fn resolve_root_git_project_for_trust_non_worktrees_gitdir_returns_none() {`
- `fn` `codex-rs/core/src/git_info.rs:1130` `async fn test_get_git_working_tree_state_unpushed_commit() {`
- `fn` `codex-rs/core/src/git_info.rs:1167` `fn test_git_info_serialization() {`
- `fn` `codex-rs/core/src/git_info.rs:1186` `fn test_git_info_serialization_with_nones() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::collections::HashSet;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use crate::util::resolve_path;`
- `use codex_app_server_protocol::GitSha;`
- `use codex_protocol::protocol::GitInfo;`
- `use futures::future::join_all;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use tokio::process::Command;`
- `use tokio::time::Duration as TokioDuration;`
- `use tokio::time::timeout;`
- `use super::*;`
- `use core_test_support::skip_if_sandbox;`
- `use std::fs;`
- `use std::path::PathBuf;`
- `use tempfile::TempDir;`
- `use tokio::time::Duration;`
- `use tokio::time::sleep;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
