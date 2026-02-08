# `codex-rs/app-server/tests/suite/fuzzy_file_search.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4027`
- sha256: `965dd863055418432553808f22a805dc05d4eccda2e5cb682d42ea86e520d017`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/fuzzy_file_search.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use anyhow::anyhow;`
- `use app_test_support::McpProcess;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::json;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
