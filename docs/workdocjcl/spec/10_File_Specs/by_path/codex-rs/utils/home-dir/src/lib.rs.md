# `codex-rs/utils/home-dir/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4647`
- sha256: `aeb597cf611176fe584aaf7f5a3a94d3921311fb0aa14a40d18d53010731a75e`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/home-dir/src/lib.rs` (read)
- env: `CODEX_HOME`

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn find_codex_home() -> std::io::Result<PathBuf> {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/home-dir/src/lib.rs:1` `use dirs::home_dir;`
- `use` `codex-rs/utils/home-dir/src/lib.rs:2` `use std::path::PathBuf;`
- `fn` `codex-rs/utils/home-dir/src/lib.rs:12` `pub fn find_codex_home() -> std::io::Result<PathBuf> {`
- `fn` `codex-rs/utils/home-dir/src/lib.rs:19` `fn find_codex_home_from_env(codex_home_env: Option<&str>) -> std::io::Result<PathBuf> {`
- `use` `codex-rs/utils/home-dir/src/lib.rs:65` `use super::find_codex_home_from_env;`
- `use` `codex-rs/utils/home-dir/src/lib.rs:66` `use dirs::home_dir;`
- `use` `codex-rs/utils/home-dir/src/lib.rs:67` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/utils/home-dir/src/lib.rs:68` `use std::fs;`
- `use` `codex-rs/utils/home-dir/src/lib.rs:69` `use std::io::ErrorKind;`
- `use` `codex-rs/utils/home-dir/src/lib.rs:70` `use tempfile::TempDir;`
- `fn` `codex-rs/utils/home-dir/src/lib.rs:73` `fn find_codex_home_env_missing_path_is_fatal() {`
- `fn` `codex-rs/utils/home-dir/src/lib.rs:89` `fn find_codex_home_env_file_path_is_fatal() {`
- `fn` `codex-rs/utils/home-dir/src/lib.rs:106` `fn find_codex_home_env_valid_directory_canonicalizes() {`
- `fn` `codex-rs/utils/home-dir/src/lib.rs:122` `fn find_codex_home_without_env_uses_default_home_dir() {`

## Dependencies (auto sample)
### Imports / Includes
- `use dirs::home_dir;`
- `use std::path::PathBuf;`
- `use super::find_codex_home_from_env;`
- `use dirs::home_dir;`
- `use pretty_assertions::assert_eq;`
- `use std::fs;`
- `use std::io::ErrorKind;`
- `use tempfile::TempDir;`
### Referenced env vars
- `CODEX_HOME`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
