# `codex-rs/core/src/tools/handlers/grep_files.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8198`
- sha256: `9978d37c701069a2ce0b71cf60824532ab670a41934a585ed5cc458b313e9995`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:1` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:2` `use std::path::Path;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:3` `use std::time::Duration;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:5` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:6` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:7` `use tokio::process::Command;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:8` `use tokio::time::timeout;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:10` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:11` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:12` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:13` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:14` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:15` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:16` `use crate::tools::registry::ToolKind;`
- `struct` `codex-rs/core/src/tools/handlers/grep_files.rs:18` `pub struct GrepFilesHandler;`
- `const` `codex-rs/core/src/tools/handlers/grep_files.rs:20` `const DEFAULT_LIMIT: usize = 100;`
- `const` `codex-rs/core/src/tools/handlers/grep_files.rs:21` `const MAX_LIMIT: usize = 2000;`
- `const` `codex-rs/core/src/tools/handlers/grep_files.rs:22` `const COMMAND_TIMEOUT: Duration = Duration::from_secs(30);`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:24` `fn default_limit() -> usize {`
- `struct` `codex-rs/core/src/tools/handlers/grep_files.rs:29` `struct GrepFilesArgs {`
- `impl` `codex-rs/core/src/tools/handlers/grep_files.rs:40` `impl ToolHandler for GrepFilesHandler {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:41` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:45` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:102` `async fn verify_path_exists(path: &Path) -> Result<(), FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:109` `async fn run_rg_search(`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:154` `fn parse_results(stdout: &[u8], limit: usize) -> Vec<String> {`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:175` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:176` `use std::process::Command as StdCommand;`
- `use` `codex-rs/core/src/tools/handlers/grep_files.rs:177` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:180` `fn parses_basic_results() {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:190` `fn parse_truncates_after_limit() {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:200` `async fn run_search_returns_results() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:218` `async fn run_search_with_glob_filter() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:234` `async fn run_search_respects_limit() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:250` `async fn run_search_handles_no_matches() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/grep_files.rs:263` `fn rg_available() -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::FunctionCallOutputBody;`
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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
