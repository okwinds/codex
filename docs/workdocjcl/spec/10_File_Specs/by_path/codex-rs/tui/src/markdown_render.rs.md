# `codex-rs/tui/src/markdown_render.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `21942`
- sha256: `33a4540ad667a88cc92a986086269b21dcb99748029012f386452ab97f8bab2d`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/markdown_render.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn render_markdown_text(input: &str) -> Text<'static> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/markdown_render.rs:1` `use crate::render::line_utils::line_to_static;`
- `use` `codex-rs/tui/src/markdown_render.rs:2` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/markdown_render.rs:3` `use crate::wrapping::word_wrap_line;`
- `use` `codex-rs/tui/src/markdown_render.rs:4` `use pulldown_cmark::CodeBlockKind;`
- `use` `codex-rs/tui/src/markdown_render.rs:5` `use pulldown_cmark::CowStr;`
- `use` `codex-rs/tui/src/markdown_render.rs:6` `use pulldown_cmark::Event;`
- `use` `codex-rs/tui/src/markdown_render.rs:7` `use pulldown_cmark::HeadingLevel;`
- `use` `codex-rs/tui/src/markdown_render.rs:8` `use pulldown_cmark::Options;`
- `use` `codex-rs/tui/src/markdown_render.rs:9` `use pulldown_cmark::Parser;`
- `use` `codex-rs/tui/src/markdown_render.rs:10` `use pulldown_cmark::Tag;`
- `use` `codex-rs/tui/src/markdown_render.rs:11` `use pulldown_cmark::TagEnd;`
- `use` `codex-rs/tui/src/markdown_render.rs:12` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/markdown_render.rs:13` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/markdown_render.rs:14` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/markdown_render.rs:15` `use ratatui::text::Text;`
- `struct` `codex-rs/tui/src/markdown_render.rs:17` `struct MarkdownStyles {`
- `impl` `codex-rs/tui/src/markdown_render.rs:34` `impl Default for MarkdownStyles {`
- `fn` `codex-rs/tui/src/markdown_render.rs:35` `fn default() -> Self {`
- `use` `codex-rs/tui/src/markdown_render.rs:36` `use ratatui::style::Stylize;`
- `struct` `codex-rs/tui/src/markdown_render.rs:58` `struct IndentContext {`
- `impl` `codex-rs/tui/src/markdown_render.rs:64` `impl IndentContext {`
- `fn` `codex-rs/tui/src/markdown_render.rs:65` `fn new(prefix: Vec<Span<'static>>, marker: Option<Vec<Span<'static>>>, is_list: bool) -> Self {`
- `fn` `codex-rs/tui/src/markdown_render.rs:74` `pub fn render_markdown_text(input: &str) -> Text<'static> {`
- `struct` `codex-rs/tui/src/markdown_render.rs:87` `struct Writer<'a, I>`
- `fn` `codex-rs/tui/src/markdown_render.rs:114` `fn new(iter: I, wrap_width: Option<usize>) -> Self {`
- `fn` `codex-rs/tui/src/markdown_render.rs:136` `fn run(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:143` `fn handle_event(&mut self, event: Event<'a>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:166` `fn start_tag(&mut self, tag: Tag<'a>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:199` `fn end_tag(&mut self, tag: TagEnd) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:223` `fn start_paragraph(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:232` `fn end_paragraph(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:238` `fn start_heading(&mut self, level: HeadingLevel) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:257` `fn end_heading(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:262` `fn start_blockquote(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:271` `fn end_blockquote(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:276` `fn text(&mut self, text: CowStr<'a>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:315` `fn code(&mut self, code: CowStr<'a>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:324` `fn html(&mut self, html: CowStr<'a>, inline: bool) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:340` `fn hard_break(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:344` `fn soft_break(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:348` `fn start_list(&mut self, index: Option<u64>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:355` `fn end_list(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:360` `fn start_item(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:397` `fn start_codeblock(&mut self, _lang: Option<String>, indent: Option<Span<'static>>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:411` `fn end_codeblock(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:417` `fn push_inline_style(&mut self, style: Style) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:423` `fn pop_inline_style(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:427` `fn push_link(&mut self, dest_url: String) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:431` `fn pop_link(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:439` `fn flush_current_line(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:465` `fn push_line(&mut self, line: Line<'static>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:487` `fn push_span(&mut self, span: Span<'static>) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:495` `fn push_blank_line(&mut self) {`
- `fn` `codex-rs/tui/src/markdown_render.rs:505` `fn prefix_spans(&self, pending_marker_line: bool) -> Vec<Span<'static>> {`
- `use` `codex-rs/tui/src/markdown_render.rs:546` `use super::*;`
- `use` `codex-rs/tui/src/markdown_render.rs:547` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/markdown_render.rs:548` `use ratatui::text::Text;`
- `fn` `codex-rs/tui/src/markdown_render.rs:550` `fn lines_to_strings(text: &Text<'_>) -> Vec<String> {`
- `fn` `codex-rs/tui/src/markdown_render.rs:563` `fn wraps_plain_text_when_width_provided() {`
- `fn` `codex-rs/tui/src/markdown_render.rs:578` `fn wraps_list_items_preserving_indent() {`
- `fn` `codex-rs/tui/src/markdown_render.rs:589` `fn wraps_nested_lists() {`
- `fn` `codex-rs/tui/src/markdown_render.rs:608` `fn wraps_ordered_lists() {`
- `fn` `codex-rs/tui/src/markdown_render.rs:624` `fn wraps_blockquotes() {`
- `fn` `codex-rs/tui/src/markdown_render.rs:639` `fn wraps_blockquotes_inside_lists() {`
- `fn` `codex-rs/tui/src/markdown_render.rs:654` `fn wraps_list_items_containing_blockquotes() {`
- `fn` `codex-rs/tui/src/markdown_render.rs:669` `fn does_not_wrap_code_blocks() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::render::line_utils::line_to_static;`
- `use crate::wrapping::RtOptions;`
- `use crate::wrapping::word_wrap_line;`
- `use pulldown_cmark::CodeBlockKind;`
- `use pulldown_cmark::CowStr;`
- `use pulldown_cmark::Event;`
- `use pulldown_cmark::HeadingLevel;`
- `use pulldown_cmark::Options;`
- `use pulldown_cmark::Parser;`
- `use pulldown_cmark::Tag;`
- `use pulldown_cmark::TagEnd;`
- `use ratatui::style::Style;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::text::Text;`
- `use ratatui::style::Stylize;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use ratatui::text::Text;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
