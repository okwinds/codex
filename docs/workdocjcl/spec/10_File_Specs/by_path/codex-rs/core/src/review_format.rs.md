# `codex-rs/core/src/review_format.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2827`
- sha256: `bc4c21f0f919fea097f2b005cdb5e81e1cda1a640e8427b63c15d19b46654e66`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/review_format.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn format_review_findings_block(`
- `pub fn render_review_output_text(output: &ReviewOutputEvent) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/review_format.rs:1` `use crate::protocol::ReviewFinding;`
- `use` `codex-rs/core/src/review_format.rs:2` `use crate::protocol::ReviewOutputEvent;`
- `fn` `codex-rs/core/src/review_format.rs:7` `fn format_location(item: &ReviewFinding) -> String {`
- `const` `codex-rs/core/src/review_format.rs:14` `const REVIEW_FALLBACK_MESSAGE: &str = "Reviewer failed to output a response.";`
- `fn` `codex-rs/core/src/review_format.rs:23` `pub fn format_review_findings_block(`
- `fn` `codex-rs/core/src/review_format.rs:64` `pub fn render_review_output_text(output: &ReviewOutputEvent) -> String {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::protocol::ReviewFinding;`
- `use crate::protocol::ReviewOutputEvent;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
