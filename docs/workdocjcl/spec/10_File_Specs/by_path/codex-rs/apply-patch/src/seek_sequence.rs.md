# `codex-rs/apply-patch/src/seek_sequence.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5651`
- sha256: `2f51a6be92aa953761b3f982d5d11c0e75ce8b4a5771bcbfb227f420c271f43d`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/apply-patch/src/seek_sequence.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `fn` `codex-rs/apply-patch/src/seek_sequence.rs:76` `fn normalise(s: &str) -> String {`
- `use` `codex-rs/apply-patch/src/seek_sequence.rs:114` `use super::seek_sequence;`
- `use` `codex-rs/apply-patch/src/seek_sequence.rs:115` `use std::string::ToString;`
- `fn` `codex-rs/apply-patch/src/seek_sequence.rs:117` `fn to_vec(strings: &[&str]) -> Vec<String> {`
- `fn` `codex-rs/apply-patch/src/seek_sequence.rs:122` `fn test_exact_match_finds_sequence() {`
- `fn` `codex-rs/apply-patch/src/seek_sequence.rs:129` `fn test_rstrip_match_ignores_trailing_whitespace() {`
- `fn` `codex-rs/apply-patch/src/seek_sequence.rs:137` `fn test_trim_match_ignores_leading_and_trailing_whitespace() {`
- `fn` `codex-rs/apply-patch/src/seek_sequence.rs:145` `fn test_pattern_longer_than_input_returns_none() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::seek_sequence;`
- `use std::string::ToString;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
