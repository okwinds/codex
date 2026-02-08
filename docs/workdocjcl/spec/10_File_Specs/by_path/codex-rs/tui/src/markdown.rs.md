# `codex-rs/tui/src/markdown.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3523`
- sha256: `0de3f1e5937985481adc34d4171e5a3e6b0dc8551eef7bbc1a0fe5486fc2dbd3`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/markdown.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/markdown.rs:1` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/markdown.rs:13` `use super::*;`
- `use` `codex-rs/tui/src/markdown.rs:14` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/markdown.rs:15` `use ratatui::text::Line;`
- `fn` `codex-rs/tui/src/markdown.rs:17` `fn lines_to_strings(lines: &[Line<'static>]) -> Vec<String> {`
- `fn` `codex-rs/tui/src/markdown.rs:30` `fn citations_render_as_plain_text() {`
- `fn` `codex-rs/tui/src/markdown.rs:45` `fn indented_code_blocks_preserve_leading_whitespace() {`
- `fn` `codex-rs/tui/src/markdown.rs:55` `fn append_markdown_preserves_full_text_line() {`
- `fn` `codex-rs/tui/src/markdown.rs:77` `fn append_markdown_matches_tui_markdown_for_ordered_item() {`
- `fn` `codex-rs/tui/src/markdown.rs:85` `fn append_markdown_keeps_ordered_list_line_unsplit_in_context() {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::text::Line;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use ratatui::text::Line;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
