# `codex-rs/tui/src/bottom_pane/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `50193`
- sha256: `4917daf7f4e9705cc53dfd1db5b0d55d96aaaac704576e4d70d044deebd14416`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `pub fn take_mention_paths(&mut self) -> HashMap<String, String> {`
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
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:16` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:17` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:19` `use crate::app_event::ConnectorsSnapshot;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:20` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:21` `use crate::bottom_pane::queued_user_messages::QueuedUserMessages;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:22` `use crate::bottom_pane::unified_exec_footer::UnifiedExecFooter;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:23` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:24` `use crate::key_hint::KeyBinding;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:25` `use crate::render::renderable::FlexRenderable;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:26` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:27` `use crate::render::renderable::RenderableItem;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:28` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:29` `use bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:30` `use codex_core::features::Features;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:31` `use codex_core::skills::model::SkillMetadata;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:32` `use codex_file_search::FileMatch;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:33` `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:34` `use codex_protocol::user_input::TextElement;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:35` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:36` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:37` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:38` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:39` `use std::time::Duration;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:41` `mod app_link_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:42` `mod approval_overlay;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:43` `mod request_user_input;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:48` `mod bottom_pane_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:55` `mod chat_composer;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:56` `mod chat_composer_history;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:57` `mod command_popup;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:58` `pub mod custom_prompt_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:59` `mod experimental_features_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:60` `mod file_search_popup;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:61` `mod footer;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:62` `mod list_selection_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:63` `mod prompt_args;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:64` `mod skill_popup;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:65` `mod skills_toggle_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:66` `mod slash_commands;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:69` `mod feedback_view;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:76` `mod paste_burst;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:77` `pub mod popup_consts;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:78` `mod queued_user_messages;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:79` `mod scroll_state;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:80` `mod selection_popup_common;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:81` `mod textarea;`
- `mod` `codex-rs/tui/src/bottom_pane/mod.rs:82` `mod unified_exec_footer;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:115` `use codex_protocol::custom_prompts::CustomPrompt;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:117` `use crate::status_indicator_widget::StatusIndicatorWidget;`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:167` `impl BottomPane {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:168` `pub fn new(params: BottomPaneParams) -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:207` `pub fn set_skills(&mut self, skills: Option<Vec<SkillMetadata>>) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:215` `pub fn set_image_paste_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:220` `pub fn set_connectors_snapshot(&mut self, snapshot: Option<ConnectorsSnapshot>) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:225` `pub fn take_mention_paths(&mut self) -> HashMap<String, String> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:235` `pub fn set_steer_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:239` `pub fn set_collaboration_modes_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:244` `pub fn set_connectors_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:249` `pub fn set_windows_degraded_sandbox_active(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:254` `pub fn set_collaboration_mode_indicator(`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:262` `pub fn set_personality_command_enabled(&mut self, enabled: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:267` `pub fn status_widget(&self) -> Option<&StatusIndicatorWidget> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:271` `pub fn skills(&self) -> Option<&Vec<SkillMetadata>> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:285` `fn active_view(&self) -> Option<&dyn BottomPaneView> {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:289` `fn push_view(&mut self, view: Box<dyn BottomPaneView>) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:295` `pub fn handle_key_event(&mut self, key_event: KeyEvent) -> InputResult {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:390` `pub fn handle_paste(&mut self, pasted: String) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:570` `pub fn set_task_running(&mut self, running: bool) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:691` `pub fn push_approval_request(&mut self, request: ApprovalRequest, features: &Features) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:711` `pub fn push_user_input_request(&mut self, request: RequestUserInputEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:739` `fn on_active_view_complete(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:744` `fn pause_status_timer_for_modal(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:750` `fn resume_status_timer_after_modal(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:837` `fn as_renderable(&'_ self) -> RenderableItem<'_> {`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:866` `impl Renderable for BottomPane {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:867` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:870` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:873` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:880` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:881` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:882` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:883` `use codex_protocol::protocol::SkillScope;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:884` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:885` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:886` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:887` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:888` `use std::cell::Cell;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:889` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:890` `use std::rc::Rc;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:891` `use tokio::sync::mpsc::unbounded_channel;`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:893` `fn snapshot_buffer(buf: &Buffer) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:905` `fn render_snapshot(pane: &BottomPane, area: Rect) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:911` `fn exec_request() -> ApprovalRequest {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:921` `fn ctrl_c_on_modal_consumes_without_showing_quit_hint() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:944` `fn overlay_not_shown_above_approval_modal() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:978` `fn composer_shown_after_denied_while_task_running() {`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:1000` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:1001` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/mod.rs:1002` `use crossterm::event::KeyModifiers;`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1046` `fn status_indicator_visible_during_command_execution() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1073` `fn status_and_composer_fill_height_without_bottom_padding() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1104` `fn status_only_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1127` `fn status_with_details_and_queued_messages_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1158` `fn queued_messages_visible_when_status_hidden_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1186` `fn status_and_queued_messages_snapshot() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1213` `fn esc_with_skill_popup_does_not_interrupt_task() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1259` `fn esc_with_slash_command_popup_does_not_interrupt_task() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1294` `fn esc_interrupts_running_task_when_no_popup() {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1319` `fn esc_routes_to_handle_key_event_when_requested() {`
- `struct` `codex-rs/tui/src/bottom_pane/mod.rs:1321` `struct EscRoutingView {`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:1326` `impl Renderable for EscRoutingView {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1327` `fn render(&self, _area: Rect, _buf: &mut Buffer) {}`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1329` `fn desired_height(&self, _width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/bottom_pane/mod.rs:1334` `impl BottomPaneView for EscRoutingView {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1335` `fn handle_key_event(&mut self, _key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1340` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/mod.rs:1346` `fn prefer_esc_to_handle_key_event(&self) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
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
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
