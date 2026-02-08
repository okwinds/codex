# `codex-rs/tui/src/bottom_pane/selection_popup_common.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15798`
- sha256: `1230f553dc79fadfa3c01bdcf80059a021884cc9dac0fd5ef57a2cff63dc9f0f`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `const` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:34` `const MENU_SURFACE_INSET_V: u16 = 1;`
- `const` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:35` `const MENU_SURFACE_INSET_H: u16 = 2;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:65` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:66` `use crate::wrapping::word_wrap_line;`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:75` `fn line_width(line: &Line<'_>) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:81` `fn truncate_line_to_width(line: Line<'static>, max_width: usize) -> Line<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:129` `fn truncate_line_with_ellipsis_if_overflow(line: Line<'static>, max_width: usize) -> Line<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:149` `fn compute_desc_col(`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:177` `fn wrap_indent(row: &GenericDisplayRow, desc_col: usize, max_width: u16) -> usize {`
- `fn` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:192` `fn build_full_line(row: &GenericDisplayRow, desc_col: usize) -> Line<'static> {`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:334` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:335` `use crate::wrapping::word_wrap_line;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:463` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/bottom_pane/selection_popup_common.rs:464` `use crate::wrapping::word_wrap_line;`

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
- `workdocjcl/spec/06_UI/TUI.md`
