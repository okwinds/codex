# `codex-rs/core/src/tools/runtimes/apply_patch.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5652`
- sha256: `031e03e87e3c6b5182e18507216407f095c9632feaf72b37e968899817e0daf5`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/runtimes/apply_patch.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ApplyPatchRequest {`
- `pub struct ApplyPatchRuntime;`
- `pub fn new() -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:7` `use crate::CODEX_APPLY_PATCH_ARG1;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:8` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:9` `use crate::sandboxing::CommandSpec;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:10` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:11` `use crate::sandboxing::execute_env;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:12` `use crate::tools::sandboxing::Approvable;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:13` `use crate::tools::sandboxing::ApprovalCtx;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:14` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:15` `use crate::tools::sandboxing::SandboxAttempt;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:16` `use crate::tools::sandboxing::Sandboxable;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:17` `use crate::tools::sandboxing::SandboxablePreference;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:18` `use crate::tools::sandboxing::ToolCtx;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:19` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:20` `use crate::tools::sandboxing::ToolRuntime;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:21` `use crate::tools::sandboxing::with_cached_approval;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:22` `use codex_apply_patch::ApplyPatchAction;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:23` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:24` `use codex_protocol::protocol::FileChange;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:25` `use codex_protocol::protocol::ReviewDecision;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:26` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:27` `use futures::future::BoxFuture;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:28` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:29` `use std::path::PathBuf;`
- `struct` `codex-rs/core/src/tools/runtimes/apply_patch.rs:32` `pub struct ApplyPatchRequest {`
- `struct` `codex-rs/core/src/tools/runtimes/apply_patch.rs:42` `pub struct ApplyPatchRuntime;`
- `impl` `codex-rs/core/src/tools/runtimes/apply_patch.rs:44` `impl ApplyPatchRuntime {`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:45` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:49` `fn build_command_spec(req: &ApplyPatchRequest) -> Result<CommandSpec, ToolError> {`
- `use` `codex-rs/core/src/tools/runtimes/apply_patch.rs:50` `use std::env;`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:70` `fn stdout_stream(ctx: &ToolCtx<'_>) -> Option<crate::exec::StdoutStream> {`
- `impl` `codex-rs/core/src/tools/runtimes/apply_patch.rs:79` `impl Sandboxable for ApplyPatchRuntime {`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:80` `fn sandbox_preference(&self) -> SandboxablePreference {`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:83` `fn escalate_on_failure(&self) -> bool {`
- `impl` `codex-rs/core/src/tools/runtimes/apply_patch.rs:88` `impl Approvable<ApplyPatchRequest> for ApplyPatchRuntime {`
- `type` `codex-rs/core/src/tools/runtimes/apply_patch.rs:89` `type ApprovalKey = AbsolutePathBuf;`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:91` `fn approval_keys(&self, req: &ApplyPatchRequest) -> Vec<Self::ApprovalKey> {`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:129` `fn wants_no_sandbox_approval(&self, policy: AskForApproval) -> bool {`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:137` `fn exec_approval_requirement(`
- `impl` `codex-rs/core/src/tools/runtimes/apply_patch.rs:145` `impl ToolRuntime<ApplyPatchRequest, ExecToolCallOutput> for ApplyPatchRuntime {`
- `fn` `codex-rs/core/src/tools/runtimes/apply_patch.rs:146` `async fn run(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::CODEX_APPLY_PATCH_ARG1;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::sandboxing::CommandSpec;`
- `use crate::sandboxing::SandboxPermissions;`
- `use crate::sandboxing::execute_env;`
- `use crate::tools::sandboxing::Approvable;`
- `use crate::tools::sandboxing::ApprovalCtx;`
- `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use crate::tools::sandboxing::SandboxAttempt;`
- `use crate::tools::sandboxing::Sandboxable;`
- `use crate::tools::sandboxing::SandboxablePreference;`
- `use crate::tools::sandboxing::ToolCtx;`
- `use crate::tools::sandboxing::ToolError;`
- `use crate::tools::sandboxing::ToolRuntime;`
- `use crate::tools::sandboxing::with_cached_approval;`
- `use codex_apply_patch::ApplyPatchAction;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::FileChange;`
- `use codex_protocol::protocol::ReviewDecision;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
