# `codex-otel`

- path: `codex-rs/otel`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `chrono`
- `codex-api`
- `codex-app-server-protocol`
- `codex-protocol`
- `codex-utils-absolute-path`
- `eventsource-stream`
- `http`
- `opentelemetry`
- `opentelemetry-appender-tracing`
- `opentelemetry-otlp`
- `opentelemetry-semantic-conventions`
- `opentelemetry_sdk`
- `reqwest`
- `serde`
- `serde_json`
- `strum_macros`
- `thiserror`
- `tokio`
- `tokio-tungstenite`
- `tracing`
- `tracing-opentelemetry`
- `tracing-subscriber`

## Features
- `disable-default-metrics-exporter`

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub mod config;`
- `pub mod metrics;`
- `pub mod otel_provider;`
- `pub mod traces;`
- `pub use crate::metrics::timer::Timer;`
- `pub use crate::metrics::runtime_metrics::RuntimeMetricTotals;`
- `pub use crate::metrics::runtime_metrics::RuntimeMetricsSummary;`
- `pub enum ToolDecisionSource {`
- `pub struct OtelEventMetadata {`
- `pub struct OtelManager {`
- `pub fn with_model(mut self, model: &str, slug: &str) -> Self {`
- `pub fn with_metrics(mut self, metrics: MetricsClient) -> Self {`
- `pub fn with_metrics_without_metadata_tags(mut self, metrics: MetricsClient) -> Self {`
- `pub fn with_metrics_config(self, config: MetricsConfig) -> MetricsResult<Self> {`
- `pub fn with_provider_metrics(self, provider: &OtelProvider) -> Self {`
- `pub fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) {`
- `pub fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) {`
- `pub fn record_duration(&self, name: &str, duration: Duration, tags: &[(&str, &str)]) {`
- `pub fn start_timer(&self, name: &str, tags: &[(&str, &str)]) -> Result<Timer, MetricsError> {`
- `pub fn shutdown_metrics(&self) -> MetricsResult<()> {`
- `pub fn snapshot_metrics(&self) -> MetricsResult<ResourceMetrics> {`
- `pub fn reset_runtime_metrics(&self) {`
- `pub fn runtime_metrics_summary(&self) -> Option<RuntimeMetricsSummary> {`
- `pub fn start_global_timer(name: &str, tags: &[(&str, &str)]) -> MetricsResult<Timer> {`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
