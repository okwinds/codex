# `codex-rs/exec/tests/event_processor_with_json_output.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `43891`
- sha256: `e5da8eea493a22a0801398917f7eb8efdf1f3c62f292425d02ed5d2649e2bbc2`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/tests/event_processor_with_json_output.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::protocol::AgentMessageEvent;`
- `use codex_core::protocol::AgentReasoningEvent;`
- `use codex_core::protocol::AgentStatus;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::CollabAgentSpawnBeginEvent;`
- `use codex_core::protocol::CollabAgentSpawnEndEvent;`
- `use codex_core::protocol::CollabWaitingEndEvent;`
- `use codex_core::protocol::ErrorEvent;`
- `use codex_core::protocol::Event;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecCommandBeginEvent;`
- `use codex_core::protocol::ExecCommandEndEvent;`
- `use codex_core::protocol::ExecCommandSource;`
- `use codex_core::protocol::FileChange;`
- `use codex_core::protocol::McpInvocation;`
- `use codex_core::protocol::McpToolCallBeginEvent;`
- `use codex_core::protocol::McpToolCallEndEvent;`
- `use codex_core::protocol::PatchApplyBeginEvent;`
- `use codex_core::protocol::PatchApplyEndEvent;`
- `use codex_core::protocol::SandboxPolicy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
