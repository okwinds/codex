# `codex-rs/tui/src/streaming/chunking.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15790`
- sha256: `02f3c37f71e460f2a779663337646cb51829dbea4b0707caadaaaef8452e3cb1`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/streaming/chunking.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/streaming/chunking.rs:79` `use std::time::Duration;`
- `use` `codex-rs/tui/src/streaming/chunking.rs:80` `use std::time::Instant;`
- `const` `codex-rs/tui/src/streaming/chunking.rs:85` `const ENTER_QUEUE_DEPTH_LINES: usize = 8;`
- `const` `codex-rs/tui/src/streaming/chunking.rs:90` `const ENTER_OLDEST_AGE: Duration = Duration::from_millis(120);`
- `const` `codex-rs/tui/src/streaming/chunking.rs:95` `const EXIT_QUEUE_DEPTH_LINES: usize = 2;`
- `const` `codex-rs/tui/src/streaming/chunking.rs:100` `const EXIT_OLDEST_AGE: Duration = Duration::from_millis(40);`
- `const` `codex-rs/tui/src/streaming/chunking.rs:103` `const EXIT_HOLD: Duration = Duration::from_millis(250);`
- `const` `codex-rs/tui/src/streaming/chunking.rs:108` `const REENTER_CATCH_UP_HOLD: Duration = Duration::from_millis(250);`
- `const` `codex-rs/tui/src/streaming/chunking.rs:113` `const SEVERE_QUEUE_DEPTH_LINES: usize = 64;`
- `const` `codex-rs/tui/src/streaming/chunking.rs:116` `const SEVERE_OLDEST_AGE: Duration = Duration::from_millis(300);`
- `impl` `codex-rs/tui/src/streaming/chunking.rs:163` `impl AdaptiveChunkingPolicy {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:216` `fn maybe_enter_catch_up(&mut self, snapshot: QueueSnapshot, now: Instant) -> bool {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:233` `fn maybe_exit_catch_up(&mut self, snapshot: QueueSnapshot, now: Instant) {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:252` `fn note_catch_up_exit(&mut self, now: Instant) {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:258` `fn reentry_hold_active(&self, now: Instant) -> bool {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:267` `fn should_enter_catch_up(snapshot: QueueSnapshot) -> bool {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:278` `fn should_exit_catch_up(snapshot: QueueSnapshot) -> bool {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:289` `fn is_severe_backlog(snapshot: QueueSnapshot) -> bool {`
- `use` `codex-rs/tui/src/streaming/chunking.rs:298` `use super::*;`
- `use` `codex-rs/tui/src/streaming/chunking.rs:299` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:301` `fn snapshot(queued_lines: usize, oldest_age_ms: u64) -> QueueSnapshot {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:309` `fn smooth_mode_is_default() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:320` `fn enters_catch_up_on_depth_threshold() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:331` `fn enters_catch_up_on_age_threshold() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:342` `fn severe_backlog_uses_faster_paced_batches() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:353` `fn catch_up_batch_drains_current_backlog() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:362` `fn exits_catch_up_after_hysteresis_hold() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:378` `fn drops_back_to_smooth_when_idle() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:396` `fn holds_reentry_after_catch_up_exit() {`
- `fn` `codex-rs/tui/src/streaming/chunking.rs:422` `fn severe_backlog_can_reenter_during_hold() {`

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
