# `codex-rs/tui/src/bottom_pane/scroll_state.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3374`
- sha256: `0194a52aa318445c2b86f87caed817ae68a718a1d7ab706c13a471ad0b0c32a2`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/scroll_state.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn new() -> Self {`
- `pub fn reset(&mut self) {`
- `pub fn clamp_selection(&mut self, len: usize) {`
- `pub fn move_up_wrap(&mut self, len: usize) {`
- `pub fn move_down_wrap(&mut self, len: usize) {`
- `pub fn ensure_visible(&mut self, len: usize, visible_rows: usize) {`

## Definitions (auto, per-file)
- `impl` `codex-rs/tui/src/bottom_pane/scroll_state.rs:13` `impl ScrollState {`
- `fn` `codex-rs/tui/src/bottom_pane/scroll_state.rs:14` `pub fn new() -> Self {`
- `fn` `codex-rs/tui/src/bottom_pane/scroll_state.rs:22` `pub fn reset(&mut self) {`
- `fn` `codex-rs/tui/src/bottom_pane/scroll_state.rs:28` `pub fn clamp_selection(&mut self, len: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/scroll_state.rs:39` `pub fn move_up_wrap(&mut self, len: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/scroll_state.rs:53` `pub fn move_down_wrap(&mut self, len: usize) {`
- `fn` `codex-rs/tui/src/bottom_pane/scroll_state.rs:67` `pub fn ensure_visible(&mut self, len: usize, visible_rows: usize) {`
- `use` `codex-rs/tui/src/bottom_pane/scroll_state.rs:89` `use super::ScrollState;`
- `fn` `codex-rs/tui/src/bottom_pane/scroll_state.rs:92` `fn wrap_navigation_and_visibility() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::ScrollState;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
