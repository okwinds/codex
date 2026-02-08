# `codex-rs/core/src/tagged_block_parser.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9986`
- sha256: `3a0a584013be99c5e4aa3b47d2f2f9d36514a2a2e9a7ffefee23460cc9d17c5d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tagged_block_parser.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `fn` `codex-rs/core/src/tagged_block_parser.rs:129` `fn finish_line(&mut self, segments: &mut Vec<TaggedLineSegment<T>>) {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:156` `fn push_text(&self, text: String, segments: &mut Vec<TaggedLineSegment<T>>) {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:164` `fn is_tag_prefix(&self, slug: &str) -> bool {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:171` `fn match_open(&self, slug: &str) -> Option<T> {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:178` `fn match_close(&self, slug: &str) -> Option<T> {`
- `use` `codex-rs/core/src/tagged_block_parser.rs:224` `use super::TagSpec;`
- `use` `codex-rs/core/src/tagged_block_parser.rs:225` `use super::TaggedLineParser;`
- `use` `codex-rs/core/src/tagged_block_parser.rs:226` `use super::TaggedLineSegment;`
- `use` `codex-rs/core/src/tagged_block_parser.rs:227` `use pretty_assertions::assert_eq;`
- `enum` `codex-rs/core/src/tagged_block_parser.rs:230` `enum Tag {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:234` `fn parser() -> TaggedLineParser<Tag> {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:243` `fn buffers_prefix_until_tag_is_decided() {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:260` `fn rejects_tag_lines_with_extra_text() {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:272` `fn closes_unterminated_tag_on_finish() {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:288` `fn accepts_tags_with_trailing_whitespace() {`
- `fn` `codex-rs/core/src/tagged_block_parser.rs:304` `fn passes_through_plain_text() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::TagSpec;`
- `use super::TaggedLineParser;`
- `use super::TaggedLineSegment;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
