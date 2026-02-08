# `codex-rs/app-server/tests/suite/v2/collaboration_mode_list.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2617`
- sha256: `b63ce5045d32e1d137329cc18945c61f3852e317dab1efa964bef9f907634238`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/collaboration_mode_list.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::CollaborationModeListParams;`
- `use codex_app_server_protocol::CollaborationModeListResponse;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_core::models_manager::test_builtin_collaboration_mode_presets;`
- `use codex_protocol::config_types::CollaborationModeMask;`
- `use codex_protocol::config_types::ModeKind;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
