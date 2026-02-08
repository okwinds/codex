# `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1879`
- sha256: `33ed3043cecc13d58cb18e744b8bf41d3fcb3308a1e4b68d6ac573d2d1e16a9d`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ReadAclMutexGuard {`
- `pub fn read_acl_mutex_exists() -> Result<bool> {`
- `pub fn acquire_read_acl_mutex() -> Result<Option<ReadAclMutexGuard>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:1` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:2` `use std::ffi::OsStr;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:3` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:4` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:5` `use windows_sys::Win32::Foundation::ERROR_ALREADY_EXISTS;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:6` `use windows_sys::Win32::Foundation::ERROR_FILE_NOT_FOUND;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:7` `use windows_sys::Win32::Foundation::HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:8` `use windows_sys::Win32::System::Threading::CreateMutexW;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:9` `use windows_sys::Win32::System::Threading::OpenMutexW;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:10` `use windows_sys::Win32::System::Threading::ReleaseMutex;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:11` `use windows_sys::Win32::System::Threading::MUTEX_ALL_ACCESS;`
- `use` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:13` `use super::to_wide;`
- `const` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:15` `const READ_ACL_MUTEX_NAME: &str = "Local\\CodexSandboxReadAcl";`
- `struct` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:17` `pub struct ReadAclMutexGuard {`
- `impl` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:21` `impl Drop for ReadAclMutexGuard {`
- `fn` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:22` `fn drop(&mut self) {`
- `fn` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:30` `pub fn read_acl_mutex_exists() -> Result<bool> {`
- `fn` `codex-rs/windows-sandbox-rs/src/read_acl_mutex.rs:46` `pub fn acquire_read_acl_mutex() -> Result<Option<ReadAclMutexGuard>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use std::ffi::OsStr;`
- `use windows_sys::Win32::Foundation::CloseHandle;`
- `use windows_sys::Win32::Foundation::GetLastError;`
- `use windows_sys::Win32::Foundation::ERROR_ALREADY_EXISTS;`
- `use windows_sys::Win32::Foundation::ERROR_FILE_NOT_FOUND;`
- `use windows_sys::Win32::Foundation::HANDLE;`
- `use windows_sys::Win32::System::Threading::CreateMutexW;`
- `use windows_sys::Win32::System::Threading::OpenMutexW;`
- `use windows_sys::Win32::System::Threading::ReleaseMutex;`
- `use windows_sys::Win32::System::Threading::MUTEX_ALL_ACCESS;`
- `use super::to_wide;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
