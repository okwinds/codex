# `codex-rs/tui/src/collab.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9250`
- sha256: `db8e09091163277b975fbbaafe1b764424e41d30aadd04f1665ef9369970a310`
- generated_utc: `2026-02-08T10:45:40Z`

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
- `use` `codex-rs/tui/src/collab.rs:8` `use codex_core::protocol::CollabResumeBeginEvent;`
- `use` `codex-rs/tui/src/collab.rs:9` `use codex_core::protocol::CollabResumeEndEvent;`
- `use` `codex-rs/tui/src/collab.rs:10` `use codex_core::protocol::CollabWaitingBeginEvent;`
- `use` `codex-rs/tui/src/collab.rs:11` `use codex_core::protocol::CollabWaitingEndEvent;`
- `use` `codex-rs/tui/src/collab.rs:12` `use codex_protocol::ThreadId;`
- `use` `codex-rs/tui/src/collab.rs:13` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/collab.rs:14` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/collab.rs:15` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/collab.rs:16` `use std::collections::HashMap;`
- `const` `codex-rs/tui/src/collab.rs:18` `const COLLAB_PROMPT_PREVIEW_GRAPHEMES: usize = 160;`
- `const` `codex-rs/tui/src/collab.rs:19` `const COLLAB_AGENT_ERROR_PREVIEW_GRAPHEMES: usize = 160;`
- `const` `codex-rs/tui/src/collab.rs:20` `const COLLAB_AGENT_RESPONSE_PREVIEW_GRAPHEMES: usize = 240;`
- `fn` `codex-rs/tui/src/collab.rs:130` `fn collab_event(title: impl Into<String>, details: Vec<Line<'static>>) -> PlainHistoryCell {`
- `fn` `codex-rs/tui/src/collab.rs:140` `fn detail_line(label: &str, value: impl Into<Span<'static>>) -> Line<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:144` `fn status_line(status: &AgentStatus) -> Line<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:148` `fn status_span(status: &AgentStatus) -> Span<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:159` `fn prompt_line(prompt: &str) -> Option<Line<'static>> {`
- `fn` `codex-rs/tui/src/collab.rs:171` `fn format_thread_ids(ids: &[ThreadId]) -> Span<'static> {`
- `fn` `codex-rs/tui/src/collab.rs:183` `fn wait_complete_lines(statuses: &HashMap<ThreadId, AgentStatus>) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/collab.rs:276` `fn push_status_count(`
- `fn` `codex-rs/tui/src/collab.rs:290` `fn detail_line_spans(label: &str, mut value: Vec<Span<'static>>) -> Line<'static> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::history_cell::PlainHistoryCell;`
- `use crate::render::line_utils::prefix_lines;`
- `use crate::text_formatting::truncate_text;`
- `use codex_core::protocol::AgentStatus;`
- `use codex_core::protocol::CollabAgentInteractionEndEvent;`
- `use codex_core::protocol::CollabAgentSpawnEndEvent;`
- `use codex_core::protocol::CollabCloseEndEvent;`
- `use codex_core::protocol::CollabResumeBeginEvent;`
- `use codex_core::protocol::CollabResumeEndEvent;`
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
- `docs/workdocjcl/spec/06_UI/TUI.md`
