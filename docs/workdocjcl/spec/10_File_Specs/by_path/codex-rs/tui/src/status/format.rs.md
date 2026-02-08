# `codex-rs/tui/src/status/format.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4026`
- sha256: `6d475bf42b2498cdb8e3c94be8f3f2b0c80717c4243dd4b7731ade8660ac6dc4`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/status/format.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/status/format.rs:1` `use ratatui::prelude::*;`
- `use` `codex-rs/tui/src/status/format.rs:2` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/status/format.rs:3` `use std::collections::BTreeSet;`
- `use` `codex-rs/tui/src/status/format.rs:4` `use unicode_width::UnicodeWidthChar;`
- `use` `codex-rs/tui/src/status/format.rs:5` `use unicode_width::UnicodeWidthStr;`
- `impl` `codex-rs/tui/src/status/format.rs:15` `impl FieldFormatter {`
- `fn` `codex-rs/tui/src/status/format.rs:68` `fn label_span(&self, label: &str) -> Span<'static> {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::prelude::*;`
- `use ratatui::style::Stylize;`
- `use std::collections::BTreeSet;`
- `use unicode_width::UnicodeWidthChar;`
- `use unicode_width::UnicodeWidthStr;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
