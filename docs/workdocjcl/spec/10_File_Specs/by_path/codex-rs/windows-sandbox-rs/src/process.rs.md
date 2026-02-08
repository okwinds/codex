# `codex-rs/windows-sandbox-rs/src/process.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5098`
- sha256: `c1fe0ac29ff3153b0fd10a1c6b4249fb3351d45b8e0236592db02d989f2f3821`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/process.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn make_env_block(env: &HashMap<String, String>) -> Vec<u16> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:1` `use crate::logging;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:2` `use crate::winutil::format_last_error;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:3` `use crate::winutil::quote_windows_arg;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:4` `use crate::winutil::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:5` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:6` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:7` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:8` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:9` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:10` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:11` `use windows_sys::Win32::Foundation::SetHandleInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:12` `use windows_sys::Win32::Foundation::HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:13` `use windows_sys::Win32::Foundation::HANDLE_FLAG_INHERIT;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:14` `use windows_sys::Win32::Foundation::INVALID_HANDLE_VALUE;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:15` `use windows_sys::Win32::System::Console::GetStdHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:16` `use windows_sys::Win32::System::Console::STD_ERROR_HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:17` `use windows_sys::Win32::System::Console::STD_INPUT_HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:18` `use windows_sys::Win32::System::Console::STD_OUTPUT_HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:19` `use windows_sys::Win32::System::Threading::CreateProcessAsUserW;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:20` `use windows_sys::Win32::System::Threading::CREATE_UNICODE_ENVIRONMENT;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:21` `use windows_sys::Win32::System::Threading::PROCESS_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:22` `use windows_sys::Win32::System::Threading::STARTF_USESTDHANDLES;`
- `use` `codex-rs/windows-sandbox-rs/src/process.rs:23` `use windows_sys::Win32::System::Threading::STARTUPINFOW;`
- `fn` `codex-rs/windows-sandbox-rs/src/process.rs:25` `pub fn make_env_block(env: &HashMap<String, String>) -> Vec<u16> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::logging;`
- `use crate::winutil::format_last_error;`
- `use crate::winutil::quote_windows_arg;`
- `use crate::winutil::to_wide;`
- `use anyhow::anyhow;`
- `use anyhow::Result;`
- `use std::collections::HashMap;`
- `use std::ffi::c_void;`
- `use std::path::Path;`
- `use windows_sys::Win32::Foundation::GetLastError;`
- `use windows_sys::Win32::Foundation::SetHandleInformation;`
- `use windows_sys::Win32::Foundation::HANDLE;`
- `use windows_sys::Win32::Foundation::HANDLE_FLAG_INHERIT;`
- `use windows_sys::Win32::Foundation::INVALID_HANDLE_VALUE;`
- `use windows_sys::Win32::System::Console::GetStdHandle;`
- `use windows_sys::Win32::System::Console::STD_ERROR_HANDLE;`
- `use windows_sys::Win32::System::Console::STD_INPUT_HANDLE;`
- `use windows_sys::Win32::System::Console::STD_OUTPUT_HANDLE;`
- `use windows_sys::Win32::System::Threading::CreateProcessAsUserW;`
- `use windows_sys::Win32::System::Threading::CREATE_UNICODE_ENVIRONMENT;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
