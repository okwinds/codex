# `codex-rs/tui/src/exec_cell/render.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `24935`
- sha256: `4a7d373f64e8bfd6ff9eaba4f6673318e1ab24d3f2f12510dbb06e7a13d781b2`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/exec_cell/render.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/exec_cell/render.rs:1` `use std::time::Instant;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:3` `use super::model::CommandOutput;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:4` `use super::model::ExecCall;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:5` `use super::model::ExecCell;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:6` `use crate::exec_command::strip_bash_lc_and_escape;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:7` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:8` `use crate::render::highlight::highlight_bash_to_lines;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:9` `use crate::render::line_utils::prefix_lines;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:10` `use crate::render::line_utils::push_owned_lines;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:11` `use crate::shimmer::shimmer_spans;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:12` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:13` `use crate::wrapping::word_wrap_line;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:14` `use crate::wrapping::word_wrap_lines;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:15` `use codex_ansi_escape::ansi_escape_line;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:16` `use codex_common::elapsed::format_duration;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:17` `use codex_core::bash::extract_bash_command;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:18` `use codex_core::protocol::ExecCommandSource;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:19` `use codex_protocol::parse_command::ParsedCommand;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:20` `use itertools::Itertools;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:21` `use ratatui::prelude::*;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:22` `use ratatui::style::Modifier;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:23` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:24` `use textwrap::WordSplitter;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:25` `use unicode_width::UnicodeWidthStr;`
- `const` `codex-rs/tui/src/exec_cell/render.rs:28` `const USER_SHELL_TOOL_CALL_MAX_LINES: usize = 50;`
- `const` `codex-rs/tui/src/exec_cell/render.rs:29` `const MAX_INTERACTION_PREVIEW_CHARS: usize = 80;`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:61` `fn format_unified_exec_interaction(command: &[String], input: Option<&str>) -> String {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:76` `fn summarize_interaction_input(input: &str) -> String {`
- `impl` `codex-rs/tui/src/exec_cell/render.rs:196` `impl HistoryCell for ExecCell {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:197` `fn display_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:205` `fn desired_transcript_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:209` `fn transcript_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `impl` `codex-rs/tui/src/exec_cell/render.rs:254` `impl ExecCell {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:255` `fn exploring_display_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:358` `fn command_display_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:494` `fn limit_lines_from_start(lines: &[Line<'static>], keep: usize) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:507` `fn truncate_lines_middle(`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:554` `fn ellipsis_line(omitted: usize) -> Line<'static> {`
- `struct` `codex-rs/tui/src/exec_cell/render.rs:560` `struct PrefixedBlock {`
- `impl` `codex-rs/tui/src/exec_cell/render.rs:565` `impl PrefixedBlock {`
- `const` `codex-rs/tui/src/exec_cell/render.rs:566` `const fn new(initial_prefix: &'static str, subsequent_prefix: &'static str) -> Self {`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:573` `fn wrap_width(self, total_width: u16) -> usize {`
- `struct` `codex-rs/tui/src/exec_cell/render.rs:581` `struct ExecDisplayLayout {`
- `impl` `codex-rs/tui/src/exec_cell/render.rs:588` `impl ExecDisplayLayout {`
- `const` `codex-rs/tui/src/exec_cell/render.rs:589` `const fn new(`
- `const` `codex-rs/tui/src/exec_cell/render.rs:604` `const EXEC_DISPLAY_LAYOUT: ExecDisplayLayout = ExecDisplayLayout::new(`
- `use` `codex-rs/tui/src/exec_cell/render.rs:613` `use super::*;`
- `use` `codex-rs/tui/src/exec_cell/render.rs:614` `use codex_core::protocol::ExecCommandSource;`
- `fn` `codex-rs/tui/src/exec_cell/render.rs:617` `fn user_shell_output_is_limited_by_screen_lines() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Instant;`
- `use super::model::CommandOutput;`
- `use super::model::ExecCall;`
- `use super::model::ExecCell;`
- `use crate::exec_command::strip_bash_lc_and_escape;`
- `use crate::history_cell::HistoryCell;`
- `use crate::render::highlight::highlight_bash_to_lines;`
- `use crate::render::line_utils::prefix_lines;`
- `use crate::render::line_utils::push_owned_lines;`
- `use crate::shimmer::shimmer_spans;`
- `use crate::wrapping::RtOptions;`
- `use crate::wrapping::word_wrap_line;`
- `use crate::wrapping::word_wrap_lines;`
- `use codex_ansi_escape::ansi_escape_line;`
- `use codex_common::elapsed::format_duration;`
- `use codex_core::bash::extract_bash_command;`
- `use codex_core::protocol::ExecCommandSource;`
- `use codex_protocol::parse_command::ParsedCommand;`
- `use itertools::Itertools;`
- `use ratatui::prelude::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
