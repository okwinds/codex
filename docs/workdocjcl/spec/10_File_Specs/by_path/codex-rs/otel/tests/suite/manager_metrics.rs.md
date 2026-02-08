# `codex-rs/otel/tests/suite/manager_metrics.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3598`
- sha256: `c1a660fecbdee5bac152320b4ee72ba4270b7a509646a2a029eca8c7235b6311`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `use codex_app_server_protocol::AuthMode;`
- `use codex_otel::OtelManager;`
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
