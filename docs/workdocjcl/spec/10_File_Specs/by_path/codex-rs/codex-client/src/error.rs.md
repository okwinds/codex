# `codex-rs/codex-client/src/error.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `646`
- sha256: `5a17dcd0fdd8b6ec8eb2e45e5818c0195af03a868de4954ccfe5b80c6f675403`
- generated_utc: `2026-02-08T10:45:22Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/error.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum TransportError {`
- `pub enum StreamError {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-client/src/error.rs:1` `use http::HeaderMap;`
- `use` `codex-rs/codex-client/src/error.rs:2` `use http::StatusCode;`
- `use` `codex-rs/codex-client/src/error.rs:3` `use thiserror::Error;`
- `enum` `codex-rs/codex-client/src/error.rs:6` `pub enum TransportError {`
- `enum` `codex-rs/codex-client/src/error.rs:25` `pub enum StreamError {`

## Dependencies (auto sample)
### Imports / Includes
- `use http::HeaderMap;`
- `use http::StatusCode;`
- `use thiserror::Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
