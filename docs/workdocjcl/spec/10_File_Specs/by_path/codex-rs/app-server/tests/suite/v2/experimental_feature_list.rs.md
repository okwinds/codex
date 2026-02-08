# `codex-rs/app-server/tests/suite/v2/experimental_feature_list.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2777`
- sha256: `9f3e284b42adc45103fcf97059340d5805c855e5f3900a687d8d6937d79bf40c`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/experimental_feature_list.rs` (read)

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
- `use codex_app_server_protocol::ExperimentalFeature;`
- `use codex_app_server_protocol::ExperimentalFeatureListParams;`
- `use codex_app_server_protocol::ExperimentalFeatureListResponse;`
- `use codex_app_server_protocol::ExperimentalFeatureStage;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_core::features::FEATURES;`
- `use codex_core::features::Stage;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
