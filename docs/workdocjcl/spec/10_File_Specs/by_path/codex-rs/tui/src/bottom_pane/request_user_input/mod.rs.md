# `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `93890`
- sha256: `67a7165ae2b30299aa2aedf10ebdac0ca898006b80f69f3e40461d7a80ee8777`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:9` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:10` `use std::collections::VecDeque;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:11` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:13` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:14` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:15` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:16` `use crossterm::event::KeyModifiers;`
- `mod` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:17` `mod layout;`
- `mod` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:18` `mod render;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:20` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:21` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:22` `use crate::bottom_pane::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:23` `use crate::bottom_pane::ChatComposer;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:24` `use crate::bottom_pane::ChatComposerConfig;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:25` `use crate::bottom_pane::InputResult;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:26` `use crate::bottom_pane::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:27` `use crate::bottom_pane::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:28` `use crate::bottom_pane::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:29` `use crate::bottom_pane::selection_popup_common::measure_rows_height;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:30` `use crate::history_cell;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:31` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:33` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:34` `use codex_protocol::request_user_input::RequestUserInputAnswer;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:35` `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:36` `use codex_protocol::request_user_input::RequestUserInputResponse;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:37` `use codex_protocol::user_input::TextElement;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:38` `use unicode_width::UnicodeWidthStr;`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:40` `const NOTES_PLACEHOLDER: &str = "Add notes";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:41` `const ANSWER_PLACEHOLDER: &str = "Type your answer (optional)";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:43` `const MIN_COMPOSER_HEIGHT: u16 = 3;`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:44` `const SELECT_OPTION_PLACEHOLDER: &str = "Select an option to add notes";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:47` `const OTHER_OPTION_LABEL: &str = "None of the above";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:48` `const OTHER_OPTION_DESCRIPTION: &str = "Optionally, add details in notes (tab).";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:49` `const UNANSWERED_CONFIRM_TITLE: &str = "Submit with unanswered questions?";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:50` `const UNANSWERED_CONFIRM_GO_BACK: &str = "Go back";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:51` `const UNANSWERED_CONFIRM_GO_BACK_DESC: &str = "Return to the first unanswered question.";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:52` `const UNANSWERED_CONFIRM_SUBMIT: &str = "Proceed";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:53` `const UNANSWERED_CONFIRM_SUBMIT_DESC_SINGULAR: &str = "question";`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:54` `const UNANSWERED_CONFIRM_SUBMIT_DESC_PLURAL: &str = "questions";`
- `enum` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:57` `enum Focus {`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:63` `struct ComposerDraft {`
- `impl` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:70` `impl ComposerDraft {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:71` `fn text_with_pending(&self) -> String {`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:88` `struct AnswerState {`
- `impl` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:105` `impl FooterTip {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:106` `fn new(text: impl Into<String>) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:113` `fn highlighted(text: impl Into<String>) -> Self {`
- `impl` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:138` `impl RequestUserInputOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:176` `fn current_index(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:180` `fn current_question(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:186` `fn current_answer_mut(&mut self) -> Option<&mut AnswerState> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:191` `fn current_answer(&self) -> Option<&AnswerState> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:196` `fn question_count(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:200` `fn has_options(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:206` `fn options_len(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:212` `fn option_index_for_digit(&self, ch: char) -> Option<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:224` `fn selected_option_index(&self) -> Option<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:232` `fn notes_has_content(&self, idx: usize) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:260` `fn focus_is_notes(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:264` `fn confirm_unanswered_active(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:350` `fn capture_composer_draft(&self) -> ComposerDraft {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:364` `fn save_current_draft(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:378` `fn restore_current_draft(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:395` `fn notes_placeholder(&self) -> &'static str {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:405` `fn sync_composer_placeholder(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:410` `fn clear_notes_draft(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:423` `fn footer_tips(&self) -> Vec<FooterTip> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:473` `fn wrap_footer_tips(&self, width: u16, tips: Vec<FooterTip>) -> Vec<Vec<FooterTip>> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:519` `fn ensure_focus_available(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:537` `fn reset_for_request(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:568` `fn options_len_for_question(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:583` `fn other_option_enabled_for_question(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:593` `fn option_label_for_index(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:608` `fn move_question(&mut self, next: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:620` `fn jump_to_question(&mut self, idx: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:631` `fn select_current_option(&mut self, committed: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:649` `fn clear_selection(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:667` `fn ensure_selected_for_notes(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:675` `fn go_next_or_submit(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:689` `fn submit_answers(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:747` `fn open_unanswered_confirmation(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:753` `fn close_unanswered_confirmation(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:757` `fn unanswered_question_count(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:761` `fn unanswered_submit_description(&self) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:771` `fn first_unanswered_index(&self) -> Option<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:781` `fn unanswered_confirmation_rows(&self) -> Vec<GenericDisplayRow> {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:812` `fn is_question_answered(&self, idx: usize, _current_text: &str) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:831` `fn unanswered_count(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:842` `fn notes_input_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:849` `fn apply_submission_to_draft(&mut self, text: String, text_elements: Vec<TextElement>) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:870` `fn apply_submission_draft(&mut self, draft: ComposerDraft) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:881` `fn handle_composer_input_result(&mut self, result: InputResult) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:920` `fn handle_confirm_unanswered_key_event(&mut self, key_event: KeyEvent) {`
- `impl` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:963` `impl BottomPaneView for RequestUserInputOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:964` `fn prefer_esc_to_handle_key_event(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:968` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1185` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1206` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1210` `fn handle_paste(&mut self, pasted: String) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1225` `fn flush_paste_burst_if_due(&mut self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1229` `fn is_in_paste_burst(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1233` `fn try_consume_user_input_request(`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1244` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1245` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1246` `use crate::bottom_pane::selection_popup_common::menu_surface_inset;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1247` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1248` `use codex_protocol::request_user_input::RequestUserInputQuestion;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1249` `use codex_protocol::request_user_input::RequestUserInputQuestionOption;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1250` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1251` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1252` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1253` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1254` `use tokio::sync::mpsc::unbounded_channel;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1255` `use unicode_width::UnicodeWidthStr;`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1257` `fn test_sender() -> (`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1265` `fn expect_interrupt_only(rx: &mut tokio::sync::mpsc::UnboundedReceiver<AppEvent>) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1277` `fn question_with_options(id: &str, header: &str) -> RequestUserInputQuestion {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1301` `fn question_with_options_and_other(id: &str, header: &str) -> RequestUserInputQuestion {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1325` `fn question_with_wrapped_options(id: &str, header: &str) -> RequestUserInputQuestion {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1355` `fn question_without_options(id: &str, header: &str) -> RequestUserInputQuestion {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1366` `fn request_event(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1377` `fn snapshot_buffer(buf: &Buffer) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1389` `fn render_snapshot(overlay: &RequestUserInputOverlay, area: Rect) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1396` `fn queued_requests_are_fifo() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1422` `fn interrupt_discards_queued_requests_and_emits_interrupt() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1449` `fn options_can_submit_empty_when_unanswered() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1471` `fn enter_commits_default_selection_on_last_option_question() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1492` `fn enter_commits_default_selection_on_non_last_option_question() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1540` `fn number_keys_select_and_submit_options() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1561` `fn vim_keys_move_option_selection() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1583` `fn typing_in_options_does_not_open_notes() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1609` `fn h_l_move_between_questions_in_options() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1633` `fn tab_opens_notes_when_option_selected() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1652` `fn switching_to_options_resets_notes_focus_when_notes_hidden() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1676` `fn switching_from_freeform_with_text_resets_focus_and_keeps_last_option_empty() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1722` `fn esc_in_notes_mode_without_options_interrupts() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1739` `fn esc_in_options_mode_interrupts() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1756` `fn esc_in_notes_mode_interrupts() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1777` `fn esc_in_notes_mode_interrupts_with_notes_visible() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1799` `fn esc_drops_committed_answers() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1827` `fn backspace_in_options_clears_selection() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1848` `fn backspace_on_empty_notes_closes_notes_ui() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1874` `fn tab_in_notes_clears_notes_and_hides_ui() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1903` `fn skipped_option_questions_count_as_unanswered() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1917` `fn highlighted_option_questions_are_unanswered() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1933` `fn freeform_requires_enter_with_text_to_mark_answered() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1962` `fn freeform_enter_with_empty_text_is_unanswered() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:1985` `fn freeform_questions_submit_empty_when_empty() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2006` `fn freeform_draft_is_not_submitted_without_enter() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2031` `fn freeform_commit_resets_when_draft_changes() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2074` `fn notes_are_captured_for_selected_option() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2116` `fn notes_submission_commits_selected_option() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2148` `fn is_other_adds_none_of_the_above_and_submits_it() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2201` `fn large_paste_is_preserved_when_switching_questions() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2229` `fn pending_paste_placeholder_survives_submission_and_back_navigation() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2260` `fn request_user_input_options_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2277` `fn request_user_input_options_notes_visible_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2300` `fn request_user_input_tight_height_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2317` `fn layout_allocates_all_wrapped_options_when_space_allows() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2345` `fn desired_height_keeps_spacers_and_preferred_options_visible() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2374` `fn footer_wraps_tips_without_splitting_individual_tips() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2411` `fn request_user_input_wrapped_options_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2444` `fn request_user_input_footer_wrap_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2472` `fn request_user_input_scroll_options_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2524` `fn request_user_input_hidden_options_footer_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2576` `fn request_user_input_freeform_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2593` `fn request_user_input_multi_question_first_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2616` `fn request_user_input_multi_question_last_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2640` `fn request_user_input_unanswered_confirmation_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/mod.rs:2666` `fn options_scroll_while_editing_notes() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::collections::VecDeque;`
- `use std::path::PathBuf;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::KeyModifiers;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::bottom_pane::CancellationEvent;`
- `use crate::bottom_pane::ChatComposer;`
- `use crate::bottom_pane::ChatComposerConfig;`
- `use crate::bottom_pane::InputResult;`
- `use crate::bottom_pane::bottom_pane_view::BottomPaneView;`
- `use crate::bottom_pane::scroll_state::ScrollState;`
- `use crate::bottom_pane::selection_popup_common::GenericDisplayRow;`
- `use crate::bottom_pane::selection_popup_common::measure_rows_height;`
- `use crate::history_cell;`
- `use crate::render::renderable::Renderable;`
- `use codex_core::protocol::Op;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
