# `codex-rs/windows-sandbox-rs/src/dpapi.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2739`
- sha256: `df9aa858bf330cc5245ba34cf26062055879c1b703828453e3ff0ca101ec77fc`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/dpapi.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn protect(data: &[u8]) -> Result<Vec<u8>> {`
- `pub fn unprotect(blob: &[u8]) -> Result<Vec<u8>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:1` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:2` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:3` `use windows_sys::Win32::Foundation::GetLastError;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:4` `use windows_sys::Win32::Foundation::LocalFree;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:5` `use windows_sys::Win32::Foundation::HLOCAL;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:6` `use windows_sys::Win32::Security::Cryptography::CryptProtectData;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:7` `use windows_sys::Win32::Security::Cryptography::CryptUnprotectData;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:8` `use windows_sys::Win32::Security::Cryptography::CRYPTPROTECT_LOCAL_MACHINE;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:9` `use windows_sys::Win32::Security::Cryptography::CRYPTPROTECT_UI_FORBIDDEN;`
- `use` `codex-rs/windows-sandbox-rs/src/dpapi.rs:10` `use windows_sys::Win32::Security::Cryptography::CRYPT_INTEGER_BLOB;`
- `fn` `codex-rs/windows-sandbox-rs/src/dpapi.rs:12` `fn make_blob(data: &[u8]) -> CRYPT_INTEGER_BLOB {`
- `fn` `codex-rs/windows-sandbox-rs/src/dpapi.rs:20` `pub fn protect(data: &[u8]) -> Result<Vec<u8>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/dpapi.rs:54` `pub fn unprotect(blob: &[u8]) -> Result<Vec<u8>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::anyhow;`
- `use anyhow::Result;`
- `use windows_sys::Win32::Foundation::GetLastError;`
- `use windows_sys::Win32::Foundation::LocalFree;`
- `use windows_sys::Win32::Foundation::HLOCAL;`
- `use windows_sys::Win32::Security::Cryptography::CryptProtectData;`
- `use windows_sys::Win32::Security::Cryptography::CryptUnprotectData;`
- `use windows_sys::Win32::Security::Cryptography::CRYPTPROTECT_LOCAL_MACHINE;`
- `use windows_sys::Win32::Security::Cryptography::CRYPTPROTECT_UI_FORBIDDEN;`
- `use windows_sys::Win32::Security::Cryptography::CRYPT_INTEGER_BLOB;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
