# `codex-rs/windows-sandbox-rs/src/setup_main_win.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `28834`
- sha256: `e4bca0537768fe80c569873355f60ff48bc7ce7584b8ef29c23ac3fbc50acef5`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/setup_main_win.rs` (read)
- env: `CODEX_HOME`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn main() -> Result<()> {`

## Definitions (auto, per-file)
- `mod` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:3` `mod firewall;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:5` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:6` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:7` `use base64::engine::general_purpose::STANDARD as BASE64;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:8` `use base64::Engine;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:9` `use codex_windows_sandbox::canonicalize_path;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:10` `use codex_windows_sandbox::convert_string_sid_to_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:11` `use codex_windows_sandbox::ensure_allow_mask_aces_with_inheritance;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:12` `use codex_windows_sandbox::ensure_allow_write_aces;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:13` `use codex_windows_sandbox::extract_setup_failure;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:14` `use codex_windows_sandbox::hide_newly_created_users;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:15` `use codex_windows_sandbox::is_command_cwd_root;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:16` `use codex_windows_sandbox::load_or_create_cap_sids;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:17` `use codex_windows_sandbox::log_note;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:18` `use codex_windows_sandbox::path_mask_allows;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:19` `use codex_windows_sandbox::protect_workspace_codex_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:20` `use codex_windows_sandbox::sandbox_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:21` `use codex_windows_sandbox::sandbox_secrets_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:22` `use codex_windows_sandbox::string_from_sid_bytes;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:23` `use codex_windows_sandbox::to_wide;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:24` `use codex_windows_sandbox::workspace_cap_sid_for_cwd;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:25` `use codex_windows_sandbox::write_setup_error_report;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:26` `use codex_windows_sandbox::SetupErrorCode;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:27` `use codex_windows_sandbox::SetupErrorReport;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:28` `use codex_windows_sandbox::SetupFailure;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:29` `use codex_windows_sandbox::LOG_FILE_NAME;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:30` `use codex_windows_sandbox::SETUP_VERSION;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:31` `use serde::Deserialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:32` `use serde::Serialize;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:33` `use std::collections::HashSet;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:34` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:35` `use std::ffi::OsStr;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:36` `use std::fs::File;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:37` `use std::io::Write;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:38` `use std::os::windows::process::CommandExt;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:39` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:40` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:41` `use std::process::Command;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:42` `use std::process::Stdio;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:43` `use std::sync::mpsc;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:44` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:45` `use windows_sys::Win32::Foundation::LocalFree;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:46` `use windows_sys::Win32::Foundation::HLOCAL;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:47` `use windows_sys::Win32::Security::Authorization::ConvertStringSidToSidW;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:48` `use windows_sys::Win32::Security::Authorization::SetEntriesInAclW;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:49` `use windows_sys::Win32::Security::Authorization::SetNamedSecurityInfoW;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:50` `use windows_sys::Win32::Security::Authorization::EXPLICIT_ACCESS_W;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:51` `use windows_sys::Win32::Security::Authorization::GRANT_ACCESS;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:52` `use windows_sys::Win32::Security::Authorization::SE_FILE_OBJECT;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:53` `use windows_sys::Win32::Security::Authorization::TRUSTEE_IS_SID;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:54` `use windows_sys::Win32::Security::Authorization::TRUSTEE_W;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:55` `use windows_sys::Win32::Security::ACL;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:56` `use windows_sys::Win32::Security::CONTAINER_INHERIT_ACE;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:57` `use windows_sys::Win32::Security::DACL_SECURITY_INFORMATION;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:58` `use windows_sys::Win32::Security::OBJECT_INHERIT_ACE;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:59` `use windows_sys::Win32::Storage::FileSystem::DELETE;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:60` `use windows_sys::Win32::Storage::FileSystem::FILE_DELETE_CHILD;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:61` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_EXECUTE;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:62` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_READ;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:63` `use windows_sys::Win32::Storage::FileSystem::FILE_GENERIC_WRITE;`
- `const` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:65` `const DENY_ACCESS: i32 = 3;`
- `mod` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:67` `mod read_acl_mutex;`
- `mod` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:68` `mod sandbox_users;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:69` `use read_acl_mutex::acquire_read_acl_mutex;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:70` `use read_acl_mutex::read_acl_mutex_exists;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:71` `use sandbox_users::provision_sandbox_users;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:72` `use sandbox_users::resolve_sandbox_users_group_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:73` `use sandbox_users::resolve_sid;`
- `use` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:74` `use sandbox_users::sid_bytes_to_psid;`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:77` `struct Payload {`
- `enum` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:94` `enum SetupMode {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:100` `fn log_line(log: &mut File, msg: &str) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:111` `fn spawn_read_acl_helper(payload: &Payload, _log: &mut File) -> Result<()> {`
- `struct` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:129` `struct ReadAclSubjects<'a> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:134` `fn apply_read_acls(`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:207` `fn read_mask_allows_or_log(`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:242` `fn lock_sandbox_dir(`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:343` `pub fn main() -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:364` `fn real_main() -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:439` `fn run_setup(payload: &Payload, log: &mut File, sbx_dir: &Path) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:446` `fn run_read_acl_only(payload: &Payload, log: &mut File) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/setup_main_win.rs:505` `fn run_setup_full(payload: &Payload, log: &mut File, sbx_dir: &Path) -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use base64::engine::general_purpose::STANDARD as BASE64;`
- `use base64::Engine;`
- `use codex_windows_sandbox::canonicalize_path;`
- `use codex_windows_sandbox::convert_string_sid_to_sid;`
- `use codex_windows_sandbox::ensure_allow_mask_aces_with_inheritance;`
- `use codex_windows_sandbox::ensure_allow_write_aces;`
- `use codex_windows_sandbox::extract_setup_failure;`
- `use codex_windows_sandbox::hide_newly_created_users;`
- `use codex_windows_sandbox::is_command_cwd_root;`
- `use codex_windows_sandbox::load_or_create_cap_sids;`
- `use codex_windows_sandbox::log_note;`
- `use codex_windows_sandbox::path_mask_allows;`
- `use codex_windows_sandbox::protect_workspace_codex_dir;`
- `use codex_windows_sandbox::sandbox_dir;`
- `use codex_windows_sandbox::sandbox_secrets_dir;`
- `use codex_windows_sandbox::string_from_sid_bytes;`
- `use codex_windows_sandbox::to_wide;`
- `use codex_windows_sandbox::workspace_cap_sid_for_cwd;`
### Referenced env vars
- `CODEX_HOME`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
