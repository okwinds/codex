# `codex-rs/core/src/tools/runtimes/unified_exec.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6679`
- sha256: `28b15933f2c2f7c8e1f31352401fa374ffe0155c88a4e49179f5d196959fda3b`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/runtimes/unified_exec.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct UnifiedExecRequest {`
- `pub struct UnifiedExecApprovalKey {`
- `pub struct UnifiedExecRuntime<'a> {`
- `pub fn new(`
- `pub fn new(manager: &'a UnifiedExecProcessManager) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:7` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:8` `use crate::error::SandboxErr;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:9` `use crate::exec::ExecExpiration;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:10` `use crate::features::Feature;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:11` `use crate::powershell::prefix_powershell_script_with_utf8;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:12` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:13` `use crate::shell::ShellType;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:14` `use crate::tools::runtimes::build_command_spec;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:15` `use crate::tools::runtimes::maybe_wrap_shell_lc_with_snapshot;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:16` `use crate::tools::sandboxing::Approvable;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:17` `use crate::tools::sandboxing::ApprovalCtx;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:18` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:19` `use crate::tools::sandboxing::SandboxAttempt;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:20` `use crate::tools::sandboxing::SandboxOverride;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:21` `use crate::tools::sandboxing::Sandboxable;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:22` `use crate::tools::sandboxing::SandboxablePreference;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:23` `use crate::tools::sandboxing::ToolCtx;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:24` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:25` `use crate::tools::sandboxing::ToolRuntime;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:26` `use crate::tools::sandboxing::with_cached_approval;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:27` `use crate::unified_exec::UnifiedExecError;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:28` `use crate::unified_exec::UnifiedExecProcess;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:29` `use crate::unified_exec::UnifiedExecProcessManager;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:30` `use codex_protocol::protocol::ReviewDecision;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:31` `use futures::future::BoxFuture;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:32` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/runtimes/unified_exec.rs:33` `use std::path::PathBuf;`
- `struct` `codex-rs/core/src/tools/runtimes/unified_exec.rs:36` `pub struct UnifiedExecRequest {`
- `struct` `codex-rs/core/src/tools/runtimes/unified_exec.rs:47` `pub struct UnifiedExecApprovalKey {`
- `struct` `codex-rs/core/src/tools/runtimes/unified_exec.rs:54` `pub struct UnifiedExecRuntime<'a> {`
- `impl` `codex-rs/core/src/tools/runtimes/unified_exec.rs:58` `impl UnifiedExecRequest {`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:59` `pub fn new(`
- `impl` `codex-rs/core/src/tools/runtimes/unified_exec.rs:80` `impl<'a> UnifiedExecRuntime<'a> {`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:81` `pub fn new(manager: &'a UnifiedExecProcessManager) -> Self {`
- `impl` `codex-rs/core/src/tools/runtimes/unified_exec.rs:86` `impl Sandboxable for UnifiedExecRuntime<'_> {`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:87` `fn sandbox_preference(&self) -> SandboxablePreference {`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:91` `fn escalate_on_failure(&self) -> bool {`
- `impl` `codex-rs/core/src/tools/runtimes/unified_exec.rs:96` `impl Approvable<UnifiedExecRequest> for UnifiedExecRuntime<'_> {`
- `type` `codex-rs/core/src/tools/runtimes/unified_exec.rs:97` `type ApprovalKey = UnifiedExecApprovalKey;`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:99` `fn approval_keys(&self, req: &UnifiedExecRequest) -> Vec<Self::ApprovalKey> {`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:142` `fn exec_approval_requirement(`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:149` `fn sandbox_mode_for_first_attempt(&self, req: &UnifiedExecRequest) -> SandboxOverride {`
- `impl` `codex-rs/core/src/tools/runtimes/unified_exec.rs:166` `impl<'a> ToolRuntime<UnifiedExecRequest, UnifiedExecProcess> for UnifiedExecRuntime<'a> {`
- `fn` `codex-rs/core/src/tools/runtimes/unified_exec.rs:167` `async fn run(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::CodexErr;`
- `use crate::error::SandboxErr;`
- `use crate::exec::ExecExpiration;`
- `use crate::features::Feature;`
- `use crate::powershell::prefix_powershell_script_with_utf8;`
- `use crate::sandboxing::SandboxPermissions;`
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
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
