# `codex-rs/app-server/tests/suite/v2/model_list.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `11068`
- sha256: `7e0b24f99a2cd2b605e985537f207cb5cdc49ce65eb79359f05c332a31b39f9f`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/model_list.rs` (read)

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
- `use anyhow::anyhow;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use app_test_support::write_models_cache;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::Model;`
- `use codex_app_server_protocol::ModelListParams;`
- `use codex_app_server_protocol::ModelListResponse;`
- `use codex_app_server_protocol::ReasoningEffortOption;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_protocol::openai_models::InputModality;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
