# `codex-rs/rmcp-client/src/program_resolver.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7828`
- sha256: `fef50c896e09c34f9b57857ccb534ba6393606707ce89422645a1aacf1c50029`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/program_resolver.rs` (read)
- env: `PATH`, `PATHEXT`

### Outputs / Side Effects
- spawns subprocesses
- writes to filesystem

## Public Surface (auto)
- `pub fn resolve(program: OsString, _env: &HashMap<String, String>) -> std::io::Result<OsString> {`
- `pub fn resolve(program: OsString, env: &HashMap<String, String>) -> std::io::Result<OsString> {`

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:13` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:14` `use std::ffi::OsString;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:17` `use std::env;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:19` `use tracing::debug;`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:27` `pub fn resolve(program: OsString, _env: &HashMap<String, String>) -> std::io::Result<OsString> {`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:41` `pub fn resolve(program: OsString, env: &HashMap<String, String>) -> std::io::Result<OsString> {`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:68` `use super::*;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:69` `use crate::utils::create_env_for_mcp_server;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:70` `use anyhow::Result;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:71` `use std::fs;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:72` `use std::path::Path;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:73` `use tempfile::TempDir;`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:74` `use tokio::process::Command;`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:79` `async fn test_unix_executes_script_without_extension() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:92` `async fn test_windows_fails_without_extension() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:108` `async fn test_windows_succeeds_with_extension() -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:125` `async fn test_resolved_program_executes_successfully() -> Result<()> {`
- `struct` `codex-rs/rmcp-client/src/program_resolver.rs:145` `struct TestExecutableEnv {`
- `impl` `codex-rs/rmcp-client/src/program_resolver.rs:152` `impl TestExecutableEnv {`
- `const` `codex-rs/rmcp-client/src/program_resolver.rs:153` `const TEST_PROGRAM: &'static str = "test_mcp_server";`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:155` `fn new() -> Result<Self> {`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:178` `fn create_executable(dir: &Path) -> Result<()> {`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:196` `fn set_executable(path: &Path) -> Result<()> {`
- `use` `codex-rs/rmcp-client/src/program_resolver.rs:197` `use std::os::unix::fs::PermissionsExt;`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:205` `fn build_path(dir: &Path) -> String {`
- `fn` `codex-rs/rmcp-client/src/program_resolver.rs:213` `fn ensure_cmd_extension() -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::ffi::OsString;`
- `use std::env;`
- `use tracing::debug;`
- `use super::*;`
- `use crate::utils::create_env_for_mcp_server;`
- `use anyhow::Result;`
- `use std::fs;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::process::Command;`
- `use std::os::unix::fs::PermissionsExt;`
### Referenced env vars
- `PATH`
- `PATHEXT`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
