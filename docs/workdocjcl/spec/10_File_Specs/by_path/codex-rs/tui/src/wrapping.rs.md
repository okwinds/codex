# `codex-rs/tui/src/wrapping.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `21500`
- sha256: `2557f6dce29de39e15ed9f3d4e224435bce02dd78591e1cfaeba8b298e4cb7e0`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/wrapping.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RtOptions<'a> {`
- `pub fn new(width: usize) -> Self {`
- `pub fn line_ending(self, line_ending: textwrap::LineEnding) -> Self {`
- `pub fn width(self, width: usize) -> Self {`
- `pub fn initial_indent(self, initial_indent: Line<'a>) -> Self {`
- `pub fn subsequent_indent(self, subsequent_indent: Line<'a>) -> Self {`
- `pub fn break_words(self, break_words: bool) -> Self {`
- `pub fn word_separator(self, word_separator: textwrap::WordSeparator) -> RtOptions<'a> {`
- `pub fn wrap_algorithm(self, wrap_algorithm: textwrap::WrapAlgorithm) -> RtOptions<'a> {`
- `pub fn word_splitter(self, word_splitter: textwrap::WordSplitter) -> RtOptions<'a> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/wrapping.rs:1` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/wrapping.rs:2` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/wrapping.rs:3` `use std::borrow::Cow;`
- `use` `codex-rs/tui/src/wrapping.rs:4` `use std::ops::Range;`
- `use` `codex-rs/tui/src/wrapping.rs:5` `use textwrap::Options;`
- `use` `codex-rs/tui/src/wrapping.rs:7` `use crate::render::line_utils::push_owned_lines;`
- `struct` `codex-rs/tui/src/wrapping.rs:52` `pub struct RtOptions<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:78` `impl From<usize> for RtOptions<'_> {`
- `fn` `codex-rs/tui/src/wrapping.rs:79` `fn from(width: usize) -> Self {`
- `impl` `codex-rs/tui/src/wrapping.rs:85` `impl<'a> RtOptions<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:86` `pub fn new(width: usize) -> Self {`
- `fn` `codex-rs/tui/src/wrapping.rs:99` `pub fn line_ending(self, line_ending: textwrap::LineEnding) -> Self {`
- `fn` `codex-rs/tui/src/wrapping.rs:106` `pub fn width(self, width: usize) -> Self {`
- `fn` `codex-rs/tui/src/wrapping.rs:110` `pub fn initial_indent(self, initial_indent: Line<'a>) -> Self {`
- `fn` `codex-rs/tui/src/wrapping.rs:117` `pub fn subsequent_indent(self, subsequent_indent: Line<'a>) -> Self {`
- `fn` `codex-rs/tui/src/wrapping.rs:124` `pub fn break_words(self, break_words: bool) -> Self {`
- `fn` `codex-rs/tui/src/wrapping.rs:131` `pub fn word_separator(self, word_separator: textwrap::WordSeparator) -> RtOptions<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:138` `pub fn wrap_algorithm(self, wrap_algorithm: textwrap::WrapAlgorithm) -> RtOptions<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:145` `pub fn word_splitter(self, word_splitter: textwrap::WordSplitter) -> RtOptions<'a> {`
- `enum` `codex-rs/tui/src/wrapping.rs:239` `enum LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:244` `impl<'a> LineInput<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:245` `fn as_ref(&self) -> &Line<'a> {`
- `trait` `codex-rs/tui/src/wrapping.rs:254` `trait IntoLineInput<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:255` `fn into_line_input(self) -> LineInput<'a>;`
- `impl` `codex-rs/tui/src/wrapping.rs:258` `impl<'a> IntoLineInput<'a> for &'a Line<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:259` `fn into_line_input(self) -> LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:264` `impl<'a> IntoLineInput<'a> for &'a mut Line<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:265` `fn into_line_input(self) -> LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:270` `impl<'a> IntoLineInput<'a> for Line<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:271` `fn into_line_input(self) -> LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:276` `impl<'a> IntoLineInput<'a> for String {`
- `fn` `codex-rs/tui/src/wrapping.rs:277` `fn into_line_input(self) -> LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:282` `impl<'a> IntoLineInput<'a> for &'a str {`
- `fn` `codex-rs/tui/src/wrapping.rs:283` `fn into_line_input(self) -> LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:288` `impl<'a> IntoLineInput<'a> for Cow<'a, str> {`
- `fn` `codex-rs/tui/src/wrapping.rs:289` `fn into_line_input(self) -> LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:294` `impl<'a> IntoLineInput<'a> for Span<'a> {`
- `fn` `codex-rs/tui/src/wrapping.rs:295` `fn into_line_input(self) -> LineInput<'a> {`
- `impl` `codex-rs/tui/src/wrapping.rs:300` `impl<'a> IntoLineInput<'a> for Vec<Span<'a>> {`
- `fn` `codex-rs/tui/src/wrapping.rs:301` `fn into_line_input(self) -> LineInput<'a> {`
- `use` `codex-rs/tui/src/wrapping.rs:400` `use super::*;`
- `use` `codex-rs/tui/src/wrapping.rs:401` `use itertools::Itertools as _;`
- `use` `codex-rs/tui/src/wrapping.rs:402` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/wrapping.rs:403` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/wrapping.rs:404` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/wrapping.rs:405` `use std::string::ToString;`
- `fn` `codex-rs/tui/src/wrapping.rs:407` `fn concat_line(line: &Line) -> String {`
- `fn` `codex-rs/tui/src/wrapping.rs:415` `fn trivial_unstyled_no_indents_wide_width() {`
- `fn` `codex-rs/tui/src/wrapping.rs:423` `fn simple_unstyled_wrap_narrow_width() {`
- `fn` `codex-rs/tui/src/wrapping.rs:432` `fn simple_styled_wrap_preserves_styles() {`
- `fn` `codex-rs/tui/src/wrapping.rs:447` `fn with_initial_and_subsequent_indents() {`
- `fn` `codex-rs/tui/src/wrapping.rs:464` `fn empty_initial_indent_subsequent_spaces() {`
- `fn` `codex-rs/tui/src/wrapping.rs:477` `fn empty_input_yields_single_empty_line() {`
- `fn` `codex-rs/tui/src/wrapping.rs:485` `fn leading_spaces_preserved_on_first_line() {`
- `fn` `codex-rs/tui/src/wrapping.rs:493` `fn multiple_spaces_between_words_dont_start_next_line_with_spaces() {`
- `fn` `codex-rs/tui/src/wrapping.rs:502` `fn break_words_false_allows_overflow_for_long_word() {`
- `fn` `codex-rs/tui/src/wrapping.rs:511` `fn hyphen_splitter_breaks_at_hyphen() {`
- `fn` `codex-rs/tui/src/wrapping.rs:520` `fn indent_consumes_width_leaving_one_char_space() {`
- `fn` `codex-rs/tui/src/wrapping.rs:533` `fn wide_unicode_wraps_by_display_width() {`
- `fn` `codex-rs/tui/src/wrapping.rs:542` `fn styled_split_within_span_preserves_style() {`
- `use` `codex-rs/tui/src/wrapping.rs:543` `use ratatui::style::Stylize;`
- `fn` `codex-rs/tui/src/wrapping.rs:556` `fn wrap_lines_applies_initial_indent_only_once() {`
- `fn` `codex-rs/tui/src/wrapping.rs:574` `fn wrap_lines_without_indents_is_concat_of_single_wraps() {`
- `fn` `codex-rs/tui/src/wrapping.rs:582` `fn wrap_lines_borrowed_applies_initial_indent_only_once() {`
- `fn` `codex-rs/tui/src/wrapping.rs:598` `fn wrap_lines_borrowed_without_indents_is_concat_of_single_wraps() {`
- `fn` `codex-rs/tui/src/wrapping.rs:606` `fn wrap_lines_accepts_borrowed_iterators() {`
- `fn` `codex-rs/tui/src/wrapping.rs:614` `fn wrap_lines_accepts_str_slices() {`
- `fn` `codex-rs/tui/src/wrapping.rs:622` `fn line_height_counts_double_width_emoji() {`
- `fn` `codex-rs/tui/src/wrapping.rs:630` `fn word_wrap_does_not_split_words_simple_english() {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use std::borrow::Cow;`
- `use std::ops::Range;`
- `use textwrap::Options;`
- `use crate::render::line_utils::push_owned_lines;`
- `use super::*;`
- `use itertools::Itertools as _;`
- `use pretty_assertions::assert_eq;`
- `use ratatui::style::Color;`
- `use ratatui::style::Stylize;`
- `use std::string::ToString;`
- `use ratatui::style::Stylize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
