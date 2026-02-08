# `codex-rs/common/src/elapsed.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2453`
- sha256: `d616006643dc9e322dda1589f9a3e9ccd4fdd49478352a5f0e637ef14d93d1d4`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/elapsed.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn format_elapsed(start_time: Instant) -> String {`
- `pub fn format_duration(duration: Duration) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/elapsed.rs:1` `use std::time::Duration;`
- `use` `codex-rs/common/src/elapsed.rs:2` `use std::time::Instant;`
- `fn` `codex-rs/common/src/elapsed.rs:6` `pub fn format_elapsed(start_time: Instant) -> String {`
- `fn` `codex-rs/common/src/elapsed.rs:16` `pub fn format_duration(duration: Duration) -> String {`
- `fn` `codex-rs/common/src/elapsed.rs:21` `fn format_elapsed_millis(millis: i64) -> String {`
- `use` `codex-rs/common/src/elapsed.rs:35` `use super::*;`
- `fn` `codex-rs/common/src/elapsed.rs:38` `fn test_format_duration_subsecond() {`
- `fn` `codex-rs/common/src/elapsed.rs:49` `fn test_format_duration_seconds() {`
- `fn` `codex-rs/common/src/elapsed.rs:61` `fn test_format_duration_minutes() {`
- `fn` `codex-rs/common/src/elapsed.rs:74` `fn test_format_duration_one_hour_has_space() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
