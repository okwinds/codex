# `codex-rs/otel/src/metrics/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `637`
- sha256: `877dc19b2fa431152420e75e3efa0a611ecb11c62323ea3fa3ca14f416eb6437`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/metrics/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn global() -> Option<MetricsClient> {`

## Definitions (auto, per-file)
- `mod` `codex-rs/otel/src/metrics/mod.rs:1` `mod client;`
- `mod` `codex-rs/otel/src/metrics/mod.rs:2` `mod config;`
- `mod` `codex-rs/otel/src/metrics/mod.rs:3` `mod error;`
- `use` `codex-rs/otel/src/metrics/mod.rs:14` `use std::sync::OnceLock;`
- `static` `codex-rs/otel/src/metrics/mod.rs:16` `static GLOBAL_METRICS: OnceLock<MetricsClient> = OnceLock::new();`
- `fn` `codex-rs/otel/src/metrics/mod.rs:22` `pub fn global() -> Option<MetricsClient> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::OnceLock;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
