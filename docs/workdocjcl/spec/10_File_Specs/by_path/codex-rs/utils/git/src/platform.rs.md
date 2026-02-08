# `codex-rs/utils/git/src/platform.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `903`
- sha256: `da4cbfb60e6b4f9849c8cc7c087f4c03c2030945002d59bb9d740ad848d0c42a`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/git/src/platform.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn create_symlink(`
- `pub fn create_symlink(`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/git/src/platform.rs:1` `use std::path::Path;`
- `use` `codex-rs/utils/git/src/platform.rs:3` `use crate::GitToolingError;`
- `fn` `codex-rs/utils/git/src/platform.rs:6` `pub fn create_symlink(`
- `use` `codex-rs/utils/git/src/platform.rs:11` `use std::os::unix::fs::symlink;`
- `fn` `codex-rs/utils/git/src/platform.rs:18` `pub fn create_symlink(`
- `use` `codex-rs/utils/git/src/platform.rs:23` `use std::os::windows::fs::FileTypeExt;`
- `use` `codex-rs/utils/git/src/platform.rs:24` `use std::os::windows::fs::symlink_dir;`
- `use` `codex-rs/utils/git/src/platform.rs:25` `use std::os::windows::fs::symlink_file;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use crate::GitToolingError;`
- `use std::os::unix::fs::symlink;`
- `use std::os::windows::fs::FileTypeExt;`
- `use std::os::windows::fs::symlink_dir;`
- `use std::os::windows::fs::symlink_file;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
