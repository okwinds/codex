# `codex-rs/linux-sandbox/build.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3834`
- sha256: `a96dfb7a35acdb8e50d5e8c0f3d5952d719fbeb89e3d4e395990a0bec11267ab`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/build.rs` (read)

### Outputs / Side Effects
- writes to filesystem
- writes to stdout/stderr

## Public Surface (auto)
- `fn main() {`

## Definitions (auto, per-file)
- `use` `codex-rs/linux-sandbox/build.rs:1` `use std::env;`
- `use` `codex-rs/linux-sandbox/build.rs:2` `use std::path::Path;`
- `use` `codex-rs/linux-sandbox/build.rs:3` `use std::path::PathBuf;`
- `fn` `codex-rs/linux-sandbox/build.rs:5` `fn main() {`
- `fn` `codex-rs/linux-sandbox/build.rs:48` `fn try_build_vendored_bwrap() -> Result<(), String> {`
- `fn` `codex-rs/linux-sandbox/build.rs:93` `fn resolve_bwrap_source_dir(manifest_dir: &Path) -> Result<PathBuf, String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::env;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
