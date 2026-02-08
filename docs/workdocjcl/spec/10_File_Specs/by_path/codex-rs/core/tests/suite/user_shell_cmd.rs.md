# `codex-rs/core/tests/suite/user_shell_cmd.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `15584`
- sha256: `bc59315d2f9e38350b761c8b68916ecccad33d47eea118d69d0d8655bed9011e`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/user_shell_cmd.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecCommandEndEvent;`
- `use codex_core::protocol::ExecCommandSource;`
- `use codex_core::protocol::ExecOutputStream;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::TurnAbortReason;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::responses;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::sse;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
