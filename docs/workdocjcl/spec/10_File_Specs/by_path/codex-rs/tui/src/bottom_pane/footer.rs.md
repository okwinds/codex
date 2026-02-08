# `codex-rs/tui/src/bottom_pane/footer.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `46240`
- sha256: `5edf931da41b58a8ddb9b20a9422678b1418a069cf390a96c8badc2e205e6a08`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/footer.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:35` `use crate::key_hint;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:36` `use crate::key_hint::KeyBinding;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:37` `use crate::render::line_utils::prefix_lines;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:38` `use crate::status::format_tokens_compact;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:39` `use crate::ui_consts::FOOTER_INDENT_COLS;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:40` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:41` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:42` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:43` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:44` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:45` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:46` `use ratatui::widgets::Paragraph;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:47` `use ratatui::widgets::Widget;`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:80` `const MODE_CYCLE_HINT: &str = "shift+tab to cycle";`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:81` `const FOOTER_CONTEXT_GAP_COLS: u16 = 1;`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:83` `impl CollaborationModeIndicator {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:84` `fn label(self, show_cycle_hint: bool) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:99` `fn styled_span(self, show_cycle_hint: bool) -> Span<'static> {`
- `enum` `codex-rs/tui/src/bottom_pane/footer.rs:233` `enum SummaryHintKind {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:241` `struct LeftSideState {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:246` `fn left_side_line(`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:449` `fn right_aligned_x(area: Rect, content_width: u16) -> Option<u16> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:534` `fn footer_from_props_lines(`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:606` `fn footer_hint_items_line(items: &[(String, String)]) -> Line<'static> {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:620` `struct ShortcutsState {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:627` `fn quit_shortcut_reminder_line(key: KeyBinding) -> Line<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:631` `fn esc_hint_line(esc_backtrack_hint: bool) -> Line<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:646` `fn shortcut_overlay_lines(state: ShortcutsState) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:697` `fn build_columns(entries: Vec<Line<'static>>) -> Vec<Line<'static>> {`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:702` `const COLUMNS: usize = 2;`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:703` `const COLUMN_PADDING: [usize; COLUMNS] = [4, 4];`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:704` `const COLUMN_GAP: usize = 4;`
- `enum` `codex-rs/tui/src/bottom_pane/footer.rs:759` `enum ShortcutId {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:774` `struct ShortcutBinding {`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:779` `impl ShortcutBinding {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:780` `fn matches(&self, state: ShortcutsState) -> bool {`
- `enum` `codex-rs/tui/src/bottom_pane/footer.rs:786` `enum DisplayCondition {`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:794` `impl DisplayCondition {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:795` `fn matches(self, state: ShortcutsState) -> bool {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:806` `struct ShortcutDescriptor {`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:813` `impl ShortcutDescriptor {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:814` `fn binding_for(&self, state: ShortcutsState) -> Option<&'static ShortcutBinding> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:818` `fn overlay_entry(&self, state: ShortcutsState) -> Option<Line<'static>> {`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:839` `const SHORTCUTS: &[ShortcutDescriptor] = &[`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:957` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:958` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:959` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:960` `use ratatui::Terminal;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:961` `use ratatui::backend::TestBackend;`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:963` `fn snapshot_footer(name: &str, props: FooterProps) {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:967` `fn snapshot_footer_with_mode_indicator(`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1066` `fn footer_snapshots() {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1292` `fn paste_image_shortcut_prefers_ctrl_alt_v_under_wsl() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::key_hint;`
- `use crate::key_hint::KeyBinding;`
- `use crate::render::line_utils::prefix_lines;`
- `use crate::status::format_tokens_compact;`
- `use crate::ui_consts::FOOTER_INDENT_COLS;`
- `use crossterm::event::KeyCode;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use ratatui::widgets::Paragraph;`
- `use ratatui::widgets::Widget;`
- `use super::*;`
- `use insta::assert_snapshot;`
- `use pretty_assertions::assert_eq;`
- `use ratatui::Terminal;`
- `use ratatui::backend::TestBackend;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
