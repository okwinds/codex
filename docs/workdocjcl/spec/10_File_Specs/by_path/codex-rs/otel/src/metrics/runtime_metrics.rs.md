# `codex-rs/otel/src/metrics/runtime_metrics.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8495`
- sha256: `e28313e667669b3f7b606e8f076d14c7134a06427a5444ee4ba482c88c69a253`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `pub fn merge(&mut self, other: Self) {`
- `pub struct RuntimeMetricsSummary {`
- `pub fn is_empty(self) -> bool {`
- `pub fn merge(&mut self, other: Self) {`
- `pub fn responses_api_summary(&self) -> RuntimeMetricsSummary {`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:1` `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:2` `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:3` `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TBT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:4` `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TTFT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:5` `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TBT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:6` `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TTFT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:7` `use crate::metrics::names::RESPONSES_API_INFERENCE_TIME_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:8` `use crate::metrics::names::RESPONSES_API_OVERHEAD_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:9` `use crate::metrics::names::SSE_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:10` `use crate::metrics::names::SSE_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:11` `use crate::metrics::names::TOOL_CALL_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:12` `use crate::metrics::names::TOOL_CALL_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:13` `use crate::metrics::names::WEBSOCKET_EVENT_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:14` `use crate::metrics::names::WEBSOCKET_EVENT_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:15` `use crate::metrics::names::WEBSOCKET_REQUEST_COUNT_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:16` `use crate::metrics::names::WEBSOCKET_REQUEST_DURATION_METRIC;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:17` `use opentelemetry_sdk::metrics::data::AggregatedMetrics;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:18` `use opentelemetry_sdk::metrics::data::Metric;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:19` `use opentelemetry_sdk::metrics::data::MetricData;`
- `use` `codex-rs/otel/src/metrics/runtime_metrics.rs:20` `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
- `struct` `codex-rs/otel/src/metrics/runtime_metrics.rs:23` `pub struct RuntimeMetricTotals {`
- `impl` `codex-rs/otel/src/metrics/runtime_metrics.rs:28` `impl RuntimeMetricTotals {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:29` `pub fn is_empty(self) -> bool {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:33` `pub fn merge(&mut self, other: Self) {`
- `struct` `codex-rs/otel/src/metrics/runtime_metrics.rs:40` `pub struct RuntimeMetricsSummary {`
- `impl` `codex-rs/otel/src/metrics/runtime_metrics.rs:54` `impl RuntimeMetricsSummary {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:55` `pub fn is_empty(self) -> bool {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:69` `pub fn merge(&mut self, other: Self) {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:95` `pub fn responses_api_summary(&self) -> RuntimeMetricsSummary {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:156` `fn sum_counter(snapshot: &ResourceMetrics, name: &str) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:165` `fn sum_counter_metric(metric: &Metric) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:175` `fn sum_histogram_ms(snapshot: &ResourceMetrics, name: &str) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:184` `fn sum_histogram_metric_ms(metric: &Metric) -> u64 {`
- `fn` `codex-rs/otel/src/metrics/runtime_metrics.rs:194` `fn f64_to_u64(value: f64) -> u64 {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::metrics::names::API_CALL_COUNT_METRIC;`
- `use crate::metrics::names::API_CALL_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TBT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_IAPI_TTFT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TBT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_ENGINE_SERVICE_TTFT_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_INFERENCE_TIME_DURATION_METRIC;`
- `use crate::metrics::names::RESPONSES_API_OVERHEAD_DURATION_METRIC;`
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
