# `codex-rs/core/src/hooks/types.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3419`
- sha256: `2d6549fed888ba805aac6d7d2c4f06640b72acb2476d0c0828a78b18840f857e`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/hooks/types.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/hooks/types.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/hooks/types.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/core/src/hooks/types.rs:4` `use chrono::DateTime;`
- `use` `codex-rs/core/src/hooks/types.rs:5` `use chrono::SecondsFormat;`
- `use` `codex-rs/core/src/hooks/types.rs:6` `use chrono::Utc;`
- `use` `codex-rs/core/src/hooks/types.rs:7` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/hooks/types.rs:8` `use futures::future::BoxFuture;`
- `use` `codex-rs/core/src/hooks/types.rs:9` `use serde::Serialize;`
- `use` `codex-rs/core/src/hooks/types.rs:10` `use serde::Serializer;`
- `impl` `codex-rs/core/src/hooks/types.rs:20` `impl Default for Hook {`
- `fn` `codex-rs/core/src/hooks/types.rs:21` `fn default() -> Self {`
- `impl` `codex-rs/core/src/hooks/types.rs:28` `impl Hook {`
- `use` `codex-rs/core/src/hooks/types.rs:78` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/hooks/types.rs:80` `use chrono::TimeZone;`
- `use` `codex-rs/core/src/hooks/types.rs:81` `use chrono::Utc;`
- `use` `codex-rs/core/src/hooks/types.rs:82` `use codex_protocol::ThreadId;`
- `use` `codex-rs/core/src/hooks/types.rs:83` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/hooks/types.rs:84` `use serde_json::json;`
- `use` `codex-rs/core/src/hooks/types.rs:86` `use super::HookEvent;`
- `use` `codex-rs/core/src/hooks/types.rs:87` `use super::HookEventAfterAgent;`
- `use` `codex-rs/core/src/hooks/types.rs:88` `use super::HookPayload;`
- `fn` `codex-rs/core/src/hooks/types.rs:91` `fn hook_payload_serializes_stable_wire_shape() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use chrono::DateTime;`
- `use chrono::SecondsFormat;`
- `use chrono::Utc;`
- `use codex_protocol::ThreadId;`
- `use futures::future::BoxFuture;`
- `use serde::Serialize;`
- `use serde::Serializer;`
- `use std::path::PathBuf;`
- `use chrono::TimeZone;`
- `use chrono::Utc;`
- `use codex_protocol::ThreadId;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::json;`
- `use super::HookEvent;`
- `use super::HookEventAfterAgent;`
- `use super::HookPayload;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
