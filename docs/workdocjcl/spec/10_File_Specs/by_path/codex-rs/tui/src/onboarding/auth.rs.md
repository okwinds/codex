# `codex-rs/tui/src/onboarding/auth.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `29862`
- sha256: `e2560ee3ff696645ff54f6c5a02109db4b9d4176048a7bb8cde43cdbcc5e8d98`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/onboarding/auth.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/onboarding/auth.rs:3` `use codex_core::AuthManager;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:4` `use codex_core::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:5` `use codex_core::auth::CLIENT_ID;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:6` `use codex_core::auth::login_with_api_key;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:7` `use codex_core::auth::read_openai_api_key_from_env;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:8` `use codex_login::DeviceCode;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:9` `use codex_login::ServerOptions;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:10` `use codex_login::ShutdownHandle;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:11` `use codex_login::run_login_server;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:12` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:13` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:14` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:15` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:16` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:17` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:18` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:19` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:20` `use ratatui::prelude::Widget;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:21` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:22` `use ratatui::style::Modifier;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:23` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:24` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:25` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:26` `use ratatui::widgets::Block;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:27` `use ratatui::widgets::BorderType;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:28` `use ratatui::widgets::Borders;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:29` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:30` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:31` `use ratatui::widgets::Wrap;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:33` `use codex_core::auth::AuthMode;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:34` `use codex_protocol::config_types::ForcedLoginMethod;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:35` `use std::sync::RwLock;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:37` `use crate::LoginStatus;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:38` `use crate::onboarding::onboarding_screen::KeyboardHandler;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:39` `use crate::onboarding::onboarding_screen::StepStateProvider;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:40` `use crate::shimmer::shimmer_spans;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:41` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:42` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:43` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:44` `use tokio::sync::Notify;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:46` `use super::onboarding_screen::StepState;`
- `mod` `codex-rs/tui/src/onboarding/auth.rs:48` `mod headless_chatgpt_login;`
- `const` `codex-rs/tui/src/onboarding/auth.rs:68` `const API_KEY_DISABLED_MESSAGE: &str = "API key login is disabled.";`
- `impl` `codex-rs/tui/src/onboarding/auth.rs:89` `impl Drop for ContinueInBrowserState {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:90` `fn drop(&mut self) {`
- `impl` `codex-rs/tui/src/onboarding/auth.rs:97` `impl KeyboardHandler for AuthModeWidget {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:98` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:155` `fn handle_paste(&mut self, pasted: String) {`
- `impl` `codex-rs/tui/src/onboarding/auth.rs:175` `impl AuthModeWidget {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:176` `fn is_api_login_allowed(&self) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:180` `fn is_chatgpt_login_allowed(&self) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:184` `fn displayed_sign_in_options(&self) -> Vec<SignInOption> {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:195` `fn selectable_sign_in_options(&self) -> Vec<SignInOption> {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:207` `fn move_highlight(&mut self, delta: isize) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:222` `fn select_option_by_index(&mut self, index: usize) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:229` `fn handle_sign_in_option(&mut self, option: SignInOption) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:251` `fn disallow_api_login(&mut self) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:258` `fn render_pick_mode(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:360` `fn render_continue_in_browser(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:397` `fn render_chatgpt_success_message(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:428` `fn render_chatgpt_success(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:440` `fn render_api_key_configured(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:452` `fn render_api_key_entry(&self, area: Rect, buf: &mut Buffer, state: &ApiKeyInputState) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:511` `fn handle_api_key_entry_key_event(&mut self, key_event: &KeyEvent) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:573` `fn handle_api_key_entry_paste(&mut self, pasted: String) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:597` `fn start_api_key_entry(&mut self) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:627` `fn save_api_key(&mut self, api_key: String) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:663` `fn handle_existing_chatgpt_login(&mut self) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:674` `fn start_chatgpt_login(&mut self) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:729` `fn start_device_code_login(&mut self) {`
- `impl` `codex-rs/tui/src/onboarding/auth.rs:745` `impl StepStateProvider for AuthModeWidget {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:746` `fn get_step_state(&self) -> StepState {`
- `impl` `codex-rs/tui/src/onboarding/auth.rs:759` `impl WidgetRef for AuthModeWidget {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:760` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `use` `codex-rs/tui/src/onboarding/auth.rs:790` `use super::*;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:791` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:792` `use tempfile::TempDir;`
- `use` `codex-rs/tui/src/onboarding/auth.rs:794` `use codex_core::auth::AuthCredentialsStoreMode;`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:796` `fn widget_forced_chatgpt() -> (AuthModeWidget, TempDir) {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:820` `fn api_key_flow_disabled_when_chatgpt_forced() {`
- `fn` `codex-rs/tui/src/onboarding/auth.rs:833` `fn saving_api_key_is_blocked_when_chatgpt_forced() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::AuthManager;`
- `use codex_core::auth::AuthCredentialsStoreMode;`
- `use codex_core::auth::CLIENT_ID;`
- `use codex_core::auth::login_with_api_key;`
- `use codex_core::auth::read_openai_api_key_from_env;`
- `use codex_login::DeviceCode;`
- `use codex_login::ServerOptions;`
- `use codex_login::ShutdownHandle;`
- `use codex_login::run_login_server;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Layout;`
- `use ratatui::layout::Rect;`
- `use ratatui::prelude::Widget;`
- `use ratatui::style::Color;`
- `use ratatui::style::Modifier;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
