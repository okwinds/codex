# `codex-rs/core/tests/suite/codex_delegate.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `8220`
- sha256: `f7af728dab7d25253b4c61042fe357a4bd767032bd12de5aff17704856223c2f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/codex_delegate.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::Constrained;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::ReviewDecision;`
- `use codex_core::protocol::ReviewRequest;`
- `use codex_core::protocol::ReviewTarget;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use core_test_support::responses::ev_apply_patch_function_call;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_reasoning_item_added;`
- `use core_test_support::responses::ev_reasoning_summary_text_delta;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
