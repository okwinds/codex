# `codex-rs/app-server/tests/suite/v2/app_list.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `12102`
- sha256: `0e34e8aee455f11fbb031105874a06c5f818798812c71f1beb83a11d67406095`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/app_list.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::borrow::Cow;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use app_test_support::ChatGptAuthFixture;`
- `use app_test_support::McpProcess;`
- `use app_test_support::to_response;`
- `use app_test_support::write_chatgpt_auth;`
- `use axum::Json;`
- `use axum::Router;`
- `use axum::extract::State;`
- `use axum::http::HeaderMap;`
- `use axum::http::StatusCode;`
- `use axum::http::header::AUTHORIZATION;`
- `use axum::routing::get;`
- `use codex_app_server_protocol::AppInfo;`
- `use codex_app_server_protocol::AppsListParams;`
- `use codex_app_server_protocol::AppsListResponse;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
