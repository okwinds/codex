# `codex-rs/core/tests/suite/otel.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `38196`
- sha256: `94e5fb2439246cf8b7817eb0498e41a45bd824d97e283b051a3c41af1aeb819d`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/otel.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::Constrained;`
- `use codex_core::features::Feature;`
- `use codex_protocol::protocol::AskForApproval;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::Op;`
- `use codex_protocol::protocol::ReviewDecision;`
- `use codex_protocol::protocol::SandboxPolicy;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_custom_tool_call;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_local_shell_call;`
- `use core_test_support::responses::ev_message_item_added;`
- `use core_test_support::responses::ev_output_text_delta;`
- `use core_test_support::responses::ev_reasoning_item;`
- `use core_test_support::responses::ev_reasoning_summary_text_delta;`
- `use core_test_support::responses::ev_reasoning_text_delta;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_response_once;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
