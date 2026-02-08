# `codex-rs/core/tests/suite/user_shell_cmd.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `11569`
- sha256: `3dd714cbd6d9906f2b12ca999fdf37ba986d9ebe59335c530045894b10d19c93`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecCommandEndEvent;`
- `use codex_core::protocol::ExecCommandSource;`
- `use codex_core::protocol::ExecOutputStream;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::TurnAbortReason;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::responses;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
