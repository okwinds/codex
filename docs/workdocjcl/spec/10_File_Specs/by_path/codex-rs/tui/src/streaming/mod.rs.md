# `codex-rs/tui/src/streaming/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3986`
- sha256: `babc77805e638bf152fb79a48cb410a6c8b5dbc844c05954e4822206e2f2a378`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/streaming/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/streaming/mod.rs:12` `use std::collections::VecDeque;`
- `use` `codex-rs/tui/src/streaming/mod.rs:13` `use std::time::Duration;`
- `use` `codex-rs/tui/src/streaming/mod.rs:14` `use std::time::Instant;`
- `use` `codex-rs/tui/src/streaming/mod.rs:16` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/streaming/mod.rs:18` `use crate::markdown_stream::MarkdownStreamCollector;`
- `struct` `codex-rs/tui/src/streaming/mod.rs:23` `struct QueuedLine {`
- `impl` `codex-rs/tui/src/streaming/mod.rs:35` `impl StreamState {`
- `use` `codex-rs/tui/src/streaming/mod.rs:103` `use super::*;`
- `use` `codex-rs/tui/src/streaming/mod.rs:104` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/streaming/mod.rs:107` `fn drain_n_clamps_to_available_lines() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::VecDeque;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use ratatui::text::Line;`
- `use crate::markdown_stream::MarkdownStreamCollector;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
