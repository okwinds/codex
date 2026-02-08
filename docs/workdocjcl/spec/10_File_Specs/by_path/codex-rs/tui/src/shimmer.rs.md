# `codex-rs/tui/src/shimmer.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2691`
- sha256: `7c9ecdf410c892d21c6f7f1f74d0c1b3db47bc06f4f119b843b657b712bbee46`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/shimmer.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/shimmer.rs:1` `use std::sync::OnceLock;`
- `use` `codex-rs/tui/src/shimmer.rs:2` `use std::time::Duration;`
- `use` `codex-rs/tui/src/shimmer.rs:3` `use std::time::Instant;`
- `use` `codex-rs/tui/src/shimmer.rs:5` `use ratatui::style::Color;`
- `use` `codex-rs/tui/src/shimmer.rs:6` `use ratatui::style::Modifier;`
- `use` `codex-rs/tui/src/shimmer.rs:7` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/shimmer.rs:8` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/shimmer.rs:10` `use crate::color::blend;`
- `use` `codex-rs/tui/src/shimmer.rs:11` `use crate::terminal_palette::default_bg;`
- `use` `codex-rs/tui/src/shimmer.rs:12` `use crate::terminal_palette::default_fg;`
- `static` `codex-rs/tui/src/shimmer.rs:14` `static PROCESS_START: OnceLock<Instant> = OnceLock::new();`
- `fn` `codex-rs/tui/src/shimmer.rs:16` `fn elapsed_since_start() -> Duration {`
- `fn` `codex-rs/tui/src/shimmer.rs:71` `fn color_for_level(intensity: f32) -> Style {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::OnceLock;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use ratatui::style::Color;`
- `use ratatui::style::Modifier;`
- `use ratatui::style::Style;`
- `use ratatui::text::Span;`
- `use crate::color::blend;`
- `use crate::terminal_palette::default_bg;`
- `use crate::terminal_palette::default_fg;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
