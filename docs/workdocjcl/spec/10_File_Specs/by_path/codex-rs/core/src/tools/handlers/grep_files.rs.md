# `codex-rs/core/src/tools/handlers/grep_files.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8166`
- sha256: `22baa8bc7210411ef6b2afcc13eff4644d005f1e829437bb446a76a3bde0906e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/grep_files.rs` (read)

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub struct GrepFilesHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:1` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:2` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:4` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:5` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:6` `use tokio::process::Command;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:7` `use tokio::time::timeout;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:9` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:10` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:11` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:12` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:13` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:14` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:15` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/grep_files.rs:17` `pub struct GrepFilesHandler;`
- `const` `codex-rs/core/src/tools/handlers/grep_files.rs:19` `const DEFAULT_LIMIT: usize = 100;`
- `const` `codex-rs/core/src/tools/handlers/grep_files.rs:20` `const MAX_LIMIT: usize = 2000;`
- `const` `codex-rs/core/src/tools/handlers/grep_files.rs:21` `const COMMAND_TIMEOUT: Duration = Duration::from_secs(30);`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:23` `fn default_limit() -> usize {`
- `struct` `codex-rs/core/src/tools/handlers/grep_files.rs:28` `struct GrepFilesArgs {`
- `impl` `codex-rs/core/src/tools/handlers/grep_files.rs:39` `impl ToolHandler for GrepFilesHandler {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:40` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:44` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:103` `async fn verify_path_exists(path: &Path) -> Result<(), FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:110` `async fn run_rg_search(`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:155` `fn parse_results(stdout: &[u8], limit: usize) -> Vec<String> {`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:176` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:177` `use std::process::Command as StdCommand;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:178` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:181` `fn parses_basic_results() {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:191` `fn parse_truncates_after_limit() {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:201` `async fn run_search_returns_results() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:219` `async fn run_search_with_glob_filter() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:235` `async fn run_search_respects_limit() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:251` `async fn run_search_handles_no_matches() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:264` `fn rg_available() -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::time::Duration;`
- `use async_trait::async_trait;`
- `use serde::Deserialize;`
- `use tokio::process::Command;`
- `use tokio::time::timeout;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use super::*;`
- `use std::process::Command as StdCommand;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
