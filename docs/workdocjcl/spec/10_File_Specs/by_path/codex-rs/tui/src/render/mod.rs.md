# `codex-rs/tui/src/render/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1090`
- sha256: `21f83df9ccb9106a1a362ed1f7f1a4c628b171e20e9e7397261ee5bd116f88f7`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/render/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Insets {`
- `pub fn tlbr(top: u16, left: u16, bottom: u16, right: u16) -> Self {`
- `pub fn vh(v: u16, h: u16) -> Self {`
- `pub trait RectExt {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/render/mod.rs:1` `use ratatui::layout::Rect;`
- `mod` `codex-rs/tui/src/render/mod.rs:3` `pub mod highlight;`
- `mod` `codex-rs/tui/src/render/mod.rs:4` `pub mod line_utils;`
- `mod` `codex-rs/tui/src/render/mod.rs:5` `pub mod renderable;`
- `struct` `codex-rs/tui/src/render/mod.rs:8` `pub struct Insets {`
- `impl` `codex-rs/tui/src/render/mod.rs:15` `impl Insets {`
- `fn` `codex-rs/tui/src/render/mod.rs:16` `pub fn tlbr(top: u16, left: u16, bottom: u16, right: u16) -> Self {`
- `fn` `codex-rs/tui/src/render/mod.rs:25` `pub fn vh(v: u16, h: u16) -> Self {`
- `trait` `codex-rs/tui/src/render/mod.rs:35` `pub trait RectExt {`
- `fn` `codex-rs/tui/src/render/mod.rs:36` `fn inset(&self, insets: Insets) -> Rect;`
- `impl` `codex-rs/tui/src/render/mod.rs:39` `impl RectExt for Rect {`
- `fn` `codex-rs/tui/src/render/mod.rs:40` `fn inset(&self, insets: Insets) -> Rect {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::layout::Rect;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
