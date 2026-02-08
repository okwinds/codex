# `codex-rs/cloud-tasks/src/ui.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `35645`
- sha256: `1b7750ddca26bc340c27b795c0e462362f256af872b43ac9aa08942179393068`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cloud-tasks/src/ui.rs` (read)
- env: `CODEX_TUI_ROUNDED`

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn draw(frame: &mut Frame, app: &mut App) {`
- `pub fn draw_new_task_page(frame: &mut Frame, area: Rect, app: &mut App) {`
- `pub fn draw_apply_modal(frame: &mut Frame, area: Rect, app: &mut App) {`
- `pub fn draw_env_modal(frame: &mut Frame, area: Rect, app: &mut App) {`
- `pub fn draw_best_of_modal(frame: &mut Frame, area: Rect, app: &mut App) {`

## Definitions (auto, per-file)
- `use` `codex-rs/cloud-tasks/src/ui.rs:1` `use ratatui::layout::Constraint;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:2` `use ratatui::layout::Direction;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:3` `use ratatui::layout::Layout;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:4` `use ratatui::prelude::*;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:5` `use ratatui::style::Color;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:6` `use ratatui::style::Modifier;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:7` `use ratatui::style::Style;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:8` `use ratatui::style::Stylize;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:9` `use ratatui::widgets::Block;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:10` `use ratatui::widgets::BorderType;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:11` `use ratatui::widgets::Borders;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:12` `use ratatui::widgets::Clear;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:13` `use ratatui::widgets::List;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:14` `use ratatui::widgets::ListItem;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:15` `use ratatui::widgets::ListState;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:16` `use ratatui::widgets::Padding;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:17` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:18` `use std::sync::OnceLock;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:19` `use std::time::Instant;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:21` `use crate::app::App;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:22` `use crate::app::AttemptView;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:23` `use crate::util::format_relative_time_now;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:24` `use codex_cloud_tasks_client::AttemptStatus;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:25` `use codex_cloud_tasks_client::TaskStatus;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:26` `use codex_tui::render_markdown_text;`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:28` `pub fn draw(frame: &mut Frame, app: &mut App) {`
- `static` `codex-rs/cloud-tasks/src/ui.rs:60` `static ROUNDED: OnceLock<bool> = OnceLock::new();`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:62` `fn rounded_enabled() -> bool {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:71` `fn overlay_outer(area: Rect) -> Rect {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:90` `fn overlay_block() -> Block<'static> {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:100` `fn overlay_content(area: Rect) -> Rect {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:104` `pub fn draw_new_task_page(frame: &mut Frame, area: Rect, app: &mut App) {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:176` `fn draw_list(frame: &mut Frame, area: Rect, app: &mut App) {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:236` `fn draw_footer(frame: &mut Frame, area: Rect, app: &mut App) {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:312` `fn draw_diff_overlay(frame: &mut Frame, area: Rect, app: &mut App) {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:469` `pub fn draw_apply_modal(frame: &mut Frame, area: Rect, app: &mut App) {`
- `use` `codex-rs/cloud-tasks/src/ui.rs:470` `use ratatui::widgets::Wrap;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:519` `use ratatui::text::Span;`
- `enum` `codex-rs/cloud-tasks/src/ui.rs:553` `enum ConversationSpeaker {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:558` `fn style_conversation_lines(`
- `use` `codex-rs/cloud-tasks/src/ui.rs:562` `use ratatui::text::Span;`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:651` `fn conversation_header_line(`
- `use` `codex-rs/cloud-tasks/src/ui.rs:655` `use ratatui::text::Span;`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:677` `fn conversation_gutter_span(speaker: ConversationSpeaker) -> ratatui::text::Span<'static> {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:684` `fn conversation_text_spans(`
- `use` `codex-rs/cloud-tasks/src/ui.rs:690` `use ratatui::text::Span;`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:739` `fn attempt_status_span(status: AttemptStatus) -> Option<ratatui::text::Span<'static>> {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:750` `fn style_diff_line(raw: &str) -> Line<'static> {`
- `use` `codex-rs/cloud-tasks/src/ui.rs:751` `use ratatui::style::Color;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:752` `use ratatui::style::Modifier;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:753` `use ratatui::style::Style;`
- `use` `codex-rs/cloud-tasks/src/ui.rs:754` `use ratatui::text::Span;`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:785` `fn render_task_item(_app: &App, t: &codex_cloud_tasks_client::TaskSummary) -> ListItem<'static> {`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:843` `fn draw_inline_spinner(`
- `use` `codex-rs/cloud-tasks/src/ui.rs:849` `use ratatui::widgets::Paragraph;`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:862` `fn draw_centered_spinner(`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:890` `pub fn draw_env_modal(frame: &mut Frame, area: Rect, app: &mut App) {`
- `use` `codex-rs/cloud-tasks/src/ui.rs:891` `use ratatui::widgets::Wrap;`
- `fn` `codex-rs/cloud-tasks/src/ui.rs:990` `pub fn draw_best_of_modal(frame: &mut Frame, area: Rect, app: &mut App) {`
- `use` `codex-rs/cloud-tasks/src/ui.rs:991` `use ratatui::widgets::Wrap;`
- `const` `codex-rs/cloud-tasks/src/ui.rs:994` `const MAX_WIDTH: u16 = 40;`
- `const` `codex-rs/cloud-tasks/src/ui.rs:995` `const MIN_WIDTH: u16 = 20;`
- `const` `codex-rs/cloud-tasks/src/ui.rs:996` `const MAX_HEIGHT: u16 = 12;`
- `const` `codex-rs/cloud-tasks/src/ui.rs:997` `const MIN_HEIGHT: u16 = 6;`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::layout::Constraint;`
- `use ratatui::layout::Direction;`
- `use ratatui::layout::Layout;`
- `use ratatui::prelude::*;`
- `use ratatui::style::Color;`
- `use ratatui::style::Modifier;`
- `use ratatui::style::Style;`
- `use ratatui::style::Stylize;`
- `use ratatui::widgets::Block;`
- `use ratatui::widgets::BorderType;`
- `use ratatui::widgets::Borders;`
- `use ratatui::widgets::Clear;`
- `use ratatui::widgets::List;`
- `use ratatui::widgets::ListItem;`
- `use ratatui::widgets::ListState;`
- `use ratatui::widgets::Padding;`
- `use ratatui::widgets::Paragraph;`
- `use std::sync::OnceLock;`
- `use std::time::Instant;`
- `use crate::app::App;`
### Referenced env vars
- `CODEX_TUI_ROUNDED`

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
