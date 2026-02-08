# `codex-rs/tui/src/key_hint.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3306`
- sha256: `07f34aab630b2658560d2d4e73719481ec8638e33eb38401d7a23643689f13c8`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/key_hint.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn is_press(&self, event: KeyEvent) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/key_hint.rs:1` `use crossterm::event::KeyCode;`
- `use` `codex-rs/tui/src/key_hint.rs:2` `use crossterm::event::KeyEvent;`
- `use` `codex-rs/tui/src/key_hint.rs:3` `use crossterm::event::KeyEventKind;`
- `use` `codex-rs/tui/src/key_hint.rs:4` `use crossterm::event::KeyModifiers;`
- `use` `codex-rs/tui/src/key_hint.rs:5` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/key_hint.rs:6` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/key_hint.rs:7` `use ratatui::text::Span;`
- `const` `codex-rs/tui/src/key_hint.rs:10` `const ALT_PREFIX: &str = "⌥ + ";`
- `const` `codex-rs/tui/src/key_hint.rs:12` `const ALT_PREFIX: &str = "⌥ + ";`
- `const` `codex-rs/tui/src/key_hint.rs:14` `const ALT_PREFIX: &str = "alt + ";`
- `const` `codex-rs/tui/src/key_hint.rs:15` `const CTRL_PREFIX: &str = "ctrl + ";`
- `const` `codex-rs/tui/src/key_hint.rs:16` `const SHIFT_PREFIX: &str = "shift + ";`
- `impl` `codex-rs/tui/src/key_hint.rs:24` `impl KeyBinding {`
- `fn` `codex-rs/tui/src/key_hint.rs:29` `pub fn is_press(&self, event: KeyEvent) -> bool {`
- `fn` `codex-rs/tui/src/key_hint.rs:56` `fn modifiers_to_string(modifiers: KeyModifiers) -> String {`
- `impl` `codex-rs/tui/src/key_hint.rs:70` `impl From<KeyBinding> for Span<'static> {`
- `fn` `codex-rs/tui/src/key_hint.rs:71` `fn from(binding: KeyBinding) -> Self {`
- `impl` `codex-rs/tui/src/key_hint.rs:75` `impl From<&KeyBinding> for Span<'static> {`
- `fn` `codex-rs/tui/src/key_hint.rs:76` `fn from(binding: &KeyBinding) -> Self {`
- `fn` `codex-rs/tui/src/key_hint.rs:94` `fn key_hint_style() -> Style {`

## Dependencies (auto sample)
### Imports / Includes
- `use crossterm::event::KeyCode;`
- `use crossterm::event::KeyEvent;`
- `use crossterm::event::KeyEventKind;`
- `use crossterm::event::KeyModifiers;`
- `use ratatui::style::Style;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Span;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
