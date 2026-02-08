# `codex-rs/utils/string/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2141`
- sha256: `15d816d2e0b20b605b93ba43c4b0dcd5c09cd93f78336b3cef283770f6d88d26`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/utils/string/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn take_bytes_at_char_boundary(s: &str, maxb: usize) -> &str {`
- `pub fn take_last_bytes_at_char_boundary(s: &str, maxb: usize) -> &str {`
- `pub fn sanitize_metric_tag_value(value: &str) -> String {`

## Definitions (auto, per-file)
- `fn` `codex-rs/utils/string/src/lib.rs:3` `pub fn take_bytes_at_char_boundary(s: &str, maxb: usize) -> &str {`
- `fn` `codex-rs/utils/string/src/lib.rs:20` `pub fn take_last_bytes_at_char_boundary(s: &str, maxb: usize) -> &str {`
- `fn` `codex-rs/utils/string/src/lib.rs:42` `pub fn sanitize_metric_tag_value(value: &str) -> String {`
- `const` `codex-rs/utils/string/src/lib.rs:43` `const MAX_LEN: usize = 256;`
- `use` `codex-rs/utils/string/src/lib.rs:67` `use super::sanitize_metric_tag_value;`
- `use` `codex-rs/utils/string/src/lib.rs:68` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/utils/string/src/lib.rs:71` `fn sanitize_metric_tag_value_trims_and_fills_unspecified() {`
- `fn` `codex-rs/utils/string/src/lib.rs:77` `fn sanitize_metric_tag_value_replaces_invalid_chars() {`

## Dependencies (auto sample)
### Imports / Includes
- `use super::sanitize_metric_tag_value;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
