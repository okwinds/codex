# `codex-rs/utils/git/src/apply.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `30707`
- sha256: `acfb62017aaa8f27ac82500bf91c4ea6673a346ec8161cfcec9a25570d4e117e`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/git/src/apply.rs` (read)
- env: `CODEX_APPLY_GIT_CFG`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct ApplyGitRequest {`
- `pub struct ApplyGitResult {`
- `pub fn apply_git_patch(req: &ApplyGitRequest) -> io::Result<ApplyGitResult> {`
- `pub fn extract_paths_from_patch(diff_text: &str) -> Vec<String> {`
- `pub fn stage_paths(git_root: &Path, diff: &str) -> io::Result<()> {`
- `pub fn parse_git_apply_output(`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/git/src/apply.rs:9` `use once_cell::sync::Lazy;`
- `use` `codex-rs/utils/git/src/apply.rs:10` `use regex::Regex;`
- `use` `codex-rs/utils/git/src/apply.rs:11` `use std::ffi::OsStr;`
- `use` `codex-rs/utils/git/src/apply.rs:12` `use std::io;`
- `use` `codex-rs/utils/git/src/apply.rs:13` `use std::path::Path;`
- `use` `codex-rs/utils/git/src/apply.rs:14` `use std::path::PathBuf;`
- `struct` `codex-rs/utils/git/src/apply.rs:18` `pub struct ApplyGitRequest {`
- `struct` `codex-rs/utils/git/src/apply.rs:27` `pub struct ApplyGitResult {`
- `fn` `codex-rs/utils/git/src/apply.rs:41` `pub fn apply_git_patch(req: &ApplyGitRequest) -> io::Result<ApplyGitResult> {`
- `fn` `codex-rs/utils/git/src/apply.rs:126` `fn resolve_git_root(cwd: &Path) -> io::Result<PathBuf> {`
- `fn` `codex-rs/utils/git/src/apply.rs:144` `fn write_temp_patch(diff: &str) -> io::Result<(tempfile::TempDir, PathBuf)> {`
- `fn` `codex-rs/utils/git/src/apply.rs:151` `fn run_git(cwd: &Path, git_cfg: &[String], args: &[String]) -> io::Result<(i32, String, String)> {`
- `fn` `codex-rs/utils/git/src/apply.rs:166` `fn quote_shell(s: &str) -> String {`
- `fn` `codex-rs/utils/git/src/apply.rs:177` `fn render_command_for_log(cwd: &Path, git_cfg: &[String], args: &[String]) -> String {`
- `fn` `codex-rs/utils/git/src/apply.rs:194` `pub fn extract_paths_from_patch(diff_text: &str) -> Vec<String> {`
- `fn` `codex-rs/utils/git/src/apply.rs:214` `fn parse_diff_git_paths(line: &str) -> Option<(String, String)> {`
- `fn` `codex-rs/utils/git/src/apply.rs:221` `fn read_diff_git_token(chars: &mut std::iter::Peekable<std::str::Chars<'_>>) -> Option<String> {`
- `fn` `codex-rs/utils/git/src/apply.rs:257` `fn normalize_diff_path(raw: &str, prefix: &str) -> Option<String> {`
- `fn` `codex-rs/utils/git/src/apply.rs:272` `fn unescape_c_string(input: &str) -> String {`
- `fn` `codex-rs/utils/git/src/apply.rs:320` `pub fn stage_paths(git_root: &Path, diff: &str) -> io::Result<()> {`
- `fn` `codex-rs/utils/git/src/apply.rs:347` `pub fn parse_git_apply_output(`
- `fn` `codex-rs/utils/git/src/apply.rs:363` `fn add(set: &mut std::collections::BTreeSet<String>, raw: &str) {`
- `static` `codex-rs/utils/git/src/apply.rs:380` `static APPLIED_CLEAN: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:382` `static APPLIED_CONFLICTS: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:384` `static APPLYING_WITH_REJECTS: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:387` `static CHECKING_PATCH: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:389` `static UNMERGED_LINE: Lazy<Regex> = Lazy::new(|| regex_ci("^U\\s+(?P<path>.+)$"));`
- `static` `codex-rs/utils/git/src/apply.rs:390` `static PATCH_FAILED: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:392` `static DOES_NOT_APPLY: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:394` `static THREE_WAY_START: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:397` `static THREE_WAY_FAILED: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:399` `static FALLBACK_DIRECT: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:401` `static LACKS_BLOB: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:406` `static INDEX_MISMATCH: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:408` `static NOT_IN_INDEX: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:410` `static ALREADY_EXISTS_WT: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:413` `static FILE_EXISTS: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:415` `static RENAMED_DELETED: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:417` `static CANNOT_APPLY_BINARY: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:422` `static BINARY_DOES_NOT_APPLY: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:425` `static BINARY_INCORRECT_RESULT: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:430` `static CANNOT_READ_CURRENT: Lazy<Regex> = Lazy::new(|| {`
- `static` `codex-rs/utils/git/src/apply.rs:433` `static SKIPPED_PATCH: Lazy<Regex> =`
- `static` `codex-rs/utils/git/src/apply.rs:435` `static CANNOT_MERGE_BINARY_WARN: Lazy<Regex> = Lazy::new(|| {`
- `fn` `codex-rs/utils/git/src/apply.rs:591` `fn regex_ci(pat: &str) -> Regex {`
- `use` `codex-rs/utils/git/src/apply.rs:597` `use super::*;`
- `use` `codex-rs/utils/git/src/apply.rs:598` `use std::path::Path;`
- `use` `codex-rs/utils/git/src/apply.rs:599` `use std::sync::Mutex;`
- `use` `codex-rs/utils/git/src/apply.rs:600` `use std::sync::OnceLock;`
- `fn` `codex-rs/utils/git/src/apply.rs:602` `fn env_lock() -> &'static Mutex<()> {`
- `static` `codex-rs/utils/git/src/apply.rs:603` `static LOCK: OnceLock<Mutex<()>> = OnceLock::new();`
- `fn` `codex-rs/utils/git/src/apply.rs:607` `fn run(cwd: &Path, args: &[&str]) -> (i32, String, String) {`
- `fn` `codex-rs/utils/git/src/apply.rs:620` `fn init_repo() -> tempfile::TempDir {`
- `fn` `codex-rs/utils/git/src/apply.rs:630` `fn read_file_normalized(path: &Path) -> String {`
- `fn` `codex-rs/utils/git/src/apply.rs:637` `fn extract_paths_handles_quoted_headers() {`
- `fn` `codex-rs/utils/git/src/apply.rs:644` `fn extract_paths_ignores_dev_null_header() {`
- `fn` `codex-rs/utils/git/src/apply.rs:651` `fn extract_paths_unescapes_c_style_in_quoted_headers() {`
- `fn` `codex-rs/utils/git/src/apply.rs:658` `fn parse_output_unescapes_quoted_paths() {`
- `fn` `codex-rs/utils/git/src/apply.rs:667` `fn apply_add_success() {`
- `fn` `codex-rs/utils/git/src/apply.rs:686` `fn apply_modify_conflict() {`
- `fn` `codex-rs/utils/git/src/apply.rs:709` `fn apply_modify_skipped_missing_index() {`
- `fn` `codex-rs/utils/git/src/apply.rs:726` `fn apply_then_revert_success() {`
- `fn` `codex-rs/utils/git/src/apply.rs:762` `fn revert_preflight_does_not_stage_index() {`
- `fn` `codex-rs/utils/git/src/apply.rs:807` `fn preflight_blocks_partial_changes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use once_cell::sync::Lazy;`
- `use regex::Regex;`
- `use std::ffi::OsStr;`
- `use std::io;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use super::*;`
- `use std::path::Path;`
- `use std::sync::Mutex;`
- `use std::sync::OnceLock;`
### Referenced env vars
- `CODEX_APPLY_GIT_CFG`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
