# `codex-rs/tui/src/streaming/commit_tick.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8290`
- sha256: `6438cb1033a47d6676e528e50d019fca8407669097d732304c2cb53bb26b0655`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/streaming/commit_tick.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:16` `use std::time::Duration;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:17` `use std::time::Instant;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:19` `use crate::history_cell::HistoryCell;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:21` `use super::chunking::AdaptiveChunkingPolicy;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:22` `use super::chunking::ChunkingDecision;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:23` `use super::chunking::ChunkingMode;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:24` `use super::chunking::DrainPlan;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:25` `use super::chunking::QueueSnapshot;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:26` `use super::controller::PlanStreamController;`
- `use` `codex-rs/tui/src/streaming/commit_tick.rs:27` `use super::controller::StreamController;`
- `impl` `codex-rs/tui/src/streaming/commit_tick.rs:48` `impl Default for CommitTickOutput {`
- `fn` `codex-rs/tui/src/streaming/commit_tick.rs:53` `fn default() -> Self {`
- `fn` `codex-rs/tui/src/streaming/commit_tick.rs:107` `fn stream_queue_snapshot(`
- `fn` `codex-rs/tui/src/streaming/commit_tick.rs:134` `fn resolve_chunking_plan(`
- `fn` `codex-rs/tui/src/streaming/commit_tick.rs:158` `fn apply_commit_tick_plan(`
- `fn` `codex-rs/tui/src/streaming/commit_tick.rs:190` `fn drain_stream_controller(`
- `fn` `codex-rs/tui/src/streaming/commit_tick.rs:204` `fn drain_plan_stream_controller(`
- `fn` `codex-rs/tui/src/streaming/commit_tick.rs:217` `fn max_duration(lhs: Option<Duration>, rhs: Option<Duration>) -> Option<Duration> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use crate::history_cell::HistoryCell;`
- `use super::chunking::AdaptiveChunkingPolicy;`
- `use super::chunking::ChunkingDecision;`
- `use super::chunking::ChunkingMode;`
- `use super::chunking::DrainPlan;`
- `use super::chunking::QueueSnapshot;`
- `use super::controller::PlanStreamController;`
- `use super::controller::StreamController;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
