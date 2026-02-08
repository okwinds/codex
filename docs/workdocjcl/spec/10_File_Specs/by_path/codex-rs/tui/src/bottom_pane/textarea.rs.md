# `codex-rs/tui/src/bottom_pane/textarea.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `85452`
- sha256: `60210db2799f26aaafa36b509c663d47b2164af07905f54109af1ad7d2801e1e`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/textarea.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new() -> Self {`
- `pub fn set_text_clearing_elements(&mut self, text: &str) {`
- `pub fn set_text_with_elements(&mut self, text: &str, elements: &[UserTextElement]) {`
- `pub fn text(&self) -> &str {`
- `pub fn insert_str(&mut self, text: &str) {`
- `pub fn insert_str_at(&mut self, pos: usize, text: &str) {`
- `pub fn replace_range(&mut self, range: std::ops::Range<usize>, text: &str) {`
- `pub fn cursor(&self) -> usize {`
- `pub fn set_cursor(&mut self, pos: usize) {`
- `pub fn desired_height(&self, width: u16) -> u16 {`
- `pub fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `pub fn cursor_pos_with_state(&self, area: Rect, state: TextAreaState) -> Option<(u16, u16)> {`
- `pub fn is_empty(&self) -> bool {`
- `pub fn input(&mut self, event: KeyEvent) {`
- `pub fn delete_backward(&mut self, n: usize) {`
- `pub fn delete_forward(&mut self, n: usize) {`
- `pub fn delete_backward_word(&mut self) {`
- `pub fn delete_forward_word(&mut self) {`
- `pub fn kill_to_end_of_line(&mut self) {`
- `pub fn kill_to_beginning_of_line(&mut self) {`
- `pub fn yank(&mut self) {`
- `pub fn move_cursor_left(&mut self) {`
- `pub fn move_cursor_right(&mut self) {`
- `pub fn move_cursor_up(&mut self) {`
- `pub fn move_cursor_down(&mut self) {`
- `pub fn move_cursor_to_beginning_of_line(&mut self, move_up_at_bol: bool) {`
- `pub fn move_cursor_to_end_of_line(&mut self, move_down_at_eol: bool) {`
- `pub fn element_payloads(&self) -> Vec<String> {`
- `pub fn text_elements(&self) -> Vec<UserTextElement> {`
- `pub fn replace_element_payload(&mut self, old: &str, new: &str) -> bool {`
- `pub fn insert_element(&mut self, text: &str) -> u64 {`
- `pub fn add_element_range(&mut self, range: Range<usize>) -> Option<u64> {`
- `pub fn remove_element_range(&mut self, range: Range<usize>) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:1` `use crate::key_hint::is_altgr;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:2` `use codex_protocol::user_input::ByteRange;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:3` `use codex_protocol::user_input::TextElement as UserTextElement;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:4` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:5` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:6` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:7` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:8` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:9` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:10` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:11` `use ratatui::widgets::StatefulWidgetRef;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:12` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:13` `use std::cell::Ref;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:14` `use std::cell::RefCell;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:15` `use std::ops::Range;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:16` `use textwrap::Options;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:17` `use unicode_segmentation::UnicodeSegmentation;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:18` `use unicode_width::UnicodeWidthStr;`
- `const` `codex-rs/tui/src/bottom_pane/textarea.rs:20` `const WORD_SEPARATORS: &str = "`~!@#$%^&*()-=+[{]}\\|;:'\",.<>/?";`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:22` `fn is_word_separator(ch: char) -> bool {`
- `struct` `codex-rs/tui/src/bottom_pane/textarea.rs:27` `struct TextElement {`
- `struct` `codex-rs/tui/src/bottom_pane/textarea.rs:51` `struct WrapCache {`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:62` `impl TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:63` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:76` `pub fn set_text_clearing_elements(&mut self, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:81` `pub fn set_text_with_elements(&mut self, text: &str, elements: &[UserTextElement]) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:85` `fn set_text_inner(&mut self, text: &str, elements: Option<&[UserTextElement]>) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:115` `pub fn text(&self) -> &str {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:119` `pub fn insert_str(&mut self, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:123` `pub fn insert_str_at(&mut self, pos: usize, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:134` `pub fn replace_range(&mut self, range: std::ops::Range<usize>, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:139` `fn replace_range_raw(&mut self, range: std::ops::Range<usize>, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:172` `pub fn cursor(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:176` `pub fn set_cursor(&mut self, pos: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:182` `pub fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:187` `pub fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:192` `pub fn cursor_pos_with_state(&self, area: Rect, state: TextAreaState) -> Option<(u16, u16)> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:205` `pub fn is_empty(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:209` `fn current_display_col(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:214` `fn wrapped_line_index_by_start(lines: &[Range<usize>], pos: usize) -> Option<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:221` `fn move_to_display_col_on_line(`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:241` `fn beginning_of_line(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:244` `fn beginning_of_current_line(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:248` `fn end_of_line(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:254` `fn end_of_current_line(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:258` `pub fn input(&mut self, event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:497` `pub fn delete_backward(&mut self, n: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:511` `pub fn delete_forward(&mut self, n: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:525` `pub fn delete_backward_word(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:535` `pub fn delete_forward_word(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:542` `pub fn kill_to_end_of_line(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:559` `pub fn kill_to_beginning_of_line(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:572` `pub fn yank(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:580` `fn kill_range(&mut self, range: Range<usize>) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:596` `pub fn move_cursor_left(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:602` `pub fn move_cursor_right(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:607` `pub fn move_cursor_up(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:670` `pub fn move_cursor_down(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:738` `pub fn move_cursor_to_beginning_of_line(&mut self, move_up_at_bol: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:748` `pub fn move_cursor_to_end_of_line(&mut self, move_down_at_eol: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:760` `pub fn element_payloads(&self) -> Vec<String> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:767` `pub fn text_elements(&self) -> Vec<UserTextElement> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:809` `pub fn replace_element_payload(&mut self, old: &str, new: &str) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:874` `pub fn insert_element(&mut self, text: &str) -> u64 {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:888` `pub fn add_element_range(&mut self, range: Range<usize>) -> Option<u64> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:917` `pub fn remove_element_range(&mut self, range: Range<usize>) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:929` `fn add_element(&mut self, range: Range<usize>) -> u64 {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:937` `fn next_element_id(&mut self) -> u64 {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:943` `fn find_element_containing(&self, pos: usize) -> Option<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:949` `fn clamp_pos_to_char_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:969` `fn clamp_pos_to_nearest_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:985` `fn clamp_pos_for_insertion(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1003` `fn expand_range_to_element_boundaries(&self, mut range: Range<usize>) -> Range<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1025` `fn shift_elements(&mut self, at: usize, removed: usize, inserted: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1050` `fn update_elements_after_replace(&mut self, start: usize, end: usize, inserted_len: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1054` `fn prev_atomic_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1080` `fn next_atomic_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1148` `fn adjust_pos_out_of_elements(&self, pos: usize, prefer_start: bool) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1162` `fn wrapped_lines(&self, width: u16) -> Ref<'_, Vec<Range<usize>>> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1188` `fn effective_scroll(`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:1217` `impl WidgetRef for &TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1218` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:1224` `impl StatefulWidgetRef for &TextArea {`
- `type` `codex-rs/tui/src/bottom_pane/textarea.rs:1225` `type State = TextAreaState;`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1227` `fn render_ref(&self, area: Rect, buf: &mut Buffer, state: &mut Self::State) {`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:1238` `impl TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1255` `fn render_lines(`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1285` `fn render_lines_masked(`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:1308` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:1310` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:1311` `use rand::prelude::*;`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1313` `fn rand_grapheme(rng: &mut rand::rngs::StdRng) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1354` `fn ta_with(text: &str) -> TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1361` `fn insert_and_replace_update_cursor_and_text() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1404` `fn insert_str_at_clamps_to_char_boundary() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1414` `fn set_text_clamps_cursor_to_char_boundary() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1425` `fn delete_backward_and_forward_edges() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1451` `fn delete_forward_deletes_element_at_left_edge() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1466` `fn delete_backward_word_and_kill_line_variants() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1517` `fn delete_forward_word_variants() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1556` `fn delete_forward_word_handles_atomic_elements() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1590` `fn delete_backward_word_respects_word_separators() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1615` `fn delete_forward_word_respects_word_separators() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1640` `fn yank_restores_last_kill() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1673` `fn cursor_left_and_right_handle_graphemes() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1696` `fn control_b_and_f_move_cursor() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1708` `fn control_b_f_fallback_control_chars_move_cursor() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1723` `fn delete_backward_word_alt_keys() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1743` `fn delete_backward_word_handles_narrow_no_break_space() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1752` `fn delete_forward_word_with_without_alt_modifier() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1767` `fn control_h_backspace() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1790` `fn altgr_ctrl_alt_char_inserts_literal() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1801` `fn cursor_vertical_movement_across_lines_and_bounds() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1833` `fn home_end_and_emacs_style_home_end() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1858` `fn end_of_line_or_down_at_end_of_text() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1874` `fn word_navigation_helpers() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1893` `fn wrapping_and_cursor_positions() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1921` `fn cursor_pos_with_state_basic_and_scroll_behaviors() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1962` `fn wrapped_navigation_across_visual_lines() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:2000` `fn cursor_pos_with_state_after_movements() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:2044` `fn wrapped_navigation_with_newlines_and_spaces() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:2069` `fn wrapped_navigation_with_wide_graphemes() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:2089` `fn fuzz_textarea_randomized() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::key_hint::is_altgr;`
- `use codex_protocol::user_input::ByteRange;`
- `use codex_protocol::user_input::TextElement as UserTextElement;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Color;`
- `use ratatui::style::Style;`
- `use ratatui::widgets::StatefulWidgetRef;`
- `use ratatui::widgets::WidgetRef;`
- `use std::cell::Ref;`
- `use std::cell::RefCell;`
- `use std::ops::Range;`
- `use textwrap::Options;`
- `use unicode_segmentation::UnicodeSegmentation;`
- `use unicode_width::UnicodeWidthStr;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
