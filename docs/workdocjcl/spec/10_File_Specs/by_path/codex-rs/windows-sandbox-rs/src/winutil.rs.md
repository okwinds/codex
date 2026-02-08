# `codex-rs/windows-sandbox-rs/src/winutil.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3662`
- sha256: `ee7c1143e5c6c441936d0df1d0ead576c8e99deb7073082cb2742c9922226976`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/winutil.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn quote_windows_arg(arg: &str) -> String {`
- `pub fn format_last_error(err: i32) -> String {`
- `pub fn string_from_sid_bytes(sid: &[u8]) -> Result<String, String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:1` `use std::ffi::OsStr;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:2` `use std::os::windows::ffi::OsStrExt;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:3` `use windows_sys::Win32::Foundation::LocalFree;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:4` `use windows_sys::Win32::Foundation::HLOCAL;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:5` `use windows_sys::Win32::System::Diagnostics::Debug::FormatMessageW;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:6` `use windows_sys::Win32::System::Diagnostics::Debug::FORMAT_MESSAGE_ALLOCATE_BUFFER;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:7` `use windows_sys::Win32::System::Diagnostics::Debug::FORMAT_MESSAGE_FROM_SYSTEM;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:8` `use windows_sys::Win32::System::Diagnostics::Debug::FORMAT_MESSAGE_IGNORE_INSERTS;`
- `use` `codex-rs/windows-sandbox-rs/src/winutil.rs:9` `use windows_sys::Win32::Security::Authorization::ConvertSidToStringSidW;`
- `fn` `codex-rs/windows-sandbox-rs/src/winutil.rs:21` `pub fn quote_windows_arg(arg: &str) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/winutil.rs:60` `pub fn format_last_error(err: i32) -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/winutil.rs:88` `pub fn string_from_sid_bytes(sid: &[u8]) -> Result<String, String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsStr;`
- `use std::os::windows::ffi::OsStrExt;`
- `use windows_sys::Win32::Foundation::LocalFree;`
- `use windows_sys::Win32::Foundation::HLOCAL;`
- `use windows_sys::Win32::System::Diagnostics::Debug::FormatMessageW;`
- `use windows_sys::Win32::System::Diagnostics::Debug::FORMAT_MESSAGE_ALLOCATE_BUFFER;`
- `use windows_sys::Win32::System::Diagnostics::Debug::FORMAT_MESSAGE_FROM_SYSTEM;`
- `use windows_sys::Win32::System::Diagnostics::Debug::FORMAT_MESSAGE_IGNORE_INSERTS;`
- `use windows_sys::Win32::Security::Authorization::ConvertSidToStringSidW;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
