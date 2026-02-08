# `codex-rs/arg0/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8338`
- sha256: `27d793285aa40e08267db37029b42df5823d016ab600a897ab82902ef2d47d25`
- generated_utc: `2026-02-03T16:08:28Z`

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
- `pub fn arg0_dispatch() -> Option<TempDir> {`
- `pub fn prepend_path_entry_for_codex_aliases() -> std::io::Result<TempDir> {`

## Definitions (auto, per-file)
- `use` `codex-rs/arg0/src/lib.rs:1` `use std::future::Future;`
- `use` `codex-rs/arg0/src/lib.rs:2` `use std::path::Path;`
- `use` `codex-rs/arg0/src/lib.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/arg0/src/lib.rs:5` `use codex_core::CODEX_APPLY_PATCH_ARG1;`
- `use` `codex-rs/arg0/src/lib.rs:7` `use std::os::unix::fs::symlink;`
- `use` `codex-rs/arg0/src/lib.rs:8` `use tempfile::TempDir;`
- `const` `codex-rs/arg0/src/lib.rs:10` `const LINUX_SANDBOX_ARG0: &str = "codex-linux-sandbox";`
- `const` `codex-rs/arg0/src/lib.rs:11` `const APPLY_PATCH_ARG0: &str = "apply_patch";`
- `const` `codex-rs/arg0/src/lib.rs:12` `const MISSPELLED_APPLY_PATCH_ARG0: &str = "applypatch";`
- `fn` `codex-rs/arg0/src/lib.rs:14` `pub fn arg0_dispatch() -> Option<TempDir> {`
- `const` `codex-rs/arg0/src/lib.rs:110` `const ILLEGAL_ENV_VAR_PREFIX: &str = "CODEX_";`
- `fn` `codex-rs/arg0/src/lib.rs:116` `fn load_dotenv() {`
- `fn` `codex-rs/arg0/src/lib.rs:152` `pub fn prepend_path_entry_for_codex_aliases() -> std::io::Result<TempDir> {`
- `use` `codex-rs/arg0/src/lib.rs:174` `use std::os::unix::fs::PermissionsExt;`
- `const` `codex-rs/arg0/src/lib.rs:215` `const PATH_SEPARATOR: &str = ":";`
- `const` `codex-rs/arg0/src/lib.rs:218` `const PATH_SEPARATOR: &str = ";";`

## Dependencies (auto sample)
### Imports / Includes
- `use std::future::Future;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_core::CODEX_APPLY_PATCH_ARG1;`
- `use std::os::unix::fs::symlink;`
- `use tempfile::TempDir;`
- `use std::os::unix::fs::PermissionsExt;`
### Referenced env vars
- `PATH`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
