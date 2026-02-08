# `codex-rs/core/src/event_mapping.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19169`
- sha256: `81f214731231a9f1699ccd85dd666b83b5322fd15b9c288d5f042805d74545ed`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/event_mapping.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn parse_turn_item(item: &ResponseItem) -> Option<TurnItem> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/event_mapping.rs:1` `use codex_protocol::items::AgentMessageContent;`
- `use` `codex-rs/core/src/event_mapping.rs:2` `use codex_protocol::items::AgentMessageItem;`
- `use` `codex-rs/core/src/event_mapping.rs:3` `use codex_protocol::items::ReasoningItem;`
- `use` `codex-rs/core/src/event_mapping.rs:4` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/event_mapping.rs:5` `use codex_protocol::items::UserMessageItem;`
- `use` `codex-rs/core/src/event_mapping.rs:6` `use codex_protocol::items::WebSearchItem;`
- `use` `codex-rs/core/src/event_mapping.rs:7` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/event_mapping.rs:8` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/core/src/event_mapping.rs:9` `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use` `codex-rs/core/src/event_mapping.rs:10` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/event_mapping.rs:11` `use codex_protocol::models::WebSearchAction;`
- `use` `codex-rs/core/src/event_mapping.rs:12` `use codex_protocol::models::is_image_close_tag_text;`
- `use` `codex-rs/core/src/event_mapping.rs:13` `use codex_protocol::models::is_image_open_tag_text;`
- `use` `codex-rs/core/src/event_mapping.rs:14` `use codex_protocol::models::is_local_image_close_tag_text;`
- `use` `codex-rs/core/src/event_mapping.rs:15` `use codex_protocol::models::is_local_image_open_tag_text;`
- `use` `codex-rs/core/src/event_mapping.rs:16` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/event_mapping.rs:17` `use tracing::warn;`
- `use` `codex-rs/core/src/event_mapping.rs:18` `use uuid::Uuid;`
- `use` `codex-rs/core/src/event_mapping.rs:20` `use crate::instructions::SkillInstructions;`
- `use` `codex-rs/core/src/event_mapping.rs:21` `use crate::instructions::UserInstructions;`
- `use` `codex-rs/core/src/event_mapping.rs:22` `use crate::session_prefix::is_session_prefix;`
- `use` `codex-rs/core/src/event_mapping.rs:23` `use crate::user_shell_command::is_user_shell_command_text;`
- `use` `codex-rs/core/src/event_mapping.rs:24` `use crate::web_search::web_search_action_detail;`
- `fn` `codex-rs/core/src/event_mapping.rs:26` `fn parse_user_message(message: &[ContentItem]) -> Option<UserMessageItem> {`
- `fn` `codex-rs/core/src/event_mapping.rs:72` `fn parse_agent_message(id: Option<&String>, message: &[ContentItem]) -> AgentMessageItem {`
- `fn` `codex-rs/core/src/event_mapping.rs:91` `pub fn parse_turn_item(item: &ResponseItem) -> Option<TurnItem> {`
- `use` `codex-rs/core/src/event_mapping.rs:148` `use super::parse_turn_item;`
- `use` `codex-rs/core/src/event_mapping.rs:149` `use codex_protocol::items::AgentMessageContent;`
- `use` `codex-rs/core/src/event_mapping.rs:150` `use codex_protocol::items::TurnItem;`
- `use` `codex-rs/core/src/event_mapping.rs:151` `use codex_protocol::items::WebSearchItem;`
- `use` `codex-rs/core/src/event_mapping.rs:152` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/event_mapping.rs:153` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/core/src/event_mapping.rs:154` `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use` `codex-rs/core/src/event_mapping.rs:155` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/event_mapping.rs:156` `use codex_protocol::models::WebSearchAction;`
- `use` `codex-rs/core/src/event_mapping.rs:157` `use codex_protocol::user_input::UserInput;`
- `use` `codex-rs/core/src/event_mapping.rs:158` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/event_mapping.rs:161` `fn parses_user_message_with_text_and_two_images() {`
- `fn` `codex-rs/core/src/event_mapping.rs:202` `fn skips_local_image_label_text() {`
- `fn` `codex-rs/core/src/event_mapping.rs:244` `fn skips_unnamed_image_label_text() {`
- `fn` `codex-rs/core/src/event_mapping.rs:286` `fn skips_user_instructions_and_env() {`
- `fn` `codex-rs/core/src/event_mapping.rs:343` `fn parses_agent_message() {`
- `fn` `codex-rs/core/src/event_mapping.rs:368` `fn parses_reasoning_summary_and_raw_content() {`
- `fn` `codex-rs/core/src/event_mapping.rs:400` `fn parses_reasoning_including_raw_content() {`
- `fn` `codex-rs/core/src/event_mapping.rs:432` `fn parses_web_search_call() {`
- `fn` `codex-rs/core/src/event_mapping.rs:461` `fn parses_web_search_open_page_call() {`
- `fn` `codex-rs/core/src/event_mapping.rs:488` `fn parses_web_search_find_in_page_call() {`
- `fn` `codex-rs/core/src/event_mapping.rs:517` `fn parses_partial_web_search_call_without_action_as_other() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::items::AgentMessageContent;`
- `use codex_protocol::items::AgentMessageItem;`
- `use codex_protocol::items::ReasoningItem;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::items::UserMessageItem;`
- `use codex_protocol::items::WebSearchItem;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ReasoningItemContent;`
- `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::models::WebSearchAction;`
- `use codex_protocol::models::is_image_close_tag_text;`
- `use codex_protocol::models::is_image_open_tag_text;`
- `use codex_protocol::models::is_local_image_close_tag_text;`
- `use codex_protocol::models::is_local_image_open_tag_text;`
- `use codex_protocol::user_input::UserInput;`
- `use tracing::warn;`
- `use uuid::Uuid;`
- `use crate::instructions::SkillInstructions;`
- `use crate::instructions::UserInstructions;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
