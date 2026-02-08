# `codex-rs/tui/src/bottom_pane/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `51369`
- sha256: `926db06baf0d7bc52ff4bce7a12a57cca396e02d373b6b643f2ca776ee8fed42`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/mod.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub fn new(params: BottomPaneParams) -> Self {`
- `pub fn set_skills(&mut self, skills: Option<Vec<SkillMetadata>>) {`
- `pub fn set_image_paste_enabled(&mut self, enabled: bool) {`
- `pub fn set_connectors_snapshot(&mut self, snapshot: Option<ConnectorsSnapshot>) {`
- `pub fn take_mention_bindings(&mut self) -> Vec<MentionBinding> {`
- `pub fn take_recent_submission_mention_bindings(&mut self) -> Vec<MentionBinding> {`
- `pub fn set_steer_enabled(&mut self, enabled: bool) {`
- `pub fn set_collaboration_modes_enabled(&mut self, enabled: bool) {`
- `pub fn set_connectors_enabled(&mut self, enabled: bool) {`
- `pub fn set_windows_degraded_sandbox_active(&mut self, enabled: bool) {`
- `pub fn set_collaboration_mode_indicator(`
- `pub fn set_personality_command_enabled(&mut self, enabled: bool) {`
- `pub fn status_widget(&self) -> Option<&StatusIndicatorWidget> {`
- `pub fn skills(&self) -> Option<&Vec<SkillMetadata>> {`
- `pub fn handle_key_event(&mut self, key_event: KeyEvent) -> InputResult {`
- `pub fn handle_paste(&mut self, pasted: String) {`
- `pub fn set_task_running(&mut self, running: bool) {`
- `pub fn push_approval_request(&mut self, request: ApprovalRequest, features: &Features) {`
- `pub fn push_user_input_request(&mut self, request: RequestUserInputEvent) {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:16` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:18` `use crate::app_event::ConnectorsSnapshot;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:19` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:20` `use crate::bottom_pane::queued_user_messages::QueuedUserMessages;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:21` `use crate::bottom_pane::unified_exec_footer::UnifiedExecFooter;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:22` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:23` `use crate::key_hint::KeyBinding;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:24` `use crate::render::renderable::FlexRenderable;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:25` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:26` `use crate::render::renderable::RenderableItem;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:27` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:28` `use bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:29` `use codex_core::features::Features;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:30` `use codex_core::skills::model::SkillMetadata;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:31` `use codex_file_search::FileMatch;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:32` `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:33` `use codex_protocol::user_input::TextElement;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:34` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:35` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:36` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:37` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:38` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:39` `use std::time::Duration;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:41` `mod app_link_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:42` `mod approval_overlay;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:43` `mod multi_select_picker;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:44` `mod request_user_input;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:45` `mod status_line_setup;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:50` `mod bottom_pane_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:65` `mod chat_composer;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:66` `mod chat_composer_history;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:67` `mod command_popup;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:68` `pub mod custom_prompt_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:69` `mod experimental_features_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:70` `mod file_search_popup;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:71` `mod footer;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:72` `mod list_selection_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:73` `mod prompt_args;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:74` `mod skill_popup;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:75` `mod skills_toggle_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:76` `mod slash_commands;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:80` `mod feedback_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:89` `mod paste_burst;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:90` `pub mod popup_consts;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:91` `mod queued_user_messages;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:92` `mod scroll_state;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:93` `mod selection_popup_common;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:94` `mod textarea;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:95` `mod unified_exec_footer;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:128` `use codex_protocol::custom_prompts::CustomPrompt;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:130` `use crate::status_indicator_widget::StatusIndicatorWidget;`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:180` `impl BottomPane {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:181` `pub fn new(params: BottomPaneParams) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:220` `pub fn set_skills(&mut self, skills: Option<Vec<SkillMetadata>>) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:228` `pub fn set_image_paste_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:233` `pub fn set_connectors_snapshot(&mut self, snapshot: Option<ConnectorsSnapshot>) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:238` `pub fn take_mention_bindings(&mut self) -> Vec<MentionBinding> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:242` `pub fn take_recent_submission_mention_bindings(&mut self) -> Vec<MentionBinding> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:253` `pub fn set_steer_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:257` `pub fn set_collaboration_modes_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:262` `pub fn set_connectors_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:267` `pub fn set_windows_degraded_sandbox_active(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:272` `pub fn set_collaboration_mode_indicator(`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:280` `pub fn set_personality_command_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:285` `pub fn status_widget(&self) -> Option<&StatusIndicatorWidget> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:289` `pub fn skills(&self) -> Option<&Vec<SkillMetadata>> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:303` `fn active_view(&self) -> Option<&dyn BottomPaneView> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:307` `fn push_view(&mut self, view: Box<dyn BottomPaneView>) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:313` `pub fn handle_key_event(&mut self, key_event: KeyEvent) -> InputResult {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:408` `pub fn handle_paste(&mut self, pasted: String) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:592` `pub fn set_task_running(&mut self, running: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:713` `pub fn push_approval_request(&mut self, request: ApprovalRequest, features: &Features) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:733` `pub fn push_user_input_request(&mut self, request: RequestUserInputEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:761` `fn on_active_view_complete(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:766` `fn pause_status_timer_for_modal(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:772` `fn resume_status_timer_after_modal(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:859` `fn as_renderable(&'_ self) -> RenderableItem<'_> {`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:898` `impl Renderable for BottomPane {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:899` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:902` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:905` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:912` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:913` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:914` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:915` `use codex_protocol::protocol::SkillScope;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:916` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:917` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:918` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:919` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:920` `use std::cell::Cell;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:921` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:922` `use std::rc::Rc;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:923` `use tokio::sync::mpsc::unbounded_channel;`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:925` `fn snapshot_buffer(buf: &Buffer) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:937` `fn render_snapshot(pane: &BottomPane, area: Rect) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:943` `fn exec_request() -> ApprovalRequest {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:953` `fn ctrl_c_on_modal_consumes_without_showing_quit_hint() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:976` `fn overlay_not_shown_above_approval_modal() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1010` `fn composer_shown_after_denied_while_task_running() {`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:1032` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:1033` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:1034` `use crossterm::event::KeyModifiers;`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1078` `fn status_indicator_visible_during_command_execution() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1105` `fn status_and_composer_fill_height_without_bottom_padding() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1136` `fn status_only_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1159` `fn status_with_details_and_queued_messages_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1190` `fn queued_messages_visible_when_status_hidden_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1218` `fn status_and_queued_messages_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1245` `fn esc_with_skill_popup_does_not_interrupt_task() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1291` `fn esc_with_slash_command_popup_does_not_interrupt_task() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1326` `fn esc_interrupts_running_task_when_no_popup() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1351` `fn esc_routes_to_handle_key_event_when_requested() {`
- `struct` `codex-rs/tui/src/bottom_pane/mod.rs:1353` `struct EscRoutingView {`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:1358` `impl Renderable for EscRoutingView {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1359` `fn render(&self, _area: Rect, _buf: &mut Buffer) {}`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1361` `fn desired_height(&self, _width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:1366` `impl BottomPaneView for EscRoutingView {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1367` `fn handle_key_event(&mut self, _key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1372` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1378` `fn prefer_esc_to_handle_key_event(&self) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use crate::app_event::ConnectorsSnapshot;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::bottom_pane::queued_user_messages::QueuedUserMessages;`
- `use crate::bottom_pane::unified_exec_footer::UnifiedExecFooter;`
- `use crate::key_hint;`
- `use crate::key_hint::KeyBinding;`
- `use crate::render::renderable::FlexRenderable;`
- `use crate::render::renderable::Renderable;`
- `use crate::render::renderable::RenderableItem;`
- `use crate::tui::FrameRequester;`
- `use bottom_pane_view::BottomPaneView;`
- `use codex_core::features::Features;`
- `use codex_core::skills::model::SkillMetadata;`
- `use codex_file_search::FileMatch;`
- `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use codex_protocol::user_input::TextElement;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use ratatui::buffer::Buffer;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
