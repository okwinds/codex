# `codex-rs/core/src/turn_metadata.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1286`
- sha256: `700272e9a1b16ca646db079408541bc9b427f03bb6aa1524323130b18bca2c51`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/turn_metadata.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/turn_metadata.rs:1` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/turn_metadata.rs:2` `use std::path::Path;`
- `use` `codex-rs/core/src/turn_metadata.rs:4` `use serde::Serialize;`
- `use` `codex-rs/core/src/turn_metadata.rs:6` `use crate::git_info::get_git_remote_urls_assume_git_repo;`
- `use` `codex-rs/core/src/turn_metadata.rs:7` `use crate::git_info::get_git_repo_root;`
- `use` `codex-rs/core/src/turn_metadata.rs:8` `use crate::git_info::get_head_commit_hash;`
- `struct` `codex-rs/core/src/turn_metadata.rs:11` `struct TurnMetadataWorkspace {`
- `struct` `codex-rs/core/src/turn_metadata.rs:19` `struct TurnMetadata {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::path::Path;`
- `use serde::Serialize;`
- `use crate::git_info::get_git_remote_urls_assume_git_repo;`
- `use crate::git_info::get_git_repo_root;`
- `use crate::git_info::get_head_commit_hash;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
