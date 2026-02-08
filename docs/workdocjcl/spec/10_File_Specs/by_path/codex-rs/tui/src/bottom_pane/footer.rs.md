# `codex-rs/tui/src/bottom_pane/footer.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `57714`
- sha256: `5368bc1fb9d2ca54da7e25eacc42f3c05df9bd411212c12ab582cdd8265a881a`
- generated_utc: `2026-02-08T10:45:39Z`

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
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:84` `const MODE_CYCLE_HINT: &str = "shift+tab to cycle";`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:85` `const FOOTER_CONTEXT_GAP_COLS: u16 = 1;`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:87` `impl CollaborationModeIndicator {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:88` `fn label(self, show_cycle_hint: bool) -> String {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:103` `fn styled_span(self, show_cycle_hint: bool) -> Span<'static> {`
- `enum` `codex-rs/tui/src/bottom_pane/footer.rs:237` `enum SummaryHintKind {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:245` `struct LeftSideState {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:250` `fn left_side_line(`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:460` `fn right_aligned_x(area: Rect, content_width: u16) -> Option<u16> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:559` `fn footer_from_props_lines(`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:641` `fn footer_hint_items_line(items: &[(String, String)]) -> Line<'static> {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:655` `struct ShortcutsState {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:662` `fn quit_shortcut_reminder_line(key: KeyBinding) -> Line<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:666` `fn esc_hint_line(esc_backtrack_hint: bool) -> Line<'static> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:681` `fn shortcut_overlay_lines(state: ShortcutsState) -> Vec<Line<'static>> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:732` `fn build_columns(entries: Vec<Line<'static>>) -> Vec<Line<'static>> {`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:737` `const COLUMNS: usize = 2;`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:738` `const COLUMN_PADDING: [usize; COLUMNS] = [4, 4];`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:739` `const COLUMN_GAP: usize = 4;`
- `enum` `codex-rs/tui/src/bottom_pane/footer.rs:794` `enum ShortcutId {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:809` `struct ShortcutBinding {`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:814` `impl ShortcutBinding {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:815` `fn matches(&self, state: ShortcutsState) -> bool {`
- `enum` `codex-rs/tui/src/bottom_pane/footer.rs:821` `enum DisplayCondition {`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:829` `impl DisplayCondition {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:830` `fn matches(self, state: ShortcutsState) -> bool {`
- `struct` `codex-rs/tui/src/bottom_pane/footer.rs:841` `struct ShortcutDescriptor {`
- `impl` `codex-rs/tui/src/bottom_pane/footer.rs:848` `impl ShortcutDescriptor {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:849` `fn binding_for(&self, state: ShortcutsState) -> Option<&'static ShortcutBinding> {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:853` `fn overlay_entry(&self, state: ShortcutsState) -> Option<Line<'static>> {`
- `const` `codex-rs/tui/src/bottom_pane/footer.rs:874` `const SHORTCUTS: &[ShortcutDescriptor] = &[`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:992` `use super::*;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:993` `use crate::bottom_pane::selection_popup_common::truncate_line_with_ellipsis_if_overflow;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:994` `use crate::test_backend::VT100Backend;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:995` `use insta::assert_snapshot;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:996` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:997` `use ratatui::Terminal;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:998` `use ratatui::backend::Backend;`
- `use` `codex-rs/tui/src/bottom_pane/footer.rs:999` `use ratatui::backend::TestBackend;`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1001` `fn snapshot_footer(name: &str, props: FooterProps) {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1160` `fn snapshot_footer_with_mode_indicator(`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1172` `fn render_footer_with_mode_indicator(`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1184` `fn footer_snapshots() {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1544` `fn footer_status_line_truncates_to_keep_mode_indicator() {`
- `fn` `codex-rs/tui/src/bottom_pane/footer.rs:1581` `fn paste_image_shortcut_prefers_ctrl_alt_v_under_wsl() {`

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
- `use crate::bottom_pane::selection_popup_common::truncate_line_with_ellipsis_if_overflow;`
- `use crate::test_backend::VT100Backend;`
- `use insta::assert_snapshot;`
- `use pretty_assertions::assert_eq;`
- `use ratatui::Terminal;`
- `use ratatui::backend::Backend;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
