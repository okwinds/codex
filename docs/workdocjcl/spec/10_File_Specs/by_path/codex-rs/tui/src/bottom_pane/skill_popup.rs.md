# `codex-rs/tui/src/bottom_pane/skill_popup.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6657`
- sha256: `250a0cc85ac6555c1fda47965564cb2370464d23634a3ac659f2f88be1be10a7`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/skill_popup.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:2` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:3` `use ratatui::layout::Constraint;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:4` `use ratatui::layout::Layout;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:5` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:6` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:7` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:8` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:10` `use super::popup_consts::MAX_POPUP_ROWS;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:11` `use super::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:12` `use super::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:13` `use super::selection_popup_common::render_rows_single_line;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:14` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:15` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:16` `use crate::render::RectExt;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:17` `use crate::text_formatting::truncate_text;`
- `use` `codex-rs/tui/src/bottom_pane/skill_popup.rs:18` `use codex_common::fuzzy_match::fuzzy_match;`
- `impl` `codex-rs/tui/src/bottom_pane/skill_popup.rs:35` `impl SkillPopup {`
- `fn` `codex-rs/tui/src/bottom_pane/skill_popup.rs:79` `fn clamp_selection(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/skill_popup.rs:85` `fn filtered_items(&self) -> Vec<usize> {`
- `fn` `codex-rs/tui/src/bottom_pane/skill_popup.rs:89` `fn rows_from_matches(`
- `fn` `codex-rs/tui/src/bottom_pane/skill_popup.rs:112` `fn filtered(&self) -> Vec<(usize, Option<Vec<usize>>, i32)> {`
- `impl` `codex-rs/tui/src/bottom_pane/skill_popup.rs:167` `impl WidgetRef for SkillPopup {`
- `fn` `codex-rs/tui/src/bottom_pane/skill_popup.rs:168` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/skill_popup.rs:201` `fn skill_popup_hint_line() -> Line<'static> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyCode;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Layout;`
- `use ratatui::layout::Rect;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Widget;`
- `use ratatui::widgets::WidgetRef;`
- `use super::popup_consts::MAX_POPUP_ROWS;`
- `use super::scroll_state::ScrollState;`
- `use super::selection_popup_common::GenericDisplayRow;`
- `use super::selection_popup_common::render_rows_single_line;`
- `use crate::key_hint;`
- `use crate::render::Insets;`
- `use crate::render::RectExt;`
- `use crate::text_formatting::truncate_text;`
- `use codex_common::fuzzy_match::fuzzy_match;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
