# `codex-rs/tui/src/bottom_pane/file_search_popup.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4945`
- sha256: `68b6d31128b3753434585a610242c2711cc134e325d73f907e608d312d6b945f`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/file_search_popup.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:3` `use codex_file_search::FileMatch;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:4` `use ratatui::buffer::Buffer;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:5` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:6` `use ratatui::widgets::WidgetRef;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:8` `use crate::render::Insets;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:9` `use crate::render::RectExt;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:11` `use super::popup_consts::MAX_POPUP_ROWS;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:12` `use super::scroll_state::ScrollState;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:13` `use super::selection_popup_common::GenericDisplayRow;`
- `use` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:14` `use super::selection_popup_common::render_rows;`
- `impl` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:31` `impl FileSearchPopup {`
- `impl` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:112` `impl WidgetRef for &FileSearchPopup {`
- `fn` `codex-rs/tui/src/bottom_pane/file_search_popup.rs:113` `fn render_ref(&self, area: Rect, buf: &mut Buffer) {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use codex_file_search::FileMatch;`
- `use ratatui::buffer::Buffer;`
- `use ratatui::layout::Rect;`
- `use ratatui::widgets::WidgetRef;`
- `use crate::render::Insets;`
- `use crate::render::RectExt;`
- `use super::popup_consts::MAX_POPUP_ROWS;`
- `use super::scroll_state::ScrollState;`
- `use super::selection_popup_common::GenericDisplayRow;`
- `use super::selection_popup_common::render_rows;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
