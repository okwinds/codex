# `codex-rs/core/tests/suite/turn_state.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4522`
- sha256: `a303641baa89a23780a6580c145420f37f879e29e662041a23634cded69befdf`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/turn_state.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use core_test_support::responses::WebSocketConnectionConfig;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_done;`
- `use core_test_support::responses::ev_reasoning_item;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::ev_shell_command_call;`
- `use core_test_support::responses::mount_response_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::sse_response;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::responses::start_websocket_server_with_headers;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
