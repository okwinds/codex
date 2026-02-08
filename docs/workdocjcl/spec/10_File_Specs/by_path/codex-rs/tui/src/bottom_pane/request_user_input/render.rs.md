# `codex-rs/tui/src/bottom_pane/request_user_input/render.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19071`
- sha256: `c4102499624ded52f0e88c9a73d0bbea1958a18bccf8bb59088c2d0a8dcbb89b`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/request_user_input/render.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:1` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:2` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:3` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:4` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:5` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:6` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:7` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:8` `use std::borrow::Cow;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:9` `use unicode_width::UnicodeWidthChar;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:10` `use unicode_width::UnicodeWidthStr;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:12` `use crate::bottom_pane::popup_consts::standard_popup_hint_line;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:13` `use crate::bottom_pane::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:14` `use crate::bottom_pane::selection_popup_common::measure_rows_height;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:15` `use crate::bottom_pane::selection_popup_common::menu_surface_inset;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:16` `use crate::bottom_pane::selection_popup_common::menu_surface_padding_height;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:17` `use crate::bottom_pane::selection_popup_common::render_menu_surface;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:18` `use crate::bottom_pane::selection_popup_common::render_rows;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:19` `use crate::bottom_pane::selection_popup_common::wrap_styled_line;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:20` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:22` `use super::DESIRED_SPACERS_BETWEEN_SECTIONS;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:23` `use super::RequestUserInputOverlay;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:24` `use super::TIP_SEPARATOR;`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:26` `const MIN_OVERLAY_HEIGHT: usize = 8;`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:27` `const PROGRESS_ROW_HEIGHT: usize = 1;`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:28` `const SPACER_ROWS_WITH_NOTES: usize = 1;`
- `const` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:29` `const SPACER_ROWS_NO_OPTIONS: usize = 0;`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:31` `struct UnansweredConfirmationData {`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:39` `struct UnansweredConfirmationLayout {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:46` `fn line_to_owned(line: Line<'_>) -> Line<'static> {`
- `impl` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:61` `impl Renderable for RequestUserInputOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:62` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:107` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:111` `fn cursor_pos(&self, area: Rect) -> Option<(u16, u16)> {`
- `impl` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:116` `impl RequestUserInputOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:117` `fn unanswered_confirmation_data(&self) -> UnansweredConfirmationData {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:132` `fn unanswered_confirmation_layout(&self, width: u16) -> UnansweredConfirmationLayout {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:151` `fn unanswered_confirmation_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:171` `fn render_unanswered_confirmation(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:413` `fn render_notes_input(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:428` `fn line_width(line: &Line<'_>) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:441` `fn truncate_line_word_boundary_with_ellipsis(`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/render.rs:461` `struct BreakPoint {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::Widget;`
- `use std::borrow::Cow;`
- `use unicode_width::UnicodeWidthChar;`
- `use unicode_width::UnicodeWidthStr;`
- `use crate::bottom_pane::popup_consts::standard_popup_hint_line;`
- `use crate::bottom_pane::scroll_state::ScrollState;`
- `use crate::bottom_pane::selection_popup_common::measure_rows_height;`
- `use crate::bottom_pane::selection_popup_common::menu_surface_inset;`
- `use crate::bottom_pane::selection_popup_common::menu_surface_padding_height;`
- `use crate::bottom_pane::selection_popup_common::render_menu_surface;`
- `use crate::bottom_pane::selection_popup_common::render_rows;`
- `use crate::bottom_pane::selection_popup_common::wrap_styled_line;`
- `use crate::render::renderable::Renderable;`
- `use super::DESIRED_SPACERS_BETWEEN_SECTIONS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
