# `codex-rs/core/tests/suite/tool_parallelism.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `13711`
- sha256: `99a272dfe0cb104ff27a943aefd75094e8e367ebcf70cacfd9fd89f8d1ba03b9`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/tool_parallelism.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::ev_shell_command_call_with_args;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::streaming_sse::StreamingSseChunk;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
