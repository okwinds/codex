# `codex-rs/tui/src/update_prompt.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10155`
- sha256: `62efda9fe46f200ff40b2e596a14e6e932804426c256520e5888907aced02b46`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/update_prompt.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/update_prompt.rs:3` `use crate::history_cell::padded_emoji;`
- `use` `codex-rs/tui/src/update_prompt.rs:4` `use crate::key_hint;`
- `use` `codex-rs/tui/src/update_prompt.rs:5` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/update_prompt.rs:6` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/update_prompt.rs:7` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/update_prompt.rs:8` `use crate::render::renderable::RenderableExt as _;`
- `use` `codex-rs/tui/src/update_prompt.rs:9` `use crate::selection_list::selection_option_row;`
- `use` `codex-rs/tui/src/update_prompt.rs:10` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/update_prompt.rs:11` `use crate::tui::Tui;`
- `use` `codex-rs/tui/src/update_prompt.rs:12` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/update_prompt.rs:13` `use crate::update_action::UpdateAction;`
- `use` `codex-rs/tui/src/update_prompt.rs:14` `use crate::updates;`
- `use` `codex-rs/tui/src/update_prompt.rs:15` `use codex_core::config::Config;`
- `use` `codex-rs/tui/src/update_prompt.rs:16` `use color_eyre::Result;`
- `use` `codex-rs/tui/src/update_prompt.rs:17` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/update_prompt.rs:18` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/update_prompt.rs:19` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/update_prompt.rs:20` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/update_prompt.rs:21` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/update_prompt.rs:22` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/update_prompt.rs:23` `use ratatui::prelude::Widget;`
- `use` `codex-rs/tui/src/update_prompt.rs:24` `use ratatui::style::Stylize as _;`
- `use` `codex-rs/tui/src/update_prompt.rs:25` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/update_prompt.rs:26` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/update_prompt.rs:27` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/update_prompt.rs:28` `use tokio_stream::StreamExt;`
- `enum` `codex-rs/tui/src/update_prompt.rs:87` `enum UpdateSelection {`
- `struct` `codex-rs/tui/src/update_prompt.rs:93` `struct UpdatePromptScreen {`
- `impl` `codex-rs/tui/src/update_prompt.rs:102` `impl UpdatePromptScreen {`
- `fn` `codex-rs/tui/src/update_prompt.rs:103` `fn new(`
- `fn` `codex-rs/tui/src/update_prompt.rs:118` `fn handle_key(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/update_prompt.rs:140` `fn set_highlight(&mut self, highlight: UpdateSelection) {`
- `fn` `codex-rs/tui/src/update_prompt.rs:147` `fn select(&mut self, selection: UpdateSelection) {`
- `fn` `codex-rs/tui/src/update_prompt.rs:153` `fn is_done(&self) -> bool {`
- `fn` `codex-rs/tui/src/update_prompt.rs:157` `fn selection(&self) -> Option<UpdateSelection> {`
- `fn` `codex-rs/tui/src/update_prompt.rs:161` `fn latest_version(&self) -> &str {`
- `impl` `codex-rs/tui/src/update_prompt.rs:166` `impl UpdateSelection {`
- `fn` `codex-rs/tui/src/update_prompt.rs:167` `fn next(self) -> Self {`
- `fn` `codex-rs/tui/src/update_prompt.rs:175` `fn prev(self) -> Self {`
- `impl` `codex-rs/tui/src/update_prompt.rs:184` `impl WidgetRef for &UpdatePromptScreen {`
- `fn` `codex-rs/tui/src/update_prompt.rs:185` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `use` `codex-rs/tui/src/update_prompt.rs:244` `use super::*;`
- `use` `codex-rs/tui/src/update_prompt.rs:245` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/update_prompt.rs:246` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/update_prompt.rs:247` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/update_prompt.rs:248` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/update_prompt.rs:249` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/update_prompt.rs:250` `use ratatui::Terminal;`
- `fn` `codex-rs/tui/src/update_prompt.rs:252` `fn new_prompt() -> UpdatePromptScreen {`
- `fn` `codex-rs/tui/src/update_prompt.rs:261` `fn update_prompt_snapshot() {`
- `fn` `codex-rs/tui/src/update_prompt.rs:271` `fn update_prompt_confirm_selects_update() {`
- `fn` `codex-rs/tui/src/update_prompt.rs:279` `fn update_prompt_dismiss_option_leaves_prompt_in_normal_state() {`
- `fn` `codex-rs/tui/src/update_prompt.rs:288` `fn update_prompt_dont_remind_selects_dismissal() {`
- `fn` `codex-rs/tui/src/update_prompt.rs:298` `fn update_prompt_ctrl_c_skips_update() {`
- `fn` `codex-rs/tui/src/update_prompt.rs:306` `fn update_prompt_navigation_wraps_between_entries() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::history_cell::padded_emoji;`
- `use crate::key_hint;`
- `use crate::render::Insets;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
- `use crate::render::renderable::RenderableExt as _;`
- `use crate::selection_list::selection_option_row;`
- `use crate::tui::FrameRequester;`
- `use crate::tui::Tui;`
- `use crate::tui::TuiEvent;`
- `use crate::update_action::UpdateAction;`
- `use crate::updates;`
- `use codex_core::config::Config;`
- `use color_eyre::Result;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
