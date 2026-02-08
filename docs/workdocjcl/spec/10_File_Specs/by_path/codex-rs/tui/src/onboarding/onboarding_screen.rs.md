# `codex-rs/tui/src/onboarding/onboarding_screen.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15153`
- sha256: `c8cd77621c4591ea076fd4ad9b3b3d59963226ce2ab46e52dcada5743e554b4e`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/onboarding/onboarding_screen.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn directory_trust_decision(&self) -> Option<TrustDirectorySelection> {`
- `pub fn should_exit(&self) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:1` `use codex_core::AuthManager;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:2` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:3` `use codex_core::git_info::get_git_repo_root;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:4` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:5` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:6` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:7` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:8` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:9` `use ratatui::prelude::Widget;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:10` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:11` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:12` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:14` `use codex_protocol::config_types::ForcedLoginMethod;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:16` `use crate::LoginStatus;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:17` `use crate::onboarding::auth::AuthModeWidget;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:18` `use crate::onboarding::auth::SignInOption;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:19` `use crate::onboarding::auth::SignInState;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:20` `use crate::onboarding::trust_directory::TrustDirectorySelection;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:21` `use crate::onboarding::trust_directory::TrustDirectoryWidget;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:22` `use crate::onboarding::welcome::WelcomeWidget;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:23` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:24` `use crate::tui::Tui;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:25` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:26` `use color_eyre::eyre::Result;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:27` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:28` `use std::sync::RwLock;`
- `enum` `codex-rs/tui/src/onboarding/onboarding_screen.rs:31` `enum Step {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:38` `fn handle_key_event(&mut self, key_event: KeyEvent);`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:39` `fn handle_paste(&mut self, _pasted: String) {}`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:50` `fn get_step_state(&self) -> StepState;`
- `impl` `codex-rs/tui/src/onboarding/onboarding_screen.rs:73` `impl OnboardingScreen {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:138` `fn current_steps_mut(&mut self) -> Vec<&mut Step> {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:153` `fn current_steps(&self) -> Vec<&Step> {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:168` `fn is_auth_in_progress(&self) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:182` `pub fn directory_trust_decision(&self) -> Option<TrustDirectorySelection> {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:195` `pub fn should_exit(&self) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:199` `fn is_api_key_entry_active(&self) -> bool {`
- `impl` `codex-rs/tui/src/onboarding/onboarding_screen.rs:212` `impl KeyboardHandler for OnboardingScreen {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:213` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:260` `fn handle_paste(&mut self, pasted: String) {`
- `impl` `codex-rs/tui/src/onboarding/onboarding_screen.rs:272` `impl WidgetRef for &OnboardingScreen {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:273` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:281` `fn used_rows(tmp: &Buffer, width: u16, height: u16) -> u16 {`
- `impl` `codex-rs/tui/src/onboarding/onboarding_screen.rs:338` `impl KeyboardHandler for Step {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:339` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:347` `fn handle_paste(&mut self, pasted: String) {`
- `impl` `codex-rs/tui/src/onboarding/onboarding_screen.rs:356` `impl StepStateProvider for Step {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:357` `fn get_step_state(&self) -> StepState {`
- `impl` `codex-rs/tui/src/onboarding/onboarding_screen.rs:366` `impl WidgetRef for Step {`
- `fn` `codex-rs/tui/src/onboarding/onboarding_screen.rs:367` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `use` `codex-rs/tui/src/onboarding/onboarding_screen.rs:386` `use tokio_stream::StreamExt;`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::AuthManager;`
- `use codex_core::config::Config;`
- `use codex_core::git_info::get_git_repo_root;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::prelude::Widget;`
- `use ratatui::style::Color;`
- `use ratatui::widgets::Clear;`
- `use ratatui::widgets::WidgetRef;`
- `use codex_protocol::config_types::ForcedLoginMethod;`
- `use crate::LoginStatus;`
- `use crate::onboarding::auth::AuthModeWidget;`
- `use crate::onboarding::auth::SignInOption;`
- `use crate::onboarding::auth::SignInState;`
- `use crate::onboarding::trust_directory::TrustDirectorySelection;`
- `use crate::onboarding::trust_directory::TrustDirectoryWidget;`
- `use crate::onboarding::welcome::WelcomeWidget;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
