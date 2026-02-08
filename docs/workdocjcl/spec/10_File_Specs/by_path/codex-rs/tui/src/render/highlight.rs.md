# `codex-rs/tui/src/render/highlight.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7327`
- sha256: `a3e398d81997a6d0673a15144d10144218680786b9ccfab3aba1ad979e6b2c76`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/render/highlight.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/render/highlight.rs:1` `use ratatui::style::Style;`
- `use` `codex-rs/tui/src/render/highlight.rs:2` `use ratatui::style::Stylize;`
- `use` `codex-rs/tui/src/render/highlight.rs:3` `use ratatui::text::Line;`
- `use` `codex-rs/tui/src/render/highlight.rs:4` `use ratatui::text::Span;`
- `use` `codex-rs/tui/src/render/highlight.rs:5` `use std::sync::OnceLock;`
- `use` `codex-rs/tui/src/render/highlight.rs:6` `use tree_sitter_highlight::Highlight;`
- `use` `codex-rs/tui/src/render/highlight.rs:7` `use tree_sitter_highlight::HighlightConfiguration;`
- `use` `codex-rs/tui/src/render/highlight.rs:8` `use tree_sitter_highlight::HighlightEvent;`
- `use` `codex-rs/tui/src/render/highlight.rs:9` `use tree_sitter_highlight::Highlighter;`
- `enum` `codex-rs/tui/src/render/highlight.rs:13` `enum BashHighlight {`
- `impl` `codex-rs/tui/src/render/highlight.rs:25` `impl BashHighlight {`
- `const` `codex-rs/tui/src/render/highlight.rs:26` `const ALL: [Self; 9] = [`
- `const` `codex-rs/tui/src/render/highlight.rs:38` `const fn as_str(self) -> &'static str {`
- `fn` `codex-rs/tui/src/render/highlight.rs:52` `fn style(self) -> Style {`
- `static` `codex-rs/tui/src/render/highlight.rs:60` `static HIGHLIGHT_CONFIG: OnceLock<HighlightConfiguration> = OnceLock::new();`
- `fn` `codex-rs/tui/src/render/highlight.rs:62` `fn highlight_names() -> &'static [&'static str] {`
- `static` `codex-rs/tui/src/render/highlight.rs:63` `static NAMES: OnceLock<[&'static str; BashHighlight::ALL.len()]> = OnceLock::new();`
- `fn` `codex-rs/tui/src/render/highlight.rs:69` `fn highlight_config() -> &'static HighlightConfiguration {`
- `fn` `codex-rs/tui/src/render/highlight.rs:86` `fn highlight_for(highlight: Highlight) -> BashHighlight {`
- `fn` `codex-rs/tui/src/render/highlight.rs:90` `fn push_segment(lines: &mut Vec<Line<'static>>, segment: &str, style: Option<Style>) {`
- `use` `codex-rs/tui/src/render/highlight.rs:148` `use super::*;`
- `use` `codex-rs/tui/src/render/highlight.rs:149` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/tui/src/render/highlight.rs:150` `use ratatui::style::Modifier;`
- `fn` `codex-rs/tui/src/render/highlight.rs:152` `fn reconstructed(lines: &[Line<'static>]) -> String {`
- `fn` `codex-rs/tui/src/render/highlight.rs:165` `fn dimmed_tokens(lines: &[Line<'static>]) -> Vec<String> {`
- `fn` `codex-rs/tui/src/render/highlight.rs:177` `fn dims_expected_bash_operators() {`
- `fn` `codex-rs/tui/src/render/highlight.rs:189` `fn dims_redirects_and_strings() {`
- `fn` `codex-rs/tui/src/render/highlight.rs:201` `fn highlights_command_and_strings() {`
- `fn` `codex-rs/tui/src/render/highlight.rs:223` `fn highlights_heredoc_body_as_string() {`

## Dependencies (auto sample)
### Imports / Includes
- `use ratatui::style::Style;`
- `use ratatui::style::Stylize;`
- `use ratatui::text::Line;`
- `use ratatui::text::Span;`
- `use std::sync::OnceLock;`
- `use tree_sitter_highlight::Highlight;`
- `use tree_sitter_highlight::HighlightConfiguration;`
- `use tree_sitter_highlight::HighlightEvent;`
- `use tree_sitter_highlight::Highlighter;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use ratatui::style::Modifier;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/06_UI/TUI.md`
