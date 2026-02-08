# `codex-rs/core/src/turn_diff_tracker.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `30737`
- sha256: `66e0944dc90e54b2b00f91a898b81f1d1143e98791e46ed1f09b7887b4cddedc`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/turn_diff_tracker.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct TurnDiffTracker {`
- `pub fn new() -> Self {`
- `pub fn on_patch_begin(&mut self, changes: &HashMap<PathBuf, FileChange>) {`
- `pub fn get_unified_diff(&mut self) -> Result<Option<String>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/turn_diff_tracker.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:2` `use std::fs;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:3` `use std::path::Path;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:4` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:5` `use std::process::Command;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:7` `use anyhow::Context;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:8` `use anyhow::Result;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:9` `use anyhow::anyhow;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:10` `use sha1::digest::Output;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:11` `use uuid::Uuid;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:13` `use crate::protocol::FileChange;`
- `const` `codex-rs/core/src/turn_diff_tracker.rs:15` `const ZERO_OID: &str = "0000000000000000000000000000000000000000";`
- `const` `codex-rs/core/src/turn_diff_tracker.rs:16` `const DEV_NULL: &str = "/dev/null";`
- `struct` `codex-rs/core/src/turn_diff_tracker.rs:18` `struct BaselineFileInfo {`
- `struct` `codex-rs/core/src/turn_diff_tracker.rs:33` `pub struct TurnDiffTracker {`
- `impl` `codex-rs/core/src/turn_diff_tracker.rs:45` `impl TurnDiffTracker {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:46` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:54` `pub fn on_patch_begin(&mut self, changes: &HashMap<PathBuf, FileChange>) {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:130` `fn get_path_for_internal(&self, internal: &str) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:143` `fn find_git_root_cached(&mut self, start: &Path) -> Option<PathBuf> {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:188` `fn relative_to_git_root_str(&mut self, path: &Path) -> String {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:203` `fn git_blob_oid_for_path(&mut self, path: &Path) -> Option<String> {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:225` `pub fn get_unified_diff(&mut self) -> Result<Option<String>> {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:252` `fn get_file_diff(&mut self, internal_file_name: &str) -> String {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:372` `fn git_blob_sha1_hex_bytes(data: &[u8]) -> Output<sha1::Sha1> {`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:375` `use sha1::Digest;`
- `enum` `codex-rs/core/src/turn_diff_tracker.rs:383` `enum FileMode {`
- `impl` `codex-rs/core/src/turn_diff_tracker.rs:390` `impl FileMode {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:391` `fn as_str(self) -> &'static str {`
- `impl` `codex-rs/core/src/turn_diff_tracker.rs:401` `impl std::fmt::Display for FileMode {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:402` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:408` `fn file_mode_for_path(path: &Path) -> Option<FileMode> {`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:409` `use std::os::unix::fs::PermissionsExt;`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:425` `fn file_mode_for_path(_path: &Path) -> Option<FileMode> {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:430` `fn blob_bytes(path: &Path, mode: FileMode) -> Option<Vec<u8>> {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:446` `fn symlink_blob_bytes(path: &Path) -> Option<Vec<u8>> {`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:447` `use std::os::unix::ffi::OsStrExt;`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:453` `fn symlink_blob_bytes(_path: &Path) -> Option<Vec<u8>> {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:458` `fn is_windows_drive_or_unc_root(p: &std::path::Path) -> bool {`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:459` `use std::path::Component;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:469` `use super::*;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:470` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/turn_diff_tracker.rs:471` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:475` `fn git_blob_sha1_hex(data: &str) -> String {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:479` `fn normalize_diff_for_test(input: &str, root: &Path) -> String {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:507` `fn accumulates_add_and_update() {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:575` `fn accumulates_delete() {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:611` `fn accumulates_move_and_update() {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:651` `fn move_without_1change_yields_no_diff() {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:675` `fn move_declared_but_file_only_appears_at_dest_is_add() {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:710` `fn update_persists_across_new_baseline_for_new_file() {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:788` `fn binary_files_differ_update() {`
- `fn` `codex-rs/core/src/turn_diff_tracker.rs:830` `fn filenames_with_spaces_add_and_update() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::fs;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::Command;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use sha1::digest::Output;`
- `use uuid::Uuid;`
- `use crate::protocol::FileChange;`
- `use sha1::Digest;`
- `use std::os::unix::fs::PermissionsExt;`
- `use std::os::unix::ffi::OsStrExt;`
- `use std::path::Component;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
