# `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `11882`
- sha256: `9d9421974fdbaac4c7cbcead363deef458775da7b79ed542a3a64c3a62545900`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:1` `use ratatui::layout::Rect;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:3` `use super::DESIRED_SPACERS_BETWEEN_SECTIONS;`
- `use` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:4` `use super::RequestUserInputOverlay;`
- `impl` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:17` `impl RequestUserInputOverlay {`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:63` `fn layout_with_options(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:99` `fn layout_with_options_normal(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:203` `fn layout_without_options(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:225` `fn layout_without_options_tight(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:247` `fn layout_without_options_normal(`
- `fn` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:282` `fn build_layout_areas(`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:330` `struct LayoutPlan {`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:341` `struct OptionsLayoutArgs {`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:351` `struct OptionsNormalArgs {`
- `struct` `codex-rs/tui/src/bottom_pane/request_user_input/layout.rs:360` `struct OptionsHeights {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::layout::Rect;`
- `use super::DESIRED_SPACERS_BETWEEN_SECTIONS;`
- `use super::RequestUserInputOverlay;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
