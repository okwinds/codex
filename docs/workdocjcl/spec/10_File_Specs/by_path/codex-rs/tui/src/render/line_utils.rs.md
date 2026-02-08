# `codex-rs/tui/src/render/line_utils.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1753`
- sha256: `b4fbe4f6596e329f4733d1612cb9bfb7f7fdc48597fc56e2726022a9b606655e`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/render/line_utils.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn line_to_static(line: &Line<'_>) -> Line<'static> {`
- `pub fn is_blank_line_spaces_only(line: &Line<'_>) -> bool {`
- `pub fn prefix_lines(`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/render/line_utils.rs:1` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/render/line_utils.rs:2` `use ratatui::text::Span;`
- `fn` `codex-rs/tui/src/render/line_utils.rs:5` `pub fn line_to_static(line: &Line<'_>) -> Line<'static> {`
- `fn` `codex-rs/tui/src/render/line_utils.rs:29` `pub fn is_blank_line_spaces_only(line: &Line<'_>) -> bool {`
- `fn` `codex-rs/tui/src/render/line_utils.rs:40` `pub fn prefix_lines(`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
