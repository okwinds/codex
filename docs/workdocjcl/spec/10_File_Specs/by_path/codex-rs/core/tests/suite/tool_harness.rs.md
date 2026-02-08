# `codex-rs/core/tests/suite/tool_harness.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `14598`
- sha256: `962e59be2e5694e0360ef684f755864237fe272cb4f98ea5226723087ba08c7a`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/tool_harness.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs;`
- `use assert_matches::assert_matches;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::plan_tool::StepStatus;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::responses;`
- `use core_test_support::responses::ResponsesRequest;`
- `use core_test_support::responses::ev_apply_patch_function_call;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_local_shell_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::sse;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
