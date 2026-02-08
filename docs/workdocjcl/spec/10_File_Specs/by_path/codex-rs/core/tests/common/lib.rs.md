# `codex-rs/core/tests/common/lib.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `13250`
- sha256: `4be938efb709b83cb0b14cf1b6a89faae75e19c5ae56bc9bb746b32af623c576`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/common/lib.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub fn test_path_buf_with_windows(unix_path: &str, windows_path: Option<&str>) -> PathBuf {`
- `pub fn test_path_buf(unix_path: &str) -> PathBuf {`
- `pub fn test_absolute_path_with_windows(`
- `pub fn test_absolute_path(unix_path: &str) -> AbsolutePathBuf {`
- `pub fn test_tmp_path() -> AbsolutePathBuf {`
- `pub fn test_tmp_path_buf() -> PathBuf {`
- `pub fn load_sse_fixture(path: impl AsRef<std::path::Path>) -> String {`
- `pub fn load_sse_fixture_with_id_from_str(raw: &str, id: &str) -> String {`
- `pub fn sandbox_env_var() -> &'static str {`
- `pub fn sandbox_network_env_var() -> &'static str {`
- `pub fn format_with_current_shell(command: &str) -> Vec<String> {`
- `pub fn format_with_current_shell_display(command: &str) -> String {`
- `pub fn format_with_current_shell_non_login(command: &str) -> Vec<String> {`
- `pub fn format_with_current_shell_display_non_login(command: &str) -> String {`
- `pub fn stdio_server_bin() -> Result<String, CargoBinError> {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_utils_cargo_bin::CargoBinError;`
- `use tempfile::TempDir;`
- `use codex_core::CodexThread;`
- `use codex_core::config::Config;`
- `use codex_core::config::ConfigBuilder;`
- `use codex_core::config::ConfigOverrides;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use regex_lite::Regex;`
- `use std::path::PathBuf;`
- `use tokio::time::Duration;`
- `use tokio::time::Duration;`
- `use tokio::time::timeout;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use notify::RecursiveMode;`
- `use notify::Watcher;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::mpsc;`
- `use std::sync::mpsc::RecvTimeoutError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
