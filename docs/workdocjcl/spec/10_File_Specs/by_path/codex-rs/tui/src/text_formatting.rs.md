# `codex-rs/tui/src/text_formatting.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19746`
- sha256: `824b6c7297bf0f6a22fb3ecaac4fe68d545384e179233b6dd0dff1685e02c155`
- generated_utc: `2026-02-08T10:45:40Z`

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
- `use` `codex-rs/tui/src/text_formatting.rs:359` `use super::*;`
- `use` `codex-rs/tui/src/text_formatting.rs:360` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/text_formatting.rs:363` `fn test_truncate_text() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:370` `fn test_truncate_empty_string() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:377` `fn test_truncate_max_graphemes_zero() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:384` `fn test_truncate_max_graphemes_one() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:391` `fn test_truncate_max_graphemes_two() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:398` `fn test_truncate_max_graphemes_three_boundary() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:405` `fn test_truncate_text_shorter_than_limit() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:412` `fn test_truncate_text_exact_length() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:419` `fn test_truncate_emoji() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:429` `fn test_truncate_unicode_combining_characters() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:436` `fn test_truncate_very_long_text() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:444` `fn test_format_json_compact_simple_object() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:451` `fn test_format_json_compact_nested_object() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:461` `fn test_center_truncate_doesnt_truncate_short_path() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:470` `fn test_center_truncate_truncates_long_path() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:482` `fn test_center_truncate_truncates_long_windows_path() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:495` `fn test_center_truncate_handles_long_segment() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:504` `fn test_format_json_compact_array() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:511` `fn test_format_json_compact_already_compact() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:518` `fn test_format_json_compact_with_whitespace() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:536` `fn test_format_json_compact_invalid_json() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:543` `fn test_format_json_compact_empty_object() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:550` `fn test_format_json_compact_empty_array() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:557` `fn test_format_json_compact_primitive_values() {`
- `fn` `codex-rs/tui/src/text_formatting.rs:566` `fn test_proper_join() {`

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
- `docs/workdocjcl/spec/06_UI/TUI.md`
