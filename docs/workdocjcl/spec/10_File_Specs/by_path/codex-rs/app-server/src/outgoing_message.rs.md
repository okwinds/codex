# `codex-rs/app-server/src/outgoing_message.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12163`
- sha256: `a04998e419bdddaa6575c8a80e4c2534a5fe1b554bc51622ab554f96443aee83`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/outgoing_message.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/outgoing_message.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:2` `use std::sync::atomic::AtomicI64;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:3` `use std::sync::atomic::Ordering;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:5` `use codex_app_server_protocol::JSONRPCErrorError;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:6` `use codex_app_server_protocol::RequestId;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:7` `use codex_app_server_protocol::Result;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:8` `use codex_app_server_protocol::ServerNotification;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:9` `use codex_app_server_protocol::ServerRequest;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:10` `use codex_app_server_protocol::ServerRequestPayload;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:11` `use serde::Serialize;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:12` `use tokio::sync::Mutex;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:13` `use tokio::sync::mpsc;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:14` `use tokio::sync::oneshot;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:15` `use tracing::warn;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:17` `use crate::error_code::INTERNAL_ERROR_CODE;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:20` `use codex_protocol::account::PlanType;`
- `impl` `codex-rs/app-server/src/outgoing_message.rs:29` `impl OutgoingMessageSender {`
- `use` `codex-rs/app-server/src/outgoing_message.rs:193` `use codex_app_server_protocol::AccountLoginCompletedNotification;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:194` `use codex_app_server_protocol::AccountRateLimitsUpdatedNotification;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:195` `use codex_app_server_protocol::AccountUpdatedNotification;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:196` `use codex_app_server_protocol::AuthMode;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:197` `use codex_app_server_protocol::ConfigWarningNotification;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:198` `use codex_app_server_protocol::LoginChatGptCompleteNotification;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:199` `use codex_app_server_protocol::RateLimitSnapshot;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:200` `use codex_app_server_protocol::RateLimitWindow;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:201` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:202` `use serde_json::json;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:203` `use uuid::Uuid;`
- `use` `codex-rs/app-server/src/outgoing_message.rs:205` `use super::*;`
- `fn` `codex-rs/app-server/src/outgoing_message.rs:208` `fn verify_server_notification_serialization() {`
- `fn` `codex-rs/app-server/src/outgoing_message.rs:233` `fn verify_account_login_completed_notification_serialization() {`
- `fn` `codex-rs/app-server/src/outgoing_message.rs:258` `fn verify_account_rate_limits_notification_serialization() {`
- `fn` `codex-rs/app-server/src/outgoing_message.rs:297` `fn verify_account_updated_notification_serialization() {`
- `fn` `codex-rs/app-server/src/outgoing_message.rs:317` `fn verify_config_warning_notification_serialization() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::sync::atomic::AtomicI64;`
- `use std::sync::atomic::Ordering;`
- `use codex_app_server_protocol::JSONRPCErrorError;`
- `use codex_app_server_protocol::RequestId;`
- `use codex_app_server_protocol::Result;`
- `use codex_app_server_protocol::ServerNotification;`
- `use codex_app_server_protocol::ServerRequest;`
- `use codex_app_server_protocol::ServerRequestPayload;`
- `use serde::Serialize;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::mpsc;`
- `use tokio::sync::oneshot;`
- `use tracing::warn;`
- `use crate::error_code::INTERNAL_ERROR_CODE;`
- `use codex_protocol::account::PlanType;`
- `use codex_app_server_protocol::AccountLoginCompletedNotification;`
- `use codex_app_server_protocol::AccountRateLimitsUpdatedNotification;`
- `use codex_app_server_protocol::AccountUpdatedNotification;`
- `use codex_app_server_protocol::AuthMode;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
