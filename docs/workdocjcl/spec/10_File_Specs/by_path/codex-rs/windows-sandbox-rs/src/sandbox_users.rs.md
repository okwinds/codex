# `codex-rs/windows-sandbox-rs/src/sandbox_users.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `16687`
- sha256: `43beb861fad2630285238a54c3110a70d14c8c2bf150771c1aae7b94e5f70668`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/sandbox_users.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn ensure_sandbox_users_group(log: &mut File) -> Result<()> {`
- `pub fn resolve_sandbox_users_group_sid() -> Result<Vec<u8>> {`
- `pub fn provision_sandbox_users(`
- `pub fn ensure_sandbox_user(username: &str, password: &str, log: &mut File) -> Result<()> {`
- `pub fn ensure_local_user(name: &str, password: &str, log: &mut File) -> Result<()> {`
- `pub fn ensure_local_group(name: &str, comment: &str, log: &mut File) -> Result<()> {`
- `pub fn ensure_local_group_member(group_name: &str, member_name: &str) -> Result<()> {`
- `pub fn resolve_sid(name: &str) -> Result<Vec<u8>> {`
- `pub fn sid_bytes_to_psid(sid: &[u8]) -> Result<*mut c_void> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:3` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:4` `use base64::engine::general_purpose::STANDARD as BASE64;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:5` `use base64::Engine;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:6` `use rand::rngs::SmallRng;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:7` `use rand::RngCore;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:8` `use rand::SeedableRng;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:9` `use serde::Serialize;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:10` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:11` `use std::ffi::OsStr;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:12` `use std::fs::File;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:13` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:14` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:15` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:16` `use windows_sys::Win32::Foundation::LocalFree;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:17` `use windows_sys::Win32::Foundation::ERROR_INSUFFICIENT_BUFFER;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:18` `use windows_sys::Win32::NetworkManagement::NetManagement::NERR_Success;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:19` `use windows_sys::Win32::NetworkManagement::NetManagement::NetLocalGroupAdd;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:20` `use windows_sys::Win32::NetworkManagement::NetManagement::NetLocalGroupAddMembers;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:21` `use windows_sys::Win32::NetworkManagement::NetManagement::NetUserAdd;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:22` `use windows_sys::Win32::NetworkManagement::NetManagement::NetUserSetInfo;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:23` `use windows_sys::Win32::NetworkManagement::NetManagement::LOCALGROUP_INFO_1;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:24` `use windows_sys::Win32::NetworkManagement::NetManagement::LOCALGROUP_MEMBERS_INFO_3;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:25` `use windows_sys::Win32::NetworkManagement::NetManagement::UF_DONT_EXPIRE_PASSWD;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:26` `use windows_sys::Win32::NetworkManagement::NetManagement::UF_SCRIPT;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:27` `use windows_sys::Win32::NetworkManagement::NetManagement::USER_INFO_1;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:28` `use windows_sys::Win32::NetworkManagement::NetManagement::USER_INFO_1003;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:29` `use windows_sys::Win32::NetworkManagement::NetManagement::USER_PRIV_USER;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:30` `use windows_sys::Win32::Security::Authorization::ConvertStringSidToSidW;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:31` `use windows_sys::Win32::Security::CopySid;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:32` `use windows_sys::Win32::Security::GetLengthSid;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:33` `use windows_sys::Win32::Security::LookupAccountNameW;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:34` `use windows_sys::Win32::Security::LookupAccountSidW;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:35` `use windows_sys::Win32::Security::SID_NAME_USE;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:37` `use codex_windows_sandbox::dpapi_protect;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:38` `use codex_windows_sandbox::sandbox_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:39` `use codex_windows_sandbox::sandbox_secrets_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:40` `use codex_windows_sandbox::string_from_sid_bytes;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:41` `use codex_windows_sandbox::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:42` `use codex_windows_sandbox::SetupErrorCode;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:43` `use codex_windows_sandbox::SetupFailure;`
- `use` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:44` `use codex_windows_sandbox::SETUP_VERSION;`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:46` `pub const SANDBOX_USERS_GROUP: &str = "CodexSandboxUsers";`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:47` `const SANDBOX_USERS_GROUP_COMMENT: &str = "Codex sandbox internal group (managed)";`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:48` `const SID_ADMINISTRATORS: &str = "S-1-5-32-544";`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:49` `const SID_USERS: &str = "S-1-5-32-545";`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:50` `const SID_AUTHENTICATED_USERS: &str = "S-1-5-11";`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:51` `const SID_EVERYONE: &str = "S-1-1-0";`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:52` `const SID_SYSTEM: &str = "S-1-5-18";`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:54` `pub fn ensure_sandbox_users_group(log: &mut File) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:58` `pub fn resolve_sandbox_users_group_sid() -> Result<Vec<u8>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:62` `pub fn provision_sandbox_users(`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:87` `pub fn ensure_sandbox_user(username: &str, password: &str, log: &mut File) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:93` `pub fn ensure_local_user(name: &str, password: &str, log: &mut File) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:157` `pub fn ensure_local_group(name: &str, comment: &str, log: &mut File) -> Result<()> {`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:158` `const ERROR_ALIAS_EXISTS: u32 = 1379;`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:159` `const NERR_GROUP_EXISTS: u32 = 2223;`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:189` `pub fn ensure_local_group_member(group_name: &str, member_name: &str) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:209` `pub fn resolve_sid(name: &str) -> Result<Vec<u8>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:247` `fn well_known_sid_str(name: &str) -> Option<&'static str> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:258` `fn sid_bytes_from_string(sid_str: &str) -> Result<Vec<u8>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:285` `fn lookup_account_name_for_sid(sid_str: &str) -> Result<String> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:345` `pub fn sid_bytes_to_psid(sid: &[u8]) -> Result<*mut c_void> {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:358` `fn random_password() -> String {`
- `const` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:359` `const CHARS: &[u8] =`
- `struct` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:373` `struct SandboxUserRecord {`
- `struct` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:379` `struct SandboxUsersFile {`
- `struct` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:386` `struct SetupMarker {`
- `fn` `codex-rs/windows-sandbox-rs/src/sandbox_users.rs:395` `fn write_secrets(`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use base64::engine::general_purpose::STANDARD as BASE64;`
- `use base64::Engine;`
- `use rand::rngs::SmallRng;`
- `use rand::RngCore;`
- `use rand::SeedableRng;`
- `use serde::Serialize;`
- `use std::ffi::c_void;`
- `use std::ffi::OsStr;`
- `use std::fs::File;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use windows_sys::Win32::Foundation::GetLastError;`
- `use windows_sys::Win32::Foundation::LocalFree;`
- `use windows_sys::Win32::Foundation::ERROR_INSUFFICIENT_BUFFER;`
- `use windows_sys::Win32::NetworkManagement::NetManagement::NERR_Success;`
- `use windows_sys::Win32::NetworkManagement::NetManagement::NetLocalGroupAdd;`
- `use windows_sys::Win32::NetworkManagement::NetManagement::NetLocalGroupAddMembers;`
- `use windows_sys::Win32::NetworkManagement::NetManagement::NetUserAdd;`
- `use windows_sys::Win32::NetworkManagement::NetManagement::NetUserSetInfo;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
