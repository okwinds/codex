# `codex-rs/tui/src/status_indicator_widget.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `12397`
- sha256: `0966af6e89ebc325ad3658fe74d7fd9dd801f064a9cf8b16e2e262dbf7f0d41f`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/status_indicator_widget.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn fmt_elapsed_compact(elapsed_secs: u64) -> String {`
- `pub fn elapsed_seconds(&self) -> u64 {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/status_indicator_widget.rs:4` `use std::time::Duration;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:5` `use std::time::Instant;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:7` `use codex_core::protocol::Op;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:8` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:9` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:10` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:11` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:12` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:13` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:14` `use ratatui::text::Text;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:15` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:16` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:17` `use unicode_width::UnicodeWidthStr;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:19` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:20` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:21` `use crate::exec_cell::spinner;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:22` `use crate::key_hint;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:23` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:24` `use crate::shimmer::shimmer_spans;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:25` `use crate::text_formatting::capitalize_first;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:26` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:27` `use crate::wrapping::RtOptions;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:28` `use crate::wrapping::word_wrap_lines;`
- `const` `codex-rs/tui/src/status_indicator_widget.rs:30` `const DETAILS_MAX_LINES: usize = 3;`
- `const` `codex-rs/tui/src/status_indicator_widget.rs:31` `const DETAILS_PREFIX: &str = "  └ ";`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:49` `pub fn fmt_elapsed_compact(elapsed_secs: u64) -> String {`
- `impl` `codex-rs/tui/src/status_indicator_widget.rs:64` `impl StatusIndicatorWidget {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:144` `fn elapsed_duration_at(&self, now: Instant) -> Duration {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:152` `fn elapsed_seconds_at(&self, now: Instant) -> u64 {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:156` `pub fn elapsed_seconds(&self) -> u64 {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:161` `fn wrapped_details_lines(&self, width: u16) -> Vec<Line<'static>> {`
- `impl` `codex-rs/tui/src/status_indicator_widget.rs:193` `impl Renderable for StatusIndicatorWidget {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:194` `fn desired_height(&self, width: u16) -> u16 {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:198` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:244` `use super::*;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:245` `use crate::app_event::AppEvent;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:246` `use crate::app_event_sender::AppEventSender;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:247` `use ratatui::Terminal;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:248` `use ratatui::backend::TestBackend;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:249` `use std::time::Duration;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:250` `use std::time::Instant;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:251` `use tokio::sync::mpsc::unbounded_channel;`
- `use` `codex-rs/tui/src/status_indicator_widget.rs:253` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:256` `fn fmt_elapsed_compact_formats_seconds_minutes_hours() {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:270` `fn renders_with_working_header() {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:284` `fn renders_truncated() {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:298` `fn renders_wrapped_details_panama_two_lines() {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:319` `fn timer_pauses_when_requested() {`
- `fn` `codex-rs/tui/src/status_indicator_widget.rs:341` `fn details_overflow_adds_ellipsis() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use codex_core::protocol::Op;`
- `use crossterm::event::KeyCode;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::text::Text;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::WidgetRef;`
- `use unicode_width::UnicodeWidthStr;`
- `use crate::app_event::AppEvent;`
- `use crate::app_event_sender::AppEventSender;`
- `use crate::exec_cell::spinner;`
- `use crate::key_hint;`
- `use crate::render::renderable::Renderable;`
- `use crate::shimmer::shimmer_spans;`
- `use crate::text_formatting::capitalize_first;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
