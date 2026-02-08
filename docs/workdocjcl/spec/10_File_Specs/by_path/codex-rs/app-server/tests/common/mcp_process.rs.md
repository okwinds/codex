# `codex-rs/app-server/tests/common/mcp_process.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `30832`
- sha256: `a75af5d6cafa2339ebd099cc3deee6090ab8dc0f934e1725c449721fe8e194a4`
- generated_utc: `2026-02-08T10:45:15Z`

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
