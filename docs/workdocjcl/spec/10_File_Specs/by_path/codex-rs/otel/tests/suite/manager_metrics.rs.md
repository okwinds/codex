# `codex-rs/otel/tests/suite/manager_metrics.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3732`
- sha256: `0de2f935dfb4fc11185fe61e6ae3eac9562bc92fa4da5c11d81ffaeb26056dc0`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/tests/suite/manager_metrics.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use crate::harness::attributes_to_map;`
- `use crate::harness::build_metrics_with_defaults;`
- `use crate::harness::find_metric;`
- `use crate::harness::latest_metrics;`
- `use codex_otel::OtelManager;`
- `use codex_otel::TelemetryAuthMode;`
- `use codex_otel::metrics::Result;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::SessionSource;`
- `use opentelemetry_sdk::metrics::data::AggregatedMetrics;`
- `use opentelemetry_sdk::metrics::data::MetricData;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::BTreeMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
