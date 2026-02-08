# `codex-rs/tui/src/text_formatting.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `18344`
- sha256: `72b63ba9a86163139ccdd21d540aa27d2b8bf8c52231f9c1f15e1dcdcbb4ec37`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/text_formatting.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/text_formatting.rs:1` `use unicode_segmentation::UnicodeSegmentation;`
- `use` `codex-rs/tui/src/text_formatting.rs:2` `use unicode_width::UnicodeWidthChar;`
- `use` `codex-rs/tui/src/text_formatting.rs:3` `use unicode_width::UnicodeWidthStr;`
- `struct` `codex-rs/tui/src/text_formatting.rs:152` `struct Segment<'a> {`
- `use` `codex-rs/tui/src/text_formatting.rs:332` `use super::*;`
- `use` `codex-rs/tui/src/text_formatting.rs:333` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/text_formatting.rs:336` `fn test_truncate_text() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:343` `fn test_truncate_empty_string() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:350` `fn test_truncate_max_graphemes_zero() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:357` `fn test_truncate_max_graphemes_one() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:364` `fn test_truncate_max_graphemes_two() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:371` `fn test_truncate_max_graphemes_three_boundary() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:378` `fn test_truncate_text_shorter_than_limit() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:385` `fn test_truncate_text_exact_length() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:392` `fn test_truncate_emoji() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:402` `fn test_truncate_unicode_combining_characters() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:409` `fn test_truncate_very_long_text() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:417` `fn test_format_json_compact_simple_object() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:424` `fn test_format_json_compact_nested_object() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:434` `fn test_center_truncate_doesnt_truncate_short_path() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:443` `fn test_center_truncate_truncates_long_path() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:455` `fn test_center_truncate_truncates_long_windows_path() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:468` `fn test_center_truncate_handles_long_segment() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:477` `fn test_format_json_compact_array() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:484` `fn test_format_json_compact_already_compact() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:491` `fn test_format_json_compact_with_whitespace() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:509` `fn test_format_json_compact_invalid_json() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:516` `fn test_format_json_compact_empty_object() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:523` `fn test_format_json_compact_empty_array() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:530` `fn test_format_json_compact_primitive_values() {`

## Dependencies (auto sample)
### Imports / Includes
- `use unicode_segmentation::UnicodeSegmentation;`
- `use unicode_width::UnicodeWidthChar;`
- `use unicode_width::UnicodeWidthStr;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
