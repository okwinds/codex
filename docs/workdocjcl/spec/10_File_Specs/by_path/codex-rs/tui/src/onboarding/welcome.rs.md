# `codex-rs/tui/src/onboarding/welcome.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5373`
- sha256: `f35c6a0dd575acedc071b15d2cfaf4828c9d2ebd01898b066826ce1454d4bdf2`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/onboarding/welcome.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/onboarding/welcome.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:2` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:3` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:4` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:5` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:6` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:7` `use ratatui::prelude::Widget;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:8` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:9` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:10` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:11` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:12` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:13` `use ratatui::widgets::Wrap;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:14` `use std::cell::Cell;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:16` `use crate::ascii_animation::AsciiAnimation;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:17` `use crate::onboarding::onboarding_screen::KeyboardHandler;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:18` `use crate::onboarding::onboarding_screen::StepStateProvider;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:19` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:21` `use super::onboarding_screen::StepState;`
- `const` `codex-rs/tui/src/onboarding/welcome.rs:23` `const MIN_ANIMATION_HEIGHT: u16 = 37;`
- `const` `codex-rs/tui/src/onboarding/welcome.rs:24` `const MIN_ANIMATION_WIDTH: u16 = 60;`
- `impl` `codex-rs/tui/src/onboarding/welcome.rs:33` `impl KeyboardHandler for WelcomeWidget {`
- `fn` `codex-rs/tui/src/onboarding/welcome.rs:34` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `impl` `codex-rs/tui/src/onboarding/welcome.rs:48` `impl WelcomeWidget {`
- `impl` `codex-rs/tui/src/onboarding/welcome.rs:67` `impl WidgetRef for &WelcomeWidget {`
- `fn` `codex-rs/tui/src/onboarding/welcome.rs:68` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `impl` `codex-rs/tui/src/onboarding/welcome.rs:99` `impl StepStateProvider for WelcomeWidget {`
- `fn` `codex-rs/tui/src/onboarding/welcome.rs:100` `fn get_step_state(&self) -> StepState {`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:110` `use super::*;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:111` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:112` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/onboarding/welcome.rs:113` `use ratatui::layout::Rect;`
- `static` `codex-rs/tui/src/onboarding/welcome.rs:115` `static VARIANT_A: [&str; 1] = ["frame-a"];`
- `static` `codex-rs/tui/src/onboarding/welcome.rs:116` `static VARIANT_B: [&str; 1] = ["frame-b"];`
- `static` `codex-rs/tui/src/onboarding/welcome.rs:117` `static VARIANTS: [&[&str]; 2] = [&VARIANT_A, &VARIANT_B];`
- `fn` `codex-rs/tui/src/onboarding/welcome.rs:119` `fn row_containing(buf: &Buffer, needle: &str) -> Option<u16> {`
- `fn` `codex-rs/tui/src/onboarding/welcome.rs:130` `fn welcome_renders_animation_on_first_draw() {`
- `fn` `codex-rs/tui/src/onboarding/welcome.rs:142` `fn welcome_skips_animation_below_height_breakpoint() {`
- `fn` `codex-rs/tui/src/onboarding/welcome.rs:153` `fn ctrl_dot_changes_animation_variant() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::prelude::Widget;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Clear;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::WidgetRef;`
- `use ratatui::widgets::Wrap;`
- `use std::cell::Cell;`
- `use crate::ascii_animation::AsciiAnimation;`
- `use crate::onboarding::onboarding_screen::KeyboardHandler;`
- `use crate::onboarding::onboarding_screen::StepStateProvider;`
- `use crate::tui::FrameRequester;`
- `use super::onboarding_screen::StepState;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
