# `codex-rs/tui/src/streaming/controller.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11613`
- sha256: `908c2d5c78a729d340acb0831d9218a6b6c26bd10b9c922d4cbb3aa56bcd862d`
- generated_utc: `2026-02-08T10:45:40Z`

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
- `use` `codex-rs/tui/src/streaming/controller.rs:7` `use std::time::Duration;`
- `use` `codex-rs/tui/src/streaming/controller.rs:8` `use std::time::Instant;`
- `use` `codex-rs/tui/src/streaming/controller.rs:10` `use super::StreamState;`
- `impl` `codex-rs/tui/src/streaming/controller.rs:20` `impl StreamController {`
- `fn` `codex-rs/tui/src/streaming/controller.rs:98` `fn emit(&mut self, lines: Vec<Line<'static>>) -> Option<Box<dyn HistoryCell>> {`
- `impl` `codex-rs/tui/src/streaming/controller.rs:117` `impl PlanStreamController {`
- `fn` `codex-rs/tui/src/streaming/controller.rs:191` `fn emit(`
- `use` `codex-rs/tui/src/streaming/controller.rs:234` `use super::*;`
- `fn` `codex-rs/tui/src/streaming/controller.rs:236` `fn lines_to_plain_strings(lines: &[ratatui::text::Line<'_>]) -> Vec<String> {`
- `fn` `codex-rs/tui/src/streaming/controller.rs:250` `async fn controller_loose_vs_tight_with_commit_ticks_matches_full() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::history_cell::HistoryCell;`
- `use crate::history_cell::{self};`
- `use crate::render::line_utils::prefix_lines;`
- `use crate::style::proposed_plan_style;`
- `use ratatui::prelude::Stylize;`
- `use ratatui::text::Line;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use super::StreamState;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
