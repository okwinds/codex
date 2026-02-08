# `codex-rs/core/src/truncate.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `18475`
- sha256: `47c6d954a9f88352748bc6e15e8879f523f0a2094297ff29a607b6b33b4b8795`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/truncate.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum TruncationPolicy {`
- `pub fn token_budget(&self) -> usize {`
- `pub fn byte_budget(&self) -> usize {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/truncate.rs:5` `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use` `codex-rs/core/src/truncate.rs:6` `use codex_protocol::openai_models::TruncationMode;`
- `use` `codex-rs/core/src/truncate.rs:7` `use codex_protocol::openai_models::TruncationPolicyConfig;`
- `use` `codex-rs/core/src/truncate.rs:8` `use codex_protocol::protocol::TruncationPolicy as ProtocolTruncationPolicy;`
- `const` `codex-rs/core/src/truncate.rs:10` `const APPROX_BYTES_PER_TOKEN: usize = 4;`
- `enum` `codex-rs/core/src/truncate.rs:13` `pub enum TruncationPolicy {`
- `impl` `codex-rs/core/src/truncate.rs:18` `impl From<TruncationPolicy> for ProtocolTruncationPolicy {`
- `fn` `codex-rs/core/src/truncate.rs:19` `fn from(value: TruncationPolicy) -> Self {`
- `impl` `codex-rs/core/src/truncate.rs:27` `impl From<TruncationPolicyConfig> for TruncationPolicy {`
- `fn` `codex-rs/core/src/truncate.rs:28` `fn from(config: TruncationPolicyConfig) -> Self {`
- `impl` `codex-rs/core/src/truncate.rs:36` `impl TruncationPolicy {`
- `fn` `codex-rs/core/src/truncate.rs:42` `pub fn token_budget(&self) -> usize {`
- `fn` `codex-rs/core/src/truncate.rs:56` `pub fn byte_budget(&self) -> usize {`
- `impl` `codex-rs/core/src/truncate.rs:64` `impl std::ops::Mul<f64> for TruncationPolicy {`
- `type` `codex-rs/core/src/truncate.rs:65` `type Output = Self;`
- `fn` `codex-rs/core/src/truncate.rs:67` `fn mul(self, multiplier: f64) -> Self::Output {`
- `fn` `codex-rs/core/src/truncate.rs:162` `fn truncate_with_token_budget(s: &str, policy: TruncationPolicy) -> (String, Option<u64>) {`
- `fn` `codex-rs/core/src/truncate.rs:186` `fn truncate_with_byte_estimate(s: &str, policy: TruncationPolicy) -> String {`
- `fn` `codex-rs/core/src/truncate.rs:221` `fn split_string(s: &str, beginning_bytes: usize, end_bytes: usize) -> (usize, &str, &str) {`
- `fn` `codex-rs/core/src/truncate.rs:261` `fn format_truncation_marker(policy: TruncationPolicy, removed_count: u64) -> String {`
- `fn` `codex-rs/core/src/truncate.rs:268` `fn split_budget(budget: usize) -> (usize, usize) {`
- `fn` `codex-rs/core/src/truncate.rs:273` `fn removed_units_for_source(`
- `fn` `codex-rs/core/src/truncate.rs:284` `fn assemble_truncated_output(prefix: &str, suffix: &str, marker: &str) -> String {`
- `use` `codex-rs/core/src/truncate.rs:310` `use super::TruncationPolicy;`
- `use` `codex-rs/core/src/truncate.rs:311` `use super::approx_token_count;`
- `use` `codex-rs/core/src/truncate.rs:312` `use super::formatted_truncate_text;`
- `use` `codex-rs/core/src/truncate.rs:313` `use super::split_string;`
- `use` `codex-rs/core/src/truncate.rs:314` `use super::truncate_function_output_items_with_policy;`
- `use` `codex-rs/core/src/truncate.rs:315` `use super::truncate_text;`
- `use` `codex-rs/core/src/truncate.rs:316` `use super::truncate_with_token_budget;`
- `use` `codex-rs/core/src/truncate.rs:317` `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use` `codex-rs/core/src/truncate.rs:318` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/truncate.rs:321` `fn split_string_works() {`
- `fn` `codex-rs/core/src/truncate.rs:327` `fn split_string_handles_empty_string() {`
- `fn` `codex-rs/core/src/truncate.rs:332` `fn split_string_only_keeps_prefix_when_tail_budget_is_zero() {`
- `fn` `codex-rs/core/src/truncate.rs:337` `fn split_string_only_keeps_suffix_when_prefix_budget_is_zero() {`
- `fn` `codex-rs/core/src/truncate.rs:342` `fn split_string_handles_overlapping_budgets_without_removal() {`
- `fn` `codex-rs/core/src/truncate.rs:347` `fn split_string_respects_utf8_boundaries() {`
- `fn` `codex-rs/core/src/truncate.rs:356` `fn truncate_bytes_less_than_placeholder_returns_placeholder() {`
- `fn` `codex-rs/core/src/truncate.rs:366` `fn truncate_tokens_less_than_placeholder_returns_placeholder() {`
- `fn` `codex-rs/core/src/truncate.rs:376` `fn truncate_tokens_under_limit_returns_original() {`
- `fn` `codex-rs/core/src/truncate.rs:386` `fn truncate_bytes_under_limit_returns_original() {`
- `fn` `codex-rs/core/src/truncate.rs:396` `fn truncate_tokens_over_limit_returns_truncated() {`
- `fn` `codex-rs/core/src/truncate.rs:406` `fn truncate_bytes_over_limit_returns_truncated() {`
- `fn` `codex-rs/core/src/truncate.rs:416` `fn truncate_bytes_reports_original_line_count_when_truncated() {`
- `fn` `codex-rs/core/src/truncate.rs:427` `fn truncate_tokens_reports_original_line_count_when_truncated() {`
- `fn` `codex-rs/core/src/truncate.rs:438` `fn truncate_with_token_budget_returns_original_when_under_limit() {`
- `fn` `codex-rs/core/src/truncate.rs:447` `fn truncate_with_token_budget_reports_truncation_at_zero_limit() {`
- `fn` `codex-rs/core/src/truncate.rs:455` `fn truncate_middle_tokens_handles_utf8_content() {`
- `fn` `codex-rs/core/src/truncate.rs:463` `fn truncate_middle_bytes_handles_utf8_content() {`
- `fn` `codex-rs/core/src/truncate.rs:470` `fn truncates_across_multiple_under_limit_texts_and_reports_omitted() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use codex_protocol::openai_models::TruncationMode;`
- `use codex_protocol::openai_models::TruncationPolicyConfig;`
- `use codex_protocol::protocol::TruncationPolicy as ProtocolTruncationPolicy;`
- `use super::TruncationPolicy;`
- `use super::approx_token_count;`
- `use super::formatted_truncate_text;`
- `use super::split_string;`
- `use super::truncate_function_output_items_with_policy;`
- `use super::truncate_text;`
- `use super::truncate_with_token_budget;`
- `use codex_protocol::models::FunctionCallOutputContentItem;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
