# `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2714`
- sha256: `13dc909ac2dbe620ad3b3c60402c313a46db4da1c8d8145cf738acd2e637052f`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:1` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:2` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:3` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:4` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:5` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:7` `use crate::live_wrap::take_prefix_by_width;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:8` `use crate::render::renderable::Renderable;`
- `impl` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:14` `impl UnifiedExecFooter {`
- `fn` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:33` `fn render_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `impl` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:46` `impl Renderable for UnifiedExecFooter {`
- `fn` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:47` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:55` `fn desired_height(&self, width: u16) -> u16 {`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:62` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:63` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:64` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:67` `fn desired_height_empty() {`
- `fn` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:73` `fn render_more_sessions() {`
- `fn` `codex-rs/tui/src/bottom_pane/unified_exec_footer.rs:84` `fn render_many_sessions() {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::widgets::Paragraph;`
- `use crate::live_wrap::take_prefix_by_width;`
- `use crate::render::renderable::Renderable;`
- `use super::*;`
- `use insta::assert_snapshot;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
