# `codex-rs/execpolicy/src/amend.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6660`
- sha256: `3e66bb53b0b2ef38bfc948e38092ea70f43df51507ba4288d69de4178d959ff2`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/execpolicy/src/amend.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum AmendError {`
- `pub fn blocking_append_allow_prefix_rule(`

## Definitions (auto, per-file)
- `use` `codex-rs/execpolicy/src/amend.rs:1` `use std::fs::OpenOptions;`
- `use` `codex-rs/execpolicy/src/amend.rs:2` `use std::io::Read;`
- `use` `codex-rs/execpolicy/src/amend.rs:3` `use std::io::Seek;`
- `use` `codex-rs/execpolicy/src/amend.rs:4` `use std::io::SeekFrom;`
- `use` `codex-rs/execpolicy/src/amend.rs:5` `use std::io::Write;`
- `use` `codex-rs/execpolicy/src/amend.rs:6` `use std::path::Path;`
- `use` `codex-rs/execpolicy/src/amend.rs:7` `use std::path::PathBuf;`
- `use` `codex-rs/execpolicy/src/amend.rs:9` `use serde_json;`
- `use` `codex-rs/execpolicy/src/amend.rs:10` `use thiserror::Error;`
- `enum` `codex-rs/execpolicy/src/amend.rs:13` `pub enum AmendError {`
- `fn` `codex-rs/execpolicy/src/amend.rs:59` `pub fn blocking_append_allow_prefix_rule(`
- `fn` `codex-rs/execpolicy/src/amend.rs:93` `fn append_locked_line(policy_path: &Path, line: &str) -> Result<(), AmendError> {`
- `use` `codex-rs/execpolicy/src/amend.rs:143` `use super::*;`
- `use` `codex-rs/execpolicy/src/amend.rs:144` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/execpolicy/src/amend.rs:145` `use tempfile::tempdir;`
- `fn` `codex-rs/execpolicy/src/amend.rs:148` `fn appends_rule_and_creates_directories() {`
- `fn` `codex-rs/execpolicy/src/amend.rs:167` `fn appends_rule_without_duplicate_newline() {`
- `fn` `codex-rs/execpolicy/src/amend.rs:194` `fn inserts_newline_when_missing_before_append() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs::OpenOptions;`
- `use std::io::Read;`
- `use std::io::Seek;`
- `use std::io::SeekFrom;`
- `use std::io::Write;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use serde_json;`
- `use thiserror::Error;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
