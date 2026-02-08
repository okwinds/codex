# `codex-rs/tui/src/bottom_pane/textarea.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `83990`
- sha256: `eb4a0aa9a7cd36424a41619ef3cba8311baae169a56fbcb08f9d6b6c61711840`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `pub fn insert_element(&mut self, text: &str) {`
- `pub fn add_element_range(&mut self, range: Range<usize>) {`
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
- `struct` `codex-rs/tui/src/bottom_pane/textarea.rs:42` `struct WrapCache {`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:53` `impl TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:54` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:66` `pub fn set_text_clearing_elements(&mut self, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:71` `pub fn set_text_with_elements(&mut self, text: &str, elements: &[UserTextElement]) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:75` `fn set_text_inner(&mut self, text: &str, elements: Option<&[UserTextElement]>) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:101` `pub fn text(&self) -> &str {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:105` `pub fn insert_str(&mut self, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:109` `pub fn insert_str_at(&mut self, pos: usize, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:120` `pub fn replace_range(&mut self, range: std::ops::Range<usize>, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:125` `fn replace_range_raw(&mut self, range: std::ops::Range<usize>, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:158` `pub fn cursor(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:162` `pub fn set_cursor(&mut self, pos: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:168` `pub fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:173` `pub fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:178` `pub fn cursor_pos_with_state(&self, area: Rect, state: TextAreaState) -> Option<(u16, u16)> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:191` `pub fn is_empty(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:195` `fn current_display_col(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:200` `fn wrapped_line_index_by_start(lines: &[Range<usize>], pos: usize) -> Option<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:207` `fn move_to_display_col_on_line(`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:227` `fn beginning_of_line(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:230` `fn beginning_of_current_line(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:234` `fn end_of_line(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:240` `fn end_of_current_line(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:244` `pub fn input(&mut self, event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:483` `pub fn delete_backward(&mut self, n: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:497` `pub fn delete_forward(&mut self, n: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:511` `pub fn delete_backward_word(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:521` `pub fn delete_forward_word(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:528` `pub fn kill_to_end_of_line(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:545` `pub fn kill_to_beginning_of_line(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:558` `pub fn yank(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:566` `fn kill_range(&mut self, range: Range<usize>) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:582` `pub fn move_cursor_left(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:588` `pub fn move_cursor_right(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:593` `pub fn move_cursor_up(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:656` `pub fn move_cursor_down(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:724` `pub fn move_cursor_to_beginning_of_line(&mut self, move_up_at_bol: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:734` `pub fn move_cursor_to_end_of_line(&mut self, move_down_at_eol: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:746` `pub fn element_payloads(&self) -> Vec<String> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:753` `pub fn text_elements(&self) -> Vec<UserTextElement> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:773` `pub fn replace_element_payload(&mut self, old: &str, new: &str) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:838` `pub fn insert_element(&mut self, text: &str) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:851` `pub fn add_element_range(&mut self, range: Range<usize>) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:875` `pub fn remove_element_range(&mut self, range: Range<usize>) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:887` `fn add_element(&mut self, range: Range<usize>) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:893` `fn find_element_containing(&self, pos: usize) -> Option<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:899` `fn clamp_pos_to_char_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:919` `fn clamp_pos_to_nearest_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:935` `fn clamp_pos_for_insertion(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:953` `fn expand_range_to_element_boundaries(&self, mut range: Range<usize>) -> Range<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:975` `fn shift_elements(&mut self, at: usize, removed: usize, inserted: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1000` `fn update_elements_after_replace(&mut self, start: usize, end: usize, inserted_len: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1004` `fn prev_atomic_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1030` `fn next_atomic_boundary(&self, pos: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1098` `fn adjust_pos_out_of_elements(&self, pos: usize, prefer_start: bool) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1112` `fn wrapped_lines(&self, width: u16) -> Ref<'_, Vec<Range<usize>>> {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1138` `fn effective_scroll(`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:1167` `impl WidgetRef for &TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1168` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:1174` `impl StatefulWidgetRef for &TextArea {`
- `type` `codex-rs/tui/src/bottom_pane/textarea.rs:1175` `type State = TextAreaState;`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1177` `fn render_ref(&self, area: Rect, buf: &mut Buffer, state: &mut Self::State) {`
- `impl` `codex-rs/tui/src/bottom_pane/textarea.rs:1188` `impl TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1205` `fn render_lines(`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1235` `fn render_lines_masked(`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:1258` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:1260` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/textarea.rs:1261` `use rand::prelude::*;`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1263` `fn rand_grapheme(rng: &mut rand::rngs::StdRng) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1304` `fn ta_with(text: &str) -> TextArea {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1311` `fn insert_and_replace_update_cursor_and_text() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1354` `fn insert_str_at_clamps_to_char_boundary() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1364` `fn set_text_clamps_cursor_to_char_boundary() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1375` `fn delete_backward_and_forward_edges() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1401` `fn delete_forward_deletes_element_at_left_edge() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1416` `fn delete_backward_word_and_kill_line_variants() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1467` `fn delete_forward_word_variants() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1506` `fn delete_forward_word_handles_atomic_elements() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1540` `fn delete_backward_word_respects_word_separators() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1565` `fn delete_forward_word_respects_word_separators() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1590` `fn yank_restores_last_kill() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1623` `fn cursor_left_and_right_handle_graphemes() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1646` `fn control_b_and_f_move_cursor() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1658` `fn control_b_f_fallback_control_chars_move_cursor() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1673` `fn delete_backward_word_alt_keys() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1693` `fn delete_backward_word_handles_narrow_no_break_space() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1702` `fn delete_forward_word_with_without_alt_modifier() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1717` `fn control_h_backspace() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1740` `fn altgr_ctrl_alt_char_inserts_literal() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1751` `fn cursor_vertical_movement_across_lines_and_bounds() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1783` `fn home_end_and_emacs_style_home_end() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1808` `fn end_of_line_or_down_at_end_of_text() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1824` `fn word_navigation_helpers() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1843` `fn wrapping_and_cursor_positions() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1871` `fn cursor_pos_with_state_basic_and_scroll_behaviors() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1912` `fn wrapped_navigation_across_visual_lines() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1950` `fn cursor_pos_with_state_after_movements() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:1994` `fn wrapped_navigation_with_newlines_and_spaces() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:2019` `fn wrapped_navigation_with_wide_graphemes() {`
- `fn` `codex-rs/tui/src/bottom_pane/textarea.rs:2039` `fn fuzz_textarea_randomized() {`

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
- `workdocjcl/spec/06_UI/TUI.md`
