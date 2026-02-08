# `codex-rs/core/src/tools/handlers/read_file.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `29550`
- sha256: `5d26166b39a2d6047417ec20dcb98a41d32d37716d9584283e3636f92471e9b5`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/read_file.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct ReadFileHandler;`
- `pub fn offset() -> usize {`
- `pub fn limit() -> usize {`
- `pub fn max_levels() -> usize {`
- `pub fn include_siblings() -> bool {`
- `pub fn include_header() -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:1` `use std::collections::VecDeque;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:4` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:5` `use codex_utils_string::take_bytes_at_char_boundary;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:6` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:8` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:9` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:10` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:11` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:12` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:13` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:14` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/read_file.rs:16` `pub struct ReadFileHandler;`
- `const` `codex-rs/core/src/tools/handlers/read_file.rs:18` `const MAX_LINE_LENGTH: usize = 500;`
- `const` `codex-rs/core/src/tools/handlers/read_file.rs:19` `const TAB_WIDTH: usize = 4;`
- `const` `codex-rs/core/src/tools/handlers/read_file.rs:22` `const COMMENT_PREFIXES: &[&str] = &["#", "//", "--"];`
- `struct` `codex-rs/core/src/tools/handlers/read_file.rs:26` `struct ReadFileArgs {`
- `enum` `codex-rs/core/src/tools/handlers/read_file.rs:45` `enum ReadMode {`
- `struct` `codex-rs/core/src/tools/handlers/read_file.rs:52` `struct IndentationArgs {`
- `struct` `codex-rs/core/src/tools/handlers/read_file.rs:71` `struct LineRecord {`
- `impl` `codex-rs/core/src/tools/handlers/read_file.rs:78` `impl LineRecord {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:79` `fn trimmed(&self) -> &str {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:83` `fn is_blank(&self) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:87` `fn is_comment(&self) -> bool {`
- `impl` `codex-rs/core/src/tools/handlers/read_file.rs:95` `impl ToolHandler for ReadFileHandler {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:96` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:100` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:157` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:158` `use crate::tools::handlers::read_file::format_line;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:159` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:160` `use tokio::fs::File;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:161` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:162` `use tokio::io::BufReader;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:164` `pub async fn read(`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:224` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:225` `use crate::tools::handlers::read_file::IndentationArgs;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:226` `use crate::tools::handlers::read_file::LineRecord;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:227` `use crate::tools::handlers::read_file::TAB_WIDTH;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:228` `use crate::tools::handlers::read_file::format_line;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:229` `use crate::tools::handlers::read_file::trim_empty_lines;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:230` `use std::collections::VecDeque;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:231` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:232` `use tokio::fs::File;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:233` `use tokio::io::AsyncBufReadExt;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:234` `use tokio::io::BufReader;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:236` `pub async fn read_block(`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:368` `async fn collect_file_lines(path: &Path) -> Result<Vec<LineRecord>, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:410` `fn compute_effective_indents(records: &[LineRecord]) -> Vec<usize> {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:424` `fn measure_indent(line: &str) -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:432` `fn format_line(bytes: &[u8]) -> String {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:441` `fn trim_empty_lines(out: &mut VecDeque<&LineRecord>) {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:451` `use super::*;`
- `impl` `codex-rs/core/src/tools/handlers/read_file.rs:453` `impl Default for IndentationArgs {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:454` `fn default() -> Self {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:465` `pub fn offset() -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:469` `pub fn limit() -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:473` `pub fn max_levels() -> usize {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:477` `pub fn include_siblings() -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:481` `pub fn include_header() -> bool {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:488` `use super::indentation::read_block;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:489` `use super::slice::read;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:490` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:491` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:492` `use tempfile::NamedTempFile;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:495` `async fn reads_requested_range() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:497` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:512` `async fn errors_when_offset_exceeds_length() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:514` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:528` `async fn reads_non_utf8_lines() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:530` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:540` `async fn trims_crlf_endings() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:542` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:551` `async fn respects_limit_even_with_more_lines() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:553` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:571` `async fn truncates_lines_longer_than_max_length() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:573` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:584` `async fn indentation_mode_captures_block() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:586` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:619` `async fn indentation_mode_expands_parents() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:621` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:625` `fn outer() {{`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:670` `async fn indentation_mode_respects_sibling_flag() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:672` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:720` `async fn indentation_mode_handles_python_sample() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:722` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:765` `async fn indentation_mode_handles_javascript_sample() -> anyhow::Result<()> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:767` `use std::io::Write as _;`
- `const` `codex-rs/core/src/tools/handlers/read_file.rs:771` `const cache = new Map();`
- `const` `codex-rs/core/src/tools/handlers/read_file.rs:778` `const handlers = {{`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:821` `fn write_cpp_sample() -> anyhow::Result<NamedTempFile> {`
- `use` `codex-rs/core/src/tools/handlers/read_file.rs:823` `use std::io::Write as _;`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:865` `async fn indentation_mode_handles_cpp_sample_shallow() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:893` `async fn indentation_mode_handles_cpp_sample() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:924` `async fn indentation_mode_handles_cpp_sample_no_headers() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/read_file.rs:955` `async fn indentation_mode_handles_cpp_sample_siblings() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::VecDeque;`
- `use std::path::PathBuf;`
- `use async_trait::async_trait;`
- `use codex_utils_string::take_bytes_at_char_boundary;`
- `use serde::Deserialize;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::handlers::read_file::format_line;`
- `use std::path::Path;`
- `use tokio::fs::File;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::io::BufReader;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::handlers::read_file::IndentationArgs;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
