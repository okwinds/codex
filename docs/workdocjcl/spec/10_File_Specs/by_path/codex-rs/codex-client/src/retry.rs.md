# `codex-rs/codex-client/src/retry.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2054`
- sha256: `3e40f4eaa166bd39dd69842ef0abe48b46cab7b5acbfa99a6d1903d03f73b9dd`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/retry.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RetryPolicy {`
- `pub struct RetryOn {`
- `pub fn should_retry(&self, err: &TransportError, attempt: u64, max_attempts: u64) -> bool {`
- `pub fn backoff(base: Duration, attempt: u64) -> Duration {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-client/src/retry.rs:1` `use crate::error::TransportError;`
- `use` `codex-rs/codex-client/src/retry.rs:2` `use crate::request::Request;`
- `use` `codex-rs/codex-client/src/retry.rs:3` `use rand::Rng;`
- `use` `codex-rs/codex-client/src/retry.rs:4` `use std::future::Future;`
- `use` `codex-rs/codex-client/src/retry.rs:5` `use std::time::Duration;`
- `use` `codex-rs/codex-client/src/retry.rs:6` `use tokio::time::sleep;`
- `struct` `codex-rs/codex-client/src/retry.rs:9` `pub struct RetryPolicy {`
- `struct` `codex-rs/codex-client/src/retry.rs:16` `pub struct RetryOn {`
- `impl` `codex-rs/codex-client/src/retry.rs:22` `impl RetryOn {`
- `fn` `codex-rs/codex-client/src/retry.rs:23` `pub fn should_retry(&self, err: &TransportError, attempt: u64, max_attempts: u64) -> bool {`
- `fn` `codex-rs/codex-client/src/retry.rs:38` `pub fn backoff(base: Duration, attempt: u64) -> Duration {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::TransportError;`
- `use crate::request::Request;`
- `use rand::Rng;`
- `use std::future::Future;`
- `use std::time::Duration;`
- `use tokio::time::sleep;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
