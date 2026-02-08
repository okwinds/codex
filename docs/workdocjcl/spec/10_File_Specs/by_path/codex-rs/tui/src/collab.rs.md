# `codex-rs/tui/src/collab.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8359`
- sha256: `6f947c1de6b430f9b335c16dc649641031cd8dba8b772abf2802ed77e5e6ca20`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/collab.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/collab.rs:1` `use crate::history_cell::PlainHistoryCell;`
- `use` `codex-rs/tui/src/collab.rs:2` `use crate::render::line_utils::prefix_lines;`
- `use` `codex-rs/tui/src/collab.rs:3` `use crate::text_formatting::truncate_text;`
- `use` `codex-rs/tui/src/collab.rs:4` `use codex_core::protocol::AgentStatus;`
- `use` `codex-rs/tui/src/collab.rs:5` `use codex_core::protocol::CollabAgentInteractionEndEvent;`
- `use` `codex-rs/tui/src/collab.rs:6` `use codex_core::protocol::CollabAgentSpawnEndEvent;`
- `use` `codex-rs/tui/src/collab.rs:7` `use codex_core::protocol::CollabCloseEndEvent;`
- `use` `codex-rs/tui/src/collab.rs:8` `use codex_core::protocol::CollabWaitingBeginEvent;`
- `use` `codex-rs/tui/src/collab.rs:9` `use codex_core::protocol::CollabWaitingEndEvent;`
- `use` `codex-rs/tui/src/collab.rs:10` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/collab.rs:11` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/collab.rs:12` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/collab.rs:13` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/collab.rs:14` `use std::collections::HashMap;`
- `const` `codex-rs/tui/src/collab.rs:16` `const COLLAB_PROMPT_PREVIEW_GRAPHEMES: usize = 160;`
- `const` `codex-rs/tui/src/collab.rs:17` `const COLLAB_AGENT_ERROR_PREVIEW_GRAPHEMES: usize = 160;`
- `const` `codex-rs/tui/src/collab.rs:18` `const COLLAB_AGENT_RESPONSE_PREVIEW_GRAPHEMES: usize = 240;`
- `fn` `codex-rs/tui/src/collab.rs:100` `fn collab_event(title: impl Into<String>, details: Vec<Line<'static>>) -> PlainHistoryCell {`
- `fn` `codex-rs/tui/src/collab.rs:110` `fn detail_line(label: &str, value: impl Into<Span<'static>>) -> Line<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:114` `fn status_line(status: &AgentStatus) -> Line<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:118` `fn status_span(status: &AgentStatus) -> Span<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:129` `fn prompt_line(prompt: &str) -> Option<Line<'static>> {`
- `fn` `codex-rs/tui/src/collab.rs:141` `fn format_thread_ids(ids: &[ThreadId]) -> Span<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:153` `fn wait_complete_lines(statuses: &HashMap<ThreadId, AgentStatus>) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/collab.rs:246` `fn push_status_count(`
- `fn` `codex-rs/tui/src/collab.rs:260` `fn detail_line_spans(label: &str, mut value: Vec<Span<'static>>) -> Line<'static> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::history_cell::PlainHistoryCell;`
- `use crate::render::line_utils::prefix_lines;`
- `use crate::text_formatting::truncate_text;`
- `use codex_core::protocol::AgentStatus;`
- `use codex_core::protocol::CollabAgentInteractionEndEvent;`
- `use codex_core::protocol::CollabAgentSpawnEndEvent;`
- `use codex_core::protocol::CollabCloseEndEvent;`
- `use codex_core::protocol::CollabWaitingBeginEvent;`
- `use codex_core::protocol::CollabWaitingEndEvent;`
- `use codex_protocol::ThreadId;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use std::collections::HashMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
