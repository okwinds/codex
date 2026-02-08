# `codex-rs/tui/src/tui/frame_rate_limiter.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2120`
- sha256: `67f461e4070265b1f7e7fc699f211beb4844f43ffda2eb38f41bd536a13a4ef6`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/tui/frame_rate_limiter.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/tui/frame_rate_limiter.rs:9` `use std::time::Duration;`
- `use` `codex-rs/tui/src/tui/frame_rate_limiter.rs:10` `use std::time::Instant;`
- `impl` `codex-rs/tui/src/tui/frame_rate_limiter.rs:21` `impl FrameRateLimiter {`
- `use` `codex-rs/tui/src/tui/frame_rate_limiter.rs:41` `use super::*;`
- `use` `codex-rs/tui/src/tui/frame_rate_limiter.rs:42` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/tui/frame_rate_limiter.rs:45` `fn default_does_not_clamp() {`
- `fn` `codex-rs/tui/src/tui/frame_rate_limiter.rs:52` `fn clamps_to_min_interval_since_last_emit() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
