# `codex-rs/core/src/context_manager/history.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15373`
- sha256: `9d4b81efbf55cc4baf1ea0f9e7e6b8fb403e58919e29d11a38d6415c17383c4f`
- generated_utc: `2026-02-08T10:45:32Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/context_manager/history.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/context_manager/history.rs:1` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/context_manager/history.rs:2` `use crate::context_manager::normalize;`
- `use` `codex-rs/core/src/context_manager/history.rs:3` `use crate::instructions::SkillInstructions;`
- `use` `codex-rs/core/src/context_manager/history.rs:4` `use crate::instructions::UserInstructions;`
- `use` `codex-rs/core/src/context_manager/history.rs:5` `use crate::session_prefix::is_session_prefix;`
- `use` `codex-rs/core/src/context_manager/history.rs:6` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/context_manager/history.rs:7` `use crate::truncate::approx_token_count;`
- `use` `codex-rs/core/src/context_manager/history.rs:8` `use crate::truncate::approx_tokens_from_byte_count;`
- `use` `codex-rs/core/src/context_manager/history.rs:9` `use crate::truncate::truncate_function_output_items_with_policy;`
- `use` `codex-rs/core/src/context_manager/history.rs:10` `use crate::truncate::truncate_text;`
- `use` `codex-rs/core/src/context_manager/history.rs:11` `use crate::user_shell_command::is_user_shell_command_text;`
- `use` `codex-rs/core/src/context_manager/history.rs:12` `use codex_protocol::models::BaseInstructions;`
- `use` `codex-rs/core/src/context_manager/history.rs:13` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/context_manager/history.rs:14` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/context_manager/history.rs:15` `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use` `codex-rs/core/src/context_manager/history.rs:16` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/context_manager/history.rs:17` `use codex_protocol::models::ResponseItem;`
- `use` `codex-rs/core/src/context_manager/history.rs:18` `use codex_protocol::protocol::TokenUsage;`
- `use` `codex-rs/core/src/context_manager/history.rs:19` `use codex_protocol::protocol::TokenUsageInfo;`
- `use` `codex-rs/core/src/context_manager/history.rs:20` `use std::ops::Deref;`
- `impl` `codex-rs/core/src/context_manager/history.rs:30` `impl ContextManager {`
- `fn` `codex-rs/core/src/context_manager/history.rs:212` `fn get_non_last_reasoning_items_tokens(&self) -> i64 {`
- `fn` `codex-rs/core/src/context_manager/history.rs:239` `fn get_trailing_codex_generated_items_tokens(&self) -> i64 {`
- `fn` `codex-rs/core/src/context_manager/history.rs:271` `fn normalize_history(&mut self) {`
- `fn` `codex-rs/core/src/context_manager/history.rs:279` `fn process_item(&self, item: &ResponseItem, policy: TruncationPolicy) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history.rs:326` `fn is_api_message(message: &ResponseItem) -> bool {`
- `fn` `codex-rs/core/src/context_manager/history.rs:342` `fn estimate_reasoning_length(encoded_len: usize) -> usize {`
- `fn` `codex-rs/core/src/context_manager/history.rs:350` `fn estimate_item_token_count(item: &ResponseItem) -> i64 {`
- `fn` `codex-rs/core/src/context_manager/history.rs:411` `fn user_message_positions(items: &[ResponseItem]) -> Vec<usize> {`
- `mod` `codex-rs/core/src/context_manager/history.rs:423` `mod tests;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::TurnContext;`
- `use crate::context_manager::normalize;`
- `use crate::instructions::SkillInstructions;`
- `use crate::instructions::UserInstructions;`
- `use crate::session_prefix::is_session_prefix;`
- `use crate::truncate::TruncationPolicy;`
- `use crate::truncate::approx_token_count;`
- `use crate::truncate::approx_tokens_from_byte_count;`
- `use crate::truncate::truncate_function_output_items_with_policy;`
- `use crate::truncate::truncate_text;`
- `use crate::user_shell_command::is_user_shell_command_text;`
- `use codex_protocol::models::BaseInstructions;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::FunctionCallOutputBody;`
- `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::protocol::TokenUsage;`
- `use codex_protocol::protocol::TokenUsageInfo;`
- `use std::ops::Deref;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
