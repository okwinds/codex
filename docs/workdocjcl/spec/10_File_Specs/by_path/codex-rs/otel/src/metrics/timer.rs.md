# `codex-rs/otel/src/metrics/timer.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1169`
- sha256: `0ae1e2251e7b6bd18183cbddb88cdf40dcb225dd40ffa2576ebf14b8923c338e`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/metrics/timer.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Timer {`
- `pub fn record(&self, additional_tags: &[(&str, &str)]) -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/metrics/timer.rs:1` `use crate::metrics::MetricsClient;`
- `use` `codex-rs/otel/src/metrics/timer.rs:2` `use crate::metrics::error::Result;`
- `use` `codex-rs/otel/src/metrics/timer.rs:3` `use std::time::Instant;`
- `struct` `codex-rs/otel/src/metrics/timer.rs:6` `pub struct Timer {`
- `impl` `codex-rs/otel/src/metrics/timer.rs:13` `impl Drop for Timer {`
- `fn` `codex-rs/otel/src/metrics/timer.rs:14` `fn drop(&mut self) {`
- `impl` `codex-rs/otel/src/metrics/timer.rs:21` `impl Timer {`
- `fn` `codex-rs/otel/src/metrics/timer.rs:34` `pub fn record(&self, additional_tags: &[(&str, &str)]) -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::metrics::MetricsClient;`
- `use crate::metrics::error::Result;`
- `use std::time::Instant;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
