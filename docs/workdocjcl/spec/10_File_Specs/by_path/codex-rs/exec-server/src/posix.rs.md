# `codex-rs/exec-server/src/posix.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9745`
- sha256: `cf2752a67368a9c1278ce6bc6a436a3b79e7a4ab589bebe3ed12383bb48ea064`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct ExecveWrapperCli {`

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix.rs:58` `use std::path::Path;`
- `use` `codex-rs/exec-server/src/posix.rs:59` `use std::path::PathBuf;`
- `use` `codex-rs/exec-server/src/posix.rs:60` `use std::sync::Arc;`
- `use` `codex-rs/exec-server/src/posix.rs:62` `use anyhow::Context as _;`
- `use` `codex-rs/exec-server/src/posix.rs:63` `use clap::Parser;`
- `use` `codex-rs/exec-server/src/posix.rs:64` `use codex_core::config::find_codex_home;`
- `use` `codex-rs/exec-server/src/posix.rs:65` `use codex_core::is_dangerous_command::command_might_be_dangerous;`
- `use` `codex-rs/exec-server/src/posix.rs:66` `use codex_core::sandboxing::SandboxPermissions;`
- `use` `codex-rs/exec-server/src/posix.rs:67` `use codex_execpolicy::Decision;`
- `use` `codex-rs/exec-server/src/posix.rs:68` `use codex_execpolicy::Policy;`
- `use` `codex-rs/exec-server/src/posix.rs:69` `use codex_execpolicy::RuleMatch;`
- `use` `codex-rs/exec-server/src/posix.rs:70` `use rmcp::ErrorData as McpError;`
- `use` `codex-rs/exec-server/src/posix.rs:71` `use tokio::sync::RwLock;`
- `use` `codex-rs/exec-server/src/posix.rs:72` `use tracing_subscriber::EnvFilter;`
- `use` `codex-rs/exec-server/src/posix.rs:73` `use tracing_subscriber::{self};`
- `use` `codex-rs/exec-server/src/posix.rs:75` `use crate::posix::mcp_escalation_policy::ExecPolicyOutcome;`
- `mod` `codex-rs/exec-server/src/posix.rs:77` `mod escalate_client;`
- `mod` `codex-rs/exec-server/src/posix.rs:78` `mod escalate_protocol;`
- `mod` `codex-rs/exec-server/src/posix.rs:79` `mod escalate_server;`
- `mod` `codex-rs/exec-server/src/posix.rs:80` `mod escalation_policy;`
- `mod` `codex-rs/exec-server/src/posix.rs:81` `mod mcp;`
- `mod` `codex-rs/exec-server/src/posix.rs:82` `mod mcp_escalation_policy;`
- `mod` `codex-rs/exec-server/src/posix.rs:83` `mod socket;`
- `mod` `codex-rs/exec-server/src/posix.rs:84` `mod stopwatch;`
- `const` `codex-rs/exec-server/src/posix.rs:90` `const CODEX_EXECVE_WRAPPER_EXE_NAME: &str = "codex-execve-wrapper";`
- `struct` `codex-rs/exec-server/src/posix.rs:94` `struct McpServerCli {`
- `fn` `codex-rs/exec-server/src/posix.rs:110` `pub async fn main_mcp_server() -> anyhow::Result<()> {`
- `struct` `codex-rs/exec-server/src/posix.rs:152` `pub struct ExecveWrapperCli {`
- `fn` `codex-rs/exec-server/src/posix.rs:160` `pub async fn main_execve_wrapper() -> anyhow::Result<()> {`
- `fn` `codex-rs/exec-server/src/posix.rs:223` `fn format_program_name(path: &Path, preserve_program_paths: bool) -> Option<String> {`
- `fn` `codex-rs/exec-server/src/posix.rs:231` `async fn load_exec_policy() -> anyhow::Result<Policy> {`
- `use` `codex-rs/exec-server/src/posix.rs:255` `use super::*;`
- `use` `codex-rs/exec-server/src/posix.rs:256` `use codex_core::sandboxing::SandboxPermissions;`
- `use` `codex-rs/exec-server/src/posix.rs:257` `use codex_execpolicy::Decision;`
- `use` `codex-rs/exec-server/src/posix.rs:258` `use codex_execpolicy::Policy;`
- `use` `codex-rs/exec-server/src/posix.rs:259` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/exec-server/src/posix.rs:260` `use std::path::Path;`
- `fn` `codex-rs/exec-server/src/posix.rs:263` `fn evaluate_exec_policy_uses_heuristics_for_dangerous_commands() {`
- `fn` `codex-rs/exec-server/src/posix.rs:279` `fn evaluate_exec_policy_respects_preserve_program_paths() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use anyhow::Context as _;`
- `use clap::Parser;`
- `use codex_core::config::find_codex_home;`
- `use codex_core::is_dangerous_command::command_might_be_dangerous;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use codex_execpolicy::Decision;`
- `use codex_execpolicy::Policy;`
- `use codex_execpolicy::RuleMatch;`
- `use rmcp::ErrorData as McpError;`
- `use tokio::sync::RwLock;`
- `use tracing_subscriber::EnvFilter;`
- `use tracing_subscriber::{self};`
- `use crate::posix::mcp_escalation_policy::ExecPolicyOutcome;`
- `use super::*;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use codex_execpolicy::Decision;`
- `use codex_execpolicy::Policy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
