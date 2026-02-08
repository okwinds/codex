# `codex-rs/core/tests/suite/agent_websocket.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6069`
- sha256: `29e62405285c2120635fcb1c60913a7ccfd04581b2a77541a173b86fcd5da142`
- generated_utc: `2026-02-08T10:45:34Z`

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
- `use codex_core::features::Feature;`
- `use core_test_support::responses::WebSocketConnectionConfig;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_done;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::ev_shell_command_call;`
- `use core_test_support::responses::start_websocket_server;`
- `use core_test_support::responses::start_websocket_server_with_headers;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
