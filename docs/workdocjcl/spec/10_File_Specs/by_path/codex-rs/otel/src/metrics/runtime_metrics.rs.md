# `codex-rs/otel/src/metrics/runtime_metrics.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4220`
- sha256: `07fdb0939db956ec917ddfe5af79c8e25902ea7f72641d2d18d1b91874f47df3`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/metrics/runtime_metrics.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RuntimeMetricTotals {`
- `pub fn is_empty(self) -> bool {`
- `pub struct RuntimeMetricsSummary {`
- `pub fn is_empty(self) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:1` `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:2` `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:3` `use crate::metrics::names::SSE_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:4` `use crate::metrics::names::SSE_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:5` `use crate::metrics::names::TOOL_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:6` `use crate::metrics::names::TOOL_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:7` `use crate::metrics::names::WEBSOCKET_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:8` `use crate::metrics::names::WEBSOCKET_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:9` `use crate::metrics::names::WEBSOCKET_REQUEST_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:10` `use crate::metrics::names::WEBSOCKET_REQUEST_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:11` `use opentelemetry_sdk::metrics::data::AggregatedMetrics;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:12` `use opentelemetry_sdk::metrics::data::Metric;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:13` `use opentelemetry_sdk::metrics::data::MetricData;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:14` `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
- `struct` `codex-rs/otel/src/metrics/runtime_metrics.rs:17` `pub struct RuntimeMetricTotals {`
- `impl` `codex-rs/otel/src/metrics/runtime_metrics.rs:22` `impl RuntimeMetricTotals {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:23` `pub fn is_empty(self) -> bool {`
- `struct` `codex-rs/otel/src/metrics/runtime_metrics.rs:29` `pub struct RuntimeMetricsSummary {`
- `impl` `codex-rs/otel/src/metrics/runtime_metrics.rs:37` `impl RuntimeMetricsSummary {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:38` `pub fn is_empty(self) -> bool {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:77` `fn sum_counter(snapshot: &ResourceMetrics, name: &str) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:86` `fn sum_counter_metric(metric: &Metric) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:96` `fn sum_histogram_ms(snapshot: &ResourceMetrics, name: &str) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:105` `fn sum_histogram_metric_ms(metric: &Metric) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:115` `fn f64_to_u64(value: f64) -> u64 {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use crate::metrics::names::SSE_EVENT_COUNT_METRIC;`
- `use crate::metrics::names::SSE_EVENT_DURATION_METRIC;`
- `use crate::metrics::names::TOOL_CALL_COUNT_METRIC;`
- `use crate::metrics::names::TOOL_CALL_DURATION_METRIC;`
- `use crate::metrics::names::WEBSOCKET_EVENT_COUNT_METRIC;`
- `use crate::metrics::names::WEBSOCKET_EVENT_DURATION_METRIC;`
- `use crate::metrics::names::WEBSOCKET_REQUEST_COUNT_METRIC;`
- `use crate::metrics::names::WEBSOCKET_REQUEST_DURATION_METRIC;`
- `use opentelemetry_sdk::metrics::data::AggregatedMetrics;`
- `use opentelemetry_sdk::metrics::data::Metric;`
- `use opentelemetry_sdk::metrics::data::MetricData;`
- `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
