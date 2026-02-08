# `codex-rs/app-server/tests/suite/set_default_model.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2006`
- sha256: `07f98205fb80c7eeabdd2ba8efb84912cfa2c03cb552eb6370c5afb2e039226c`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/set_default_model.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SetDefaultModelParams;`
- `use codex_app_server_protocol::SetDefaultModelResponse;`
- `use codex_core::config::ConfigToml;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
