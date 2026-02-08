# `codex-rs/windows-sandbox-rs/src/acl.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `21933`
- sha256: `1f4079d866a9e9aada62871420ed4e60518459a426add9276a2039e235c6494f`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/acl.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn path_mask_allows(`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:1` `use crate::winutil::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:2` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:3` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:4` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:5` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:6` `use windows_sys::Win32::Foundation::CloseHandle;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:7` `use windows_sys::Win32::Foundation::LocalFree;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:8` `use windows_sys::Win32::Foundation::ERROR_SUCCESS;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:9` `use windows_sys::Win32::Foundation::HLOCAL;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:10` `use windows_sys::Win32::Foundation::INVALID_HANDLE_VALUE;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:11` `use windows_sys::Win32::Security::AclSizeInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:12` `use windows_sys::Win32::Security::Authorization::GetNamedSecurityInfoW;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:13` `use windows_sys::Win32::Security::Authorization::GetSecurityInfo;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:14` `use windows_sys::Win32::Security::Authorization::SetEntriesInAclW;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:15` `use windows_sys::Win32::Security::Authorization::SetNamedSecurityInfoW;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:16` `use windows_sys::Win32::Security::Authorization::SetSecurityInfo;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:17` `use windows_sys::Win32::Security::Authorization::EXPLICIT_ACCESS_W;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:18` `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_SID;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:19` `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_UNKNOWN;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:20` `use windows_sys::Win32::Security::Authorization::TRUSTEE_W;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:21` `use windows_sys::Win32::Security::EqualSid;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:22` `use windows_sys::Win32::Security::GetAce;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:23` `use windows_sys::Win32::Security::GetAclInformation;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:24` `use windows_sys::Win32::Security::MapGenericMask;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:25` `use windows_sys::Win32::Security::ACCESS_ALLOWED_ACE;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:26` `use windows_sys::Win32::Security::ACE_HEADER;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:27` `use windows_sys::Win32::Security::ACL;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:28` `use windows_sys::Win32::Security::ACL_SIZE_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:29` `use windows_sys::Win32::Security::DACL_SECURITY_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:30` `use windows_sys::Win32::Security::GENERIC_MAPPING;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:31` `use windows_sys::Win32::Storage::FileSystem::CreateFileW;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:32` `use windows_sys::Win32::Storage::FileSystem::FILE_ALL_ACCESS;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:33` `use windows_sys::Win32::Storage::FileSystem::FILE_APPEND_DATA;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:34` `use windows_sys::Win32::Storage::FileSystem::FILE_ATTRIBUTE_NORMAL;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:35` `use windows_sys::Win32::Storage::FileSystem::FILE_FLAG_BACKUP_SEMANTICS;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:36` `use windows_sys::Win32::Storage::FileSystem::FILE_DELETE_CHILD;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:37` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_EXECUTE;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:38` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_READ;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:39` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_WRITE;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:40` `use windows_sys::Win32::Storage::FileSystem::FILE_SHARE_DELETE;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:41` `use windows_sys::Win32::Storage::FileSystem::FILE_SHARE_READ;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:42` `use windows_sys::Win32::Storage::FileSystem::FILE_SHARE_WRITE;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:43` `use windows_sys::Win32::Storage::FileSystem::FILE_WRITE_ATTRIBUTES;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:44` `use windows_sys::Win32::Storage::FileSystem::FILE_WRITE_DATA;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:45` `use windows_sys::Win32::Storage::FileSystem::FILE_WRITE_EA;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:46` `use windows_sys::Win32::Storage::FileSystem::OPEN_EXISTING;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:47` `use windows_sys::Win32::Storage::FileSystem::READ_CONTROL;`
- `use` `codex-rs/windows-sandbox-rs/src/acl.rs:48` `use windows_sys::Win32::Storage::FileSystem::DELETE;`
- `const` `codex-rs/windows-sandbox-rs/src/acl.rs:49` `const SE_KERNEL_OBJECT: u32 = 6;`
- `const` `codex-rs/windows-sandbox-rs/src/acl.rs:50` `const INHERIT_ONLY_ACE: u8 = 0x08;`
- `const` `codex-rs/windows-sandbox-rs/src/acl.rs:51` `const GENERIC_WRITE_MASK: u32 = 0x4000_0000;`
- `const` `codex-rs/windows-sandbox-rs/src/acl.rs:52` `const DENY_ACCESS: i32 = 3;`
- `fn` `codex-rs/windows-sandbox-rs/src/acl.rs:160` `pub fn path_mask_allows(`
- `const` `codex-rs/windows-sandbox-rs/src/acl.rs:262` `const WRITE_ALLOW_MASK: u32 = FILE_GENERIC_READ`
- `const` `codex-rs/windows-sandbox-rs/src/acl.rs:632` `const CONTAINER_INHERIT_ACE: u32 = 0x2;`
- `const` `codex-rs/windows-sandbox-rs/src/acl.rs:633` `const OBJECT_INHERIT_ACE: u32 = 0x1;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::winutil::to_wide;`
- `use anyhow::anyhow;`
- `use anyhow::Result;`
- `use std::ffi::c_void;`
- `use std::path::Path;`
- `use windows_sys::Win32::Foundation::CloseHandle;`
- `use windows_sys::Win32::Foundation::LocalFree;`
- `use windows_sys::Win32::Foundation::ERROR_SUCCESS;`
- `use windows_sys::Win32::Foundation::HLOCAL;`
- `use windows_sys::Win32::Foundation::INVALID_HANDLE_VALUE;`
- `use windows_sys::Win32::Security::AclSizeInformation;`
- `use windows_sys::Win32::Security::Authorization::GetNamedSecurityInfoW;`
- `use windows_sys::Win32::Security::Authorization::GetSecurityInfo;`
- `use windows_sys::Win32::Security::Authorization::SetEntriesInAclW;`
- `use windows_sys::Win32::Security::Authorization::SetNamedSecurityInfoW;`
- `use windows_sys::Win32::Security::Authorization::SetSecurityInfo;`
- `use windows_sys::Win32::Security::Authorization::EXPLICIT_ACCESS_W;`
- `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_SID;`
- `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_UNKNOWN;`
- `use windows_sys::Win32::Security::Authorization::TRUSTEE_W;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
