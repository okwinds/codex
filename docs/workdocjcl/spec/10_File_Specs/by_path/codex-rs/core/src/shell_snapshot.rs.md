# `codex-rs/core/src/shell_snapshot.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `26875`
- sha256: `6d95b89535ab66c51022ccd0e8407e2d47df21a42ff0ee512a17c54c84c48265`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/shell_snapshot.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct ShellSnapshot {`
- `pub fn start_snapshotting(`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/shell_snapshot.rs:1` `use std::io::ErrorKind;`
- `use` `codex-rs/core/src/shell_snapshot.rs:2` `use std::path::Path;`
- `use` `codex-rs/core/src/shell_snapshot.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/shell_snapshot.rs:4` `use std::process::Stdio;`
- `use` `codex-rs/core/src/shell_snapshot.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/core/src/shell_snapshot.rs:6` `use std::time::Duration;`
- `use` `codex-rs/core/src/shell_snapshot.rs:7` `use std::time::SystemTime;`
- `use` `codex-rs/core/src/shell_snapshot.rs:9` `use crate::rollout::list::find_thread_path_by_id_str;`
- `use` `codex-rs/core/src/shell_snapshot.rs:10` `use crate::shell::Shell;`
- `use` `codex-rs/core/src/shell_snapshot.rs:11` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/shell_snapshot.rs:12` `use crate::shell::get_shell;`
- `use` `codex-rs/core/src/shell_snapshot.rs:13` `use anyhow::Context;`
- `use` `codex-rs/core/src/shell_snapshot.rs:14` `use anyhow::Result;`
- `use` `codex-rs/core/src/shell_snapshot.rs:15` `use anyhow::anyhow;`
- `use` `codex-rs/core/src/shell_snapshot.rs:16` `use anyhow::bail;`
- `use` `codex-rs/core/src/shell_snapshot.rs:17` `use codex_otel::OtelManager;`
- `use` `codex-rs/core/src/shell_snapshot.rs:18` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/shell_snapshot.rs:19` `use tokio::fs;`
- `use` `codex-rs/core/src/shell_snapshot.rs:20` `use tokio::process::Command;`
- `use` `codex-rs/core/src/shell_snapshot.rs:21` `use tokio::sync::watch;`
- `use` `codex-rs/core/src/shell_snapshot.rs:22` `use tokio::time::timeout;`
- `use` `codex-rs/core/src/shell_snapshot.rs:23` `use tracing::Instrument;`
- `use` `codex-rs/core/src/shell_snapshot.rs:24` `use tracing::info_span;`
- `struct` `codex-rs/core/src/shell_snapshot.rs:27` `pub struct ShellSnapshot {`
- `const` `codex-rs/core/src/shell_snapshot.rs:31` `const SNAPSHOT_TIMEOUT: Duration = Duration::from_secs(10);`
- `const` `codex-rs/core/src/shell_snapshot.rs:32` `const SNAPSHOT_RETENTION: Duration = Duration::from_secs(60 * 60 * 24 * 3); // 3 days retention.`
- `const` `codex-rs/core/src/shell_snapshot.rs:33` `const SNAPSHOT_DIR: &str = "shell_snapshots";`
- `const` `codex-rs/core/src/shell_snapshot.rs:34` `const EXCLUDED_EXPORT_VARS: &[&str] = &["PWD", "OLDPWD"];`
- `impl` `codex-rs/core/src/shell_snapshot.rs:36` `impl ShellSnapshot {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:37` `pub fn start_snapshotting(`
- `fn` `codex-rs/core/src/shell_snapshot.rs:65` `async fn try_new(codex_home: &Path, session_id: ThreadId, shell: &Shell) -> Option<Self> {`
- `impl` `codex-rs/core/src/shell_snapshot.rs:110` `impl Drop for ShellSnapshot {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:111` `fn drop(&mut self) {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:121` `async fn write_shell_snapshot(shell_type: ShellType, output_path: &Path) -> Result<PathBuf> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:146` `async fn capture_snapshot(shell: &Shell) -> Result<String> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:157` `fn strip_snapshot_preamble(snapshot: &str) -> Result<String> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:166` `async fn validate_snapshot(shell: &Shell, snapshot_path: &Path) -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:174` `async fn run_shell_script(shell: &Shell, script: &str) -> Result<String> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:178` `async fn run_script_with_timeout(`
- `fn` `codex-rs/core/src/shell_snapshot.rs:214` `fn excluded_exports_regex() -> String {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:218` `fn zsh_snapshot_script() -> String {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:262` `fn bash_snapshot_script() -> String {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:306` `fn sh_snapshot_script() -> String {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:374` `fn powershell_snapshot_script() -> &'static str {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:402` `pub async fn cleanup_stale_snapshots(codex_home: &Path, active_session_id: ThreadId) -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:463` `async fn remove_snapshot_file(path: &Path) {`
- `use` `codex-rs/core/src/shell_snapshot.rs:471` `use super::*;`
- `use` `codex-rs/core/src/shell_snapshot.rs:472` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/shell_snapshot.rs:474` `use std::os::unix::ffi::OsStrExt;`
- `use` `codex-rs/core/src/shell_snapshot.rs:476` `use std::process::Command;`
- `use` `codex-rs/core/src/shell_snapshot.rs:478` `use std::process::Command as StdCommand;`
- `use` `codex-rs/core/src/shell_snapshot.rs:480` `use tempfile::tempdir;`
- `struct` `codex-rs/core/src/shell_snapshot.rs:483` `struct BlockingStdinPipe {`
- `impl` `codex-rs/core/src/shell_snapshot.rs:489` `impl BlockingStdinPipe {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:490` `fn install() -> Result<Self> {`
- `impl` `codex-rs/core/src/shell_snapshot.rs:528` `impl Drop for BlockingStdinPipe {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:529` `fn drop(&mut self) {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:539` `fn assert_posix_snapshot_sections(snapshot: &str) {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:550` `async fn get_snapshot(shell_type: ShellType) -> Result<String> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:559` `fn strip_snapshot_preamble_removes_leading_output() {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:566` `fn strip_snapshot_preamble_requires_marker() {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:573` `fn bash_snapshot_filters_invalid_exports() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:597` `async fn try_new_creates_and_deletes_snapshot_file() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:620` `async fn snapshot_shell_does_not_inherit_stdin() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:652` `async fn timed_out_snapshot_shell_is_terminated() -> Result<()> {`
- `use` `codex-rs/core/src/shell_snapshot.rs:653` `use std::process::Stdio;`
- `use` `codex-rs/core/src/shell_snapshot.rs:654` `use tokio::time::Duration as TokioDuration;`
- `use` `codex-rs/core/src/shell_snapshot.rs:655` `use tokio::time::Instant;`
- `use` `codex-rs/core/src/shell_snapshot.rs:656` `use tokio::time::sleep;`
- `fn` `codex-rs/core/src/shell_snapshot.rs:704` `async fn macos_zsh_snapshot_includes_sections() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:712` `async fn linux_bash_snapshot_includes_sections() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:720` `async fn linux_sh_snapshot_includes_sections() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:729` `async fn windows_powershell_snapshot_includes_sections() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:737` `async fn write_rollout_stub(codex_home: &Path, session_id: ThreadId) -> Result<PathBuf> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:750` `async fn cleanup_stale_snapshots_removes_orphans_and_keeps_live() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:777` `async fn cleanup_stale_snapshots_removes_stale_rollouts() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:798` `async fn cleanup_stale_snapshots_skips_active_session() -> Result<()> {`
- `fn` `codex-rs/core/src/shell_snapshot.rs:818` `fn set_file_mtime(path: &Path, age: Duration) -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::ErrorKind;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Stdio;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use std::time::SystemTime;`
- `use crate::rollout::list::find_thread_path_by_id_str;`
- `use crate::shell::Shell;`
- `use crate::shell::ShellType;`
- `use crate::shell::get_shell;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use anyhow::bail;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::ThreadId;`
- `use tokio::fs;`
- `use tokio::process::Command;`
- `use tokio::sync::watch;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
