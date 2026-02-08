# `codex-rs/core/tests/suite/approvals.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `69592`
- sha256: `231a5c8a25f8b16b52522fb4a517bd4427955d83080ffb54c72487b09072e697`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/approvals.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_core::config::Constrained;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::ApplyPatchApprovalRequestEvent;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecApprovalRequestEvent;`
- `use codex_core::protocol::ExecPolicyAmendment;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::protocol::ReviewDecision;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_apply_patch_function_call;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_once;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
