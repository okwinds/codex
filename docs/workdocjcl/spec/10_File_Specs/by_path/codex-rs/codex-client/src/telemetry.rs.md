# `codex-rs/codex-client/src/telemetry.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `321`
- sha256: `f08020bb4d86bc224227b8b1a2f62f3a846fad7003dbdf782a027e72e9bfbee1`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/telemetry.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub trait RequestTelemetry: Send + Sync {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-client/src/telemetry.rs:1` `use crate::error::TransportError;`
- `use` `codex-rs/codex-client/src/telemetry.rs:2` `use http::StatusCode;`
- `use` `codex-rs/codex-client/src/telemetry.rs:3` `use std::time::Duration;`
- `trait` `codex-rs/codex-client/src/telemetry.rs:6` `pub trait RequestTelemetry: Send + Sync {`
- `fn` `codex-rs/codex-client/src/telemetry.rs:7` `fn on_request(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::error::TransportError;`
- `use http::StatusCode;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
