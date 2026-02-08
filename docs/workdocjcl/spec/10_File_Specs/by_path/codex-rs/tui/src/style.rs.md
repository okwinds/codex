# `codex-rs/tui/src/style.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1270`
- sha256: `5859c393283a132bb209a99ab9c2021fdb07e7452dcaba6d09492083468ba8ba`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/style.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn user_message_style() -> Style {`
- `pub fn proposed_plan_style() -> Style {`
- `pub fn user_message_style_for(terminal_bg: Option<(u8, u8, u8)>) -> Style {`
- `pub fn proposed_plan_style_for(terminal_bg: Option<(u8, u8, u8)>) -> Style {`
- `pub fn user_message_bg(terminal_bg: (u8, u8, u8)) -> Color {`
- `pub fn proposed_plan_bg(terminal_bg: (u8, u8, u8)) -> Color {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/style.rs:1` `use crate::color::blend;`
- `use` `codex-rs/tui/src/style.rs:2` `use crate::color::is_light;`
- `use` `codex-rs/tui/src/style.rs:3` `use crate::terminal_palette::best_color;`
- `use` `codex-rs/tui/src/style.rs:4` `use crate::terminal_palette::default_bg;`
- `use` `codex-rs/tui/src/style.rs:5` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/style.rs:6` `use ratatui::style::Style;`
- `fn` `codex-rs/tui/src/style.rs:8` `pub fn user_message_style() -> Style {`
- `fn` `codex-rs/tui/src/style.rs:12` `pub fn proposed_plan_style() -> Style {`
- `fn` `codex-rs/tui/src/style.rs:17` `pub fn user_message_style_for(terminal_bg: Option<(u8, u8, u8)>) -> Style {`
- `fn` `codex-rs/tui/src/style.rs:24` `pub fn proposed_plan_style_for(terminal_bg: Option<(u8, u8, u8)>) -> Style {`
- `fn` `codex-rs/tui/src/style.rs:32` `pub fn user_message_bg(terminal_bg: (u8, u8, u8)) -> Color {`
- `fn` `codex-rs/tui/src/style.rs:42` `pub fn proposed_plan_bg(terminal_bg: (u8, u8, u8)) -> Color {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::color::blend;`
- `use crate::color::is_light;`
- `use crate::terminal_palette::best_color;`
- `use crate::terminal_palette::default_bg;`
- `use ratatui::style::Color;`
- `use ratatui::style::Style;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
