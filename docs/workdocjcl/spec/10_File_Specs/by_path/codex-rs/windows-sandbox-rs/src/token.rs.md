# `codex-rs/windows-sandbox-rs/src/token.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13093`
- sha256: `eb74f7e8e9c6379459ce19e98fa03c7509d15af98813863b1157f4fa89df8562`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/token.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:1` `use crate::winutil::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:2` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:3` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:4` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:5` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:6` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:7` `use windows_sys::Win32::Foundation::LocalFree;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:8` `use windows_sys::Win32::Foundation::ERROR_SUCCESS;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:9` `use windows_sys::Win32::Foundation::HANDLE;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:10` `use windows_sys::Win32::Foundation::HLOCAL;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:11` `use windows_sys::Win32::Foundation::LUID;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:12` `use windows_sys::Win32::Security::AdjustTokenPrivileges;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:13` `use windows_sys::Win32::Security::Authorization::SetEntriesInAclW;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:14` `use windows_sys::Win32::Security::Authorization::EXPLICIT_ACCESS_W;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:15` `use windows_sys::Win32::Security::Authorization::GRANT_ACCESS;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:16` `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_SID;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:17` `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_UNKNOWN;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:18` `use windows_sys::Win32::Security::Authorization::TRUSTEE_W;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:19` `use windows_sys::Win32::Security::CopySid;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:20` `use windows_sys::Win32::Security::CreateRestrictedToken;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:21` `use windows_sys::Win32::Security::CreateWellKnownSid;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:22` `use windows_sys::Win32::Security::GetLengthSid;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:23` `use windows_sys::Win32::Security::GetTokenInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:24` `use windows_sys::Win32::Security::LookupPrivilegeValueW;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:25` `use windows_sys::Win32::Security::SetTokenInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:27` `use windows_sys::Win32::Security::TokenDefaultDacl;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:28` `use windows_sys::Win32::Security::TokenGroups;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:29` `use windows_sys::Win32::Security::ACL;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:30` `use windows_sys::Win32::Security::SID_AND_ATTRIBUTES;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:31` `use windows_sys::Win32::Security::TOKEN_ADJUST_DEFAULT;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:32` `use windows_sys::Win32::Security::TOKEN_ADJUST_PRIVILEGES;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:33` `use windows_sys::Win32::Security::TOKEN_ADJUST_SESSIONID;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:34` `use windows_sys::Win32::Security::TOKEN_ASSIGN_PRIMARY;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:35` `use windows_sys::Win32::Security::TOKEN_DUPLICATE;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:36` `use windows_sys::Win32::Security::TOKEN_PRIVILEGES;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:37` `use windows_sys::Win32::Security::TOKEN_QUERY;`
- `use` `codex-rs/windows-sandbox-rs/src/token.rs:38` `use windows_sys::Win32::System::Threading::GetCurrentProcess;`
- `const` `codex-rs/windows-sandbox-rs/src/token.rs:40` `const DISABLE_MAX_PRIVILEGE: u32 = 0x01;`
- `const` `codex-rs/windows-sandbox-rs/src/token.rs:41` `const LUA_TOKEN: u32 = 0x04;`
- `const` `codex-rs/windows-sandbox-rs/src/token.rs:42` `const WRITE_RESTRICTED: u32 = 0x08;`
- `const` `codex-rs/windows-sandbox-rs/src/token.rs:43` `const GENERIC_ALL: u32 = 0x1000_0000;`
- `const` `codex-rs/windows-sandbox-rs/src/token.rs:44` `const WIN_WORLD_SID: i32 = 1;`
- `const` `codex-rs/windows-sandbox-rs/src/token.rs:45` `const SE_GROUP_LOGON_ID: u32 = 0xC0000000;`
- `struct` `codex-rs/windows-sandbox-rs/src/token.rs:48` `struct TokenDefaultDaclInfo {`
- `fn` `codex-rs/windows-sandbox-rs/src/token.rs:134` `fn ConvertStringSidToSidW(StringSid: *const u16, Sid: *mut *mut c_void) -> i32;`
- `fn` `codex-rs/windows-sandbox-rs/src/token.rs:157` `fn OpenProcessToken(`
- `struct` `codex-rs/windows-sandbox-rs/src/token.rs:218` `struct TOKEN_LINKED_TOKEN {`
- `const` `codex-rs/windows-sandbox-rs/src/token.rs:221` `const TOKEN_LINKED_TOKEN_CLASS: i32 = 19; // TokenLinkedToken`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::winutil::to_wide;`
- `use anyhow::anyhow;`
- `use anyhow::Result;`
- `use std::ffi::c_void;`
- `use windows_sys::Win32::Foundation::CloseHandle;`
- `use windows_sys::Win32::Foundation::GetLastError;`
- `use windows_sys::Win32::Foundation::LocalFree;`
- `use windows_sys::Win32::Foundation::ERROR_SUCCESS;`
- `use windows_sys::Win32::Foundation::HANDLE;`
- `use windows_sys::Win32::Foundation::HLOCAL;`
- `use windows_sys::Win32::Foundation::LUID;`
- `use windows_sys::Win32::Security::AdjustTokenPrivileges;`
- `use windows_sys::Win32::Security::Authorization::SetEntriesInAclW;`
- `use windows_sys::Win32::Security::Authorization::EXPLICIT_ACCESS_W;`
- `use windows_sys::Win32::Security::Authorization::GRANT_ACCESS;`
- `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_SID;`
- `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_UNKNOWN;`
- `use windows_sys::Win32::Security::Authorization::TRUSTEE_W;`
- `use windows_sys::Win32::Security::CopySid;`
- `use windows_sys::Win32::Security::CreateRestrictedToken;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
