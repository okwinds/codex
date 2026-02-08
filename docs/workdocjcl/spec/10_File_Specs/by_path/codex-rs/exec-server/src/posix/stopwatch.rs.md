# `codex-rs/exec-server/src/posix/stopwatch.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6185`
- sha256: `dc03554643adc59879d17972723c3bccd8f7911bd7b033cc5effe67e137aabea`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/stopwatch.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:1` `use std::future::Future;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:3` `use std::time::Duration;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:4` `use std::time::Instant;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:6` `use tokio::sync::Mutex;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:7` `use tokio::sync::Notify;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:8` `use tokio_util::sync::CancellationToken;`
- `struct` `codex-rs/exec-server/src/posix/stopwatch.rs:18` `struct StopwatchState {`
- `impl` `codex-rs/exec-server/src/posix/stopwatch.rs:24` `impl Stopwatch {`
- `fn` `codex-rs/exec-server/src/posix/stopwatch.rs:93` `async fn pause(&self) {`
- `fn` `codex-rs/exec-server/src/posix/stopwatch.rs:104` `async fn resume(&self) {`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:119` `use super::Stopwatch;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:120` `use tokio::time::Duration;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:121` `use tokio::time::Instant;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:122` `use tokio::time::sleep;`
- `use` `codex-rs/exec-server/src/posix/stopwatch.rs:123` `use tokio::time::timeout;`
- `fn` `codex-rs/exec-server/src/posix/stopwatch.rs:126` `async fn cancellation_receiver_fires_after_limit() {`
- `fn` `codex-rs/exec-server/src/posix/stopwatch.rs:135` `async fn pause_prevents_timeout_until_resumed() {`
- `fn` `codex-rs/exec-server/src/posix/stopwatch.rs:162` `async fn overlapping_pauses_only_resume_once() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::future::Future;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use tokio::sync::Mutex;`
- `use tokio::sync::Notify;`
- `use tokio_util::sync::CancellationToken;`
- `use super::Stopwatch;`
- `use tokio::time::Duration;`
- `use tokio::time::Instant;`
- `use tokio::time::sleep;`
- `use tokio::time::timeout;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
