# `codex-rs/tui/src/public_widgets/composer_input.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4529`
- sha256: `3232f9539c82adb494a592959ca82f0d1c9439bd5cf0534738139ed9af7f1018`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/public_widgets/composer_input.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ComposerAction {`
- `pub struct ComposerInput {`
- `pub fn new() -> Self {`
- `pub fn is_empty(&self) -> bool {`
- `pub fn clear(&mut self) {`
- `pub fn input(&mut self, key: KeyEvent) -> ComposerAction {`
- `pub fn handle_paste(&mut self, pasted: String) -> bool {`
- `pub fn set_hint_items(&mut self, items: Vec<(impl Into<String>, impl Into<String>)>) {`
- `pub fn clear_hint_items(&mut self) {`
- `pub fn desired_height(&self, width: u16) -> u16 {`
- `pub fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `pub fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `pub fn is_in_paste_burst(&self) -> bool {`
- `pub fn flush_paste_burst_if_due(&mut self) -> bool {`
- `pub fn recommended_flush_delay() -> Duration {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:7` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:8` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:9` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:10` `use std::time::Duration;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:12` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:13` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:14` `use crate::bottom_pane::ChatComposer;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:15` `use crate::bottom_pane::InputResult;`
- `use` `codex-rs/tui/src/public_widgets/composer_input.rs:16` `use crate::render::renderable::Renderable;`
- `enum` `codex-rs/tui/src/public_widgets/composer_input.rs:19` `pub enum ComposerAction {`
- `struct` `codex-rs/tui/src/public_widgets/composer_input.rs:28` `pub struct ComposerInput {`
- `impl` `codex-rs/tui/src/public_widgets/composer_input.rs:34` `impl ComposerInput {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:36` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:45` `pub fn is_empty(&self) -> bool {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:50` `pub fn clear(&mut self) {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:56` `pub fn input(&mut self, key: KeyEvent) -> ComposerAction {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:65` `pub fn handle_paste(&mut self, pasted: String) -> bool {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:73` `pub fn set_hint_items(&mut self, items: Vec<(impl Into<String>, impl Into<String>)>) {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:82` `pub fn clear_hint_items(&mut self) {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:87` `pub fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:92` `pub fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:97` `pub fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:102` `pub fn is_in_paste_burst(&self) -> bool {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:108` `pub fn flush_paste_burst_if_due(&mut self) -> bool {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:116` `pub fn recommended_flush_delay() -> Duration {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:120` `fn drain_app_events(&mut self) {`
- `impl` `codex-rs/tui/src/public_widgets/composer_input.rs:125` `impl Default for ComposerInput {`
- `fn` `codex-rs/tui/src/public_widgets/composer_input.rs:126` `fn default() -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyEvent;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use std::time::Duration;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::bottom_pane::ChatComposer;`
- `use crate::bottom_pane::InputResult;`
- `use crate::render::renderable::Renderable;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
