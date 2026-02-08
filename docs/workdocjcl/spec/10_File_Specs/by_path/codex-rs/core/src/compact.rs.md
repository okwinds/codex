# `codex-rs/core/src/compact.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `34087`
- sha256: `a14a8b353d59983f6a15d3e798a6e8385c9ce799b419c2fd6bab35340e02dd48`
- generated_utc: `2026-02-08T10:45:28Z`

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
- `use` `codex-rs/core/src/compact.rs:5` `use crate::client::ModelClientSession;`
- `use` `codex-rs/core/src/compact.rs:6` `use crate::client_common::ResponseEvent;`
- `use` `codex-rs/core/src/compact.rs:7` `use crate::codex::Session;`
- `use` `codex-rs/core/src/compact.rs:8` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/compact.rs:9` `use crate::codex::get_last_assistant_message_from_turn;`
- `use` `codex-rs/core/src/compact.rs:10` `use crate::error::CodexErr;`
- `use` `codex-rs/core/src/compact.rs:11` `use crate::error::Result as CodexResult;`
- `use` `codex-rs/core/src/compact.rs:12` `use crate::protocol::CompactedItem;`
- `use` `codex-rs/core/src/compact.rs:13` `use crate::protocol::EventMsg;`
- `use` `codex-rs/core/src/compact.rs:14` `use crate::protocol::TurnContextItem;`
- `use` `codex-rs/core/src/compact.rs:15` `use crate::protocol::TurnStartedEvent;`
- `use` `codex-rs/core/src/compact.rs:16` `use crate::protocol::WarningEvent;`
- `use` `codex-rs/core/src/compact.rs:17` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/compact.rs:18` `use crate::truncate::approx_token_count;`
- `use` `codex-rs/core/src/compact.rs:19` `use crate::truncate::truncate_text;`
- `use` `codex-rs/core/src/compact.rs:20` `use crate::util::backoff;`
- `use` `codex-rs/core/src/compact.rs:21` `use codex_protocol::items::ContextCompactionItem;`
- `use` `codex-rs/core/src/compact.rs:22` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/compact.rs:23` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/compact.rs:24` `use codex_protocol::models::ResponseInputItem;`
- `use` `codex-rs/core/src/compact.rs:25` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/compact.rs:26` `use codex_protocol::protocol::RolloutItem;`
- `use` `codex-rs/core/src/compact.rs:27` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/compact.rs:28` `use futures::prelude::*;`
- `use` `codex-rs/core/src/compact.rs:29` `use tracing::error;`
- `const` `codex-rs/core/src/compact.rs:31` `pub const SUMMARIZATION_PROMPT: &str = include_str!("../templates/compact/prompt.md");`
- `const` `codex-rs/core/src/compact.rs:32` `pub const SUMMARY_PREFIX: &str = include_str!("../templates/compact/summary_prefix.md");`
- `const` `codex-rs/core/src/compact.rs:33` `const COMPACT_USER_MESSAGE_MAX_TOKENS: usize = 20_000;`
- `fn` `codex-rs/core/src/compact.rs:67` `async fn run_compact_task_inner(`
- `fn` `codex-rs/core/src/compact.rs:217` `pub fn content_items_to_text(content: &[ContentItem]) -> Option<String> {`
- `fn` `codex-rs/core/src/compact.rs:294` `fn should_keep_compacted_history_item(item: &ResponseItem) -> bool {`
- `fn` `codex-rs/core/src/compact.rs:318` `fn build_compacted_history_with_limit(`
- `fn` `codex-rs/core/src/compact.rs:373` `async fn drain_to_completed(`
- `use` `codex-rs/core/src/compact.rs:423` `use super::*;`
- `use` `codex-rs/core/src/compact.rs:424` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/compact.rs:427` `fn content_items_to_text_joins_non_empty_segments() {`
- `fn` `codex-rs/core/src/compact.rs:446` `fn content_items_to_text_ignores_image_only_content() {`
- `fn` `codex-rs/core/src/compact.rs:457` `fn collect_user_messages_extracts_user_text_only() {`
- `fn` `codex-rs/core/src/compact.rs:486` `fn collect_user_messages_filters_session_prefix_entries() {`
- `fn` `codex-rs/core/src/compact.rs:524` `fn build_token_limited_compacted_history_truncates_overlong_user_messages() {`
- `fn` `codex-rs/core/src/compact.rs:566` `fn build_token_limited_compacted_history_appends_summary_message() {`
- `fn` `codex-rs/core/src/compact.rs:588` `fn process_compacted_history_replaces_developer_messages() {`
- `fn` `codex-rs/core/src/compact.rs:691` `fn process_compacted_history_reinjects_full_initial_context() {`
- `fn` `codex-rs/core/src/compact.rs:793` `fn process_compacted_history_drops_non_user_content_messages() {`
- `fn` `codex-rs/core/src/compact.rs:876` `fn process_compacted_history_inserts_context_before_last_real_user_message_only() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use crate::ModelProviderInfo;`
- `use crate::Prompt;`
- `use crate::client::ModelClientSession;`
- `use crate::client_common::ResponseEvent;`
- `use crate::codex::Session;`
- `use crate::codex::TurnContext;`
- `use crate::codex::get_last_assistant_message_from_turn;`
- `use crate::error::CodexErr;`
- `use crate::error::Result as CodexResult;`
- `use crate::protocol::CompactedItem;`
- `use crate::protocol::EventMsg;`
- `use crate::protocol::TurnContextItem;`
- `use crate::protocol::TurnStartedEvent;`
- `use crate::protocol::WarningEvent;`
- `use crate::truncate::TruncationPolicy;`
- `use crate::truncate::approx_token_count;`
- `use crate::truncate::truncate_text;`
- `use crate::util::backoff;`
- `use codex_protocol::items::ContextCompactionItem;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
