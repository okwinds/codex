# `codex-rs/app-server/tests/suite/v2/thread_unarchive.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4148`
- sha256: `d16f1110199ca63a65dcaf81698dc4c638d0813e28681e38e1670feace75b39b`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_unarchive.rs` (read)

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
- `use codex_app_server_protocol::ThreadArchiveParams;`
- `use codex_app_server_protocol::ThreadArchiveResponse;`
- `use codex_app_server_protocol::ThreadStartParams;`
- `use codex_app_server_protocol::ThreadStartResponse;`
- `use codex_app_server_protocol::ThreadUnarchiveParams;`
- `use codex_app_server_protocol::ThreadUnarchiveResponse;`
- `use codex_core::find_archived_thread_path_by_id_str;`
- `use codex_core::find_thread_path_by_id_str;`
- `use std::fs::FileTimes;`
- `use std::fs::OpenOptions;`
- `use std::path::Path;`
- `use std::time::Duration;`
- `use std::time::SystemTime;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
