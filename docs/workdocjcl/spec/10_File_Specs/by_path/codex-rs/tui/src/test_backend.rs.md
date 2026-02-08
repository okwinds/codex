# `codex-rs/tui/src/test_backend.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3583`
- sha256: `6643fb77c22bb5c0478efb0f5ac7a8fe36a1dd08001a4c835b0d34459151f6a5`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/test_backend.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct VT100Backend {`
- `pub fn new(width: u16, height: u16) -> Self {`
- `pub fn vt100(&self) -> &vt100::Parser {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/test_backend.rs:1` `use std::fmt::{self};`
- `use` `codex-rs/tui/src/test_backend.rs:2` `use std::io::Write;`
- `use` `codex-rs/tui/src/test_backend.rs:3` `use std::io::{self};`
- `use` `codex-rs/tui/src/test_backend.rs:5` `use ratatui::prelude::CrosstermBackend;`
- `use` `codex-rs/tui/src/test_backend.rs:7` `use ratatui::backend::Backend;`
- `use` `codex-rs/tui/src/test_backend.rs:8` `use ratatui::backend::ClearType;`
- `use` `codex-rs/tui/src/test_backend.rs:9` `use ratatui::backend::WindowSize;`
- `use` `codex-rs/tui/src/test_backend.rs:10` `use ratatui::buffer::Cell;`
- `use` `codex-rs/tui/src/test_backend.rs:11` `use ratatui::layout::Position;`
- `use` `codex-rs/tui/src/test_backend.rs:12` `use ratatui::layout::Size;`
- `struct` `codex-rs/tui/src/test_backend.rs:21` `pub struct VT100Backend {`
- `impl` `codex-rs/tui/src/test_backend.rs:25` `impl VT100Backend {`
- `fn` `codex-rs/tui/src/test_backend.rs:27` `pub fn new(width: u16, height: u16) -> Self {`
- `fn` `codex-rs/tui/src/test_backend.rs:34` `pub fn vt100(&self) -> &vt100::Parser {`
- `impl` `codex-rs/tui/src/test_backend.rs:39` `impl Write for VT100Backend {`
- `fn` `codex-rs/tui/src/test_backend.rs:40` `fn write(&mut self, buf: &[u8]) -> io::Result<usize> {`
- `fn` `codex-rs/tui/src/test_backend.rs:44` `fn flush(&mut self) -> io::Result<()> {`
- `impl` `codex-rs/tui/src/test_backend.rs:49` `impl fmt::Display for VT100Backend {`
- `fn` `codex-rs/tui/src/test_backend.rs:50` `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
- `impl` `codex-rs/tui/src/test_backend.rs:55` `impl Backend for VT100Backend {`
- `fn` `codex-rs/tui/src/test_backend.rs:64` `fn hide_cursor(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/test_backend.rs:69` `fn show_cursor(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/test_backend.rs:74` `fn get_cursor_position(&mut self) -> io::Result<Position> {`
- `fn` `codex-rs/tui/src/test_backend.rs:82` `fn clear(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/test_backend.rs:86` `fn clear_region(&mut self, clear_type: ClearType) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/test_backend.rs:90` `fn append_lines(&mut self, line_count: u16) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/test_backend.rs:94` `fn size(&self) -> io::Result<Size> {`
- `fn` `codex-rs/tui/src/test_backend.rs:99` `fn window_size(&mut self) -> io::Result<WindowSize> {`
- `fn` `codex-rs/tui/src/test_backend.rs:110` `fn flush(&mut self) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/test_backend.rs:114` `fn scroll_region_up(&mut self, region: std::ops::Range<u16>, scroll_by: u16) -> io::Result<()> {`
- `fn` `codex-rs/tui/src/test_backend.rs:118` `fn scroll_region_down(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::fmt::{self};`
- `use std::io::Write;`
- `use std::io::{self};`
- `use ratatui::prelude::CrosstermBackend;`
- `use ratatui::backend::Backend;`
- `use ratatui::backend::ClearType;`
- `use ratatui::backend::WindowSize;`
- `use ratatui::buffer::Cell;`
- `use ratatui::layout::Position;`
- `use ratatui::layout::Size;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
