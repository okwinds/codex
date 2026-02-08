# `codex-rs/windows-sandbox-rs/src/command_runner_win.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10672`
- sha256: `3c14f4f547778081ad4439b6ffc1d32bcd046fd74932b4bba4cd3d94223d22d8`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/command_runner_win.rs` (read)

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn main() -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:3` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:4` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:5` `use codex_windows_sandbox::allow_null_device;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:6` `use codex_windows_sandbox::convert_string_sid_to_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:7` `use codex_windows_sandbox::create_process_as_user;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:8` `use codex_windows_sandbox::create_readonly_token_with_caps_from;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:9` `use codex_windows_sandbox::create_workspace_write_token_with_caps_from;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:10` `use codex_windows_sandbox::get_current_token_for_restriction;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:11` `use codex_windows_sandbox::hide_current_user_profile_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:12` `use codex_windows_sandbox::log_note;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:13` `use codex_windows_sandbox::parse_policy;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:14` `use codex_windows_sandbox::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:15` `use codex_windows_sandbox::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:16` `use serde::Deserialize;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:17` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:18` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:19` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:20` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:21` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:22` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:23` `use windows_sys::Win32::Foundation::LocalFree;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:24` `use windows_sys::Win32::Foundation::HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:25` `use windows_sys::Win32::Foundation::HLOCAL;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:26` `use windows_sys::Win32::Storage::FileSystem::CreateFileW;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:27` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_READ;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:28` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_WRITE;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:29` `use windows_sys::Win32::Storage::FileSystem::OPEN_EXISTING;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:30` `use windows_sys::Win32::System::JobObjects::AssignProcessToJobObject;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:31` `use windows_sys::Win32::System::JobObjects::CreateJobObjectW;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:32` `use windows_sys::Win32::System::JobObjects::JobObjectExtendedLimitInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:33` `use windows_sys::Win32::System::JobObjects::SetInformationJobObject;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:34` `use windows_sys::Win32::System::JobObjects::JOBOBJECT_EXTENDED_LIMIT_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:35` `use windows_sys::Win32::System::JobObjects::JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:36` `use windows_sys::Win32::System::Threading::TerminateProcess;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:37` `use windows_sys::Win32::System::Threading::WaitForSingleObject;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:38` `use windows_sys::Win32::System::Threading::INFINITE;`
- `mod` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:41` `mod cwd_junction;`
- `mod` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:44` `mod read_acl_mutex;`
- `struct` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:47` `struct RunnerRequest {`
- `const` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:63` `const WAIT_TIMEOUT: u32 = 0x0000_0102;`
- `fn` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:84` `fn read_request_file(req_path: &Path) -> Result<String> {`
- `fn` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:91` `pub fn main() -> Result<()> {`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:297` `use super::read_request_file;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:298` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:299` `use std::fs;`
- `fn` `codex-rs/windows-sandbox-rs/src/command_runner_win.rs:302` `fn removes_request_file_after_read() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_windows_sandbox::allow_null_device;`
- `use codex_windows_sandbox::convert_string_sid_to_sid;`
- `use codex_windows_sandbox::create_process_as_user;`
- `use codex_windows_sandbox::create_readonly_token_with_caps_from;`
- `use codex_windows_sandbox::create_workspace_write_token_with_caps_from;`
- `use codex_windows_sandbox::get_current_token_for_restriction;`
- `use codex_windows_sandbox::hide_current_user_profile_dir;`
- `use codex_windows_sandbox::log_note;`
- `use codex_windows_sandbox::parse_policy;`
- `use codex_windows_sandbox::to_wide;`
- `use codex_windows_sandbox::SandboxPolicy;`
- `use serde::Deserialize;`
- `use std::collections::HashMap;`
- `use std::ffi::c_void;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use windows_sys::Win32::Foundation::CloseHandle;`
- `use windows_sys::Win32::Foundation::GetLastError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
