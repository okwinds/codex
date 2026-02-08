# `codex-rs/state/src/extract.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6601`
- sha256: `6e2b53a1b5fd1a4f4cd6c9cb070a032890ce03b3f0e7edc6b661269d9fcc0af0`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/state/src/extract.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn apply_rollout_item(`

## Definitions (auto, per-file)
- `use` `codex-rs/state/src/extract.rs:1` `use crate::model::ThreadMetadata;`
- `use` `codex-rs/state/src/extract.rs:2` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/state/src/extract.rs:3` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/state/src/extract.rs:4` `use codex_protocol::models::is_local_image_close_tag_text;`
- `use` `codex-rs/state/src/extract.rs:5` `use codex_protocol::models::is_local_image_open_tag_text;`
- `use` `codex-rs/state/src/extract.rs:6` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/state/src/extract.rs:7` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/state/src/extract.rs:8` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/state/src/extract.rs:9` `use codex_protocol::protocol::TurnContextItem;`
- `use` `codex-rs/state/src/extract.rs:10` `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
- `use` `codex-rs/state/src/extract.rs:11` `use serde::Serialize;`
- `use` `codex-rs/state/src/extract.rs:12` `use serde_json::Value;`
- `fn` `codex-rs/state/src/extract.rs:15` `pub fn apply_rollout_item(`
- `fn` `codex-rs/state/src/extract.rs:32` `fn apply_session_meta_from_item(metadata: &mut ThreadMetadata, meta_line: &SessionMetaLine) {`
- `fn` `codex-rs/state/src/extract.rs:53` `fn apply_turn_context(metadata: &mut ThreadMetadata, turn_ctx: &TurnContextItem) {`
- `fn` `codex-rs/state/src/extract.rs:59` `fn apply_event_msg(metadata: &mut ThreadMetadata, event: &EventMsg) {`
- `fn` `codex-rs/state/src/extract.rs:76` `fn apply_response_item(metadata: &mut ThreadMetadata, item: &ResponseItem) {`
- `fn` `codex-rs/state/src/extract.rs:85` `fn extract_user_message_text(item: &ResponseItem) -> Option<String> {`
- `fn` `codex-rs/state/src/extract.rs:111` `fn strip_user_message_prefix(text: &str) -> &str {`
- `use` `codex-rs/state/src/extract.rs:128` `use super::extract_user_message_text;`
- `use` `codex-rs/state/src/extract.rs:129` `use crate::model::ThreadMetadata;`
- `use` `codex-rs/state/src/extract.rs:130` `use chrono::DateTime;`
- `use` `codex-rs/state/src/extract.rs:131` `use chrono::Utc;`
- `use` `codex-rs/state/src/extract.rs:132` `use codex_protocol::ThreadId;`
- `use` `codex-rs/state/src/extract.rs:133` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/state/src/extract.rs:134` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/state/src/extract.rs:135` `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
- `use` `codex-rs/state/src/extract.rs:136` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/state/src/extract.rs:137` `use std::path::PathBuf;`
- `use` `codex-rs/state/src/extract.rs:138` `use uuid::Uuid;`
- `fn` `codex-rs/state/src/extract.rs:141` `fn extracts_user_message_text() {`
- `fn` `codex-rs/state/src/extract.rs:161` `fn diff_fields_detects_changes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::model::ThreadMetadata;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::models::is_local_image_close_tag_text;`
- `use codex_protocol::models::is_local_image_open_tag_text;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::SessionMetaLine;`
- `use codex_protocol::protocol::TurnContextItem;`
- `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use super::extract_user_message_text;`
- `use crate::model::ThreadMetadata;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/02_Data/ENTITIES.md`
