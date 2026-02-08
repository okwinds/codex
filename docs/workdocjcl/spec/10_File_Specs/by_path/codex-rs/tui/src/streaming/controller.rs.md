# `codex-rs/tui/src/streaming/controller.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9873`
- sha256: `652706b4bf9d4e206bae1c316a9b24920e676a03373574185f3eb1e951bb6a3c`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/streaming/controller.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/streaming/controller.rs:1` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/streaming/controller.rs:2` `use crate::history_cell::{self};`
- `use` `codex-rs/tui/src/streaming/controller.rs:3` `use crate::render::line_utils::prefix_lines;`
- `use` `codex-rs/tui/src/streaming/controller.rs:4` `use crate::style::proposed_plan_style;`
- `use` `codex-rs/tui/src/streaming/controller.rs:5` `use ratatui::prelude::Stylize;`
- `use` `codex-rs/tui/src/streaming/controller.rs:6` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/streaming/controller.rs:8` `use super::StreamState;`
- `impl` `codex-rs/tui/src/streaming/controller.rs:18` `impl StreamController {`
- `fn` `codex-rs/tui/src/streaming/controller.rs:74` `fn emit(&mut self, lines: Vec<Line<'static>>) -> Option<Box<dyn HistoryCell>> {`
- `impl` `codex-rs/tui/src/streaming/controller.rs:93` `impl PlanStreamController {`
- `fn` `codex-rs/tui/src/streaming/controller.rs:145` `fn emit(`
- `use` `codex-rs/tui/src/streaming/controller.rs:188` `use super::*;`
- `fn` `codex-rs/tui/src/streaming/controller.rs:190` `fn lines_to_plain_strings(lines: &[ratatui::text::Line<'_>]) -> Vec<String> {`
- `fn` `codex-rs/tui/src/streaming/controller.rs:204` `async fn controller_loose_vs_tight_with_commit_ticks_matches_full() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::history_cell::HistoryCell;`
- `use crate::history_cell::{self};`
- `use crate::render::line_utils::prefix_lines;`
- `use crate::style::proposed_plan_style;`
- `use ratatui::prelude::Stylize;`
- `use ratatui::text::Line;`
- `use super::StreamState;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
