# `codex-rs/windows-sandbox-rs/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `20460`
- sha256: `390d923c6c035ccaec49b3f2608547d3af4115f4472e436ace253128a487e7a7`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct CaptureResult {`
- `pub fn run_windows_sandbox_capture(`
- `pub struct CaptureResult {`
- `pub fn run_windows_sandbox_capture(`
- `pub fn apply_world_writable_scan_and_denies(`

## Definitions (auto, per-file)
- `mod` `codex-rs/windows-sandbox-rs/src/lib.rs:27` `mod setup;`
- `mod` `codex-rs/windows-sandbox-rs/src/lib.rs:30` `mod elevated_impl;`
- `mod` `codex-rs/windows-sandbox-rs/src/lib.rs:33` `mod setup_error;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:137` `use super::acl::add_allow_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:138` `use super::acl::add_deny_write_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:139` `use super::acl::allow_null_device;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:140` `use super::acl::revoke_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:141` `use super::allow::compute_allow_paths;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:142` `use super::allow::AllowDenyPaths;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:143` `use super::cap::load_or_create_cap_sids;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:144` `use super::cap::workspace_cap_sid_for_cwd;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:145` `use super::env::apply_no_network_to_env;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:146` `use super::env::ensure_non_interactive_pager;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:147` `use super::env::normalize_null_device_env;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:148` `use super::logging::debug_log;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:149` `use super::logging::log_failure;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:150` `use super::logging::log_start;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:151` `use super::logging::log_success;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:152` `use super::path_normalization::canonicalize_path;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:153` `use super::policy::parse_policy;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:154` `use super::policy::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:155` `use super::process::make_env_block;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:156` `use super::token::convert_string_sid_to_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:157` `use super::token::create_workspace_write_token_with_caps_from;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:158` `use super::winutil::format_last_error;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:159` `use super::winutil::quote_windows_arg;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:160` `use super::winutil::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:161` `use super::workspace_acl::is_command_cwd_root;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:162` `use super::workspace_acl::protect_workspace_codex_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:163` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:164` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:165` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:166` `use std::io;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:167` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:168` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:169` `use std::ptr;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:170` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:171` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:172` `use windows_sys::Win32::Foundation::SetHandleInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:173` `use windows_sys::Win32::Foundation::HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:174` `use windows_sys::Win32::Foundation::HANDLE_FLAG_INHERIT;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:175` `use windows_sys::Win32::System::Pipes::CreatePipe;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:176` `use windows_sys::Win32::System::Threading::CreateProcessAsUserW;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:177` `use windows_sys::Win32::System::Threading::GetExitCodeProcess;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:178` `use windows_sys::Win32::System::Threading::WaitForSingleObject;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:179` `use windows_sys::Win32::System::Threading::CREATE_UNICODE_ENVIRONMENT;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:180` `use windows_sys::Win32::System::Threading::INFINITE;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:181` `use windows_sys::Win32::System::Threading::PROCESS_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:182` `use windows_sys::Win32::System::Threading::STARTF_USESTDHANDLES;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:183` `use windows_sys::Win32::System::Threading::STARTUPINFOW;`
- `type` `codex-rs/windows-sandbox-rs/src/lib.rs:185` `type PipeHandles = ((HANDLE, HANDLE), (HANDLE, HANDLE), (HANDLE, HANDLE));`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:187` `fn should_apply_network_block(policy: &SandboxPolicy) -> bool {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:191` `fn ensure_codex_home_exists(p: &Path) -> Result<()> {`
- `struct` `codex-rs/windows-sandbox-rs/src/lib.rs:224` `pub struct CaptureResult {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:231` `pub fn run_windows_sandbox_capture(`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:507` `use super::should_apply_network_block;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:508` `use crate::policy::SandboxPolicy;`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:510` `fn workspace_policy(network_access: bool) -> SandboxPolicy {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:520` `fn applies_network_block_when_access_is_disabled() {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:525` `fn skips_network_block_when_access_is_allowed() {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:530` `fn applies_network_block_for_read_only() {`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:538` `use anyhow::bail;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:539` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:540` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:541` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:542` `use std::path::Path;`
- `struct` `codex-rs/windows-sandbox-rs/src/lib.rs:545` `pub struct CaptureResult {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:552` `pub fn run_windows_sandbox_capture(`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:564` `pub fn apply_world_writable_scan_and_denies(`

## Dependencies (auto sample)
### Imports / Includes
- `use super::acl::add_allow_ace;`
- `use super::acl::add_deny_write_ace;`
- `use super::acl::allow_null_device;`
- `use super::acl::revoke_ace;`
- `use super::allow::compute_allow_paths;`
- `use super::allow::AllowDenyPaths;`
- `use super::cap::load_or_create_cap_sids;`
- `use super::cap::workspace_cap_sid_for_cwd;`
- `use super::env::apply_no_network_to_env;`
- `use super::env::ensure_non_interactive_pager;`
- `use super::env::normalize_null_device_env;`
- `use super::logging::debug_log;`
- `use super::logging::log_failure;`
- `use super::logging::log_start;`
- `use super::logging::log_success;`
- `use super::path_normalization::canonicalize_path;`
- `use super::policy::parse_policy;`
- `use super::policy::SandboxPolicy;`
- `use super::process::make_env_block;`
- `use super::token::convert_string_sid_to_sid;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
