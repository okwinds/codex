# `codex-rs/windows-sandbox-rs/src/identity.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6283`
- sha256: `70576733de0b50ff575552cf5537c8d87f10a5b88b3a874063417a087c493738`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/identity.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct SandboxCreds {`
- `pub fn sandbox_setup_is_complete(codex_home: &Path) -> bool {`
- `pub fn require_logon_sandbox_creds(`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:1` `use crate::dpapi;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:2` `use crate::logging::debug_log;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:3` `use crate::policy::SandboxPolicy;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:4` `use crate::setup::gather_read_roots;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:5` `use crate::setup::gather_write_roots;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:6` `use crate::setup::run_elevated_setup;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:7` `use crate::setup::sandbox_users_path;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:8` `use crate::setup::setup_marker_path;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:9` `use crate::setup::SandboxUserRecord;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:10` `use crate::setup::SandboxUsersFile;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:11` `use crate::setup::SetupMarker;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:12` `use anyhow::anyhow;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:13` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:14` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:15` `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:16` `use base64::Engine;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:17` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:18` `use std::fs;`
- `use` `codex-rs/windows-sandbox-rs/src/identity.rs:19` `use std::path::Path;`
- `struct` `codex-rs/windows-sandbox-rs/src/identity.rs:22` `struct SandboxIdentity {`
- `struct` `codex-rs/windows-sandbox-rs/src/identity.rs:28` `pub struct SandboxCreds {`
- `fn` `codex-rs/windows-sandbox-rs/src/identity.rs:37` `pub fn sandbox_setup_is_complete(codex_home: &Path) -> bool {`
- `fn` `codex-rs/windows-sandbox-rs/src/identity.rs:45` `fn load_marker(codex_home: &Path) -> Result<Option<SetupMarker>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/identity.rs:70` `fn load_users(codex_home: &Path) -> Result<Option<SandboxUsersFile>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/identity.rs:95` `fn decode_password(record: &SandboxUserRecord) -> Result<String> {`
- `fn` `codex-rs/windows-sandbox-rs/src/identity.rs:104` `fn select_identity(policy: &SandboxPolicy, codex_home: &Path) -> Result<Option<SandboxIdentity>> {`
- `fn` `codex-rs/windows-sandbox-rs/src/identity.rs:125` `pub fn require_logon_sandbox_creds(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::dpapi;`
- `use crate::logging::debug_log;`
- `use crate::policy::SandboxPolicy;`
- `use crate::setup::gather_read_roots;`
- `use crate::setup::gather_write_roots;`
- `use crate::setup::run_elevated_setup;`
- `use crate::setup::sandbox_users_path;`
- `use crate::setup::setup_marker_path;`
- `use crate::setup::SandboxUserRecord;`
- `use crate::setup::SandboxUsersFile;`
- `use crate::setup::SetupMarker;`
- `use anyhow::anyhow;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use base64::engine::general_purpose::STANDARD as BASE64_STANDARD;`
- `use base64::Engine;`
- `use std::collections::HashMap;`
- `use std::fs;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
