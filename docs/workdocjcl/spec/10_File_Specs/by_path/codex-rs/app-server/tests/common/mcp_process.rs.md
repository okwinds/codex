# `codex-rs/app-server/tests/common/mcp_process.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `29693`
- sha256: `99abba115015d4e67acb2b3595f82c83825cf82a5e1121fc14b954ae3f18c016`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/common/mcp_process.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct McpProcess {`
- `pub fn clear_message_buffer(&mut self) {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::VecDeque;`
- `use std::path::Path;`
- `use std::process::Stdio;`
- `use std::sync::atomic::AtomicI64;`
- `use std::sync::atomic::Ordering;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::io::AsyncWriteExt;`
- `use tokio::io::BufReader;`
- `use tokio::process::Child;`
- `use tokio::process::ChildStdin;`
- `use tokio::process::ChildStdout;`
- `use anyhow::Context;`
- `use codex_app_server_protocol::AddConversationListenerParams;`
- `use codex_app_server_protocol::AppsListParams;`
- `use codex_app_server_protocol::ArchiveConversationParams;`
- `use codex_app_server_protocol::CancelLoginAccountParams;`
- `use codex_app_server_protocol::CancelLoginChatGptParams;`
- `use codex_app_server_protocol::ClientInfo;`
- `use codex_app_server_protocol::ClientNotification;`
- `use codex_app_server_protocol::CollaborationModeListParams;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
