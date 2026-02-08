# `codex-rs/core/src/tools/handlers/list_dir.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15521`
- sha256: `967239b9767f7ecb9a29673fcd0b7bcdc58f8ea374a0e575ba1db1cebda18f6c`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/list_dir.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub struct ListDirHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:1` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:2` `use std::collections::VecDeque;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:3` `use std::ffi::OsStr;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:4` `use std::fs::FileType;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:5` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:6` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:8` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:9` `use codex_utils_string::take_bytes_at_char_boundary;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:11` `use tokio::fs;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:13` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:14` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:15` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:16` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:17` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:18` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:19` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/list_dir.rs:21` `pub struct ListDirHandler;`
- `const` `codex-rs/core/src/tools/handlers/list_dir.rs:23` `const MAX_ENTRY_LENGTH: usize = 500;`
- `const` `codex-rs/core/src/tools/handlers/list_dir.rs:24` `const INDENTATION_SPACES: usize = 2;`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:26` `fn default_offset() -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:30` `fn default_limit() -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:34` `fn default_depth() -> usize {`
- `struct` `codex-rs/core/src/tools/handlers/list_dir.rs:39` `struct ListDirArgs {`
- `impl` `codex-rs/core/src/tools/handlers/list_dir.rs:50` `impl ToolHandler for ListDirHandler {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:51` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:55` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:112` `async fn list_dir_slice(`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:151` `async fn collect_entries(`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:211` `fn format_entry_name(path: &Path) -> String {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:220` `fn format_entry_component(name: &OsStr) -> String {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:229` `fn format_entry_line(entry: &DirEntry) -> String {`
- `struct` `codex-rs/core/src/tools/handlers/list_dir.rs:242` `struct DirEntry {`
- `enum` `codex-rs/core/src/tools/handlers/list_dir.rs:250` `enum DirEntryKind {`
- `impl` `codex-rs/core/src/tools/handlers/list_dir.rs:257` `impl From<&FileType> for DirEntryKind {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:258` `fn from(file_type: &FileType) -> Self {`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:273` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:274` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:275` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:278` `async fn lists_directory_entries() {`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:304` `use std::os::unix::fs::symlink;`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:336` `async fn errors_when_offset_exceeds_entries() {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:353` `async fn respects_depth_parameter() {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:407` `async fn paginates_in_sorted_order() {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:445` `async fn handles_large_limit_without_overflow() {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:468` `async fn indicates_truncated_results() {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:490` `async fn truncation_respects_sorted_order() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use std::collections::VecDeque;`
- `use std::ffi::OsStr;`
- `use std::fs::FileType;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use async_trait::async_trait;`
- `use codex_utils_string::take_bytes_at_char_boundary;`
- `use serde::Deserialize;`
- `use tokio::fs;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
