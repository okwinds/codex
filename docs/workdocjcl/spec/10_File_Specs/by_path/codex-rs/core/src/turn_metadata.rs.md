# `codex-rs/core/src/turn_metadata.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2675`
- sha256: `00079d022120c31481496c65530e9bbf74905b1803b4f4df5d9d39c9dbc892fa`
- generated_utc: `2026-02-08T10:45:34Z`

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
- `use` `codex-rs/core/src/turn_metadata.rs:7` `use std::collections::BTreeMap;`
- `use` `codex-rs/core/src/turn_metadata.rs:8` `use std::future::Future;`
- `use` `codex-rs/core/src/turn_metadata.rs:9` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/turn_metadata.rs:10` `use std::time::Duration;`
- `use` `codex-rs/core/src/turn_metadata.rs:12` `use serde::Serialize;`
- `use` `codex-rs/core/src/turn_metadata.rs:13` `use tracing::warn;`
- `use` `codex-rs/core/src/turn_metadata.rs:15` `use crate::git_info::get_git_remote_urls_assume_git_repo;`
- `use` `codex-rs/core/src/turn_metadata.rs:16` `use crate::git_info::get_git_repo_root;`
- `use` `codex-rs/core/src/turn_metadata.rs:17` `use crate::git_info::get_head_commit_hash;`
- `struct` `codex-rs/core/src/turn_metadata.rs:47` `struct TurnMetadataWorkspace {`
- `struct` `codex-rs/core/src/turn_metadata.rs:55` `struct TurnMetadata {`
- `fn` `codex-rs/core/src/turn_metadata.rs:59` `pub async fn build_turn_metadata_header(cwd: PathBuf) -> Option<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::BTreeMap;`
- `use std::future::Future;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use serde::Serialize;`
- `use tracing::warn;`
- `use crate::git_info::get_git_remote_urls_assume_git_repo;`
- `use crate::git_info::get_git_repo_root;`
- `use crate::git_info::get_head_commit_hash;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
