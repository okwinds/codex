# `codex-rs/app-server/tests/suite/config.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5522`
- sha256: `79464b7a40981c67d0500eeae9f65a58624a253d47a26cda6c60151ddc9f711b`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/config.rs` (read)

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
- `use app_test_support::test_tmp_path;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::GetUserSavedConfigResponse;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::Profile;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SandboxSettings;`
- `use codex_app_server_protocol::Tools;`
- `use codex_app_server_protocol::UserSavedConfig;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_protocol::config_types::ForcedLoginMethod;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::config_types::SandboxMode;`
- `use codex_protocol::config_types::Verbosity;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
