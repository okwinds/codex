# `codex-rs/tui/src/diff_render.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `24615`
- sha256: `4708b5f44a0673d6fffb82d7fb1ac57666d614f0cce10f6a4c988c163d9eb5c7`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/diff_render.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct DiffSummary {`
- `pub fn new(changes: HashMap<PathBuf, FileChange>, cwd: PathBuf) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/diff_render.rs:1` `use diffy::Hunk;`
- `use` `codex-rs/tui/src/diff_render.rs:2` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/diff_render.rs:3` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/diff_render.rs:4` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/diff_render.rs:5` `use ratatui::style::Modifier;`
- `use` `codex-rs/tui/src/diff_render.rs:6` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/diff_render.rs:7` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/diff_render.rs:8` `use ratatui::text::Line as RtLine;`
- `use` `codex-rs/tui/src/diff_render.rs:9` `use ratatui::text::Span as RtSpan;`
- `use` `codex-rs/tui/src/diff_render.rs:10` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/diff_render.rs:11` `use std::collections::HashMap;`
- `use` `codex-rs/tui/src/diff_render.rs:12` `use std::path::Path;`
- `use` `codex-rs/tui/src/diff_render.rs:13` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/diff_render.rs:15` `use crate::exec_command::relativize_to_home;`
- `use` `codex-rs/tui/src/diff_render.rs:16` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/diff_render.rs:17` `use crate::render::line_utils::prefix_lines;`
- `use` `codex-rs/tui/src/diff_render.rs:18` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/diff_render.rs:19` `use crate::render::renderable::InsetRenderable;`
- `use` `codex-rs/tui/src/diff_render.rs:20` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/diff_render.rs:21` `use codex_core::git_info::get_git_repo_root;`
- `use` `codex-rs/tui/src/diff_render.rs:22` `use codex_core::protocol::FileChange;`
- `enum` `codex-rs/tui/src/diff_render.rs:25` `enum DiffLineType {`
- `struct` `codex-rs/tui/src/diff_render.rs:31` `pub struct DiffSummary {`
- `impl` `codex-rs/tui/src/diff_render.rs:36` `impl DiffSummary {`
- `fn` `codex-rs/tui/src/diff_render.rs:37` `pub fn new(changes: HashMap<PathBuf, FileChange>, cwd: PathBuf) -> Self {`
- `impl` `codex-rs/tui/src/diff_render.rs:42` `impl Renderable for FileChange {`
- `fn` `codex-rs/tui/src/diff_render.rs:43` `fn render(&self, area: Rect, buf: &mut Buffer) {`
- `fn` `codex-rs/tui/src/diff_render.rs:49` `fn desired_height(&self, width: u16) -> u16 {`
- `impl` `codex-rs/tui/src/diff_render.rs:56` `impl From<DiffSummary> for Box<dyn Renderable> {`
- `fn` `codex-rs/tui/src/diff_render.rs:57` `fn from(val: DiffSummary) -> Self {`
- `struct` `codex-rs/tui/src/diff_render.rs:90` `struct Row {`
- `fn` `codex-rs/tui/src/diff_render.rs:99` `fn collect_rows(changes: &HashMap<PathBuf, FileChange>) -> Vec<Row> {`
- `fn` `codex-rs/tui/src/diff_render.rs:126` `fn render_line_count_summary(added: usize, removed: usize) -> Vec<RtSpan<'static>> {`
- `fn` `codex-rs/tui/src/diff_render.rs:136` `fn render_changes_block(rows: Vec<Row>, wrap_cols: usize, cwd: &Path) -> Vec<RtLine<'static>> {`
- `fn` `codex-rs/tui/src/diff_render.rs:196` `fn render_change(change: &FileChange, out: &mut Vec<RtLine<'static>>, width: usize) {`
- `fn` `codex-rs/tui/src/diff_render.rs:345` `fn push_wrapped_diff_line(`
- `fn` `codex-rs/tui/src/diff_render.rs:406` `fn line_number_width(max_line_number: usize) -> usize {`
- `fn` `codex-rs/tui/src/diff_render.rs:414` `fn style_gutter() -> Style {`
- `fn` `codex-rs/tui/src/diff_render.rs:418` `fn style_context() -> Style {`
- `fn` `codex-rs/tui/src/diff_render.rs:422` `fn style_add() -> Style {`
- `fn` `codex-rs/tui/src/diff_render.rs:426` `fn style_del() -> Style {`
- `use` `codex-rs/tui/src/diff_render.rs:432` `use super::*;`
- `use` `codex-rs/tui/src/diff_render.rs:433` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/diff_render.rs:434` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/diff_render.rs:435` `use ratatui::Terminal;`
- `use` `codex-rs/tui/src/diff_render.rs:436` `use ratatui::backend::TestBackend;`
- `use` `codex-rs/tui/src/diff_render.rs:437` `use ratatui::text::Text;`
- `use` `codex-rs/tui/src/diff_render.rs:438` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/diff_render.rs:439` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/diff_render.rs:440` `use ratatui::widgets::Wrap;`
- `fn` `codex-rs/tui/src/diff_render.rs:441` `fn diff_summary_for_tests(changes: &HashMap<PathBuf, FileChange>) -> Vec<RtLine<'static>> {`
- `fn` `codex-rs/tui/src/diff_render.rs:445` `fn snapshot_lines(name: &str, lines: Vec<RtLine<'static>>, width: u16, height: u16) {`
- `fn` `codex-rs/tui/src/diff_render.rs:457` `fn snapshot_lines_text(name: &str, lines: &[RtLine<'static>]) {`
- `fn` `codex-rs/tui/src/diff_render.rs:475` `fn display_path_prefers_cwd_without_git_repo() {`
- `fn` `codex-rs/tui/src/diff_render.rs:495` `fn ui_snapshot_wrap_behavior_insert() {`
- `fn` `codex-rs/tui/src/diff_render.rs:508` `fn ui_snapshot_apply_update_block() {`
- `fn` `codex-rs/tui/src/diff_render.rs:528` `fn ui_snapshot_apply_update_with_rename_block() {`
- `fn` `codex-rs/tui/src/diff_render.rs:548` `fn ui_snapshot_apply_multiple_files_block() {`
- `fn` `codex-rs/tui/src/diff_render.rs:576` `fn ui_snapshot_apply_add_block() {`
- `fn` `codex-rs/tui/src/diff_render.rs:591` `fn ui_snapshot_apply_delete_block() {`
- `fn` `codex-rs/tui/src/diff_render.rs:605` `fn ui_snapshot_apply_update_block_wraps_long_lines() {`
- `fn` `codex-rs/tui/src/diff_render.rs:627` `fn ui_snapshot_apply_update_block_wraps_long_lines_text() {`
- `fn` `codex-rs/tui/src/diff_render.rs:648` `fn ui_snapshot_apply_update_block_line_numbers_three_digits_text() {`
- `fn` `codex-rs/tui/src/diff_render.rs:675` `fn ui_snapshot_apply_update_block_relativizes_path() {`

## Dependencies (auto sample)
### Imports / Includes
- `use diffy::Hunk;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Color;`
- `use ratatui::style::Modifier;`
- `use ratatui::style::Style;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line as RtLine;`
- `use ratatui::text::Span as RtSpan;`
- `use ratatui::widgets::Paragraph;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use crate::exec_command::relativize_to_home;`
- `use crate::render::Insets;`
- `use crate::render::line_utils::prefix_lines;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::InsetRenderable;`
- `use crate::render::renderable::Renderable;`
- `use codex_core::git_info::get_git_repo_root;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
