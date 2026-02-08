# `codex-rs/windows-sandbox-rs/src/elevated_impl.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `20182`
- sha256: `8a1c8c3390ea1149801cd412dfc708e9307046c4aa1fc00ede4bf3692ac5c964`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/elevated_impl.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn run_windows_sandbox_capture(`
- `pub struct CaptureResult {`
- `pub fn run_windows_sandbox_capture(`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:2` `use crate::acl::allow_null_device;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:3` `use crate::allow::compute_allow_paths;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:4` `use crate::allow::AllowDenyPaths;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:5` `use crate::cap::load_or_create_cap_sids;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:6` `use crate::env::ensure_non_interactive_pager;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:7` `use crate::env::inherit_path_env;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:8` `use crate::env::normalize_null_device_env;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:9` `use crate::identity::require_logon_sandbox_creds;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:10` `use crate::logging::log_failure;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:11` `use crate::logging::log_note;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:12` `use crate::logging::log_start;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:13` `use crate::logging::log_success;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:14` `use crate::policy::parse_policy;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:15` `use crate::policy::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:16` `use crate::token::convert_string_sid_to_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:17` `use crate::winutil::quote_windows_arg;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:18` `use crate::winutil::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:19` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:20` `use rand::rngs::SmallRng;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:21` `use rand::Rng;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:22` `use rand::SeedableRng;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:23` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:24` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:25` `use std::fs;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:26` `use std::io;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:27` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:28` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:29` `use std::ptr;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:30` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:31` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:32` `use windows_sys::Win32::Foundation::HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:33` `use windows_sys::Win32::Security::Authorization::ConvertStringSecurityDescriptorToSecurityDescriptorW;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:34` `use windows_sys::Win32::Security::PSECURITY_DESCRIPTOR;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:35` `use windows_sys::Win32::Security::SECURITY_ATTRIBUTES;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:36` `use windows_sys::Win32::System::Diagnostics::Debug::SetErrorMode;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:37` `use windows_sys::Win32::System::Pipes::ConnectNamedPipe;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:38` `use windows_sys::Win32::System::Pipes::CreateNamedPipeW;`
- `const` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:40` `const PIPE_ACCESS_DUPLEX: u32 = 0x0000_0003;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:41` `use windows_sys::Win32::System::Pipes::PIPE_READMODE_BYTE;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:42` `use windows_sys::Win32::System::Pipes::PIPE_TYPE_BYTE;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:43` `use windows_sys::Win32::System::Pipes::PIPE_WAIT;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:44` `use windows_sys::Win32::System::Threading::CreateProcessWithLogonW;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:45` `use windows_sys::Win32::System::Threading::GetExitCodeProcess;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:46` `use windows_sys::Win32::System::Threading::WaitForSingleObject;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:47` `use windows_sys::Win32::System::Threading::INFINITE;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:48` `use windows_sys::Win32::System::Threading::LOGON_WITH_PROFILE;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:49` `use windows_sys::Win32::System::Threading::PROCESS_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:50` `use windows_sys::Win32::System::Threading::STARTUPINFOW;`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:54` `fn find_git_root(start: &Path) -> Option<PathBuf> {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:84` `fn ensure_codex_home_exists(p: &Path) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:92` `fn inject_git_safe_directory(`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:114` `fn find_runner_exe() -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:127` `fn pipe_name(suffix: &str) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:133` `fn create_named_pipe(name: &str, access: u32) -> io::Result<HANDLE> {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:177` `fn connect_pipe(h: HANDLE) -> io::Result<()> {`
- `const` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:181` `const ERROR_PIPE_CONNECTED: u32 = 535;`
- `struct` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:192` `struct RunnerPayload {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:211` `pub fn run_windows_sandbox_capture(`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:464` `use crate::policy::SandboxPolicy;`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:466` `fn workspace_policy(network_access: bool) -> SandboxPolicy {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:476` `fn applies_network_block_when_access_is_disabled() {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:481` `fn skips_network_block_when_access_is_allowed() {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:486` `fn applies_network_block_for_read_only() {`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:497` `use anyhow::bail;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:498` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:499` `use codex_protocol::protocol::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:500` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:501` `use std::path::Path;`
- `struct` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:504` `pub struct CaptureResult {`
- `fn` `codex-rs/windows-sandbox-rs/src/elevated_impl.rs:512` `pub fn run_windows_sandbox_capture(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::acl::allow_null_device;`
- `use crate::allow::compute_allow_paths;`
- `use crate::allow::AllowDenyPaths;`
- `use crate::cap::load_or_create_cap_sids;`
- `use crate::env::ensure_non_interactive_pager;`
- `use crate::env::inherit_path_env;`
- `use crate::env::normalize_null_device_env;`
- `use crate::identity::require_logon_sandbox_creds;`
- `use crate::logging::log_failure;`
- `use crate::logging::log_note;`
- `use crate::logging::log_start;`
- `use crate::logging::log_success;`
- `use crate::policy::parse_policy;`
- `use crate::policy::SandboxPolicy;`
- `use crate::token::convert_string_sid_to_sid;`
- `use crate::winutil::quote_windows_arg;`
- `use crate::winutil::to_wide;`
- `use anyhow::Result;`
- `use rand::rngs::SmallRng;`
- `use rand::Rng;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
