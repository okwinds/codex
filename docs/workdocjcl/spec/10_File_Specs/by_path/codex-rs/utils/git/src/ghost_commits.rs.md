# `codex-rs/utils/git/src/ghost_commits.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `61175`
- sha256: `97c1927620594b6f05c2eb1bfb88d42c5b4d966e60a6d5acd9d2ca06ba3218f2`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/git/src/ghost_commits.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct CreateGhostCommitOptions<'a> {`
- `pub struct RestoreGhostCommitOptions<'a> {`
- `pub struct GhostSnapshotConfig {`
- `pub struct GhostSnapshotReport {`
- `pub struct LargeUntrackedDir {`
- `pub struct IgnoredUntrackedFile {`
- `pub fn new(repo_path: &'a Path) -> Self {`
- `pub fn message(mut self, message: &'a str) -> Self {`
- `pub fn ghost_snapshot(mut self, ghost_snapshot: GhostSnapshotConfig) -> Self {`
- `pub fn ignore_large_untracked_files(mut self, bytes: i64) -> Self {`
- `pub fn new(repo_path: &'a Path) -> Self {`
- `pub fn ghost_snapshot(mut self, ghost_snapshot: GhostSnapshotConfig) -> Self {`
- `pub fn ignore_large_untracked_files(mut self, bytes: i64) -> Self {`
- `pub fn ignore_large_untracked_dirs(mut self, file_count: i64) -> Self {`
- `pub fn create_ghost_commit(`
- `pub fn capture_ghost_snapshot_report(`
- `pub fn create_ghost_commit_with_report(`
- `pub fn restore_ghost_commit(repo_path: &Path, commit: &GhostCommit) -> Result<(), GitToolingError> {`
- `pub fn restore_ghost_commit_with_options(`
- `pub fn restore_to_commit(repo_path: &Path, commit_id: &str) -> Result<(), GitToolingError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/git/src/ghost_commits.rs:1` `use std::collections::BTreeMap;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:2` `use std::collections::HashSet;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:3` `use std::ffi::OsString;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:4` `use std::fs;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:5` `use std::io;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:6` `use std::path::Component;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:7` `use std::path::Path;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:10` `use tempfile::Builder;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:12` `use crate::GhostCommit;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:13` `use crate::GitToolingError;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:14` `use crate::operations::apply_repo_prefix_to_force_include;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:15` `use crate::operations::ensure_git_repository;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:16` `use crate::operations::normalize_relative_path;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:17` `use crate::operations::repo_subdir;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:18` `use crate::operations::resolve_head;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:19` `use crate::operations::resolve_repository_root;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:20` `use crate::operations::run_git_for_status;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:21` `use crate::operations::run_git_for_stdout;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:22` `use crate::operations::run_git_for_stdout_all;`
- `const` `codex-rs/utils/git/src/ghost_commits.rs:25` `const DEFAULT_COMMIT_MESSAGE: &str = "codex snapshot";`
- `const` `codex-rs/utils/git/src/ghost_commits.rs:27` `const DEFAULT_IGNORE_LARGE_UNTRACKED_DIRS: i64 = 200;`
- `const` `codex-rs/utils/git/src/ghost_commits.rs:29` `const DEFAULT_IGNORE_LARGE_UNTRACKED_FILES: i64 = 10 * 1024 * 1024;`
- `const` `codex-rs/utils/git/src/ghost_commits.rs:35` `const DEFAULT_IGNORED_DIR_NAMES: &[&str] = &[`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:51` `pub struct CreateGhostCommitOptions<'a> {`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:59` `pub struct RestoreGhostCommitOptions<'a> {`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:65` `pub struct GhostSnapshotConfig {`
- `impl` `codex-rs/utils/git/src/ghost_commits.rs:71` `impl Default for GhostSnapshotConfig {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:72` `fn default() -> Self {`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:83` `pub struct GhostSnapshotReport {`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:90` `pub struct LargeUntrackedDir {`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:97` `pub struct IgnoredUntrackedFile {`
- `impl` `codex-rs/utils/git/src/ghost_commits.rs:102` `impl<'a> CreateGhostCommitOptions<'a> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:104` `pub fn new(repo_path: &'a Path) -> Self {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:114` `pub fn message(mut self, message: &'a str) -> Self {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:119` `pub fn ghost_snapshot(mut self, ghost_snapshot: GhostSnapshotConfig) -> Self {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:128` `pub fn ignore_large_untracked_files(mut self, bytes: i64) -> Self {`
- `impl` `codex-rs/utils/git/src/ghost_commits.rs:156` `impl<'a> RestoreGhostCommitOptions<'a> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:158` `pub fn new(repo_path: &'a Path) -> Self {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:165` `pub fn ghost_snapshot(mut self, ghost_snapshot: GhostSnapshotConfig) -> Self {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:173` `pub fn ignore_large_untracked_files(mut self, bytes: i64) -> Self {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:183` `pub fn ignore_large_untracked_dirs(mut self, file_count: i64) -> Self {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:193` `fn detect_large_untracked_dirs(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:244` `fn to_session_relative_path(path: &Path, repo_prefix: Option<&Path>) -> PathBuf {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:255` `pub fn create_ghost_commit(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:262` `pub fn capture_ghost_snapshot_report(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:302` `pub fn create_ghost_commit_with_report(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:427` `pub fn restore_ghost_commit(repo_path: &Path, commit: &GhostCommit) -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:432` `pub fn restore_ghost_commit_with_options(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:457` `pub fn restore_to_commit(repo_path: &Path, commit_id: &str) -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:467` `fn restore_to_commit_inner(`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:497` `struct UntrackedSnapshot {`
- `struct` `codex-rs/utils/git/src/ghost_commits.rs:507` `struct StatusSnapshot {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:514` `fn capture_status_snapshot(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:673` `fn capture_existing_untracked(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:690` `fn extract_status_path_after_fields(record: &str, fields_before_path: i64) -> Option<&str> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:706` `fn should_ignore_for_snapshot(path: &Path) -> bool {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:719` `fn prepare_force_include(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:734` `fn is_force_included(path: &Path, force_include: &[PathBuf]) -> bool {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:740` `fn untracked_file_size(path: &Path) -> io::Result<Option<i64>> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:751` `fn add_paths_to_index(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:775` `fn dedupe_paths(paths: Vec<PathBuf>) -> Vec<PathBuf> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:786` `fn merge_preserved_untracked_files(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:798` `fn merge_preserved_untracked_dirs(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:817` `fn remove_new_untracked(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:848` `fn should_preserve(`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:863` `fn remove_path(path: &Path) -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:883` `fn default_commit_identity() -> Vec<(OsString, OsString)> {`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:906` `use super::*;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:907` `use crate::operations::run_git_for_stdout;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:908` `use assert_matches::assert_matches;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:909` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:910` `use std::fs::File;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:911` `use std::process::Command;`
- `use` `codex-rs/utils/git/src/ghost_commits.rs:912` `use walkdir::WalkDir;`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:915` `fn run_git_in(repo_path: &Path, args: &[&str]) {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:925` `fn run_git_stdout(repo_path: &Path, args: &[&str]) -> String {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:936` `fn init_test_repo(repo: &Path) {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:941` `fn create_sparse_file(path: &Path, bytes: i64) -> io::Result<()> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:951` `fn create_and_restore_roundtrip() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1021` `fn snapshot_ignores_large_untracked_files() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1077` `fn create_snapshot_reports_large_untracked_dirs() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1140` `fn restore_preserves_large_untracked_dirs_when_threshold_disabled()`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1194` `fn snapshot_ignores_default_ignored_directories() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1301` `fn restore_preserves_default_ignored_directories() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1356` `fn create_snapshot_reports_nested_large_untracked_dirs_under_tracked_parent()`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1418` `fn create_snapshot_without_existing_head() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1446` `fn create_ghost_commit_uses_custom_message() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1476` `fn create_ghost_commit_rejects_force_include_parent_path() {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1488` `fn restore_requires_git_repository() {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1496` `fn restore_from_subdirectory_restores_files_relatively() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1540` `fn restore_from_subdirectory_preserves_parent_vscode() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1584` `fn restore_preserves_ignored_files() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1629` `fn restore_preserves_new_ignored_directory() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1667` `fn restore_preserves_new_ignored_file() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1704` `fn restore_respects_removed_ignored_file() -> Result<(), GitToolingError> {`
- `fn` `codex-rs/utils/git/src/ghost_commits.rs:1740` `fn restore_preserves_ignored_glob_matches() -> Result<(), GitToolingError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::collections::HashSet;`
- `use std::ffi::OsString;`
- `use std::fs;`
- `use std::io;`
- `use std::path::Component;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tempfile::Builder;`
- `use crate::GhostCommit;`
- `use crate::GitToolingError;`
- `use crate::operations::apply_repo_prefix_to_force_include;`
- `use crate::operations::ensure_git_repository;`
- `use crate::operations::normalize_relative_path;`
- `use crate::operations::repo_subdir;`
- `use crate::operations::resolve_head;`
- `use crate::operations::resolve_repository_root;`
- `use crate::operations::run_git_for_status;`
- `use crate::operations::run_git_for_stdout;`
- `use crate::operations::run_git_for_stdout_all;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
