# `codex-rs/tui/src/insert_history.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `19722`
- sha256: `a8d1d92071ea94f92fc22ba46cb681f0582f8e8326b48aa1101f11e3fb1c717f`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/insert_history.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct SetScrollRegion(pub std::ops::Range<u16>);`
- `pub struct ResetScrollRegion;`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/insert_history.rs:1` `use std::fmt;`
- `use` `codex-rs/tui/src/insert_history.rs:2` `use std::io;`
- `use` `codex-rs/tui/src/insert_history.rs:3` `use std::io::Write;`
- `use` `codex-rs/tui/src/insert_history.rs:5` `use crate::wrapping::word_wrap_lines_borrowed;`
- `use` `codex-rs/tui/src/insert_history.rs:6` `use crossterm::Command;`
- `use` `codex-rs/tui/src/insert_history.rs:7` `use crossterm::cursor::MoveTo;`
- `use` `codex-rs/tui/src/insert_history.rs:8` `use crossterm::queue;`
- `use` `codex-rs/tui/src/insert_history.rs:9` `use crossterm::style::Color as CColor;`
- `use` `codex-rs/tui/src/insert_history.rs:10` `use crossterm::style::Colors;`
- `use` `codex-rs/tui/src/insert_history.rs:11` `use crossterm::style::Print;`
- `use` `codex-rs/tui/src/insert_history.rs:12` `use crossterm::style::SetAttribute;`
- `use` `codex-rs/tui/src/insert_history.rs:13` `use crossterm::style::SetBackgroundColor;`
- `use` `codex-rs/tui/src/insert_history.rs:14` `use crossterm::style::SetColors;`
- `use` `codex-rs/tui/src/insert_history.rs:15` `use crossterm::style::SetForegroundColor;`
- `use` `codex-rs/tui/src/insert_history.rs:16` `use crossterm::terminal::Clear;`
- `use` `codex-rs/tui/src/insert_history.rs:17` `use crossterm::terminal::ClearType;`
- `use` `codex-rs/tui/src/insert_history.rs:18` `use ratatui::layout::Size;`
- `use` `codex-rs/tui/src/insert_history.rs:19` `use ratatui::prelude::Backend;`
- `use` `codex-rs/tui/src/insert_history.rs:20` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/insert_history.rs:21` `use ratatui::style::Modifier;`
- `use` `codex-rs/tui/src/insert_history.rs:22` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/insert_history.rs:23` `use ratatui::text::Span;`
- `struct` `codex-rs/tui/src/insert_history.rs:138` `pub struct SetScrollRegion(pub std::ops::Range<u16>);`
- `impl` `codex-rs/tui/src/insert_history.rs:140` `impl Command for SetScrollRegion {`
- `fn` `codex-rs/tui/src/insert_history.rs:141` `fn write_ansi(&self, f: &mut impl fmt::Write) -> fmt::Result {`
- `fn` `codex-rs/tui/src/insert_history.rs:146` `fn execute_winapi(&self) -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/insert_history.rs:151` `fn is_ansi_code_supported(&self) -> bool {`
- `struct` `codex-rs/tui/src/insert_history.rs:158` `pub struct ResetScrollRegion;`
- `impl` `codex-rs/tui/src/insert_history.rs:160` `impl Command for ResetScrollRegion {`
- `fn` `codex-rs/tui/src/insert_history.rs:161` `fn write_ansi(&self, f: &mut impl fmt::Write) -> fmt::Result {`
- `fn` `codex-rs/tui/src/insert_history.rs:166` `fn execute_winapi(&self) -> std::io::Result<()> {`
- `fn` `codex-rs/tui/src/insert_history.rs:171` `fn is_ansi_code_supported(&self) -> bool {`
- `struct` `codex-rs/tui/src/insert_history.rs:177` `struct ModifierDiff {`
- `impl` `codex-rs/tui/src/insert_history.rs:182` `impl ModifierDiff {`
- `use` `codex-rs/tui/src/insert_history.rs:187` `use crossterm::style::Attribute as CAttribute;`
- `use` `codex-rs/tui/src/insert_history.rs:287` `use super::*;`
- `use` `codex-rs/tui/src/insert_history.rs:288` `use crate::markdown_render::render_markdown_text;`
- `use` `codex-rs/tui/src/insert_history.rs:289` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/insert_history.rs:290` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/insert_history.rs:291` `use ratatui::style::Color;`
- `fn` `codex-rs/tui/src/insert_history.rs:294` `fn writes_bold_then_regular_spans() {`
- `use` `codex-rs/tui/src/insert_history.rs:295` `use ratatui::style::Stylize;`
- `fn` `codex-rs/tui/src/insert_history.rs:322` `fn vt100_blockquote_line_emits_green_fg() {`
- `fn` `codex-rs/tui/src/insert_history.rs:357` `fn vt100_blockquote_wrap_preserves_color_on_all_wrapped_lines() {`
- `fn` `codex-rs/tui/src/insert_history.rs:423` `fn vt100_colored_prefix_then_plain_text_resets_color() {`
- `fn` `codex-rs/tui/src/insert_history.rs:481` `fn vt100_deep_nested_mixed_list_third_level_marker_is_colored() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt;`
- `use std::io;`
- `use std::io::Write;`
- `use crate::wrapping::word_wrap_lines_borrowed;`
- `use crossterm::Command;`
- `use crossterm::cursor::MoveTo;`
- `use crossterm::queue;`
- `use crossterm::style::Color as CColor;`
- `use crossterm::style::Colors;`
- `use crossterm::style::Print;`
- `use crossterm::style::SetAttribute;`
- `use crossterm::style::SetBackgroundColor;`
- `use crossterm::style::SetColors;`
- `use crossterm::style::SetForegroundColor;`
- `use crossterm::terminal::Clear;`
- `use crossterm::terminal::ClearType;`
- `use ratatui::layout::Size;`
- `use ratatui::prelude::Backend;`
- `use ratatui::style::Color;`
- `use ratatui::style::Modifier;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
