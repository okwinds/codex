# `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14153`
- sha256: `76a3e5b2789c5f9eaecad843f7f1c909a1d57f16d87dbd995597b395d64f4f0e`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:3` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:4` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:5` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:6` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:7` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:8` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:9` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:10` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:11` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:12` `use ratatui::widgets::Block;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:13` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:15` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:16` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:17` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:18` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:19` `use crate::render::RectExt as _;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:20` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:21` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:22` `use crate::skills_helpers::match_skill;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:23` `use crate::skills_helpers::truncate_skill_name;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:24` `use crate::style::user_message_style;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:25` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:27` `use super::CancellationEvent;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:28` `use super::bottom_pane_view::BottomPaneView;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:29` `use super::popup_consts::MAX_POPUP_ROWS;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:30` `use super::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:31` `use super::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:32` `use super::selection_popup_common::render_rows_single_line;`
- `const` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:34` `const SEARCH_PLACEHOLDER: &str = "Type to search skills";`
- `const` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:35` `const SEARCH_PROMPT_PREFIX: &str = "> ";`
- `impl` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:56` `impl SkillsToggleView {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:78` `fn visible_len(&self) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:82` `fn max_visible_rows(len: usize) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:86` `fn apply_filter(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:131` `fn build_rows(&self) -> Vec<GenericDisplayRow> {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:152` `fn move_up(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:159` `fn move_down(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:166` `fn toggle_selected(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:184` `fn close(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:196` `fn rows_width(total_width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:200` `fn rows_height(&self, rows: &[GenericDisplayRow]) -> u16 {`
- `impl` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:205` `impl BottomPaneView for SkillsToggleView {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:206` `fn handle_key_event(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:271` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:275` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `impl` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:281` `impl Renderable for SkillsToggleView {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:282` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:292` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:371` `fn skills_toggle_hint_line() -> Line<'static> {`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:385` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:386` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:387` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:388` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:389` `use tokio::sync::mpsc::unbounded_channel;`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:391` `fn render_lines(view: &SkillsToggleView, width: u16) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/skills_toggle_view.rs:415` `fn renders_basic_popup() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Layout;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Block;`
- `use ratatui::widgets::Widget;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::key_hint;`
- `use crate::render::Insets;`
- `use crate::render::RectExt as _;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
- `use crate::skills_helpers::match_skill;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
