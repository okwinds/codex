# `codex-rs/tui/src/cwd_prompt.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8549`
- sha256: `ff3731dcfe3b5131101785c2c0431df3036bf074b8ee997aa78e211c52587046`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/cwd_prompt.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/cwd_prompt.rs:1` `use std::path::Path;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:3` `use crate::key_hint;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:4` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:5` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:6` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:7` `use crate::render::renderable::RenderableExt as _;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:8` `use crate::selection_list::selection_option_row;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:9` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:10` `use crate::tui::Tui;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:11` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:12` `use color_eyre::Result;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:13` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:14` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:15` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:16` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:17` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:18` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:19` `use ratatui::prelude::Widget;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:20` `use ratatui::style::Stylize as _;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:21` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:22` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:23` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:24` `use tokio_stream::StreamExt;`
- `impl` `codex-rs/tui/src/cwd_prompt.rs:32` `impl CwdPromptAction {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:33` `fn verb(self) -> &'static str {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:40` `fn past_participle(self) -> &'static str {`
- `impl` `codex-rs/tui/src/cwd_prompt.rs:54` `impl CwdSelection {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:55` `fn next(self) -> Self {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:62` `fn prev(self) -> Self {`
- `struct` `codex-rs/tui/src/cwd_prompt.rs:108` `struct CwdPromptScreen {`
- `impl` `codex-rs/tui/src/cwd_prompt.rs:117` `impl CwdPromptScreen {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:118` `fn new(`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:134` `fn handle_key(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:155` `fn set_highlight(&mut self, highlight: CwdSelection) {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:162` `fn select(&mut self, selection: CwdSelection) {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:168` `fn is_done(&self) -> bool {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:172` `fn selection(&self) -> Option<CwdSelection> {`
- `impl` `codex-rs/tui/src/cwd_prompt.rs:177` `impl WidgetRef for &CwdPromptScreen {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:178` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `use` `codex-rs/tui/src/cwd_prompt.rs:231` `use super::*;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:232` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:233` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:234` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:235` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/cwd_prompt.rs:236` `use ratatui::Terminal;`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:238` `fn new_prompt() -> CwdPromptScreen {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:248` `fn cwd_prompt_snapshot() {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:258` `fn cwd_prompt_fork_snapshot() {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:273` `fn cwd_prompt_selects_session_by_default() {`
- `fn` `codex-rs/tui/src/cwd_prompt.rs:280` `fn cwd_prompt_can_select_current() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use crate::key_hint;`
- `use crate::render::Insets;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
- `use crate::render::renderable::RenderableExt as _;`
- `use crate::selection_list::selection_option_row;`
- `use crate::tui::FrameRequester;`
- `use crate::tui::Tui;`
- `use crate::tui::TuiEvent;`
- `use color_eyre::Result;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::prelude::Widget;`
- `use ratatui::style::Stylize as _;`
- `use ratatui::text::Line;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
