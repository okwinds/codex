# `codex-rs/otel/tests/harness/mod.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2707`
- sha256: `14597aed8edee486bb174b9559c193534e04bb6c282f54bb8adac94ae605dc22`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/tests/harness/mod.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_otel::metrics::MetricsClient;`
- `use codex_otel::metrics::MetricsConfig;`
- `use codex_otel::metrics::Result;`
- `use opentelemetry::KeyValue;`
- `use opentelemetry_sdk::metrics::InMemoryMetricExporter;`
- `use opentelemetry_sdk::metrics::data::AggregatedMetrics;`
- `use opentelemetry_sdk::metrics::data::Metric;`
- `use opentelemetry_sdk::metrics::data::MetricData;`
- `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
- `use std::collections::BTreeMap;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
