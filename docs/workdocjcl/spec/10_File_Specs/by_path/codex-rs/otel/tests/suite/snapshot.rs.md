# `codex-rs/otel/tests/suite/snapshot.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3974`
- sha256: `fde36c9dc53025d5bd301c8076bc78eba160ba43dde6787dbd4f50f82b0e48f8`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `use codex_app_server_protocol::AuthMode;`
- `use codex_otel::OtelManager;`
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
