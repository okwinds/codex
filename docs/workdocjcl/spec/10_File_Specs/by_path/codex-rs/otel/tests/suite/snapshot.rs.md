# `codex-rs/otel/tests/suite/snapshot.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4060`
- sha256: `41a071f1ab408358b63ee5e8b1b3dbd5eca1e1ac78c55eede1156b6a8f7a2e56`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/tests/suite/snapshot.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use crate::harness::attributes_to_map;`
- `use crate::harness::find_metric;`
- `use codex_otel::OtelManager;`
- `use codex_otel::TelemetryAuthMode;`
- `use codex_otel::metrics::MetricsClient;`
- `use codex_otel::metrics::MetricsConfig;`
- `use codex_otel::metrics::Result;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::SessionSource;`
- `use opentelemetry_sdk::metrics::InMemoryMetricExporter;`
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
