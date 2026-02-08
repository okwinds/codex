# `codex-rs/windows-sandbox-rs/src/workspace_acl.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `596`
- sha256: `13bdb4072eb494c6b7e2804491a381ec603d0274105a052e9c6c107ab67fb179`
- generated_utc: `2026-02-08T10:45:42Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/workspace_acl.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn is_command_cwd_root(root: &Path, canonical_command_cwd: &Path) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/workspace_acl.rs:1` `use crate::acl::add_deny_write_ace;`
- `use` `codex-rs/windows-sandbox-rs/src/workspace_acl.rs:2` `use crate::path_normalization::canonicalize_path;`
- `use` `codex-rs/windows-sandbox-rs/src/workspace_acl.rs:3` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/workspace_acl.rs:4` `use std::ffi::c_void;`
- `use` `codex-rs/windows-sandbox-rs/src/workspace_acl.rs:5` `use std::path::Path;`
- `fn` `codex-rs/windows-sandbox-rs/src/workspace_acl.rs:7` `pub fn is_command_cwd_root(root: &Path, canonical_command_cwd: &Path) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::acl::add_deny_write_ace;`
- `use crate::path_normalization::canonicalize_path;`
- `use anyhow::Result;`
- `use std::ffi::c_void;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
