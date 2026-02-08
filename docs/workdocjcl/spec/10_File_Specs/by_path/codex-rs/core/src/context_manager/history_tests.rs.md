# `codex-rs/core/src/context_manager/history_tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `36733`
- sha256: `dfa3af22c007e0dda74e3e88108591903f444f78ab29464b7ac470fcbbad9d03`
- generated_utc: `2026-02-08T10:45:32Z`

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
- `use` `codex-rs/core/src/context_manager/history_tests.rs:5` `use codex_protocol::models::BaseInstructions;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:6` `use codex_protocol::models::ContentItem;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:7` `use codex_protocol::models::FunctionCallOutputBody;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:8` `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:9` `use codex_protocol::models::FunctionCallOutputPayload;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:10` `use codex_protocol::models::LocalShellAction;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:11` `use codex_protocol::models::LocalShellExecAction;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:12` `use codex_protocol::models::LocalShellStatus;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:13` `use codex_protocol::models::ReasoningItemContent;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:14` `use codex_protocol::models::ReasoningItemReasoningSummary;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:15` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/context_manager/history_tests.rs:16` `use regex_lite::Regex;`
- `const` `codex-rs/core/src/context_manager/history_tests.rs:18` `const EXEC_FORMAT_MAX_BYTES: usize = 10_000;`
- `const` `codex-rs/core/src/context_manager/history_tests.rs:19` `const EXEC_FORMAT_MAX_TOKENS: usize = 2_500;`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:21` `fn assistant_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:33` `fn create_history_with_items(items: Vec<ResponseItem>) -> ContextManager {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:41` `fn user_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:53` `fn user_input_text_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:65` `fn function_call_output(call_id: &str, content: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:72` `fn custom_tool_call_output(call_id: &str, output: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:79` `fn reasoning_msg(text: &str) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:92` `fn reasoning_with_encrypted_content(len: usize) -> ResponseItem {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:103` `fn truncate_exec_output(content: &str) -> String {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:107` `fn approx_token_count_for_text(text: &str) -> i64 {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:112` `fn filters_non_api_messages() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:170` `fn non_last_reasoning_tokens_return_zero_when_no_user_messages() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:177` `fn non_last_reasoning_tokens_ignore_entries_after_last_user() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:192` `fn trailing_codex_generated_tokens_stop_at_first_non_generated_item() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:212` `fn trailing_codex_generated_tokens_exclude_function_call_tail() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:224` `fn total_token_usage_includes_only_trailing_codex_generated_items() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:249` `fn get_history_for_prompt_drops_ghost_commits() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:259` `fn estimate_token_count_with_base_instructions_uses_provided_text() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:281` `fn remove_first_item_removes_matching_output_for_function_call() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:300` `fn remove_first_item_removes_matching_call_for_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:319` `fn remove_last_item_removes_matching_call_for_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:340` `fn replace_last_turn_images_replaces_tool_output_images() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:379` `fn replace_last_turn_images_does_not_touch_user_images() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:396` `fn remove_first_item_handles_local_shell_pair() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:421` `fn drop_last_n_user_turns_preserves_prefix() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:456` `fn drop_last_n_user_turns_ignores_session_prefix_user_messages() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:542` `fn remove_first_item_handles_custom_tool_pair() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:562` `fn normalization_retains_local_shell_outputs() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:588` `fn record_items_truncates_function_call_output_content() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:624` `fn record_items_truncates_custom_tool_call_output_content() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:654` `fn record_items_respects_custom_token_limit() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:679` `fn assert_truncated_message_matches(message: &str, line: &str, expected_removed: usize) {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:705` `fn truncated_message_pattern(line: &str) -> String {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:711` `fn format_exec_output_truncates_large_error() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:722` `fn format_exec_output_marks_byte_truncation_without_omitted_lines() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:734` `fn format_exec_output_returns_original_when_within_limits() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:740` `fn format_exec_output_reports_omitted_lines_and_keeps_head_and_tail() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:762` `fn format_exec_output_prefers_line_marker_when_both_limits_exceeded() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:776` `fn normalize_adds_missing_output_for_function_call() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:806` `fn normalize_adds_missing_output_for_custom_tool_call() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:838` `fn normalize_adds_missing_output_for_local_shell_call_with_id() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:880` `fn normalize_removes_orphan_function_call_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:894` `fn normalize_removes_orphan_custom_tool_call_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:908` `fn normalize_mixed_inserts_and_removals() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:993` `fn normalize_adds_missing_output_for_function_call_inserts_output() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1022` `fn normalize_adds_missing_output_for_custom_tool_call_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1037` `fn normalize_adds_missing_output_for_local_shell_call_with_id_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1057` `fn normalize_removes_orphan_function_call_output_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1069` `fn normalize_removes_orphan_custom_tool_call_output_panics_in_debug() {`
- `fn` `codex-rs/core/src/context_manager/history_tests.rs:1081` `fn normalize_mixed_inserts_and_removals_panics_in_debug() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::*;`
- `use crate::truncate;`
- `use crate::truncate::TruncationPolicy;`
- `use codex_git::GhostCommit;`
- `use codex_protocol::models::BaseInstructions;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::FunctionCallOutputBody;`
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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
