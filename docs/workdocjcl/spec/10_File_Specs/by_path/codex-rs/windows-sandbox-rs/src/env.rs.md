# `codex-rs/windows-sandbox-rs/src/env.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5549`
- sha256: `8540d3a2bc5f29b3b13e62204424074bf8a1841dfb3eef8d76b739437fa20e93`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/windows-sandbox-rs/src/env.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub fn normalize_null_device_env(env_map: &mut HashMap<String, String>) {`
- `pub fn ensure_non_interactive_pager(env_map: &mut HashMap<String, String>) {`
- `pub fn inherit_path_env(env_map: &mut HashMap<String, String>) {`
- `pub fn apply_no_network_to_env(env_map: &mut HashMap<String, String>) -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/windows-sandbox-rs/src/env.rs:1` `use anyhow::{anyhow, Result};`
- `use` `codex-rs/windows-sandbox-rs/src/env.rs:2` `use dirs_next::home_dir;`
- `use` `codex-rs/windows-sandbox-rs/src/env.rs:3` `use std::collections::HashMap;`
- `use` `codex-rs/windows-sandbox-rs/src/env.rs:4` `use std::env;`
- `use` `codex-rs/windows-sandbox-rs/src/env.rs:5` `use std::fs::{self, File};`
- `use` `codex-rs/windows-sandbox-rs/src/env.rs:6` `use std::io::Write;`
- `use` `codex-rs/windows-sandbox-rs/src/env.rs:7` `use std::path::{Path, PathBuf};`
- `fn` `codex-rs/windows-sandbox-rs/src/env.rs:9` `pub fn normalize_null_device_env(env_map: &mut HashMap<String, String>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/env.rs:21` `pub fn ensure_non_interactive_pager(env_map: &mut HashMap<String, String>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/env.rs:32` `pub fn inherit_path_env(env_map: &mut HashMap<String, String>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/env.rs:45` `fn prepend_path(env_map: &mut HashMap<String, String>, prefix: &str) {`
- `fn` `codex-rs/windows-sandbox-rs/src/env.rs:68` `fn reorder_pathext_for_stubs(env_map: &mut HashMap<String, String>) {`
- `fn` `codex-rs/windows-sandbox-rs/src/env.rs:102` `fn ensure_denybin(tools: &[&str], denybin_dir: Option<&Path>) -> Result<PathBuf> {`
- `fn` `codex-rs/windows-sandbox-rs/src/env.rs:123` `pub fn apply_no_network_to_env(env_map: &mut HashMap<String, String>) -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::{anyhow, Result};`
- `use dirs_next::home_dir;`
- `use std::collections::HashMap;`
- `use std::env;`
- `use std::fs::{self, File};`
- `use std::io::Write;`
- `use std::path::{Path, PathBuf};`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
