# `codex-rs/windows-sandbox-rs/src/path_normalization.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `749`
- sha256: `a067e1402e65f88e0fadd1fd607afb6b2ee07e16e5f34ee4088195e7b6c19e71`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/path_normalization.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn canonicalize_path(path: &Path) -> PathBuf {`
- `pub fn canonical_path_key(path: &Path) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:1` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:2` `use std::path::PathBuf;`
- `fn` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:4` `pub fn canonicalize_path(path: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:8` `pub fn canonical_path_key(path: &Path) -> String {`
- `use` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:17` `use super::canonical_path_key;`
- `use` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:18` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:19` `use std::path::Path;`
- `fn` `codex-rs/windows-sandbox-rs/src/path_normalization.rs:22` `fn canonical_path_key_normalizes_case_and_separators() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use super::canonical_path_key;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
