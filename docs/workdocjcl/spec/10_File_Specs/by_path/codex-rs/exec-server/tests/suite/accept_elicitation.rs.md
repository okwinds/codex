# `codex-rs/exec-server/tests/suite/accept_elicitation.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6677`
- sha256: `351049b01c3cf007cc7bf4adc11a3872955df646124b5bcb0089a645ff911946`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/tests/suite/accept_elicitation.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::borrow::Cow;`
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::sync::Mutex;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::ensure;`
- `use codex_exec_server::ExecResult;`
- `use exec_server_test_support::InteractiveClient;`
- `use exec_server_test_support::create_transport;`
- `use exec_server_test_support::notify_readable_sandbox;`
- `use exec_server_test_support::write_default_execpolicy;`
- `use maplit::hashset;`
- `use pretty_assertions::assert_eq;`
- `use rmcp::ServiceExt;`
- `use rmcp::model::CallToolRequestParam;`
- `use rmcp::model::CallToolResult;`
- `use rmcp::model::CreateElicitationRequestParam;`
- `use rmcp::model::EmptyResult;`
- `use rmcp::model::ServerResult;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
