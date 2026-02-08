# `codex-rs/windows-sandbox-rs/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `18593`
- sha256: `4f2efe6c6330094f1f0957f5340cb0cc1d89c76037d4b417dd8c6702c48ab44e`
- generated_utc: `2026-02-03T16:08:31Z`

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
- `mod` `codex-rs/windows-sandbox-rs/src/lib.rs:14` `mod setup;`
- `mod` `codex-rs/windows-sandbox-rs/src/lib.rs:17` `mod elevated_impl;`
- `mod` `codex-rs/windows-sandbox-rs/src/lib.rs:20` `mod setup_error;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:112` `use super::acl::add_allow_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:113` `use super::acl::add_deny_write_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:114` `use super::acl::allow_null_device;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:115` `use super::acl::revoke_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:116` `use super::allow::compute_allow_paths;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:117` `use super::allow::AllowDenyPaths;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:118` `use super::cap::load_or_create_cap_sids;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:119` `use super::env::apply_no_network_to_env;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:120` `use super::env::ensure_non_interactive_pager;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:121` `use super::env::normalize_null_device_env;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:122` `use super::logging::debug_log;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:123` `use super::logging::log_failure;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:124` `use super::logging::log_start;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:125` `use super::logging::log_success;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:126` `use super::policy::parse_policy;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:127` `use super::policy::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:128` `use super::process::make_env_block;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:129` `use super::token::convert_string_sid_to_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:130` `use super::winutil::format_last_error;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:131` `use super::winutil::quote_windows_arg;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:132` `use super::winutil::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:133` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:134` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:135` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:136` `use std::io;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:137` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:138` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:139` `use std::ptr;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:140` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:141` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:142` `use windows_sys::Win32::Foundation::SetHandleInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:143` `use windows_sys::Win32::Foundation::HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:144` `use windows_sys::Win32::Foundation::HANDLE_FLAG_INHERIT;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:145` `use windows_sys::Win32::System::Pipes::CreatePipe;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:146` `use windows_sys::Win32::System::Threading::CreateProcessAsUserW;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:147` `use windows_sys::Win32::System::Threading::GetExitCodeProcess;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:148` `use windows_sys::Win32::System::Threading::WaitForSingleObject;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:149` `use windows_sys::Win32::System::Threading::CREATE_UNICODE_ENVIRONMENT;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:150` `use windows_sys::Win32::System::Threading::INFINITE;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:151` `use windows_sys::Win32::System::Threading::PROCESS_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:152` `use windows_sys::Win32::System::Threading::STARTF_USESTDHANDLES;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:153` `use windows_sys::Win32::System::Threading::STARTUPINFOW;`
- `type` `codex-rs/windows-sandbox-rs/src/lib.rs:155` `type PipeHandles = ((HANDLE, HANDLE), (HANDLE, HANDLE), (HANDLE, HANDLE));`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:157` `fn should_apply_network_block(policy: &SandboxPolicy) -> bool {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:161` `fn ensure_codex_home_exists(p: &Path) -> Result<()> {`
- `struct` `codex-rs/windows-sandbox-rs/src/lib.rs:194` `pub struct CaptureResult {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:201` `pub fn run_windows_sandbox_capture(`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:457` `use super::should_apply_network_block;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:458` `use crate::policy::SandboxPolicy;`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:460` `fn workspace_policy(network_access: bool) -> SandboxPolicy {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:470` `fn applies_network_block_when_access_is_disabled() {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:475` `fn skips_network_block_when_access_is_allowed() {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:480` `fn applies_network_block_for_read_only() {`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:488` `use anyhow::bail;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:489` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:490` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:491` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/lib.rs:492` `use std::path::Path;`
- `struct` `codex-rs/windows-sandbox-rs/src/lib.rs:495` `pub struct CaptureResult {`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:502` `pub fn run_windows_sandbox_capture(`
- `fn` `codex-rs/windows-sandbox-rs/src/lib.rs:514` `pub fn apply_world_writable_scan_and_denies(`

## Dependencies (auto sample)
### Imports / Includes
- `use super::acl::add_allow_ace;`
- `use super::acl::add_deny_write_ace;`
- `use super::acl::allow_null_device;`
- `use super::acl::revoke_ace;`
- `use super::allow::compute_allow_paths;`
- `use super::allow::AllowDenyPaths;`
- `use super::cap::load_or_create_cap_sids;`
- `use super::env::apply_no_network_to_env;`
- `use super::env::ensure_non_interactive_pager;`
- `use super::env::normalize_null_device_env;`
- `use super::logging::debug_log;`
- `use super::logging::log_failure;`
- `use super::logging::log_start;`
- `use super::logging::log_success;`
- `use super::policy::parse_policy;`
- `use super::policy::SandboxPolicy;`
- `use super::process::make_env_block;`
- `use super::token::convert_string_sid_to_sid;`
- `use super::winutil::format_last_error;`
- `use super::winutil::quote_windows_arg;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
