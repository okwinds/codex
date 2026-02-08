# `codex-rs/tui/src/bottom_pane/selection_popup_common.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `22813`
- sha256: `35a08c8c52d2eb20cf18cf61fda970a64c7626fc53ade2062cd9402563fc126c`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/selection_popup_common.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:1` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:2` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:5` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:6` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:7` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:8` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:9` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:10` `use ratatui::widgets::Block;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:11` `use ratatui::widgets::Widget;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:12` `use unicode_width::UnicodeWidthChar;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:13` `use unicode_width::UnicodeWidthStr;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:15` `use crate::key_hint::KeyBinding;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:16` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:17` `use crate::render::RectExt as _;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:18` `use crate::style::user_message_style;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:20` `use super::scroll_state::ScrollState;`
- `const` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:55` `const FIXED_LEFT_COLUMN_NUMERATOR: usize = 3;`
- `const` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:56` `const FIXED_LEFT_COLUMN_DENOMINATOR: usize = 10;`
- `const` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:58` `const MENU_SURFACE_INSET_V: u16 = 1;`
- `const` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:59` `const MENU_SURFACE_INSET_H: u16 = 2;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:94` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:95` `use crate::wrapping::word_wrap_line;`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:104` `fn line_width(line: &Line<'_>) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:200` `fn compute_desc_col(`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:252` `fn wrap_indent(row: &GenericDisplayRow, desc_col: usize, max_width: u16) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:267` `fn build_full_line(row: &GenericDisplayRow, desc_col: usize) -> Line<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:350` `fn render_rows_inner(`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:420` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:421` `use crate::wrapping::word_wrap_line;`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:659` `fn measure_rows_height_inner(`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:693` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:694` `use crate::wrapping::word_wrap_line;`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Color;`
- `use ratatui::style::Style;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Block;`
- `use ratatui::widgets::Widget;`
- `use unicode_width::UnicodeWidthChar;`
- `use unicode_width::UnicodeWidthStr;`
- `use crate::key_hint::KeyBinding;`
- `use crate::render::Insets;`
- `use crate::render::RectExt as _;`
- `use crate::style::user_message_style;`
- `use super::scroll_state::ScrollState;`
- `use crate::wrapping::RtOptions;`
- `use crate::wrapping::word_wrap_line;`
- `use crate::wrapping::RtOptions;`
- `use crate::wrapping::word_wrap_line;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
