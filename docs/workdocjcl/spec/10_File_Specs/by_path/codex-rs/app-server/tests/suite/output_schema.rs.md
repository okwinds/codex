# `codex-rs/app-server/tests/suite/output_schema.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `9240`
- sha256: `5ebd1b9f0c7e13d0a64cb35b1a91a67b8377322499e473e80ab839a61e7206df`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/output_schema.rs` (read)

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
- `use codex_app_server_protocol::AddConversationListenerParams;`
- `use codex_app_server_protocol::InputItem;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::NewConversationParams;`
- `use codex_app_server_protocol::NewConversationResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SendUserTurnParams;`
- `use codex_app_server_protocol::SendUserTurnResponse;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use core_test_support::responses;`
- `use core_test_support::skip_if_no_network;`
- `use pretty_assertions::assert_eq;`
- `use std::path::Path;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
