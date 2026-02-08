# `codex-rs/utils/git/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2661`
- sha256: `df4af7f5f521d77251dbc0536c195e7004aa251028729aec0779c1d983147593`
- generated_utc: `2026-02-03T16:08:31Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/git/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct GhostCommit {`
- `pub fn new(`
- `pub fn id(&self) -> &str {`
- `pub fn parent(&self) -> Option<&str> {`
- `pub fn preexisting_untracked_files(&self) -> &[PathBuf] {`
- `pub fn preexisting_untracked_dirs(&self) -> &[PathBuf] {`

## Definitions (auto, per-file)
- `use` `codex-rs/utils/git/src/lib.rs:1` `use std::fmt;`
- `use` `codex-rs/utils/git/src/lib.rs:2` `use std::path::PathBuf;`
- `mod` `codex-rs/utils/git/src/lib.rs:4` `mod apply;`
- `mod` `codex-rs/utils/git/src/lib.rs:5` `mod branch;`
- `mod` `codex-rs/utils/git/src/lib.rs:6` `mod errors;`
- `mod` `codex-rs/utils/git/src/lib.rs:7` `mod ghost_commits;`
- `mod` `codex-rs/utils/git/src/lib.rs:8` `mod operations;`
- `mod` `codex-rs/utils/git/src/lib.rs:9` `mod platform;`
- `use` `codex-rs/utils/git/src/lib.rs:32` `use schemars::JsonSchema;`
- `use` `codex-rs/utils/git/src/lib.rs:33` `use serde::Deserialize;`
- `use` `codex-rs/utils/git/src/lib.rs:34` `use serde::Serialize;`
- `use` `codex-rs/utils/git/src/lib.rs:35` `use ts_rs::TS;`
- `type` `codex-rs/utils/git/src/lib.rs:37` `type CommitID = String;`
- `struct` `codex-rs/utils/git/src/lib.rs:41` `pub struct GhostCommit {`
- `impl` `codex-rs/utils/git/src/lib.rs:48` `impl GhostCommit {`
- `fn` `codex-rs/utils/git/src/lib.rs:50` `pub fn new(`
- `fn` `codex-rs/utils/git/src/lib.rs:65` `pub fn id(&self) -> &str {`
- `fn` `codex-rs/utils/git/src/lib.rs:70` `pub fn parent(&self) -> Option<&str> {`
- `fn` `codex-rs/utils/git/src/lib.rs:75` `pub fn preexisting_untracked_files(&self) -> &[PathBuf] {`
- `fn` `codex-rs/utils/git/src/lib.rs:80` `pub fn preexisting_untracked_dirs(&self) -> &[PathBuf] {`
- `impl` `codex-rs/utils/git/src/lib.rs:85` `impl fmt::Display for GhostCommit {`
- `fn` `codex-rs/utils/git/src/lib.rs:86` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt;`
- `use std::path::PathBuf;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
