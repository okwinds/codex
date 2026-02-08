# `codex-rs/ansi-escape/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2164`
- sha256: `4ee1d3709d986a783ba479f6df4b11033a5c26645f51795c50311d7e16642e0c`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/ansi-escape/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn ansi_escape_line(s: &str) -> Line<'static> {`
- `pub fn ansi_escape(s: &str) -> Text<'static> {`

## Definitions (auto, per-file)
- `use` `codex-rs/ansi-escape/src/lib.rs:1` `use ansi_to_tui::Error;`
- `use` `codex-rs/ansi-escape/src/lib.rs:2` `use ansi_to_tui::IntoText;`
- `use` `codex-rs/ansi-escape/src/lib.rs:3` `use ratatui::text::Line;`
- `use` `codex-rs/ansi-escape/src/lib.rs:4` `use ratatui::text::Text;`
- `fn` `codex-rs/ansi-escape/src/lib.rs:11` `fn expand_tabs(s: &str) -> std::borrow::Cow<'_, str> {`
- `fn` `codex-rs/ansi-escape/src/lib.rs:26` `pub fn ansi_escape_line(s: &str) -> Line<'static> {`
- `fn` `codex-rs/ansi-escape/src/lib.rs:40` `pub fn ansi_escape(s: &str) -> Text<'static> {`

## Dependencies (auto sample)
### Imports / Includes
- `use ansi_to_tui::Error;`
- `use ansi_to_tui::IntoText;`
- `use ratatui::text::Line;`
- `use ratatui::text::Text;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
