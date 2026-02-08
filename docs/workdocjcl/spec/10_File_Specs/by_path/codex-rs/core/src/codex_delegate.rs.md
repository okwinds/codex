# `codex-rs/core/src/codex_delegate.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17012`
- sha256: `72b88c7c03664d9a5b0d2996dc1df7b145dec15e4843b7c3090a320f5dcf4a47`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/codex_delegate.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/codex_delegate.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/codex_delegate.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/codex_delegate.rs:3` `use std::sync::atomic::AtomicU64;`
- `use` `codex-rs/core/src/codex_delegate.rs:5` `use async_channel::Receiver;`
- `use` `codex-rs/core/src/codex_delegate.rs:6` `use async_channel::Sender;`
- `use` `codex-rs/core/src/codex_delegate.rs:7` `use codex_async_utils::OrCancelExt;`
- `use` `codex-rs/core/src/codex_delegate.rs:8` `use codex_protocol::protocol::ApplyPatchApprovalRequestEvent;`
- `use` `codex-rs/core/src/codex_delegate.rs:9` `use codex_protocol::protocol::Event;`
- `use` `codex-rs/core/src/codex_delegate.rs:10` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/core/src/codex_delegate.rs:11` `use codex_protocol::protocol::ExecApprovalRequestEvent;`
- `use` `codex-rs/core/src/codex_delegate.rs:12` `use codex_protocol::protocol::Op;`
- `use` `codex-rs/core/src/codex_delegate.rs:13` `use codex_protocol::protocol::RequestUserInputEvent;`
- `use` `codex-rs/core/src/codex_delegate.rs:14` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/core/src/codex_delegate.rs:15` `use codex_protocol::protocol::SubAgentSource;`
- `use` `codex-rs/core/src/codex_delegate.rs:16` `use codex_protocol::protocol::Submission;`
- `use` `codex-rs/core/src/codex_delegate.rs:17` `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use` `codex-rs/core/src/codex_delegate.rs:18` `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use` `codex-rs/core/src/codex_delegate.rs:19` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/codex_delegate.rs:20` `use std::time::Duration;`
- `use` `codex-rs/core/src/codex_delegate.rs:21` `use tokio::time::timeout;`
- `use` `codex-rs/core/src/codex_delegate.rs:22` `use tokio_util::sync::CancellationToken;`
- `use` `codex-rs/core/src/codex_delegate.rs:24` `use crate::AuthManager;`
- `use` `codex-rs/core/src/codex_delegate.rs:25` `use crate::codex::Codex;`
- `use` `codex-rs/core/src/codex_delegate.rs:26` `use crate::codex::CodexSpawnOk;`
- `use` `codex-rs/core/src/codex_delegate.rs:27` `use crate::codex::SUBMISSION_CHANNEL_CAPACITY;`
- `use` `codex-rs/core/src/codex_delegate.rs:28` `use crate::codex::Session;`
- `use` `codex-rs/core/src/codex_delegate.rs:29` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/codex_delegate.rs:30` `use crate::config::Config;`
- `use` `codex-rs/core/src/codex_delegate.rs:31` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/codex_delegate.rs:32` `use crate::models_manager::manager::ModelsManager;`
- `use` `codex-rs/core/src/codex_delegate.rs:33` `use codex_protocol::protocol::InitialHistory;`
- `fn` `codex-rs/core/src/codex_delegate.rs:176` `async fn forward_events(`
- `fn` `codex-rs/core/src/codex_delegate.rs:274` `async fn shutdown_delegate(codex: &Codex) {`
- `fn` `codex-rs/core/src/codex_delegate.rs:292` `async fn forward_ops(`
- `fn` `codex-rs/core/src/codex_delegate.rs:307` `async fn handle_exec_approval(`
- `fn` `codex-rs/core/src/codex_delegate.rs:336` `async fn handle_patch_approval(`
- `fn` `codex-rs/core/src/codex_delegate.rs:363` `async fn handle_request_user_input(`
- `use` `codex-rs/core/src/codex_delegate.rs:438` `use super::*;`
- `use` `codex-rs/core/src/codex_delegate.rs:439` `use async_channel::bounded;`
- `use` `codex-rs/core/src/codex_delegate.rs:440` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/codex_delegate.rs:441` `use codex_protocol::protocol::AgentStatus;`
- `use` `codex-rs/core/src/codex_delegate.rs:442` `use codex_protocol::protocol::RawResponseItemEvent;`
- `use` `codex-rs/core/src/codex_delegate.rs:443` `use codex_protocol::protocol::TurnAbortReason;`
- `use` `codex-rs/core/src/codex_delegate.rs:444` `use codex_protocol::protocol::TurnAbortedEvent;`
- `use` `codex-rs/core/src/codex_delegate.rs:445` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/codex_delegate.rs:446` `use tokio::sync::watch;`
- `fn` `codex-rs/core/src/codex_delegate.rs:449` `async fn forward_events_cancelled_while_send_blocked_shuts_down_delegate() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicU64;`
- `use async_channel::Receiver;`
- `use async_channel::Sender;`
- `use codex_async_utils::OrCancelExt;`
- `use codex_protocol::protocol::ApplyPatchApprovalRequestEvent;`
- `use codex_protocol::protocol::Event;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::ExecApprovalRequestEvent;`
- `use codex_protocol::protocol::Op;`
- `use codex_protocol::protocol::RequestUserInputEvent;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::protocol::SubAgentSource;`
- `use codex_protocol::protocol::Submission;`
- `use codex_protocol::request_user_input::RequestUserInputArgs;`
- `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use codex_protocol::user_input::UserInput;`
- `use std::time::Duration;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
