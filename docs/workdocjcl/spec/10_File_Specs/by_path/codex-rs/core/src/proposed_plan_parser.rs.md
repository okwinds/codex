# `codex-rs/core/src/proposed_plan_parser.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5743`
- sha256: `db38f9dfc63a5ef0c1a77825b7612e5223585eedda889460b03d97a78f42899f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/proposed_plan_parser.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/proposed_plan_parser.rs:1` `use crate::tagged_block_parser::TagSpec;`
- `use` `codex-rs/core/src/proposed_plan_parser.rs:2` `use crate::tagged_block_parser::TaggedLineParser;`
- `use` `codex-rs/core/src/proposed_plan_parser.rs:3` `use crate::tagged_block_parser::TaggedLineSegment;`
- `const` `codex-rs/core/src/proposed_plan_parser.rs:5` `const OPEN_TAG: &str = "<proposed_plan>";`
- `const` `codex-rs/core/src/proposed_plan_parser.rs:6` `const CLOSE_TAG: &str = "</proposed_plan>";`
- `enum` `codex-rs/core/src/proposed_plan_parser.rs:9` `enum PlanTag {`
- `impl` `codex-rs/core/src/proposed_plan_parser.rs:30` `impl ProposedPlanParser {`
- `fn` `codex-rs/core/src/proposed_plan_parser.rs:58` `fn map_plan_segment(segment: TaggedLineSegment<PlanTag>) -> ProposedPlanSegment {`
- `use` `codex-rs/core/src/proposed_plan_parser.rs:103` `use super::ProposedPlanParser;`
- `use` `codex-rs/core/src/proposed_plan_parser.rs:104` `use super::ProposedPlanSegment;`
- `use` `codex-rs/core/src/proposed_plan_parser.rs:105` `use super::strip_proposed_plan_blocks;`
- `use` `codex-rs/core/src/proposed_plan_parser.rs:106` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/proposed_plan_parser.rs:109` `fn streams_proposed_plan_segments() {`
- `fn` `codex-rs/core/src/proposed_plan_parser.rs:135` `fn preserves_non_tag_lines() {`
- `fn` `codex-rs/core/src/proposed_plan_parser.rs:149` `fn closes_unterminated_plan_block_on_finish() {`
- `fn` `codex-rs/core/src/proposed_plan_parser.rs:165` `fn closes_tag_line_without_trailing_newline() {`
- `fn` `codex-rs/core/src/proposed_plan_parser.rs:181` `fn strips_proposed_plan_blocks_from_text() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::tagged_block_parser::TagSpec;`
- `use crate::tagged_block_parser::TaggedLineParser;`
- `use crate::tagged_block_parser::TaggedLineSegment;`
- `use super::ProposedPlanParser;`
- `use super::ProposedPlanSegment;`
- `use super::strip_proposed_plan_blocks;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
