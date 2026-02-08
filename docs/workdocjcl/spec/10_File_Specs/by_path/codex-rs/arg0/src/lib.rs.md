# `codex-rs/arg0/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12081`
- sha256: `54ec1bdb3bca752250e0fdb77acb5ea70d97837c7f0eae953f729def3df1daae`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/arg0/src/lib.rs` (read)
- env: `PATH`

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct Arg0PathEntryGuard {`
- `pub fn arg0_dispatch() -> Option<Arg0PathEntryGuard> {`
- `pub fn prepend_path_entry_for_codex_aliases() -> std::io::Result<Arg0PathEntryGuard> {`

## Definitions (auto, per-file)
- `use` `codex-rs/arg0/src/lib.rs:1` `use std::fs::File;`
- `use` `codex-rs/arg0/src/lib.rs:2` `use std::future::Future;`
- `use` `codex-rs/arg0/src/lib.rs:3` `use std::path::Path;`
- `use` `codex-rs/arg0/src/lib.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/arg0/src/lib.rs:6` `use codex_core::CODEX_APPLY_PATCH_ARG1;`
- `use` `codex-rs/arg0/src/lib.rs:8` `use std::os::unix::fs::symlink;`
- `use` `codex-rs/arg0/src/lib.rs:9` `use tempfile::TempDir;`
- `const` `codex-rs/arg0/src/lib.rs:11` `const LINUX_SANDBOX_ARG0: &str = "codex-linux-sandbox";`
- `const` `codex-rs/arg0/src/lib.rs:12` `const APPLY_PATCH_ARG0: &str = "apply_patch";`
- `const` `codex-rs/arg0/src/lib.rs:13` `const MISSPELLED_APPLY_PATCH_ARG0: &str = "applypatch";`
- `const` `codex-rs/arg0/src/lib.rs:14` `const LOCK_FILENAME: &str = ".lock";`
- `struct` `codex-rs/arg0/src/lib.rs:17` `pub struct Arg0PathEntryGuard {`
- `impl` `codex-rs/arg0/src/lib.rs:22` `impl Arg0PathEntryGuard {`
- `fn` `codex-rs/arg0/src/lib.rs:23` `fn new(temp_dir: TempDir, lock_file: File) -> Self {`
- `fn` `codex-rs/arg0/src/lib.rs:31` `pub fn arg0_dispatch() -> Option<Arg0PathEntryGuard> {`
- `const` `codex-rs/arg0/src/lib.rs:127` `const ILLEGAL_ENV_VAR_PREFIX: &str = "CODEX_";`
- `fn` `codex-rs/arg0/src/lib.rs:133` `fn load_dotenv() {`
- `fn` `codex-rs/arg0/src/lib.rs:169` `pub fn prepend_path_entry_for_codex_aliases() -> std::io::Result<Arg0PathEntryGuard> {`
- `use` `codex-rs/arg0/src/lib.rs:191` `use std::os::unix::fs::PermissionsExt;`
- `const` `codex-rs/arg0/src/lib.rs:246` `const PATH_SEPARATOR: &str = ":";`
- `const` `codex-rs/arg0/src/lib.rs:249` `const PATH_SEPARATOR: &str = ";";`
- `fn` `codex-rs/arg0/src/lib.rs:268` `fn janitor_cleanup(temp_root: &Path) -> std::io::Result<()> {`
- `fn` `codex-rs/arg0/src/lib.rs:297` `fn try_lock_dir(dir: &Path) -> std::io::Result<Option<File>> {`
- `use` `codex-rs/arg0/src/lib.rs:314` `use super::LOCK_FILENAME;`
- `use` `codex-rs/arg0/src/lib.rs:315` `use super::janitor_cleanup;`
- `use` `codex-rs/arg0/src/lib.rs:316` `use std::fs;`
- `use` `codex-rs/arg0/src/lib.rs:317` `use std::fs::File;`
- `use` `codex-rs/arg0/src/lib.rs:318` `use std::path::Path;`
- `fn` `codex-rs/arg0/src/lib.rs:320` `fn create_lock(dir: &Path) -> std::io::Result<File> {`
- `fn` `codex-rs/arg0/src/lib.rs:331` `fn janitor_skips_dirs_without_lock_file() -> std::io::Result<()> {`
- `fn` `codex-rs/arg0/src/lib.rs:343` `fn janitor_skips_dirs_with_held_lock() -> std::io::Result<()> {`
- `fn` `codex-rs/arg0/src/lib.rs:357` `fn janitor_removes_dirs_with_unlocked_lock() -> std::io::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::File;`
- `use std::future::Future;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_core::CODEX_APPLY_PATCH_ARG1;`
- `use std::os::unix::fs::symlink;`
- `use tempfile::TempDir;`
- `use std::os::unix::fs::PermissionsExt;`
- `use super::LOCK_FILENAME;`
- `use super::janitor_cleanup;`
- `use std::fs;`
- `use std::fs::File;`
- `use std::path::Path;`
### Referenced env vars
- `PATH`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
