# `codex-rs/core/src/tools/orchestrator.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7021`
- sha256: `0e146f0d7129313deb83cbb0e3d2c6b44088c3dade668bfece8bf25b08431631`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/orchestrator.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new() -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/orchestrator.rs:8` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:9` `use crate::error::SandboxErr;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:10` `use crate::exec::ExecToolCallOutput;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:11` `use crate::sandboxing::SandboxManager;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:12` `use crate::tools::sandboxing::ApprovalCtx;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:13` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:14` `use crate::tools::sandboxing::SandboxAttempt;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:15` `use crate::tools::sandboxing::SandboxOverride;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:16` `use crate::tools::sandboxing::ToolCtx;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:17` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:18` `use crate::tools::sandboxing::ToolRuntime;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:19` `use crate::tools::sandboxing::default_exec_approval_requirement;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:20` `use codex_otel::ToolDecisionSource;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:21` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:22` `use codex_protocol::protocol::ReviewDecision;`
- `impl` `codex-rs/core/src/tools/orchestrator.rs:28` `impl ToolOrchestrator {`
- `fn` `codex-rs/core/src/tools/orchestrator.rs:29` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/tools/orchestrator.rs:168` `fn build_denial_reason_from_output(_output: &ExecToolCallOutput) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::CodexErr;`
- `use crate::error::SandboxErr;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::sandboxing::SandboxManager;`
- `use crate::tools::sandboxing::ApprovalCtx;`
- `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use crate::tools::sandboxing::SandboxAttempt;`
- `use crate::tools::sandboxing::SandboxOverride;`
- `use crate::tools::sandboxing::ToolCtx;`
- `use crate::tools::sandboxing::ToolError;`
- `use crate::tools::sandboxing::ToolRuntime;`
- `use crate::tools::sandboxing::default_exec_approval_requirement;`
- `use codex_otel::ToolDecisionSource;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::ReviewDecision;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
