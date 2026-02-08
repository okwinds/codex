# `codex-rs/tui/src/tui/frame_requester.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14112`
- sha256: `629599433594ebaf4dd1037efa31198686879833e2f8816478bd388c49080174`
- generated_utc: `2026-02-08T10:45:41Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/tui/frame_requester.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct FrameRequester {`
- `pub fn new(draw_tx: broadcast::Sender<()>) -> Self {`
- `pub fn schedule_frame(&self) {`
- `pub fn schedule_frame_in(&self, dur: Duration) {`

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/tui/frame_requester.rs:15` `use std::time::Duration;`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:16` `use std::time::Instant;`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:18` `use tokio::sync::broadcast;`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:19` `use tokio::sync::mpsc;`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:21` `use super::frame_rate_limiter::FrameRateLimiter;`
- `struct` `codex-rs/tui/src/tui/frame_requester.rs:31` `pub struct FrameRequester {`
- `impl` `codex-rs/tui/src/tui/frame_requester.rs:35` `impl FrameRequester {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:39` `pub fn new(draw_tx: broadcast::Sender<()>) -> Self {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:49` `pub fn schedule_frame(&self) {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:54` `pub fn schedule_frame_in(&self, dur: Duration) {`
- `impl` `codex-rs/tui/src/tui/frame_requester.rs:60` `impl FrameRequester {`
- `struct` `codex-rs/tui/src/tui/frame_requester.rs:76` `struct FrameScheduler {`
- `impl` `codex-rs/tui/src/tui/frame_requester.rs:82` `impl FrameScheduler {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:84` `fn new(receiver: mpsc::UnboundedReceiver<Instant>, draw_tx: broadcast::Sender<()>) -> Self {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:96` `async fn run(mut self) {`
- `const` `codex-rs/tui/src/tui/frame_requester.rs:97` `const ONE_YEAR: Duration = Duration::from_secs(60 * 60 * 24 * 365);`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:131` `use super::super::frame_rate_limiter::MIN_FRAME_INTERVAL;`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:132` `use super::*;`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:133` `use tokio::time;`
- `use` `codex-rs/tui/src/tui/frame_requester.rs:134` `use tokio_util::time::FutureExt;`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:137` `async fn test_schedule_frame_immediate_triggers_once() {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:160` `async fn test_schedule_frame_in_triggers_at_delay() {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:186` `async fn test_coalesces_multiple_requests_into_single_draw() {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:212` `async fn test_coalesces_mixed_immediate_and_delayed_requests() {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:235` `async fn test_limits_draw_notifications_to_120fps() {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:266` `async fn test_rate_limit_clamps_early_delayed_requests() {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:298` `async fn test_rate_limit_does_not_delay_future_draws() {`
- `fn` `codex-rs/tui/src/tui/frame_requester.rs:327` `async fn test_multiple_delayed_requests_coalesce_to_earliest() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use tokio::sync::broadcast;`
- `use tokio::sync::mpsc;`
- `use super::frame_rate_limiter::FrameRateLimiter;`
- `use super::super::frame_rate_limiter::MIN_FRAME_INTERVAL;`
- `use super::*;`
- `use tokio::time;`
- `use tokio_util::time::FutureExt;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
