# `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17206`
- sha256: `d31f042e10bbc54874ffa55509cba6e05a458a7d7900740f501685d3d8ade1ad`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs` (read)
- env: `USERNAME`, `USERPROFILE`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn sandbox_dir(codex_home: &Path) -> PathBuf {`
- `pub fn sandbox_secrets_dir(codex_home: &Path) -> PathBuf {`
- `pub fn setup_marker_path(codex_home: &Path) -> PathBuf {`
- `pub fn sandbox_users_path(codex_home: &Path) -> PathBuf {`
- `pub fn run_setup_refresh(`
- `pub struct SetupMarker {`
- `pub fn version_matches(&self) -> bool {`
- `pub struct SandboxUserRecord {`
- `pub struct SandboxUsersFile {`
- `pub fn version_matches(&self) -> bool {`
- `pub fn run_elevated_setup(`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:1` `use serde::Deserialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:2` `use serde::Serialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:3` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:4` `use std::collections::HashSet;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:5` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:6` `use std::os::windows::process::CommandExt;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:7` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:9` `use std::process::Command;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:10` `use std::process::Stdio;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:12` `use crate::allow::compute_allow_paths;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:13` `use crate::allow::AllowDenyPaths;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:14` `use crate::logging::log_note;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:15` `use crate::policy::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:16` `use crate::setup_error::clear_setup_error_report;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:17` `use crate::setup_error::failure;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:18` `use crate::setup_error::read_setup_error_report;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:19` `use crate::setup_error::SetupErrorCode;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:20` `use crate::setup_error::SetupFailure;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:21` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:22` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:23` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:24` `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:25` `use base64::Engine;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:27` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:28` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:29` `use windows_sys::Win32::Security::AllocateAndInitializeSid;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:30` `use windows_sys::Win32::Security::CheckTokenMembership;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:31` `use windows_sys::Win32::Security::FreeSid;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:32` `use windows_sys::Win32::Security::SECURITY_NT_AUTHORITY;`
- `const` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:34` `pub const SETUP_VERSION: u32 = 5;`
- `const` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:35` `pub const OFFLINE_USERNAME: &str = "CodexSandboxOffline";`
- `const` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:36` `pub const ONLINE_USERNAME: &str = "CodexSandboxOnline";`
- `const` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:37` `const ERROR_CANCELLED: u32 = 1223;`
- `const` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:38` `const SECURITY_BUILTIN_DOMAIN_RID: u32 = 0x0000_0020;`
- `const` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:39` `const DOMAIN_ALIAS_RID_ADMINS: u32 = 0x0000_0220;`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:41` `pub fn sandbox_dir(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:45` `pub fn sandbox_secrets_dir(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:49` `pub fn setup_marker_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:53` `pub fn sandbox_users_path(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:57` `pub fn run_setup_refresh(`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:127` `pub struct SetupMarker {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:135` `impl SetupMarker {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:136` `pub fn version_matches(&self) -> bool {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:142` `pub struct SandboxUserRecord {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:149` `pub struct SandboxUsersFile {`
- `impl` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:155` `impl SandboxUsersFile {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:156` `pub fn version_matches(&self) -> bool {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:161` `fn is_elevated() -> Result<bool> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:193` `fn canonical_existing(paths: &[PathBuf]) -> Vec<PathBuf> {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:257` `struct ElevationPayload {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:269` `fn quote_arg(arg: &str) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:305` `fn find_setup_exe() -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:317` `fn report_helper_failure(`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:336` `fn run_setup_exe(`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:341` `use windows_sys::Win32::System::Threading::GetExitCodeProcess;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:342` `use windows_sys::Win32::System::Threading::WaitForSingleObject;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:343` `use windows_sys::Win32::System::Threading::INFINITE;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:344` `use windows_sys::Win32::UI::Shell::ShellExecuteExW;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:345` `use windows_sys::Win32::UI::Shell::SEE_MASK_NOCLOSEPROCESS;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:346` `use windows_sys::Win32::UI::Shell::SHELLEXECUTEINFOW;`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:447` `pub fn run_elevated_setup(`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:492` `fn build_payload_roots(`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_orchestrator.rs:517` `fn filter_sensitive_write_roots(mut roots: Vec<PathBuf>, codex_home: &Path) -> Vec<PathBuf> {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::collections::HashMap;`
- `use std::collections::HashSet;`
- `use std::ffi::c_void;`
- `use std::os::windows::process::CommandExt;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Command;`
- `use std::process::Stdio;`
- `use crate::allow::compute_allow_paths;`
- `use crate::allow::AllowDenyPaths;`
- `use crate::logging::log_note;`
- `use crate::policy::SandboxPolicy;`
- `use crate::setup_error::clear_setup_error_report;`
- `use crate::setup_error::failure;`
- `use crate::setup_error::read_setup_error_report;`
- `use crate::setup_error::SetupErrorCode;`
- `use crate::setup_error::SetupFailure;`
- `use anyhow::anyhow;`
### Referenced env vars
- `USERNAME`
- `USERPROFILE`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
