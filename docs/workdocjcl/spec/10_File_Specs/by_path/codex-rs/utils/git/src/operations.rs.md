# `codex-rs/utils/git/src/operations.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6570`
- sha256: `b31498223ede720915ca6f79215b7d718e0a291821f2a82b3d6548471f517a9f`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/git/src/operations.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/utils/git/src/operations.rs:1` `use std::ffi::OsStr;`
- `use` `codex-rs/utils/git/src/operations.rs:2` `use std::ffi::OsString;`
- `use` `codex-rs/utils/git/src/operations.rs:3` `use std::path::Component;`
- `use` `codex-rs/utils/git/src/operations.rs:4` `use std::path::Path;`
- `use` `codex-rs/utils/git/src/operations.rs:5` `use std::path::PathBuf;`
- `use` `codex-rs/utils/git/src/operations.rs:6` `use std::process::Command;`
- `use` `codex-rs/utils/git/src/operations.rs:8` `use crate::GitToolingError;`
- `fn` `codex-rs/utils/git/src/operations.rs:125` `fn non_empty_path(path: &Path) -> Option<PathBuf> {`
- `fn` `codex-rs/utils/git/src/operations.rs:224` `fn build_command_string(args: &[OsString]) -> String {`
- `struct` `codex-rs/utils/git/src/operations.rs:236` `struct GitRun {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsStr;`
- `use std::ffi::OsString;`
- `use std::path::Component;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Command;`
- `use crate::GitToolingError;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
