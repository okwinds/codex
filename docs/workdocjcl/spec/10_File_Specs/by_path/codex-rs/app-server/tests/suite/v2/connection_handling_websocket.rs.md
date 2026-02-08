# `codex-rs/app-server/tests/suite/v2/connection_handling_websocket.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `8687`
- sha256: `0a081b92bed55b305ed9ba6a4a891df56712dd3c2224254a1990df1c79acbaa4`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/connection_handling_websocket.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::bail;`
- `use app_test_support::create_mock_responses_server_sequence_unchecked;`
- `use codex_app_server_protocol::ClientInfo;`
- `use codex_app_server_protocol::InitializeParams;`
- `use codex_app_server_protocol::JSONRPCError;`
- `use codex_app_server_protocol::JSONRPCMessage;`
- `use codex_app_server_protocol::JSONRPCRequest;`
- `use codex_app_server_protocol::JSONRPCResponse;`
- `use codex_app_server_protocol::RequestId;`
- `use futures::SinkExt;`
- `use futures::StreamExt;`
- `use serde_json::json;`
- `use std::net::SocketAddr;`
- `use std::path::Path;`
- `use std::process::Stdio;`
- `use tempfile::TempDir;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::process::Child;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
