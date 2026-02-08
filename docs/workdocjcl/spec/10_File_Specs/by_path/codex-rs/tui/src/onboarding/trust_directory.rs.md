# `codex-rs/tui/src/onboarding/trust_directory.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7971`
- sha256: `c44c11409234d5b37941253e8cf7998ee28ef990cc69810b311754299205acdc`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/onboarding/trust_directory.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum TrustDirectorySelection {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:3` `use codex_core::config::set_project_trust_level;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:4` `use codex_core::git_info::resolve_root_git_project_for_trust;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:5` `use codex_protocol::config_types::TrustLevel;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:6` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:7` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:8` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:9` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:10` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:11` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:12` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:13` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:14` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:15` `use ratatui::widgets::Wrap;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:17` `use crate::key_hint;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:18` `use crate::onboarding::onboarding_screen::KeyboardHandler;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:19` `use crate::onboarding::onboarding_screen::StepStateProvider;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:20` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:21` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:22` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:23` `use crate::render::renderable::RenderableExt as _;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:24` `use crate::selection_list::selection_option_row;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:26` `use super::onboarding_screen::StepState;`
- `enum` `codex-rs/tui/src/onboarding/trust_directory.rs:37` `pub enum TrustDirectorySelection {`
- `impl` `codex-rs/tui/src/onboarding/trust_directory.rs:42` `impl WidgetRef for &TrustDirectoryWidget {`
- `fn` `codex-rs/tui/src/onboarding/trust_directory.rs:43` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/onboarding/trust_directory.rs:120` `impl KeyboardHandler for TrustDirectoryWidget {`
- `fn` `codex-rs/tui/src/onboarding/trust_directory.rs:121` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `impl` `codex-rs/tui/src/onboarding/trust_directory.rs:144` `impl StepStateProvider for TrustDirectoryWidget {`
- `fn` `codex-rs/tui/src/onboarding/trust_directory.rs:145` `fn get_step_state(&self) -> StepState {`
- `impl` `codex-rs/tui/src/onboarding/trust_directory.rs:153` `impl TrustDirectoryWidget {`
- `fn` `codex-rs/tui/src/onboarding/trust_directory.rs:154` `fn handle_trust(&mut self) {`
- `fn` `codex-rs/tui/src/onboarding/trust_directory.rs:165` `fn handle_dont_trust(&mut self) {`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:183` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:185` `use super::*;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:186` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:187` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:188` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:189` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:190` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:191` `use ratatui::Terminal;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:192` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/onboarding/trust_directory.rs:193` `use tempfile::TempDir;`
- `fn` `codex-rs/tui/src/onboarding/trust_directory.rs:196` `fn release_event_does_not_change_selection() {`
- `fn` `codex-rs/tui/src/onboarding/trust_directory.rs:220` `fn renders_snapshot_for_git_repo() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use codex_core::config::set_project_trust_level;`
- `use codex_core::git_info::resolve_root_git_project_for_trust;`
- `use codex_protocol::config_types::TrustLevel;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::WidgetRef;`
- `use ratatui::widgets::Wrap;`
- `use crate::key_hint;`
- `use crate::onboarding::onboarding_screen::KeyboardHandler;`
- `use crate::onboarding::onboarding_screen::StepStateProvider;`
- `use crate::render::Insets;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
