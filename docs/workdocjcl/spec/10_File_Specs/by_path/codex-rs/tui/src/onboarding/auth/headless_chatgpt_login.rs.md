# `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12367`
- sha256: `3190150a08d7fc00efad3154ae5074c07f5ce1961e7ba95ee947e13e466015d8`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:1` `use codex_core::AuthManager;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:2` `use codex_login::ServerOptions;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:3` `use codex_login::complete_device_code_login;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:4` `use codex_login::request_device_code;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:5` `use codex_login::run_login_server;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:6` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:7` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:8` `use ratatui::prelude::Widget;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:9` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:10` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:11` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:12` `use ratatui::widgets::Wrap;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:13` `use std::sync::Arc;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:14` `use std::sync::RwLock;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:15` `use tokio::sync::Notify;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:17` `use crate::shimmer::shimmer_spans;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:18` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:20` `use super::AuthModeWidget;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:21` `use super::ContinueInBrowserState;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:22` `use super::ContinueWithDeviceCodeState;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:23` `use super::SignInState;`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:190` `fn device_code_attempt_matches(state: &SignInState, cancel: &Arc<Notify>) -> bool {`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:201` `fn begin_device_code_attempt(`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:214` `fn set_device_code_state_for_active_attempt(`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:231` `fn set_device_code_success_message_for_active_attempt(`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:251` `use super::*;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:252` `use codex_core::auth::AuthCredentialsStoreMode;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:253` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:254` `use tempfile::TempDir;`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:256` `fn device_code_sign_in_state(cancel: Arc<Notify>) -> Arc<RwLock<SignInState>> {`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:266` `fn device_code_attempt_matches_only_for_matching_cancel() {`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:285` `fn begin_device_code_attempt_sets_state() {`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:301` `fn set_device_code_state_for_active_attempt_updates_only_when_active() {`
- `fn` `codex-rs/tui/src/onboarding/auth/headless_chatgpt_login.rs:337` `fn set_device_code_success_message_for_active_attempt_updates_only_when_active() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::AuthManager;`
- `use codex_login::ServerOptions;`
- `use codex_login::complete_device_code_login;`
- `use codex_login::request_device_code;`
- `use codex_login::run_login_server;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::prelude::Widget;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::Wrap;`
- `use std::sync::Arc;`
- `use std::sync::RwLock;`
- `use tokio::sync::Notify;`
- `use crate::shimmer::shimmer_spans;`
- `use crate::tui::FrameRequester;`
- `use super::AuthModeWidget;`
- `use super::ContinueInBrowserState;`
- `use super::ContinueWithDeviceCodeState;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
