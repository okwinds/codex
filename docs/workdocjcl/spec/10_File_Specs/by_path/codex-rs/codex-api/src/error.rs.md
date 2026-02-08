# `codex-rs/codex-api/src/error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `974`
- sha256: `e8520cb868d9229e0bd9c64e93d03beafd46a08e82993e90ee84e052ee644604`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/error.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ApiError {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/error.rs:1` `use crate::rate_limits::RateLimitError;`
- `use` `codex-rs/codex-api/src/error.rs:2` `use codex_client::TransportError;`
- `use` `codex-rs/codex-api/src/error.rs:3` `use http::StatusCode;`
- `use` `codex-rs/codex-api/src/error.rs:4` `use std::time::Duration;`
- `use` `codex-rs/codex-api/src/error.rs:5` `use thiserror::Error;`
- `enum` `codex-rs/codex-api/src/error.rs:8` `pub enum ApiError {`
- `impl` `codex-rs/codex-api/src/error.rs:32` `impl From<RateLimitError> for ApiError {`
- `fn` `codex-rs/codex-api/src/error.rs:33` `fn from(err: RateLimitError) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::rate_limits::RateLimitError;`
- `use codex_client::TransportError;`
- `use http::StatusCode;`
- `use std::time::Duration;`
- `use thiserror::Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
