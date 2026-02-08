# `codex-rs/apply-patch/src/parser.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `25696`
- sha256: `8bc5adbfa0b79a82433f261ee3acb347897e87b46e1c560f7ba67d5efac2b865`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/apply-patch/src/parser.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ParseError {`
- `pub enum Hunk {`
- `pub fn resolve_path(&self, cwd: &Path) -> PathBuf {`
- `pub struct UpdateFileChunk {`
- `pub fn parse_patch(patch: &str) -> Result<ApplyPatchArgs, ParseError> {`

## Definitions (auto, per-file)
- `use` `codex-rs/apply-patch/src/parser.rs:25` `use crate::ApplyPatchArgs;`
- `use` `codex-rs/apply-patch/src/parser.rs:26` `use std::path::Path;`
- `use` `codex-rs/apply-patch/src/parser.rs:27` `use std::path::PathBuf;`
- `use` `codex-rs/apply-patch/src/parser.rs:29` `use thiserror::Error;`
- `const` `codex-rs/apply-patch/src/parser.rs:31` `const BEGIN_PATCH_MARKER: &str = "*** Begin Patch";`
- `const` `codex-rs/apply-patch/src/parser.rs:32` `const END_PATCH_MARKER: &str = "*** End Patch";`
- `const` `codex-rs/apply-patch/src/parser.rs:33` `const ADD_FILE_MARKER: &str = "*** Add File: ";`
- `const` `codex-rs/apply-patch/src/parser.rs:34` `const DELETE_FILE_MARKER: &str = "*** Delete File: ";`
- `const` `codex-rs/apply-patch/src/parser.rs:35` `const UPDATE_FILE_MARKER: &str = "*** Update File: ";`
- `const` `codex-rs/apply-patch/src/parser.rs:36` `const MOVE_TO_MARKER: &str = "*** Move to: ";`
- `const` `codex-rs/apply-patch/src/parser.rs:37` `const EOF_MARKER: &str = "*** End of File";`
- `const` `codex-rs/apply-patch/src/parser.rs:38` `const CHANGE_CONTEXT_MARKER: &str = "@@ ";`
- `const` `codex-rs/apply-patch/src/parser.rs:39` `const EMPTY_CHANGE_CONTEXT_MARKER: &str = "@@";`
- `const` `codex-rs/apply-patch/src/parser.rs:47` `const PARSE_IN_STRICT_MODE: bool = false;`
- `enum` `codex-rs/apply-patch/src/parser.rs:50` `pub enum ParseError {`
- `use` `codex-rs/apply-patch/src/parser.rs:56` `use ParseError::*;`
- `enum` `codex-rs/apply-patch/src/parser.rs:60` `pub enum Hunk {`
- `impl` `codex-rs/apply-patch/src/parser.rs:78` `impl Hunk {`
- `fn` `codex-rs/apply-patch/src/parser.rs:79` `pub fn resolve_path(&self, cwd: &Path) -> PathBuf {`
- `use` `codex-rs/apply-patch/src/parser.rs:88` `use Hunk::*;`
- `struct` `codex-rs/apply-patch/src/parser.rs:91` `pub struct UpdateFileChunk {`
- `fn` `codex-rs/apply-patch/src/parser.rs:106` `pub fn parse_patch(patch: &str) -> Result<ApplyPatchArgs, ParseError> {`
- `enum` `codex-rs/apply-patch/src/parser.rs:115` `enum ParseMode {`
- `fn` `codex-rs/apply-patch/src/parser.rs:154` `fn parse_patch_text(patch: &str, mode: ParseMode) -> Result<ApplyPatchArgs, ParseError> {`
- `fn` `codex-rs/apply-patch/src/parser.rs:187` `fn check_patch_boundaries_strict(lines: &[&str]) -> Result<(), ParseError> {`
- `fn` `codex-rs/apply-patch/src/parser.rs:226` `fn check_start_and_end_lines_strict(`
- `fn` `codex-rs/apply-patch/src/parser.rs:248` `fn parse_one_hunk(lines: &[&str], line_number: usize) -> Result<(Hunk, usize), ParseError> {`
- `fn` `codex-rs/apply-patch/src/parser.rs:343` `fn parse_update_file_chunk(`
- `fn` `codex-rs/apply-patch/src/parser.rs:437` `fn test_parse_patch() {`
- `fn` `codex-rs/apply-patch/src/parser.rs:587` `fn test_parse_patch_lenient() {`
- `fn` `codex-rs/apply-patch/src/parser.rs:673` `fn test_parse_one_hunk() {`
- `fn` `codex-rs/apply-patch/src/parser.rs:686` `fn test_update_file_chunk() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::ApplyPatchArgs;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use thiserror::Error;`
- `use ParseError::*;`
- `use Hunk::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
