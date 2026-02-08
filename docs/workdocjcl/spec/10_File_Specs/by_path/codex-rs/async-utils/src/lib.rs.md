# `codex-rs/async-utils/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2044`
- sha256: `30398fd33b4954a6036b575e6d7c08ca73d93ce2601f7e14a3a8fc6b56ba65ea`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/async-utils/src/lib.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub enum CancelErr {`
- `pub trait OrCancelExt: Sized {`

## Definitions (auto, per-file)
- `use` `codex-rs/async-utils/src/lib.rs:1` `use async_trait::async_trait;`
- `use` `codex-rs/async-utils/src/lib.rs:2` `use std::future::Future;`
- `use` `codex-rs/async-utils/src/lib.rs:3` `use tokio_util::sync::CancellationToken;`
- `enum` `codex-rs/async-utils/src/lib.rs:6` `pub enum CancelErr {`
- `trait` `codex-rs/async-utils/src/lib.rs:11` `pub trait OrCancelExt: Sized {`
- `type` `codex-rs/async-utils/src/lib.rs:12` `type Output;`
- `fn` `codex-rs/async-utils/src/lib.rs:14` `async fn or_cancel(self, token: &CancellationToken) -> Result<Self::Output, CancelErr>;`
- `type` `codex-rs/async-utils/src/lib.rs:23` `type Output = F::Output;`
- `fn` `codex-rs/async-utils/src/lib.rs:25` `async fn or_cancel(self, token: &CancellationToken) -> Result<Self::Output, CancelErr> {`
- `use` `codex-rs/async-utils/src/lib.rs:35` `use super::*;`
- `use` `codex-rs/async-utils/src/lib.rs:36` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/async-utils/src/lib.rs:37` `use std::time::Duration;`
- `use` `codex-rs/async-utils/src/lib.rs:38` `use tokio::task;`
- `use` `codex-rs/async-utils/src/lib.rs:39` `use tokio::time::sleep;`
- `fn` `codex-rs/async-utils/src/lib.rs:42` `async fn returns_ok_when_future_completes_first() {`
- `fn` `codex-rs/async-utils/src/lib.rs:52` `async fn returns_err_when_token_cancelled_first() {`
- `fn` `codex-rs/async-utils/src/lib.rs:73` `async fn returns_err_when_token_already_cancelled() {`

## Dependencies (auto sample)
### Imports / Includes
- `use async_trait::async_trait;`
- `use std::future::Future;`
- `use tokio_util::sync::CancellationToken;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use std::time::Duration;`
- `use tokio::task;`
- `use tokio::time::sleep;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
