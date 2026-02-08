# `codex-rs/core/src/hooks/user_notification.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4643`
- sha256: `47ab95dbd093e397f4ae5b49411b6c7d154893cb3b32da0403e9a7acc77dd295`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/hooks/user_notification.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/hooks/user_notification.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:3` `use serde::Serialize;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:4` `use std::path::Path;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:5` `use std::process::Stdio;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:7` `use super::registry::command_from_argv;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:8` `use super::types::Hook;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:9` `use super::types::HookEvent;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:10` `use super::types::HookOutcome;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:11` `use super::types::HookPayload;`
- `enum` `codex-rs/core/src/hooks/user_notification.rs:16` `enum UserNotification {`
- `use` `codex-rs/core/src/hooks/user_notification.rs:75` `use std::path::Path;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:77` `use super::*;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:78` `use anyhow::Result;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:79` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:80` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:81` `use serde_json::Value;`
- `use` `codex-rs/core/src/hooks/user_notification.rs:82` `use serde_json::json;`
- `fn` `codex-rs/core/src/hooks/user_notification.rs:84` `fn expected_notification_json() -> Value {`
- `fn` `codex-rs/core/src/hooks/user_notification.rs:96` `fn test_user_notification() -> Result<()> {`
- `fn` `codex-rs/core/src/hooks/user_notification.rs:113` `fn legacy_notify_json_matches_historical_wire_shape() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use serde::Serialize;`
- `use std::path::Path;`
- `use std::process::Stdio;`
- `use super::registry::command_from_argv;`
- `use super::types::Hook;`
- `use super::types::HookEvent;`
- `use super::types::HookOutcome;`
- `use super::types::HookPayload;`
- `use std::path::Path;`
- `use super::*;`
- `use anyhow::Result;`
- `use codex_protocol::ThreadId;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
