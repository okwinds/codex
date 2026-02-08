# `codex-rs/core/src/tools/runtimes/shell.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5577`
- sha256: `4f20d6530b472847f611ed172febe640c3e5f08133f89c7d3c2ed22ae9e7e0e6`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/runtimes/shell.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ShellRequest {`
- `pub struct ShellRuntime;`
- `pub fn new() -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:7` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:8` `use crate::features::Feature;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:9` `use crate::powershell::prefix_powershell_script_with_utf8;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:10` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:11` `use crate::sandboxing::execute_env;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:12` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:13` `use crate::tools::runtimes::build_command_spec;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:14` `use crate::tools::runtimes::maybe_wrap_shell_lc_with_snapshot;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:15` `use crate::tools::sandboxing::Approvable;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:16` `use crate::tools::sandboxing::ApprovalCtx;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:17` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:18` `use crate::tools::sandboxing::SandboxAttempt;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:19` `use crate::tools::sandboxing::SandboxOverride;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:20` `use crate::tools::sandboxing::Sandboxable;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:21` `use crate::tools::sandboxing::SandboxablePreference;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:22` `use crate::tools::sandboxing::ToolCtx;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:23` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:24` `use crate::tools::sandboxing::ToolRuntime;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:25` `use crate::tools::sandboxing::with_cached_approval;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:26` `use codex_protocol::protocol::ReviewDecision;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:27` `use futures::future::BoxFuture;`
- `use` `codex-rs/core/src/tools/runtimes/shell.rs:28` `use std::path::PathBuf;`
- `struct` `codex-rs/core/src/tools/runtimes/shell.rs:31` `pub struct ShellRequest {`
- `struct` `codex-rs/core/src/tools/runtimes/shell.rs:42` `pub struct ShellRuntime;`
- `impl` `codex-rs/core/src/tools/runtimes/shell.rs:51` `impl ShellRuntime {`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:52` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:56` `fn stdout_stream(ctx: &ToolCtx<'_>) -> Option<crate::exec::StdoutStream> {`
- `impl` `codex-rs/core/src/tools/runtimes/shell.rs:65` `impl Sandboxable for ShellRuntime {`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:66` `fn sandbox_preference(&self) -> SandboxablePreference {`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:69` `fn escalate_on_failure(&self) -> bool {`
- `impl` `codex-rs/core/src/tools/runtimes/shell.rs:74` `impl Approvable<ShellRequest> for ShellRuntime {`
- `type` `codex-rs/core/src/tools/runtimes/shell.rs:75` `type ApprovalKey = ApprovalKey;`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:77` `fn approval_keys(&self, req: &ShellRequest) -> Vec<Self::ApprovalKey> {`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:119` `fn exec_approval_requirement(&self, req: &ShellRequest) -> Option<ExecApprovalRequirement> {`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:123` `fn sandbox_mode_for_first_attempt(&self, req: &ShellRequest) -> SandboxOverride {`
- `impl` `codex-rs/core/src/tools/runtimes/shell.rs:140` `impl ToolRuntime<ShellRequest, ExecToolCallOutput> for ShellRuntime {`
- `fn` `codex-rs/core/src/tools/runtimes/shell.rs:141` `async fn run(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec::ExecToolCallOutput;`
- `use crate::features::Feature;`
- `use crate::powershell::prefix_powershell_script_with_utf8;`
- `use crate::sandboxing::SandboxPermissions;`
- `use crate::sandboxing::execute_env;`
- `use crate::shell::ShellType;`
- `use crate::tools::runtimes::build_command_spec;`
- `use crate::tools::runtimes::maybe_wrap_shell_lc_with_snapshot;`
- `use crate::tools::sandboxing::Approvable;`
- `use crate::tools::sandboxing::ApprovalCtx;`
- `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use crate::tools::sandboxing::SandboxAttempt;`
- `use crate::tools::sandboxing::SandboxOverride;`
- `use crate::tools::sandboxing::Sandboxable;`
- `use crate::tools::sandboxing::SandboxablePreference;`
- `use crate::tools::sandboxing::ToolCtx;`
- `use crate::tools::sandboxing::ToolError;`
- `use crate::tools::sandboxing::ToolRuntime;`
- `use crate::tools::sandboxing::with_cached_approval;`
- `use codex_protocol::protocol::ReviewDecision;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
