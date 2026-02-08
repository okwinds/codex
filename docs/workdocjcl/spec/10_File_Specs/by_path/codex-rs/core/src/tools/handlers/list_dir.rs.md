# `codex-rs/core/src/tools/handlers/list_dir.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15475`
- sha256: `f3af44dd8184e6f38356b9953fe15b9af5343d39509dd6fd5b53c405d5ae6899`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:1` `use std::collections::VecDeque;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:2` `use std::ffi::OsStr;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:3` `use std::fs::FileType;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:4` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:5` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:7` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:8` `use codex_utils_string::take_bytes_at_char_boundary;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:9` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:10` `use tokio::fs;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:12` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:13` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:14` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:15` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:16` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:17` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/list_dir.rs:18` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/list_dir.rs:20` `pub struct ListDirHandler;`
- `const` `codex-rs/core/src/tools/handlers/list_dir.rs:22` `const MAX_ENTRY_LENGTH: usize = 500;`
- `const` `codex-rs/core/src/tools/handlers/list_dir.rs:23` `const INDENTATION_SPACES: usize = 2;`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:25` `fn default_offset() -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:29` `fn default_limit() -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:33` `fn default_depth() -> usize {`
- `struct` `codex-rs/core/src/tools/handlers/list_dir.rs:38` `struct ListDirArgs {`
- `impl` `codex-rs/core/src/tools/handlers/list_dir.rs:49` `impl ToolHandler for ListDirHandler {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:50` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/list_dir.rs:54` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
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
- `use std::os::unix::fs::symlink;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
