# `codex-rs/windows-sandbox-rs/src/cap.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4220`
- sha256: `ba3ad790203b370eaf55ca39f45ab5b02d41bbef256bebac82c2f7f7bcbf03f1`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/cap.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct CapSids {`
- `pub fn cap_sid_file(codex_home: &Path) -> PathBuf {`
- `pub fn load_or_create_cap_sids(codex_home: &Path) -> Result<CapSids> {`
- `pub fn workspace_cap_sid_for_cwd(codex_home: &Path, cwd: &Path) -> Result<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:1` `use anyhow::Context;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:2` `use anyhow::Result;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:3` `use rand::rngs::SmallRng;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:4` `use rand::RngCore;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:5` `use rand::SeedableRng;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:6` `use serde::Deserialize;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:7` `use serde::Serialize;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:8` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:9` `use std::fs;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:10` `use std::path::Path;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:11` `use std::path::PathBuf;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:12` `use crate::path_normalization::canonical_path_key;`
- `struct` `codex-rs/windows-sandbox-rs/src/cap.rs:15` `pub struct CapSids {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:27` `pub fn cap_sid_file(codex_home: &Path) -> PathBuf {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:31` `fn make_random_cap_sid_string() -> String {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:40` `fn persist_caps(path: &Path, caps: &CapSids) -> Result<()> {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:49` `pub fn load_or_create_cap_sids(codex_home: &Path) -> Result<CapSids> {`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:79` `pub fn workspace_cap_sid_for_cwd(codex_home: &Path, cwd: &Path) -> Result<String> {`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:94` `use super::load_or_create_cap_sids;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:95` `use super::workspace_cap_sid_for_cwd;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:96` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/windows-sandbox-rs/src/cap.rs:97` `use std::path::PathBuf;`
- `fn` `codex-rs/windows-sandbox-rs/src/cap.rs:100` `fn equivalent_cwd_spellings_share_workspace_sid_key() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use rand::rngs::SmallRng;`
- `use rand::RngCore;`
- `use rand::SeedableRng;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::collections::HashMap;`
- `use std::fs;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use crate::path_normalization::canonical_path_key;`
- `use super::load_or_create_cap_sids;`
- `use super::workspace_cap_sid_for_cwd;`
- `use pretty_assertions::assert_eq;`
- `use std::path::PathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
