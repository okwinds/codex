# `codex-rs/common/src/fuzzy_match.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6208`
- sha256: `48691a7f8d4cc240a2129bcf0b7c8ca645d5518c80efc66ee6dd0362f8f810b6`
- generated_utc: `2026-02-08T10:45:25Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/fuzzy_match.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn fuzzy_match(haystack: &str, needle: &str) -> Option<(Vec<usize>, i32)> {`
- `pub fn fuzzy_indices(haystack: &str, needle: &str) -> Option<Vec<usize>> {`

## Definitions (auto, per-file)
- `fn` `codex-rs/common/src/fuzzy_match.rs:12` `pub fn fuzzy_match(haystack: &str, needle: &str) -> Option<(Vec<usize>, i32)> {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:72` `pub fn fuzzy_indices(haystack: &str, needle: &str) -> Option<Vec<usize>> {`
- `use` `codex-rs/common/src/fuzzy_match.rs:82` `use super::*;`
- `fn` `codex-rs/common/src/fuzzy_match.rs:85` `fn ascii_basic_indices() {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:96` `fn unicode_dotted_i_istanbul_highlighting() {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:107` `fn unicode_german_sharp_s_casefold() {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:112` `fn prefer_contiguous_match_over_spread() {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:129` `fn start_of_string_bonus_applies() {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:146` `fn empty_needle_matches_with_max_score_and_no_indices() {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:156` `fn case_insensitive_matching_basic() {`
- `fn` `codex-rs/common/src/fuzzy_match.rs:167` `fn indices_are_deduped_for_multichar_lowercase_expansion() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
