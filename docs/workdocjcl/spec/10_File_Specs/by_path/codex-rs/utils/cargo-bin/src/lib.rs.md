# `codex-rs/utils/cargo-bin/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7763`
- sha256: `fec28c3a7545d9079f328335bc14eef17fb541719d4e93042311517ee1ede984`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/cargo-bin/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum CargoBinError {`
- `pub fn cargo_bin(name: &str) -> Result<PathBuf, CargoBinError> {`
- `pub fn runfiles_available() -> bool {`
- `pub fn resolve_bazel_runfile(`
- `pub fn resolve_cargo_runfile(resource: &Path) -> std::io::Result<PathBuf> {`
- `pub fn repo_root() -> io::Result<PathBuf> {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/cargo-bin/src/lib.rs:1` `use std::ffi::OsString;`
- `use` `codex-rs/utils/cargo-bin/src/lib.rs:2` `use std::io;`
- `use` `codex-rs/utils/cargo-bin/src/lib.rs:3` `use std::path::Path;`
- `use` `codex-rs/utils/cargo-bin/src/lib.rs:4` `use std::path::PathBuf;`
- `const` `codex-rs/utils/cargo-bin/src/lib.rs:9` `const RUNFILES_MANIFEST_ONLY_ENV: &str = "RUNFILES_MANIFEST_ONLY";`
- `enum` `codex-rs/utils/cargo-bin/src/lib.rs:12` `pub enum CargoBinError {`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:39` `pub fn cargo_bin(name: &str) -> Result<PathBuf, CargoBinError> {`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:71` `fn cargo_bin_env_keys(name: &str) -> Vec<String> {`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:84` `pub fn runfiles_available() -> bool {`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:88` `fn resolve_bin_from_env(key: &str, value: OsString) -> Result<PathBuf, CargoBinError> {`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:135` `pub fn resolve_bazel_runfile(`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:163` `pub fn resolve_cargo_runfile(resource: &Path) -> std::io::Result<PathBuf> {`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:168` `pub fn repo_root() -> io::Result<PathBuf> {`
- `fn` `codex-rs/utils/cargo-bin/src/lib.rs:204` `fn normalize_runfile_path(path: &Path) -> PathBuf {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsString;`
- `use std::io;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
