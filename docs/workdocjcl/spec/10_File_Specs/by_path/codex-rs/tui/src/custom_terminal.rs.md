# `codex-rs/tui/src/custom_terminal.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `25067`
- sha256: `d0850b81eedaa36d50b7426d6afb923660b57102d3c8973feccd43d833e8548e`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/custom_terminal.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub struct Frame<'a> {`
- `pub fn buffer_mut(&mut self) -> &mut Buffer {`
- `pub struct Terminal<B>`
- `pub fn with_options(mut backend: B) -> io::Result<Self> {`
- `pub fn get_frame(&mut self) -> Frame<'_> {`
- `pub fn backend_mut(&mut self) -> &mut B {`
- `pub fn flush(&mut self) -> io::Result<()> {`
- `pub fn resize(&mut self, screen_size: Size) -> io::Result<()> {`
- `pub fn set_viewport_area(&mut self, area: Rect) {`
- `pub fn autoresize(&mut self) -> io::Result<()> {`
- `pub fn hide_cursor(&mut self) -> io::Result<()> {`
- `pub fn show_cursor(&mut self) -> io::Result<()> {`
- `pub fn get_cursor_position(&mut self) -> io::Result<Position> {`
- `pub fn clear(&mut self) -> io::Result<()> {`
- `pub fn clear_scrollback(&mut self) -> io::Result<()> {`
- `pub fn swap_buffers(&mut self) {`
- `pub fn size(&self) -> io::Result<Size> {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/custom_terminal.rs:24` `use std::io;`
- `use` `codex-rs/tui/src/custom_terminal.rs:25` `use std::io::Write;`
- `use` `codex-rs/tui/src/custom_terminal.rs:27` `use crossterm::cursor::MoveTo;`
- `use` `codex-rs/tui/src/custom_terminal.rs:28` `use crossterm::queue;`
- `use` `codex-rs/tui/src/custom_terminal.rs:29` `use crossterm::style::Colors;`
- `use` `codex-rs/tui/src/custom_terminal.rs:30` `use crossterm::style::Print;`
- `use` `codex-rs/tui/src/custom_terminal.rs:31` `use crossterm::style::SetAttribute;`
- `use` `codex-rs/tui/src/custom_terminal.rs:32` `use crossterm::style::SetBackgroundColor;`
- `use` `codex-rs/tui/src/custom_terminal.rs:33` `use crossterm::style::SetColors;`
- `use` `codex-rs/tui/src/custom_terminal.rs:34` `use crossterm::style::SetForegroundColor;`
- `use` `codex-rs/tui/src/custom_terminal.rs:35` `use crossterm::terminal::Clear;`
- `use` `codex-rs/tui/src/custom_terminal.rs:36` `use derive_more::IsVariant;`
- `use` `codex-rs/tui/src/custom_terminal.rs:37` `use ratatui::backend::Backend;`
- `use` `codex-rs/tui/src/custom_terminal.rs:38` `use ratatui::backend::ClearType;`
- `use` `codex-rs/tui/src/custom_terminal.rs:39` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/custom_terminal.rs:40` `use ratatui::layout::Position;`
- `use` `codex-rs/tui/src/custom_terminal.rs:41` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/custom_terminal.rs:42` `use ratatui::layout::Size;`
- `use` `codex-rs/tui/src/custom_terminal.rs:43` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/custom_terminal.rs:44` `use ratatui::style::Modifier;`
- `use` `codex-rs/tui/src/custom_terminal.rs:45` `use ratatui::widgets::WidgetRef;`
- `struct` `codex-rs/tui/src/custom_terminal.rs:48` `pub struct Frame<'a> {`
- `impl` `codex-rs/tui/src/custom_terminal.rs:62` `impl Frame<'_> {`
- `const` `codex-rs/tui/src/custom_terminal.rs:70` `pub const fn area(&self) -> Rect {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:98` `pub fn buffer_mut(&mut self) -> &mut Buffer {`
- `struct` `codex-rs/tui/src/custom_terminal.rs:104` `pub struct Terminal<B>`
- `fn` `codex-rs/tui/src/custom_terminal.rs:132` `fn drop(&mut self) {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:148` `pub fn with_options(mut backend: B) -> io::Result<Self> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:163` `pub fn get_frame(&mut self) -> Frame<'_> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:172` `fn current_buffer(&self) -> &Buffer {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:177` `fn current_buffer_mut(&mut self) -> &mut Buffer {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:182` `fn previous_buffer(&self) -> &Buffer {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:187` `fn previous_buffer_mut(&mut self) -> &mut Buffer {`
- `const` `codex-rs/tui/src/custom_terminal.rs:192` `pub const fn backend(&self) -> &B {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:197` `pub fn backend_mut(&mut self) -> &mut B {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:203` `pub fn flush(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:216` `pub fn resize(&mut self, screen_size: Size) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:222` `pub fn set_viewport_area(&mut self, area: Rect) {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:229` `pub fn autoresize(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:342` `pub fn hide_cursor(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:349` `pub fn show_cursor(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:359` `pub fn get_cursor_position(&mut self) -> io::Result<Position> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:372` `pub fn clear(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:385` `pub fn clear_scrollback(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:398` `pub fn swap_buffers(&mut self) {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:404` `pub fn size(&self) -> io::Result<Size> {`
- `use` `codex-rs/tui/src/custom_terminal.rs:409` `use ratatui::buffer::Cell;`
- `use` `codex-rs/tui/src/custom_terminal.rs:410` `use unicode_width::UnicodeWidthStr;`
- `enum` `codex-rs/tui/src/custom_terminal.rs:413` `enum DrawCommand {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:418` `fn diff_buffers(a: &Buffer, b: &Buffer) -> Vec<DrawCommand> {`
- `struct` `codex-rs/tui/src/custom_terminal.rs:542` `struct ModifierDiff {`
- `impl` `codex-rs/tui/src/custom_terminal.rs:547` `impl ModifierDiff {`
- `use` `codex-rs/tui/src/custom_terminal.rs:549` `use crossterm::style::Attribute as CAttribute;`
- `use` `codex-rs/tui/src/custom_terminal.rs:608` `use super::*;`
- `use` `codex-rs/tui/src/custom_terminal.rs:609` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/custom_terminal.rs:610` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/custom_terminal.rs:611` `use ratatui::style::Style;`
- `fn` `codex-rs/tui/src/custom_terminal.rs:614` `fn diff_buffers_does_not_emit_clear_to_end_for_full_width_row() {`
- `fn` `codex-rs/tui/src/custom_terminal.rs:642` `fn diff_buffers_clear_to_end_starts_after_wide_char() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::io;`
- `use std::io::Write;`
- `use crossterm::cursor::MoveTo;`
- `use crossterm::queue;`
- `use crossterm::style::Colors;`
- `use crossterm::style::Print;`
- `use crossterm::style::SetAttribute;`
- `use crossterm::style::SetBackgroundColor;`
- `use crossterm::style::SetColors;`
- `use crossterm::style::SetForegroundColor;`
- `use crossterm::terminal::Clear;`
- `use derive_more::IsVariant;`
- `use ratatui::backend::Backend;`
- `use ratatui::backend::ClearType;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Position;`
- `use ratatui::layout::Rect;`
- `use ratatui::layout::Size;`
- `use ratatui::style::Color;`
- `use ratatui::style::Modifier;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
