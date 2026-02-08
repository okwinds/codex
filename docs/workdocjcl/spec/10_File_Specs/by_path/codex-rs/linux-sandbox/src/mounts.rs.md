# `codex-rs/linux-sandbox/src/mounts.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11877`
- sha256: `155b411b5fed91d06245b43927498e7e9ccf0a5e45b9d48bcb7d59138afc8a71`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/src/mounts.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/linux-sandbox/src/mounts.rs:3` `use std::ffi::CString;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:4` `use std::os::unix::ffi::OsStrExt;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:5` `use std::path::Path;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:7` `use codex_core::error::CodexErr;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:8` `use codex_core::error::Result;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:9` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:10` `use codex_core::protocol::WritableRoot;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:11` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:52` `fn collect_read_only_mount_targets(`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:84` `fn is_git_pointer_file(path: &AbsolutePathBuf) -> bool {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:89` `fn resolve_gitdir_from_file(dot_git: &AbsolutePathBuf) -> Result<AbsolutePathBuf> {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:123` `fn unshare_mount_namespace() -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:132` `fn unshare_user_and_mount_namespaces() -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:140` `fn is_running_as_root() -> bool {`
- `struct` `codex-rs/linux-sandbox/src/mounts.rs:145` `struct CapUserHeader {`
- `struct` `codex-rs/linux-sandbox/src/mounts.rs:151` `struct CapUserData {`
- `const` `codex-rs/linux-sandbox/src/mounts.rs:157` `const LINUX_CAPABILITY_VERSION_3: u32 = 0x2008_0522;`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:160` `fn write_user_namespace_maps(uid: libc::uid_t, gid: libc::gid_t) -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:169` `fn drop_caps() -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:196` `fn write_proc_file(path: &str, contents: impl AsRef<[u8]>) -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:202` `fn make_mounts_private() -> Result<()> {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:222` `fn bind_mount_read_only(path: &Path) -> Result<()> {`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:261` `use super::*;`
- `use` `codex-rs/linux-sandbox/src/mounts.rs:262` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:265` `fn collect_read_only_mount_targets_errors_on_missing_path() {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:291` `fn collect_read_only_mount_targets_adds_gitdir_for_pointer_file() {`
- `fn` `codex-rs/linux-sandbox/src/mounts.rs:313` `fn collect_read_only_mount_targets_errors_on_invalid_gitdir_pointer() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::CString;`
- `use std::os::unix::ffi::OsStrExt;`
- `use std::path::Path;`
- `use codex_core::error::CodexErr;`
- `use codex_core::error::Result;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::WritableRoot;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
