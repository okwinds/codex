# `codex-rs/windows-sandbox-rs/src/hide_users.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5320`
- sha256: `531e042fa8e3b0cb686fe28375ab50457b52eeee6190754224297218d089e8e0`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/hide_users.rs` (read)
- env: `USERPROFILE`

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn hide_newly_created_users(usernames: &[String], log_base: &Path) {`
- `pub fn hide_current_user_profile_dir(log_base: &Path) {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:3` `use crate::logging::log_note;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:4` `use crate::winutil::format_last_error;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:5` `use crate::winutil::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:6` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:7` `use std::ffi::OsStr;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:8` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:9` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:10` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:11` `use windows_sys::Win32::Storage::FileSystem::GetFileAttributesW;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:12` `use windows_sys::Win32::Storage::FileSystem::SetFileAttributesW;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:13` `use windows_sys::Win32::Storage::FileSystem::FILE_ATTRIBUTE_HIDDEN;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:14` `use windows_sys::Win32::Storage::FileSystem::FILE_ATTRIBUTE_SYSTEM;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:15` `use windows_sys::Win32::Storage::FileSystem::INVALID_FILE_ATTRIBUTES;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:16` `use windows_sys::Win32::System::Registry::RegCloseKey;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:17` `use windows_sys::Win32::System::Registry::RegCreateKeyExW;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:18` `use windows_sys::Win32::System::Registry::RegSetValueExW;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:19` `use windows_sys::Win32::System::Registry::HKEY;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:20` `use windows_sys::Win32::System::Registry::HKEY_LOCAL_MACHINE;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:21` `use windows_sys::Win32::System::Registry::KEY_WRITE;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:22` `use windows_sys::Win32::System::Registry::REG_DWORD;`
- `use` `codex-rs/windows-sandbox-rs/src/hide_users.rs:23` `use windows_sys::Win32::System::Registry::REG_OPTION_NON_VOLATILE;`
- `const` `codex-rs/windows-sandbox-rs/src/hide_users.rs:25` `const USERLIST_KEY_PATH: &str =`
- `fn` `codex-rs/windows-sandbox-rs/src/hide_users.rs:28` `pub fn hide_newly_created_users(usernames: &[String], log_base: &Path) {`
- `fn` `codex-rs/windows-sandbox-rs/src/hide_users.rs:45` `pub fn hide_current_user_profile_dir(log_base: &Path) {`
- `fn` `codex-rs/windows-sandbox-rs/src/hide_users.rs:78` `fn hide_users_in_winlogon(usernames: &[String], log_base: &Path) -> anyhow::Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/hide_users.rs:109` `fn create_userlist_key() -> anyhow::Result<HKEY> {`
- `fn` `codex-rs/windows-sandbox-rs/src/hide_users.rs:135` `fn hide_directory(path: &Path) -> anyhow::Result<bool> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::logging::log_note;`
- `use crate::winutil::format_last_error;`
- `use crate::winutil::to_wide;`
- `use anyhow::anyhow;`
- `use std::ffi::OsStr;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use windows_sys::Win32::Foundation::GetLastError;`
- `use windows_sys::Win32::Storage::FileSystem::GetFileAttributesW;`
- `use windows_sys::Win32::Storage::FileSystem::SetFileAttributesW;`
- `use windows_sys::Win32::Storage::FileSystem::FILE_ATTRIBUTE_HIDDEN;`
- `use windows_sys::Win32::Storage::FileSystem::FILE_ATTRIBUTE_SYSTEM;`
- `use windows_sys::Win32::Storage::FileSystem::INVALID_FILE_ATTRIBUTES;`
- `use windows_sys::Win32::System::Registry::RegCloseKey;`
- `use windows_sys::Win32::System::Registry::RegCreateKeyExW;`
- `use windows_sys::Win32::System::Registry::RegSetValueExW;`
- `use windows_sys::Win32::System::Registry::HKEY;`
- `use windows_sys::Win32::System::Registry::HKEY_LOCAL_MACHINE;`
- `use windows_sys::Win32::System::Registry::KEY_WRITE;`
- `use windows_sys::Win32::System::Registry::REG_DWORD;`
### Referenced env vars
- `USERPROFILE`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
