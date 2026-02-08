# `codex-rs/core/src/tools/handlers/unified_exec.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11837`
- sha256: `43d6760a235d98a4a2f152e886fc07c1f0d1768eb29bdb48f9a9a2b3e0e78ecc`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/unified_exec.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct UnifiedExecHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:1` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:2` `use crate::is_safe_command::is_known_safe_command;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:3` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:4` `use crate::protocol::TerminalInteractionEvent;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:5` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:6` `use crate::shell::Shell;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:7` `use crate::shell::get_shell_by_model_provided_path;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:8` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:9` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:10` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:11` `use crate::tools::handlers::apply_patch::intercept_apply_patch;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:12` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:13` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:14` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:15` `use crate::unified_exec::ExecCommandRequest;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:16` `use crate::unified_exec::UnifiedExecContext;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:17` `use crate::unified_exec::UnifiedExecProcessManager;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:18` `use crate::unified_exec::UnifiedExecResponse;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:19` `use crate::unified_exec::WriteStdinRequest;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:20` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:21` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:22` `use serde::Deserialize;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:23` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:24` `use std::sync::Arc;`
- `struct` `codex-rs/core/src/tools/handlers/unified_exec.rs:26` `pub struct UnifiedExecHandler;`
- `struct` `codex-rs/core/src/tools/handlers/unified_exec.rs:29` `struct ExecCommandArgs {`
- `struct` `codex-rs/core/src/tools/handlers/unified_exec.rs:52` `struct WriteStdinArgs {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:63` `fn default_exec_yield_time_ms() -> u64 {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:67` `fn default_write_stdin_yield_time_ms() -> u64 {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:71` `fn default_login() -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:75` `fn default_tty() -> bool {`
- `impl` `codex-rs/core/src/tools/handlers/unified_exec.rs:80` `impl ToolHandler for UnifiedExecHandler {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:81` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:85` `fn matches_kind(&self, payload: &ToolPayload) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:89` `async fn is_mutating(&self, invocation: &ToolInvocation) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:105` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:248` `fn get_command(args: &ExecCommandArgs, session_shell: Arc<Shell>) -> Vec<String> {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:260` `fn format_response(response: &UnifiedExecResponse) -> String {`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:291` `use super::*;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:292` `use crate::shell::default_user_shell;`
- `use` `codex-rs/core/src/tools/handlers/unified_exec.rs:293` `use std::sync::Arc;`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:296` `fn test_get_command_uses_default_shell_when_unspecified() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:311` `fn test_get_command_respects_explicit_bash_shell() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:331` `fn test_get_command_respects_explicit_powershell_shell() -> anyhow::Result<()> {`
- `fn` `codex-rs/core/src/tools/handlers/unified_exec.rs:345` `fn test_get_command_respects_explicit_cmd_shell() -> anyhow::Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::function_tool::FunctionCallError;`
- `use crate::is_safe_command::is_known_safe_command;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::TerminalInteractionEvent;`
- `use crate::sandboxing::SandboxPermissions;`
- `use crate::shell::Shell;`
- `use crate::shell::get_shell_by_model_provided_path;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::handlers::apply_patch::intercept_apply_patch;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::registry::ToolHandler;`
- `use crate::tools::registry::ToolKind;`
- `use crate::unified_exec::ExecCommandRequest;`
- `use crate::unified_exec::UnifiedExecContext;`
- `use crate::unified_exec::UnifiedExecProcessManager;`
- `use crate::unified_exec::UnifiedExecResponse;`
- `use crate::unified_exec::WriteStdinRequest;`
- `use async_trait::async_trait;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
