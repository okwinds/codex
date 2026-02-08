# `codex-rs/core/src/tools/orchestrator.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7224`
- sha256: `358c09f42d02a3f5b7721590089d2bceec5ff5fb7833be6daeee48467441e21e`
- generated_utc: `2026-02-08T10:45:33Z`

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
- `use` `codex-rs/core/src/tools/orchestrator.rs:11` `use crate::features::Feature;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:12` `use crate::sandboxing::SandboxManager;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:13` `use crate::tools::sandboxing::ApprovalCtx;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:14` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:15` `use crate::tools::sandboxing::SandboxAttempt;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:16` `use crate::tools::sandboxing::SandboxOverride;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:17` `use crate::tools::sandboxing::ToolCtx;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:18` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:19` `use crate::tools::sandboxing::ToolRuntime;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:20` `use crate::tools::sandboxing::default_exec_approval_requirement;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:21` `use codex_otel::ToolDecisionSource;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:22` `use codex_protocol::protocol::AskForApproval;`
- `use` `codex-rs/core/src/tools/orchestrator.rs:23` `use codex_protocol::protocol::ReviewDecision;`
- `impl` `codex-rs/core/src/tools/orchestrator.rs:29` `impl ToolOrchestrator {`
- `fn` `codex-rs/core/src/tools/orchestrator.rs:30` `pub fn new() -> Self {`
- `fn` `codex-rs/core/src/tools/orchestrator.rs:172` `fn build_denial_reason_from_output(_output: &ExecToolCallOutput) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::CodexErr;`
- `use crate::error::SandboxErr;`
- `use crate::exec::ExecToolCallOutput;`
- `use crate::features::Feature;`
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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
