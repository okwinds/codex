# `codex-rs/tui/src/markdown_stream.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `23179`
- sha256: `b40f7f3ef3653257bbd785396fab45a3c1467a322b80169c8c73afd219695a24`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/markdown_stream.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new(width: Option<usize>) -> Self {`
- `pub fn clear(&mut self) {`
- `pub fn push_delta(&mut self, delta: &str) {`
- `pub fn commit_complete_lines(&mut self) -> Vec<Line<'static>> {`
- `pub fn finalize_and_drain(&mut self) -> Vec<Line<'static>> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/markdown_stream.rs:1` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/markdown_stream.rs:3` `use crate::markdown;`
- `impl` `codex-rs/tui/src/markdown_stream.rs:13` `impl MarkdownStreamCollector {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:14` `pub fn new(width: Option<usize>) -> Self {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:22` `pub fn clear(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:27` `pub fn push_delta(&mut self, delta: &str) {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:35` `pub fn commit_complete_lines(&mut self) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:69` `pub fn finalize_and_drain(&mut self) -> Vec<Line<'static>> {`
- `use` `codex-rs/tui/src/markdown_stream.rs:120` `use super::*;`
- `use` `codex-rs/tui/src/markdown_stream.rs:121` `use ratatui::style::Color;`
- `fn` `codex-rs/tui/src/markdown_stream.rs:124` `async fn no_commit_until_newline() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:135` `async fn finalize_commits_partial_line() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:143` `async fn e2e_stream_blockquote_simple_is_green() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:156` `async fn e2e_stream_blockquote_nested_is_green() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:179` `async fn e2e_stream_blockquote_with_list_items_is_green() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:187` `async fn e2e_stream_nested_mixed_lists_ordered_marker_is_light_blue() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:218` `async fn e2e_stream_blockquote_wrap_preserves_green_style() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:253` `async fn heading_starts_on_new_line_when_following_paragraph() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:308` `async fn heading_not_inlined_when_split_across_chunks() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:375` `fn lines_to_plain_strings(lines: &[ratatui::text::Line<'_>]) -> Vec<String> {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:389` `async fn lists_and_fences_commit_without_duplication() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:398` `async fn utf8_boundary_safety_and_wide_chars() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:427` `async fn e2e_stream_deep_nested_third_level_marker_is_light_blue() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:476` `async fn empty_fenced_block_is_dropped_and_separator_preserved_before_heading() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:494` `async fn paragraph_then_empty_fence_then_heading_keeps_heading_on_new_line() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:513` `async fn loose_list_with_split_dashes_matches_full_render() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:533` `async fn loose_vs_tight_list_items_streaming_matches_full() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:633` `async fn assert_streamed_equals_full(deltas: &[&str]) {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:644` `async fn fuzz_class_bullet_duplication_variant_1() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:653` `async fn fuzz_class_bullet_duplication_variant_2() {`
- `fn` `codex-rs/tui/src/markdown_stream.rs:662` `async fn streaming_html_block_then_text_matches_full() {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::text::Line;`
- `use crate::markdown;`
- `use super::*;`
- `use ratatui::style::Color;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
