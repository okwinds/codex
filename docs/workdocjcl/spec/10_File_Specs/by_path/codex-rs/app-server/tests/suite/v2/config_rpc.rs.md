# `codex-rs/app-server/tests/suite/v2/config_rpc.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `16966`
- sha256: `6e8f1033dddb3250e2049abb7a49eb32aa3ab799be82ebaaaf94ab8c88c268be`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/config_rpc.rs` (read)

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
- `use app_test_support::test_path_buf_with_windows;`
- `use app_test_support::test_tmp_path_buf;`
- `use app_test_support::to_response;`
- `use codex_app_server_protocol::AskForApproval;`
- `use codex_app_server_protocol::ConfigBatchWriteParams;`
- `use codex_app_server_protocol::ConfigEdit;`
- `use codex_app_server_protocol::ConfigLayerSource;`
- `use codex_app_server_protocol::ConfigReadParams;`
- `use codex_app_server_protocol::ConfigReadResponse;`
- `use codex_app_server_protocol::ConfigValueWriteParams;`
- `use codex_app_server_protocol::ConfigWriteResponse;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::MergeStrategy;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SandboxMode;`
- `use codex_app_server_protocol::ToolsV2;`
- `use codex_app_server_protocol::WriteStatus;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
