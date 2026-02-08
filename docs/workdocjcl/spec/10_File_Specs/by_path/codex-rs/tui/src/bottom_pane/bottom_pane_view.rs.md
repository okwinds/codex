# `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2237`
- sha256: `93bbe4f773e99b31250e842303f8656746ee5c37a808dc2cd73701feb19feccf`
- generated_utc: `2026-02-08T10:45:39Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:1` `use crate::bottom_pane::ApprovalRequest;`
- `use` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:2` `use crate::render::renderable::Renderable;`
- `use` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:3` `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:4` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:6` `use super::CancellationEvent;`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:12` `fn handle_key_event(&mut self, _key_event: KeyEvent) {}`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:15` `fn is_complete(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:20` `fn on_ctrl_c(&mut self) -> CancellationEvent {`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:26` `fn prefer_esc_to_handle_key_event(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:32` `fn handle_paste(&mut self, _pasted: String) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:40` `fn flush_paste_burst_if_due(&mut self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:48` `fn is_in_paste_burst(&self) -> bool {`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:54` `fn try_consume_approval_request(`
- `fn` `codex-rs/tui/src/bottom_pane/bottom_pane_view.rs:63` `fn try_consume_user_input_request(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::bottom_pane::ApprovalRequest;`
- `use crate::render::renderable::Renderable;`
- `use codex_protocol::request_user_input::RequestUserInputEvent;`
- `use crossterm::event::KeyEvent;`
- `use super::CancellationEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
