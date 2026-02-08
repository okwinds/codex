# `codex-rs/tui/src/markdown_render_tests.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `28513`
- sha256: `1908bc734787e4571cd1e88d122f1b4baed4a935cc97c76d7b1ca1f07e6c591c`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/markdown_render_tests.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/markdown_render_tests.rs:1` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/markdown_render_tests.rs:2` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/markdown_render_tests.rs:3` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/markdown_render_tests.rs:4` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/markdown_render_tests.rs:5` `use ratatui::text::Text;`
- `use` `codex-rs/tui/src/markdown_render_tests.rs:7` `use crate::markdown_render::render_markdown_text;`
- `use` `codex-rs/tui/src/markdown_render_tests.rs:8` `use insta::assert_snapshot;`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:11` `fn empty() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:16` `fn paragraph_single() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:24` `fn paragraph_soft_break() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:32` `fn paragraph_multiple() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:40` `fn headings() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:60` `fn blockquote_single() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:67` `fn blockquote_soft_break() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:90` `fn blockquote_multiple_with_break() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:101` `fn blockquote_three_paragraphs_short_lines() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:115` `fn blockquote_nested_two_levels() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:127` `fn blockquote_with_list_items() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:138` `fn blockquote_with_ordered_list() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:159` `fn blockquote_list_then_nested_blockquote() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:170` `fn list_item_with_inline_blockquote_on_same_line() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:181` `fn blockquote_surrounded_by_blank_lines() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:207` `fn blockquote_in_ordered_list_on_next_line() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:226` `fn blockquote_in_unordered_list_on_next_line() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:245` `fn blockquote_two_paragraphs_inside_ordered_list_has_blank_line() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:271` `fn blockquote_inside_nested_list() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:288` `fn list_item_text_then_blockquote() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:305` `fn list_item_blockquote_then_text() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:322` `fn list_item_text_blockquote_text() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:339` `fn blockquote_with_heading_and_paragraph() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:364` `fn blockquote_heading_inherits_heading_style() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:382` `fn blockquote_with_code_block() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:399` `fn blockquote_with_multiline_code_block() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:416` `fn nested_blockquote_with_inline_and_fenced_code() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:459` `fn list_unordered_single() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:466` `fn list_unordered_multiple() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:476` `fn list_ordered() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:486` `fn list_nested() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:496` `fn list_ordered_custom_start() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:506` `fn nested_unordered_in_ordered() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:519` `fn nested_ordered_in_unordered() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:532` `fn loose_list_item_multiple_paragraphs() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:545` `fn tight_item_with_soft_break() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:556` `fn deeply_nested_mixed_three_levels() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:569` `fn loose_items_due_to_blank_line_between_items() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:580` `fn mixed_tight_then_loose_in_one_list() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:591` `fn ordered_item_with_indented_continuation_is_tight() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:602` `fn inline_code() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:609` `fn strong() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:617` `fn emphasis() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:625` `fn strikethrough() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:633` `fn strong_emphasis() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:643` `fn link() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:655` `fn code_block_unhighlighted() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:662` `fn code_block_multiple_lines_root() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:673` `fn code_block_indented() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:685` `fn horizontal_rule_renders_em_dashes() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:702` `fn code_block_with_inner_triple_backticks_outer_four() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:739` `fn code_block_inside_unordered_list_item_is_indented() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:756` `fn code_block_multiple_lines_inside_unordered_list() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:773` `fn code_block_inside_unordered_list_item_multiple_lines() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:790` `fn markdown_render_complex_snapshot() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:861` `fn ordered_item_with_code_block_and_nested_bullet() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:887` `fn nested_five_levels_mixed_lists() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:904` `fn html_inline_is_verbatim() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:912` `fn html_block_is_verbatim_multiline() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:924` `fn html_in_tight_ordered_item_soft_breaks_with_space() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:935` `fn html_continuation_paragraph_in_unordered_item_indented() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:947` `fn unordered_item_continuation_paragraph_is_indented() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:972` `fn ordered_item_continuation_paragraph_is_indented() {`
- `fn` `codex-rs/tui/src/markdown_render_tests.rs:984` `fn nested_item_continuation_paragraph_is_indented() {`

## Dependencies (auto sample)
### Imports / Includes
- `use pretty_assertions::assert_eq;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::text::Text;`
- `use crate::markdown_render::render_markdown_text;`
- `use insta::assert_snapshot;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
