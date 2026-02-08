# `codex-rs/apply-patch/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `34113`
- sha256: `b35046f0cfe1327a893f4d7ab2c43d5c3905a83de2be7e1448d5dabb6870abd7`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/apply-patch/src/lib.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum ApplyPatchError {`
- `pub struct IoError {`
- `pub struct ApplyPatchArgs {`
- `pub enum ApplyPatchFileChange {`
- `pub enum MaybeApplyPatchVerified {`
- `pub struct ApplyPatchAction {`
- `pub fn is_empty(&self) -> bool {`
- `pub fn changes(&self) -> &HashMap<PathBuf, ApplyPatchFileChange> {`
- `pub fn new_add_for_test(path: &Path, content: String) -> Self {`
- `pub fn apply_patch(`
- `pub fn apply_hunks(`
- `pub struct AffectedPaths {`
- `pub struct ApplyPatchFileUpdate {`
- `pub fn unified_diff_from_chunks(`
- `pub fn unified_diff_from_chunks_with_context(`
- `pub fn print_summary(`

## Definitions (auto, per-file)
- `mod` `codex-rs/apply-patch/src/lib.rs:1` `mod invocation;`
- `mod` `codex-rs/apply-patch/src/lib.rs:2` `mod parser;`
- `mod` `codex-rs/apply-patch/src/lib.rs:3` `mod seek_sequence;`
- `mod` `codex-rs/apply-patch/src/lib.rs:4` `mod standalone_executable;`
- `use` `codex-rs/apply-patch/src/lib.rs:6` `use std::collections::HashMap;`
- `use` `codex-rs/apply-patch/src/lib.rs:7` `use std::path::Path;`
- `use` `codex-rs/apply-patch/src/lib.rs:8` `use std::path::PathBuf;`
- `use` `codex-rs/apply-patch/src/lib.rs:10` `use anyhow::Context;`
- `use` `codex-rs/apply-patch/src/lib.rs:11` `use anyhow::Result;`
- `use` `codex-rs/apply-patch/src/lib.rs:14` `use parser::ParseError::*;`
- `use` `codex-rs/apply-patch/src/lib.rs:15` `use parser::UpdateFileChunk;`
- `use` `codex-rs/apply-patch/src/lib.rs:17` `use similar::TextDiff;`
- `use` `codex-rs/apply-patch/src/lib.rs:18` `use thiserror::Error;`
- `use` `codex-rs/apply-patch/src/lib.rs:23` `use crate::invocation::ExtractHeredocError;`
- `const` `codex-rs/apply-patch/src/lib.rs:26` `pub const APPLY_PATCH_TOOL_INSTRUCTIONS: &str = include_str!("../apply_patch_tool_instructions.md");`
- `enum` `codex-rs/apply-patch/src/lib.rs:29` `pub enum ApplyPatchError {`
- `impl` `codex-rs/apply-patch/src/lib.rs:44` `impl From<std::io::Error> for ApplyPatchError {`
- `fn` `codex-rs/apply-patch/src/lib.rs:45` `fn from(err: std::io::Error) -> Self {`
- `impl` `codex-rs/apply-patch/src/lib.rs:53` `impl From<&std::io::Error> for ApplyPatchError {`
- `fn` `codex-rs/apply-patch/src/lib.rs:54` `fn from(err: &std::io::Error) -> Self {`
- `struct` `codex-rs/apply-patch/src/lib.rs:64` `pub struct IoError {`
- `impl` `codex-rs/apply-patch/src/lib.rs:70` `impl PartialEq for IoError {`
- `fn` `codex-rs/apply-patch/src/lib.rs:71` `fn eq(&self, other: &Self) -> bool {`
- `struct` `codex-rs/apply-patch/src/lib.rs:79` `pub struct ApplyPatchArgs {`
- `enum` `codex-rs/apply-patch/src/lib.rs:86` `pub enum ApplyPatchFileChange {`
- `enum` `codex-rs/apply-patch/src/lib.rs:102` `pub enum MaybeApplyPatchVerified {`
- `struct` `codex-rs/apply-patch/src/lib.rs:119` `pub struct ApplyPatchAction {`
- `impl` `codex-rs/apply-patch/src/lib.rs:131` `impl ApplyPatchAction {`
- `fn` `codex-rs/apply-patch/src/lib.rs:132` `pub fn is_empty(&self) -> bool {`
- `fn` `codex-rs/apply-patch/src/lib.rs:137` `pub fn changes(&self) -> &HashMap<PathBuf, ApplyPatchFileChange> {`
- `fn` `codex-rs/apply-patch/src/lib.rs:143` `pub fn new_add_for_test(path: &Path, content: String) -> Self {`
- `fn` `codex-rs/apply-patch/src/lib.rs:174` `pub fn apply_patch(`
- `fn` `codex-rs/apply-patch/src/lib.rs:207` `pub fn apply_hunks(`
- `struct` `codex-rs/apply-patch/src/lib.rs:262` `pub struct AffectedPaths {`
- `fn` `codex-rs/apply-patch/src/lib.rs:270` `fn apply_hunks_to_files(hunks: &[Hunk]) -> anyhow::Result<AffectedPaths> {`
- `struct` `codex-rs/apply-patch/src/lib.rs:332` `struct AppliedPatch {`
- `fn` `codex-rs/apply-patch/src/lib.rs:339` `fn derive_new_contents_from_chunks(`
- `fn` `codex-rs/apply-patch/src/lib.rs:377` `fn compute_replacements(`
- `fn` `codex-rs/apply-patch/src/lib.rs:469` `fn apply_replacements(`
- `struct` `codex-rs/apply-patch/src/lib.rs:497` `pub struct ApplyPatchFileUpdate {`
- `fn` `codex-rs/apply-patch/src/lib.rs:502` `pub fn unified_diff_from_chunks(`
- `fn` `codex-rs/apply-patch/src/lib.rs:509` `pub fn unified_diff_from_chunks_with_context(`
- `fn` `codex-rs/apply-patch/src/lib.rs:528` `pub fn print_summary(`
- `use` `codex-rs/apply-patch/src/lib.rs:547` `use super::*;`
- `use` `codex-rs/apply-patch/src/lib.rs:548` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/apply-patch/src/lib.rs:549` `use std::fs;`
- `use` `codex-rs/apply-patch/src/lib.rs:550` `use std::string::ToString;`
- `use` `codex-rs/apply-patch/src/lib.rs:551` `use tempfile::tempdir;`
- `fn` `codex-rs/apply-patch/src/lib.rs:554` `fn wrap_patch(body: &str) -> String {`
- `fn` `codex-rs/apply-patch/src/lib.rs:559` `fn test_add_file_hunk_creates_file_with_contents() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:585` `fn test_delete_file_hunk_removes_file() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:605` `fn test_update_file_hunk_modifies_content() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:634` `fn test_update_file_hunk_can_move_file() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:668` `fn test_multiple_update_chunks_apply_to_single_file() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:708` `fn test_update_file_hunk_interleaved_changes() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:756` `fn test_pure_addition_chunk_followed_by_removal() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:789` `fn test_update_line_with_unicode_dash() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:828` `fn test_unified_diff() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:868` `fn test_unified_diff_first_line_replacement() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:904` `fn test_unified_diff_last_line_replacement() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:941` `fn test_unified_diff_insert_at_eof() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:975` `fn test_unified_diff_interleaved_changes() {`
- `fn` `codex-rs/apply-patch/src/lib.rs:1047` `fn test_apply_patch_fails_on_write_error() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use parser::ParseError::*;`
- `use parser::UpdateFileChunk;`
- `use similar::TextDiff;`
- `use thiserror::Error;`
- `use crate::invocation::ExtractHeredocError;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use std::fs;`
- `use std::string::ToString;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
