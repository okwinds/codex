# `codex-rs/core/src/context_manager/history_tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `36626`
- sha256: `3fe550c0226e24423a06fdbfa44aed2729060bfefe4603685f4212657ba32b16`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/context_manager/history_tests.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/context_manager/history_tests.rs:1` `use super::*;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:2` `use crate::truncate;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:3` `use crate::truncate::TruncationPolicy;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:4` `use codex_git::GhostCommit;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:5` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:6` `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:7` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:8` `use codex_protocol::models::LocalShellAction;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:9` `use codex_protocol::models::LocalShellExecAction;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:10` `use codex_protocol::models::LocalShellStatus;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:11` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:12` `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:13` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:14` `use regex_lite::Regex;`
- `const` `codex-rs/core/src/context_manager/history_tests.rs:16` `const EXEC_FORMAT_MAX_BYTES: usize = 10_000;`
- `const` `codex-rs/core/src/context_manager/history_tests.rs:17` `const EXEC_FORMAT_MAX_TOKENS: usize = 2_500;`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:19` `fn assistant_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:31` `fn create_history_with_items(items: Vec<ResponseItem>) -> ContextManager {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:39` `fn user_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:51` `fn user_input_text_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:63` `fn function_call_output(call_id: &str, content: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:73` `fn custom_tool_call_output(call_id: &str, output: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:80` `fn reasoning_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:93` `fn reasoning_with_encrypted_content(len: usize) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:104` `fn truncate_exec_output(content: &str) -> String {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:109` `fn filters_non_api_messages() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:167` `fn non_last_reasoning_tokens_return_zero_when_no_user_messages() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:174` `fn non_last_reasoning_tokens_ignore_entries_after_last_user() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:189` `fn trailing_codex_generated_tokens_stop_at_first_non_generated_item() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:209` `fn trailing_codex_generated_tokens_exclude_function_call_tail() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:221` `fn total_token_usage_includes_only_trailing_codex_generated_items() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:246` `fn get_history_for_prompt_drops_ghost_commits() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:256` `fn remove_first_item_removes_matching_output_for_function_call() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:278` `fn remove_first_item_removes_matching_call_for_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:300` `fn remove_last_item_removes_matching_call_for_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:324` `fn replace_last_turn_images_replaces_tool_output_images() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:361` `fn replace_last_turn_images_does_not_touch_user_images() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:378` `fn remove_first_item_handles_local_shell_pair() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:406` `fn drop_last_n_user_turns_preserves_prefix() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:441` `fn drop_last_n_user_turns_ignores_session_prefix_user_messages() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:527` `fn remove_first_item_handles_custom_tool_pair() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:547` `fn normalization_retains_local_shell_outputs() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:576` `fn record_items_truncates_function_call_output_content() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:614` `fn record_items_truncates_custom_tool_call_output_content() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:644` `fn record_items_respects_custom_token_limit() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:666` `fn assert_truncated_message_matches(message: &str, line: &str, expected_removed: usize) {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:692` `fn truncated_message_pattern(line: &str) -> String {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:698` `fn format_exec_output_truncates_large_error() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:709` `fn format_exec_output_marks_byte_truncation_without_omitted_lines() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:721` `fn format_exec_output_returns_original_when_within_limits() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:727` `fn format_exec_output_reports_omitted_lines_and_keeps_head_and_tail() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:749` `fn format_exec_output_prefers_line_marker_when_both_limits_exceeded() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:763` `fn normalize_adds_missing_output_for_function_call() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:796` `fn normalize_adds_missing_output_for_custom_tool_call() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:828` `fn normalize_adds_missing_output_for_local_shell_call_with_id() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:873` `fn normalize_removes_orphan_function_call_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:890` `fn normalize_removes_orphan_custom_tool_call_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:904` `fn normalize_mixed_inserts_and_removals() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:998` `fn normalize_adds_missing_output_for_function_call_inserts_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1030` `fn normalize_adds_missing_output_for_custom_tool_call_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1045` `fn normalize_adds_missing_output_for_local_shell_call_with_id_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1065` `fn normalize_removes_orphan_function_call_output_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1080` `fn normalize_removes_orphan_custom_tool_call_output_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1092` `fn normalize_mixed_inserts_and_removals_panics_in_debug() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::*;`
- `use crate::truncate;`
- `use crate::truncate::TruncationPolicy;`
- `use codex_git::GhostCommit;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use codex_protocol::models::FunctionCallOutputPayload;`
- `use codex_protocol::models::LocalShellAction;`
- `use codex_protocol::models::LocalShellExecAction;`
- `use codex_protocol::models::LocalShellStatus;`
- `use codex_protocol::models::ReasoningItemContent;`
- `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use pretty_assertions::assert_eq;`
- `use regex_lite::Regex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
