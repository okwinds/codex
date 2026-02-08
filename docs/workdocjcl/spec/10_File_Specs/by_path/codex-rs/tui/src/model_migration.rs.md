# `codex-rs/tui/src/model_migration.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `18065`
- sha256: `22825829b2a56389e85aebe9c0f9ad5b035306f43137fb15305db4cdd982ba54`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/model_migration.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/model_migration.rs:1` `use crate::key_hint;`
- `use` `codex-rs/tui/src/model_migration.rs:2` `use crate::markdown_render::render_markdown_text_with_width;`
- `use` `codex-rs/tui/src/model_migration.rs:3` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/model_migration.rs:4` `use crate::render::renderable::ColumnRenderable;`
- `use` `codex-rs/tui/src/model_migration.rs:5` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/model_migration.rs:6` `use crate::render::renderable::RenderableExt as _;`
- `use` `codex-rs/tui/src/model_migration.rs:7` `use crate::selection_list::selection_option_row;`
- `use` `codex-rs/tui/src/model_migration.rs:8` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/model_migration.rs:9` `use crate::tui::Tui;`
- `use` `codex-rs/tui/src/model_migration.rs:10` `use crate::tui::TuiEvent;`
- `use` `codex-rs/tui/src/model_migration.rs:11` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/model_migration.rs:12` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/model_migration.rs:13` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/model_migration.rs:14` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/model_migration.rs:15` `use ratatui::prelude::Stylize as _;`
- `use` `codex-rs/tui/src/model_migration.rs:16` `use ratatui::prelude::Widget;`
- `use` `codex-rs/tui/src/model_migration.rs:17` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/model_migration.rs:18` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/model_migration.rs:19` `use ratatui::widgets::Clear;`
- `use` `codex-rs/tui/src/model_migration.rs:20` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/model_migration.rs:21` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/model_migration.rs:22` `use ratatui::widgets::Wrap;`
- `use` `codex-rs/tui/src/model_migration.rs:23` `use tokio_stream::StreamExt;`
- `enum` `codex-rs/tui/src/model_migration.rs:42` `enum MigrationMenuOption {`
- `impl` `codex-rs/tui/src/model_migration.rs:47` `impl MigrationMenuOption {`
- `fn` `codex-rs/tui/src/model_migration.rs:48` `fn all() -> [Self; 2] {`
- `fn` `codex-rs/tui/src/model_migration.rs:52` `fn label(self) -> &'static str {`
- `struct` `codex-rs/tui/src/model_migration.rs:171` `struct ModelMigrationScreen {`
- `impl` `codex-rs/tui/src/model_migration.rs:179` `impl ModelMigrationScreen {`
- `fn` `codex-rs/tui/src/model_migration.rs:180` `fn new(request_frame: FrameRequester, copy: ModelMigrationCopy) -> Self {`
- `fn` `codex-rs/tui/src/model_migration.rs:190` `fn finish_with(&mut self, outcome: ModelMigrationOutcome) {`
- `fn` `codex-rs/tui/src/model_migration.rs:196` `fn accept(&mut self) {`
- `fn` `codex-rs/tui/src/model_migration.rs:200` `fn reject(&mut self) {`
- `fn` `codex-rs/tui/src/model_migration.rs:204` `fn exit(&mut self) {`
- `fn` `codex-rs/tui/src/model_migration.rs:208` `fn confirm_selection(&mut self) {`
- `fn` `codex-rs/tui/src/model_migration.rs:219` `fn highlight_option(&mut self, option: MigrationMenuOption) {`
- `fn` `codex-rs/tui/src/model_migration.rs:226` `fn handle_key(&mut self, key_event: KeyEvent) {`
- `fn` `codex-rs/tui/src/model_migration.rs:243` `fn is_done(&self) -> bool {`
- `fn` `codex-rs/tui/src/model_migration.rs:247` `fn outcome(&self) -> ModelMigrationOutcome {`
- `impl` `codex-rs/tui/src/model_migration.rs:252` `impl WidgetRef for &ModelMigrationScreen {`
- `fn` `codex-rs/tui/src/model_migration.rs:253` `fn render_ref(&self, area: ratatui::layout::Rect, buf: &mut ratatui::buffer::Buffer) {`
- `impl` `codex-rs/tui/src/model_migration.rs:273` `impl ModelMigrationScreen {`
- `fn` `codex-rs/tui/src/model_migration.rs:274` `fn handle_menu_key(&mut self, code: KeyCode) {`
- `fn` `codex-rs/tui/src/model_migration.rs:295` `fn heading_line(&self) -> Line<'static> {`
- `fn` `codex-rs/tui/src/model_migration.rs:301` `fn render_content(&self, column: &mut ColumnRenderable) {`
- `fn` `codex-rs/tui/src/model_migration.rs:305` `fn render_lines(&self, lines: &[Line<'static>], column: &mut ColumnRenderable) {`
- `fn` `codex-rs/tui/src/model_migration.rs:315` `fn render_markdown_content(`
- `fn` `codex-rs/tui/src/model_migration.rs:330` `fn render_menu(&self, column: &mut ColumnRenderable) {`
- `struct` `codex-rs/tui/src/model_migration.rs:366` `struct AltScreenGuard<'a> {`
- `impl` `codex-rs/tui/src/model_migration.rs:370` `impl<'a> AltScreenGuard<'a> {`
- `fn` `codex-rs/tui/src/model_migration.rs:371` `fn enter(tui: &'a mut Tui) -> Self {`
- `impl` `codex-rs/tui/src/model_migration.rs:377` `impl Drop for AltScreenGuard<'_> {`
- `fn` `codex-rs/tui/src/model_migration.rs:378` `fn drop(&mut self) {`
- `fn` `codex-rs/tui/src/model_migration.rs:383` `fn is_ctrl_exit_combo(key_event: KeyEvent) -> bool {`
- `fn` `codex-rs/tui/src/model_migration.rs:388` `fn fill_migration_markdown(template: &str, current_model: &str, target_model: &str) -> String {`
- `use` `codex-rs/tui/src/model_migration.rs:396` `use super::ModelMigrationScreen;`
- `use` `codex-rs/tui/src/model_migration.rs:397` `use super::migration_copy_for_models;`
- `use` `codex-rs/tui/src/model_migration.rs:398` `use crate::custom_terminal::Terminal;`
- `use` `codex-rs/tui/src/model_migration.rs:399` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/model_migration.rs:400` `use crate::tui::FrameRequester;`
- `use` `codex-rs/tui/src/model_migration.rs:401` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/model_migration.rs:402` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/model_migration.rs:403` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/model_migration.rs:404` `use ratatui::layout::Rect;`
- `fn` `codex-rs/tui/src/model_migration.rs:407` `fn prompt_snapshot() {`
- `fn` `codex-rs/tui/src/model_migration.rs:441` `fn prompt_snapshot_gpt5_family() {`
- `fn` `codex-rs/tui/src/model_migration.rs:468` `fn prompt_snapshot_gpt5_codex() {`
- `fn` `codex-rs/tui/src/model_migration.rs:495` `fn prompt_snapshot_gpt5_codex_mini() {`
- `fn` `codex-rs/tui/src/model_migration.rs:522` `fn escape_key_accepts_prompt() {`
- `fn` `codex-rs/tui/src/model_migration.rs:551` `fn selecting_use_existing_model_rejects_upgrade() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::key_hint;`
- `use crate::markdown_render::render_markdown_text_with_width;`
- `use crate::render::Insets;`
- `use crate::render::renderable::ColumnRenderable;`
- `use crate::render::renderable::Renderable;`
- `use crate::render::renderable::RenderableExt as _;`
- `use crate::selection_list::selection_option_row;`
- `use crate::tui::FrameRequester;`
- `use crate::tui::Tui;`
- `use crate::tui::TuiEvent;`
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::prelude::Stylize as _;`
- `use ratatui::prelude::Widget;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Clear;`
- `use ratatui::widgets::Paragraph;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
