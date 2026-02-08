# `codex-rs/core/src/tools/handlers/shell.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `16171`
- sha256: `ce48a6ffbfe30a3782b336f705da34129f90c11962715fb8cadc743d2931edd3`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/handlers/shell.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ShellHandler;`
- `pub struct ShellCommandHandler;`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/handlers/shell.rs:1` `use async_trait::async_trait;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:2` `use codex_protocol::models::ShellCommandToolCallParams;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:3` `use codex_protocol::models::ShellToolCallParams;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:4` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:6` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:7` `use crate::exec::ExecParams;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:8` `use crate::exec_env::create_env;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:9` `use crate::exec_policy::ExecApprovalRequest;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:10` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:11` `use crate::is_safe_command::is_known_safe_command;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:12` `use crate::protocol::ExecCommandSource;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:13` `use crate::shell::Shell;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:14` `use crate::tools::context::ToolInvocation;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:15` `use crate::tools::context::ToolOutput;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:16` `use crate::tools::context::ToolPayload;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:17` `use crate::tools::events::ToolEmitter;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:18` `use crate::tools::events::ToolEventCtx;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:19` `use crate::tools::handlers::apply_patch::intercept_apply_patch;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:20` `use crate::tools::handlers::parse_arguments;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:21` `use crate::tools::orchestrator::ToolOrchestrator;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:22` `use crate::tools::registry::ToolHandler;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:23` `use crate::tools::registry::ToolKind;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:24` `use crate::tools::runtimes::shell::ShellRequest;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:25` `use crate::tools::runtimes::shell::ShellRuntime;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:26` `use crate::tools::sandboxing::ToolCtx;`
- `struct` `codex-rs/core/src/tools/handlers/shell.rs:28` `pub struct ShellHandler;`
- `struct` `codex-rs/core/src/tools/handlers/shell.rs:30` `pub struct ShellCommandHandler;`
- `struct` `codex-rs/core/src/tools/handlers/shell.rs:32` `struct RunExecLikeArgs {`
- `impl` `codex-rs/core/src/tools/handlers/shell.rs:43` `impl ShellHandler {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:44` `fn to_exec_params(params: &ShellToolCallParams, turn_context: &TurnContext) -> ExecParams {`
- `impl` `codex-rs/core/src/tools/handlers/shell.rs:58` `impl ShellCommandHandler {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:59` `fn base_command(shell: &Shell, command: &str, login: Option<bool>) -> Vec<String> {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:64` `fn to_exec_params(`
- `impl` `codex-rs/core/src/tools/handlers/shell.rs:86` `impl ToolHandler for ShellHandler {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:87` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:91` `fn matches_kind(&self, payload: &ToolPayload) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:98` `async fn is_mutating(&self, invocation: &ToolInvocation) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:110` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `impl` `codex-rs/core/src/tools/handlers/shell.rs:159` `impl ToolHandler for ShellCommandHandler {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:160` `fn kind(&self) -> ToolKind {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:164` `fn matches_kind(&self, payload: &ToolPayload) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:168` `async fn is_mutating(&self, invocation: &ToolInvocation) -> bool {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:182` `async fn handle(&self, invocation: ToolInvocation) -> Result<ToolOutput, FunctionCallError> {`
- `impl` `codex-rs/core/src/tools/handlers/shell.rs:215` `impl ShellHandler {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:216` `async fn run_exec_like(args: RunExecLikeArgs) -> Result<ToolOutput, FunctionCallError> {`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:328` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:329` `use std::sync::Arc;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:331` `use codex_protocol::models::ShellCommandToolCallParams;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:332` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:334` `use crate::codex::make_session_and_context;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:335` `use crate::exec_env::create_env;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:336` `use crate::is_safe_command::is_known_safe_command;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:337` `use crate::powershell::try_find_powershell_executable_blocking;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:338` `use crate::powershell::try_find_pwsh_executable_blocking;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:339` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:340` `use crate::shell::Shell;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:341` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:342` `use crate::shell_snapshot::ShellSnapshot;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:343` `use crate::tools::handlers::ShellCommandHandler;`
- `use` `codex-rs/core/src/tools/handlers/shell.rs:344` `use tokio::sync::watch;`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:350` `fn commands_generated_by_shell_command_handler_can_be_matched_by_is_known_safe_command() {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:384` `fn assert_safe(shell: &Shell, command: &str) {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:394` `async fn shell_command_handler_to_exec_params_uses_session_shell_and_turn_context() {`
- `fn` `codex-rs/core/src/tools/handlers/shell.rs:431` `fn shell_command_handler_respects_explicit_login_flag() {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use codex_protocol::models::ShellCommandToolCallParams;`
- `use codex_protocol::models::ShellToolCallParams;`
- `use std::sync::Arc;`
- `use crate::codex::TurnContext;`
- `use crate::exec::ExecParams;`
- `use crate::exec_env::create_env;`
- `use crate::exec_policy::ExecApprovalRequest;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::is_safe_command::is_known_safe_command;`
- `use crate::protocol::ExecCommandSource;`
- `use crate::shell::Shell;`
- `use crate::tools::context::ToolInvocation;`
- `use crate::tools::context::ToolOutput;`
- `use crate::tools::context::ToolPayload;`
- `use crate::tools::events::ToolEmitter;`
- `use crate::tools::events::ToolEventCtx;`
- `use crate::tools::handlers::apply_patch::intercept_apply_patch;`
- `use crate::tools::handlers::parse_arguments;`
- `use crate::tools::orchestrator::ToolOrchestrator;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
