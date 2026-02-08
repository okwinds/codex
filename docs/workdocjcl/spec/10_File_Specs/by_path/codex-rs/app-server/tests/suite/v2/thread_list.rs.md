# `codex-rs/app-server/tests/suite/v2/thread_list.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `31285`
- sha256: `709976acad6e7973611883dcb6241910d20ad03cbfbb83709c2e9fd5db2352dc`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/thread_list.rs` (read)

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
- `use app_test_support::create_fake_rollout;`
- `use app_test_support::create_fake_rollout_with_source;`
- `use app_test_support::rollout_path;`
- `use app_test_support::to_response;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_app_server_protocol::GitInfo as ApiGitInfo;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::SessionSource;`
- `use codex_app_server_protocol::ThreadListResponse;`
- `use codex_app_server_protocol::ThreadSortKey;`
- `use codex_app_server_protocol::ThreadSourceKind;`
- `use codex_core::ARCHIVED_SESSIONS_SUBDIR;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::GitInfo as CoreGitInfo;`
- `use codex_protocol::protocol::SessionSource as CoreSessionSource;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
