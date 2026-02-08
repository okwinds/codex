# `codex-rs/otel/src/metrics/config.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2645`
- sha256: `314a220130020e571240f14f5bacb5d80affb669285229dca6538d76c8a1ea24`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/metrics/config.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum MetricsExporter {`
- `pub struct MetricsConfig {`
- `pub fn otlp(`
- `pub fn in_memory(`
- `pub fn with_export_interval(mut self, interval: Duration) -> Self {`
- `pub fn with_runtime_reader(mut self) -> Self {`
- `pub fn with_tag(mut self, key: impl Into<String>, value: impl Into<String>) -> Result<Self> {`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/metrics/config.rs:1` `use crate::config::OtelExporter;`
- `use` `codex-rs/otel/src/metrics/config.rs:2` `use crate::metrics::Result;`
- `use` `codex-rs/otel/src/metrics/config.rs:3` `use crate::metrics::validation::validate_tag_key;`
- `use` `codex-rs/otel/src/metrics/config.rs:4` `use crate::metrics::validation::validate_tag_value;`
- `use` `codex-rs/otel/src/metrics/config.rs:5` `use opentelemetry_sdk::metrics::InMemoryMetricExporter;`
- `use` `codex-rs/otel/src/metrics/config.rs:6` `use std::collections::BTreeMap;`
- `use` `codex-rs/otel/src/metrics/config.rs:7` `use std::time::Duration;`
- `enum` `codex-rs/otel/src/metrics/config.rs:10` `pub enum MetricsExporter {`
- `struct` `codex-rs/otel/src/metrics/config.rs:16` `pub struct MetricsConfig {`
- `impl` `codex-rs/otel/src/metrics/config.rs:26` `impl MetricsConfig {`
- `fn` `codex-rs/otel/src/metrics/config.rs:27` `pub fn otlp(`
- `fn` `codex-rs/otel/src/metrics/config.rs:45` `pub fn in_memory(`
- `fn` `codex-rs/otel/src/metrics/config.rs:63` `pub fn with_export_interval(mut self, interval: Duration) -> Self {`
- `fn` `codex-rs/otel/src/metrics/config.rs:69` `pub fn with_runtime_reader(mut self) -> Self {`
- `fn` `codex-rs/otel/src/metrics/config.rs:75` `pub fn with_tag(mut self, key: impl Into<String>, value: impl Into<String>) -> Result<Self> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::OtelExporter;`
- `use crate::metrics::Result;`
- `use crate::metrics::validation::validate_tag_key;`
- `use crate::metrics::validation::validate_tag_value;`
- `use opentelemetry_sdk::metrics::InMemoryMetricExporter;`
- `use std::collections::BTreeMap;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
