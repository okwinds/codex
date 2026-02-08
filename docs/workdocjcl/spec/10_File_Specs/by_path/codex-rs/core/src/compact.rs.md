# `codex-rs/core/src/compact.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `20194`
- sha256: `741273470531ccb4e14751556e0fb6b8fbefc6a755ca11b29db249131110934a`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/compact.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn content_items_to_text(content: &[ContentItem]) -> Option<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/compact.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/core/src/compact.rs:3` `use crate::ModelProviderInfo;`
- `use` `codex-rs/core/src/compact.rs:4` `use crate::Prompt;`
- `use` `codex-rs/core/src/compact.rs:5` `use crate::client_common::ResponseEvent;`
- `use` `codex-rs/core/src/compact.rs:6` `use crate::codex::Session;`
- `use` `codex-rs/core/src/compact.rs:7` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/compact.rs:8` `use crate::codex::get_last_assistant_message_from_turn;`
- `use` `codex-rs/core/src/compact.rs:9` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/compact.rs:10` `use crate::error::Result as CodexResult;`
- `use` `codex-rs/core/src/compact.rs:11` `use crate::features::Feature;`
- `use` `codex-rs/core/src/compact.rs:12` `use crate::protocol::CompactedItem;`
- `use` `codex-rs/core/src/compact.rs:13` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/compact.rs:14` `use crate::protocol::TurnContextItem;`
- `use` `codex-rs/core/src/compact.rs:15` `use crate::protocol::TurnStartedEvent;`
- `use` `codex-rs/core/src/compact.rs:16` `use crate::protocol::WarningEvent;`
- `use` `codex-rs/core/src/compact.rs:17` `use crate::session_prefix::TURN_ABORTED_OPEN_TAG;`
- `use` `codex-rs/core/src/compact.rs:18` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/compact.rs:19` `use crate::truncate::approx_token_count;`
- `use` `codex-rs/core/src/compact.rs:20` `use crate::truncate::truncate_text;`
- `use` `codex-rs/core/src/compact.rs:21` `use crate::util::backoff;`
- `use` `codex-rs/core/src/compact.rs:22` `use codex_protocol::items::ContextCompactionItem;`
- `use` `codex-rs/core/src/compact.rs:23` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/compact.rs:24` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/compact.rs:25` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/compact.rs:26` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/compact.rs:27` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/compact.rs:28` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/compact.rs:29` `use futures::prelude::*;`
- `use` `codex-rs/core/src/compact.rs:30` `use tracing::error;`
- `const` `codex-rs/core/src/compact.rs:32` `pub const SUMMARIZATION_PROMPT: &str = include_str!("../templates/compact/prompt.md");`
- `const` `codex-rs/core/src/compact.rs:33` `pub const SUMMARY_PREFIX: &str = include_str!("../templates/compact/summary_prefix.md");`
- `const` `codex-rs/core/src/compact.rs:34` `const COMPACT_USER_MESSAGE_MAX_TOKENS: usize = 20_000;`
- `fn` `codex-rs/core/src/compact.rs:70` `async fn run_compact_task_inner(`
- `fn` `codex-rs/core/src/compact.rs:208` `pub fn content_items_to_text(content: &[ContentItem]) -> Option<String> {`
- `fn` `codex-rs/core/src/compact.rs:243` `fn collect_turn_aborted_marker(item: &ResponseItem) -> Option<String> {`
- `fn` `codex-rs/core/src/compact.rs:280` `fn build_compacted_history_with_limit(`
- `fn` `codex-rs/core/src/compact.rs:335` `async fn drain_to_completed(`
- `use` `codex-rs/core/src/compact.rs:377` `use super::*;`
- `use` `codex-rs/core/src/compact.rs:378` `use crate::session_prefix::TURN_ABORTED_OPEN_TAG;`
- `use` `codex-rs/core/src/compact.rs:379` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/compact.rs:382` `fn content_items_to_text_joins_non_empty_segments() {`
- `fn` `codex-rs/core/src/compact.rs:401` `fn content_items_to_text_ignores_image_only_content() {`
- `fn` `codex-rs/core/src/compact.rs:412` `fn collect_user_messages_extracts_user_text_only() {`
- `fn` `codex-rs/core/src/compact.rs:441` `fn collect_user_messages_filters_session_prefix_entries() {`
- `fn` `codex-rs/core/src/compact.rs:479` `fn build_token_limited_compacted_history_truncates_overlong_user_messages() {`
- `fn` `codex-rs/core/src/compact.rs:521` `fn build_token_limited_compacted_history_appends_summary_message() {`
- `fn` `codex-rs/core/src/compact.rs:543` `fn build_compacted_history_preserves_turn_aborted_markers() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use crate::ModelProviderInfo;`
- `use crate::Prompt;`
- `use crate::client_common::ResponseEvent;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::codex::get_last_assistant_message_from_turn;`
- `use crate::error::CodexErr;`
- `use crate::error::Result as CodexResult;`
- `use crate::features::Feature;`
- `use crate::protocol::CompactedItem;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::TurnContextItem;`
- `use crate::protocol::TurnStartedEvent;`
- `use crate::protocol::WarningEvent;`
- `use crate::session_prefix::TURN_ABORTED_OPEN_TAG;`
- `use crate::truncate::TruncationPolicy;`
- `use crate::truncate::approx_token_count;`
- `use crate::truncate::truncate_text;`
- `use crate::util::backoff;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
