# `codex-rs/core/tests/suite/agent_websocket.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2173`
- sha256: `b82e330db3aa16094a26bb28a3a0add5c756e73300f2477236d34f9707b3d09d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/agent_websocket.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_done;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::ev_shell_command_call;`
- `use core_test_support::responses::start_websocket_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
