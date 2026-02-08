# `codex-rs/state/src/extract.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8648`
- sha256: `e95581bd1288f5faf271c60770cd62ca0f31ed040a72fda0aa5cd347855cd86e`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `use` `codex-rs/state/src/extract.rs:2` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/state/src/extract.rs:3` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/state/src/extract.rs:4` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/state/src/extract.rs:5` `use codex_protocol::protocol::SessionMetaLine;`
- `use` `codex-rs/state/src/extract.rs:6` `use codex_protocol::protocol::TurnContextItem;`
- `use` `codex-rs/state/src/extract.rs:7` `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
- `use` `codex-rs/state/src/extract.rs:8` `use codex_protocol::protocol::UserMessageEvent;`
- `use` `codex-rs/state/src/extract.rs:9` `use serde::Serialize;`
- `use` `codex-rs/state/src/extract.rs:10` `use serde_json::Value;`
- `const` `codex-rs/state/src/extract.rs:12` `const IMAGE_ONLY_USER_MESSAGE_PLACEHOLDER: &str = "[Image]";`
- `fn` `codex-rs/state/src/extract.rs:15` `pub fn apply_rollout_item(`
- `fn` `codex-rs/state/src/extract.rs:32` `fn apply_session_meta_from_item(metadata: &mut ThreadMetadata, meta_line: &SessionMetaLine) {`
- `fn` `codex-rs/state/src/extract.rs:56` `fn apply_turn_context(metadata: &mut ThreadMetadata, turn_ctx: &TurnContextItem) {`
- `fn` `codex-rs/state/src/extract.rs:62` `fn apply_event_msg(metadata: &mut ThreadMetadata, event: &EventMsg) {`
- `fn` `codex-rs/state/src/extract.rs:84` `fn apply_response_item(_metadata: &mut ThreadMetadata, _item: &ResponseItem) {`
- `fn` `codex-rs/state/src/extract.rs:88` `fn strip_user_message_prefix(text: &str) -> &str {`
- `fn` `codex-rs/state/src/extract.rs:95` `fn user_message_preview(user: &UserMessageEvent) -> Option<String> {`
- `use` `codex-rs/state/src/extract.rs:121` `use super::apply_rollout_item;`
- `use` `codex-rs/state/src/extract.rs:122` `use crate::model::ThreadMetadata;`
- `use` `codex-rs/state/src/extract.rs:123` `use chrono::DateTime;`
- `use` `codex-rs/state/src/extract.rs:124` `use chrono::Utc;`
- `use` `codex-rs/state/src/extract.rs:125` `use codex_protocol::ThreadId;`
- `use` `codex-rs/state/src/extract.rs:126` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/state/src/extract.rs:127` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/state/src/extract.rs:128` `use codex_protocol::protocol::EventMsg;`
- `use` `codex-rs/state/src/extract.rs:129` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/state/src/extract.rs:130` `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
- `use` `codex-rs/state/src/extract.rs:131` `use codex_protocol::protocol::UserMessageEvent;`
- `use` `codex-rs/state/src/extract.rs:133` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/state/src/extract.rs:134` `use std::path::PathBuf;`
- `use` `codex-rs/state/src/extract.rs:135` `use uuid::Uuid;`
- `fn` `codex-rs/state/src/extract.rs:138` `fn response_item_user_messages_do_not_set_title_or_first_user_message() {`
- `fn` `codex-rs/state/src/extract.rs:157` `fn event_msg_user_messages_set_title_and_first_user_message() {`
- `fn` `codex-rs/state/src/extract.rs:176` `fn event_msg_image_only_user_message_sets_image_placeholder_preview() {`
- `fn` `codex-rs/state/src/extract.rs:195` `fn event_msg_blank_user_message_without_images_keeps_first_user_message_empty() {`
- `fn` `codex-rs/state/src/extract.rs:210` `fn metadata_for_test() -> ThreadMetadata {`
- `fn` `codex-rs/state/src/extract.rs:235` `fn diff_fields_detects_changes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::model::ThreadMetadata;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::SessionMetaLine;`
- `use codex_protocol::protocol::TurnContextItem;`
- `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
- `use codex_protocol::protocol::UserMessageEvent;`
- `use serde::Serialize;`
- `use serde_json::Value;`
- `use super::apply_rollout_item;`
- `use crate::model::ThreadMetadata;`
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::EventMsg;`
- `use codex_protocol::protocol::RolloutItem;`
- `use codex_protocol::protocol::USER_MESSAGE_BEGIN;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/02_Data/ENTITIES.md`
