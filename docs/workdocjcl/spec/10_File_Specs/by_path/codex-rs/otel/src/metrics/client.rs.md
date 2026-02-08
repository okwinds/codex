# `codex-rs/otel/src/metrics/client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13892`
- sha256: `ab3e5fbbcbda4118c4593cdf05b4c7d534cbc6badf80f54e1d41dbe2d9e5bd65`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/metrics/client.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct MetricsClient(std::sync::Arc<MetricsClientInner>);`
- `pub fn new(config: MetricsConfig) -> Result<Self> {`
- `pub fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) -> Result<()> {`
- `pub fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) -> Result<()> {`
- `pub fn record_duration(`
- `pub fn start_timer(`
- `pub fn snapshot(&self) -> Result<ResourceMetrics> {`
- `pub fn shutdown(&self) -> Result<()> {`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/metrics/client.rs:1` `use crate::config::OtelExporter;`
- `use` `codex-rs/otel/src/metrics/client.rs:2` `use crate::config::OtelHttpProtocol;`
- `use` `codex-rs/otel/src/metrics/client.rs:3` `use crate::metrics::MetricsError;`
- `use` `codex-rs/otel/src/metrics/client.rs:4` `use crate::metrics::Result;`
- `use` `codex-rs/otel/src/metrics/client.rs:5` `use crate::metrics::config::MetricsConfig;`
- `use` `codex-rs/otel/src/metrics/client.rs:6` `use crate::metrics::config::MetricsExporter;`
- `use` `codex-rs/otel/src/metrics/client.rs:7` `use crate::metrics::timer::Timer;`
- `use` `codex-rs/otel/src/metrics/client.rs:8` `use crate::metrics::validation::validate_metric_name;`
- `use` `codex-rs/otel/src/metrics/client.rs:9` `use crate::metrics::validation::validate_tag_key;`
- `use` `codex-rs/otel/src/metrics/client.rs:10` `use crate::metrics::validation::validate_tag_value;`
- `use` `codex-rs/otel/src/metrics/client.rs:11` `use crate::metrics::validation::validate_tags;`
- `use` `codex-rs/otel/src/metrics/client.rs:12` `use codex_utils_string::sanitize_metric_tag_value;`
- `use` `codex-rs/otel/src/metrics/client.rs:13` `use opentelemetry::KeyValue;`
- `use` `codex-rs/otel/src/metrics/client.rs:14` `use opentelemetry::metrics::Counter;`
- `use` `codex-rs/otel/src/metrics/client.rs:15` `use opentelemetry::metrics::Histogram;`
- `use` `codex-rs/otel/src/metrics/client.rs:16` `use opentelemetry::metrics::Meter;`
- `use` `codex-rs/otel/src/metrics/client.rs:17` `use opentelemetry::metrics::MeterProvider as _;`
- `use` `codex-rs/otel/src/metrics/client.rs:18` `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_METRICS_TIMEOUT;`
- `use` `codex-rs/otel/src/metrics/client.rs:19` `use opentelemetry_otlp::Protocol;`
- `use` `codex-rs/otel/src/metrics/client.rs:20` `use opentelemetry_otlp::WithExportConfig;`
- `use` `codex-rs/otel/src/metrics/client.rs:21` `use opentelemetry_otlp::WithHttpConfig;`
- `use` `codex-rs/otel/src/metrics/client.rs:22` `use opentelemetry_otlp::WithTonicConfig;`
- `use` `codex-rs/otel/src/metrics/client.rs:23` `use opentelemetry_otlp::tonic_types::metadata::MetadataMap;`
- `use` `codex-rs/otel/src/metrics/client.rs:24` `use opentelemetry_otlp::tonic_types::transport::ClientTlsConfig;`
- `use` `codex-rs/otel/src/metrics/client.rs:25` `use opentelemetry_sdk::Resource;`
- `use` `codex-rs/otel/src/metrics/client.rs:26` `use opentelemetry_sdk::metrics::InstrumentKind;`
- `use` `codex-rs/otel/src/metrics/client.rs:27` `use opentelemetry_sdk::metrics::ManualReader;`
- `use` `codex-rs/otel/src/metrics/client.rs:28` `use opentelemetry_sdk::metrics::PeriodicReader;`
- `use` `codex-rs/otel/src/metrics/client.rs:29` `use opentelemetry_sdk::metrics::Pipeline;`
- `use` `codex-rs/otel/src/metrics/client.rs:30` `use opentelemetry_sdk::metrics::SdkMeterProvider;`
- `use` `codex-rs/otel/src/metrics/client.rs:31` `use opentelemetry_sdk::metrics::Temporality;`
- `use` `codex-rs/otel/src/metrics/client.rs:32` `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
- `use` `codex-rs/otel/src/metrics/client.rs:33` `use opentelemetry_sdk::metrics::reader::MetricReader;`
- `use` `codex-rs/otel/src/metrics/client.rs:34` `use opentelemetry_semantic_conventions as semconv;`
- `use` `codex-rs/otel/src/metrics/client.rs:35` `use std::collections::BTreeMap;`
- `use` `codex-rs/otel/src/metrics/client.rs:36` `use std::collections::HashMap;`
- `use` `codex-rs/otel/src/metrics/client.rs:37` `use std::sync::Arc;`
- `use` `codex-rs/otel/src/metrics/client.rs:38` `use std::sync::Mutex;`
- `use` `codex-rs/otel/src/metrics/client.rs:39` `use std::sync::Weak;`
- `use` `codex-rs/otel/src/metrics/client.rs:40` `use std::time::Duration;`
- `use` `codex-rs/otel/src/metrics/client.rs:41` `use tracing::debug;`
- `const` `codex-rs/otel/src/metrics/client.rs:43` `const ENV_ATTRIBUTE: &str = "env";`
- `const` `codex-rs/otel/src/metrics/client.rs:44` `const METER_NAME: &str = "codex";`
- `const` `codex-rs/otel/src/metrics/client.rs:45` `const DURATION_UNIT: &str = "ms";`
- `const` `codex-rs/otel/src/metrics/client.rs:46` `const DURATION_DESCRIPTION: &str = "Duration in milliseconds.";`
- `struct` `codex-rs/otel/src/metrics/client.rs:49` `struct SharedManualReader {`
- `impl` `codex-rs/otel/src/metrics/client.rs:53` `impl SharedManualReader {`
- `fn` `codex-rs/otel/src/metrics/client.rs:54` `fn new(inner: Arc<ManualReader>) -> Self {`
- `impl` `codex-rs/otel/src/metrics/client.rs:59` `impl MetricReader for SharedManualReader {`
- `fn` `codex-rs/otel/src/metrics/client.rs:60` `fn register_pipeline(&self, pipeline: Weak<Pipeline>) {`
- `fn` `codex-rs/otel/src/metrics/client.rs:64` `fn collect(&self, rm: &mut ResourceMetrics) -> opentelemetry_sdk::error::OTelSdkResult {`
- `fn` `codex-rs/otel/src/metrics/client.rs:68` `fn force_flush(&self) -> opentelemetry_sdk::error::OTelSdkResult {`
- `fn` `codex-rs/otel/src/metrics/client.rs:72` `fn shutdown_with_timeout(&self, timeout: Duration) -> opentelemetry_sdk::error::OTelSdkResult {`
- `fn` `codex-rs/otel/src/metrics/client.rs:76` `fn temporality(&self, kind: InstrumentKind) -> Temporality {`
- `struct` `codex-rs/otel/src/metrics/client.rs:82` `struct MetricsClientInner {`
- `impl` `codex-rs/otel/src/metrics/client.rs:92` `impl MetricsClientInner {`
- `fn` `codex-rs/otel/src/metrics/client.rs:93` `fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) -> Result<()> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:114` `fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) -> Result<()> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:129` `fn duration_histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) -> Result<()> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:148` `fn attributes(&self, tags: &[(&str, &str)]) -> Result<Vec<KeyValue>> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:170` `fn shutdown(&self) -> Result<()> {`
- `struct` `codex-rs/otel/src/metrics/client.rs:184` `pub struct MetricsClient(std::sync::Arc<MetricsClientInner>);`
- `impl` `codex-rs/otel/src/metrics/client.rs:186` `impl MetricsClient {`
- `fn` `codex-rs/otel/src/metrics/client.rs:188` `pub fn new(config: MetricsConfig) -> Result<Self> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:244` `pub fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) -> Result<()> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:249` `pub fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) -> Result<()> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:254` `pub fn record_duration(`
- `fn` `codex-rs/otel/src/metrics/client.rs:267` `pub fn start_timer(`
- `fn` `codex-rs/otel/src/metrics/client.rs:276` `pub fn snapshot(&self) -> Result<ResourceMetrics> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:288` `pub fn shutdown(&self) -> Result<()> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:293` `fn os_resource_attributes() -> Vec<KeyValue> {`
- `fn` `codex-rs/otel/src/metrics/client.rs:332` `fn build_otlp_metric_exporter(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::OtelExporter;`
- `use crate::config::OtelHttpProtocol;`
- `use crate::metrics::MetricsError;`
- `use crate::metrics::Result;`
- `use crate::metrics::config::MetricsConfig;`
- `use crate::metrics::config::MetricsExporter;`
- `use crate::metrics::timer::Timer;`
- `use crate::metrics::validation::validate_metric_name;`
- `use crate::metrics::validation::validate_tag_key;`
- `use crate::metrics::validation::validate_tag_value;`
- `use crate::metrics::validation::validate_tags;`
- `use codex_utils_string::sanitize_metric_tag_value;`
- `use opentelemetry::KeyValue;`
- `use opentelemetry::metrics::Counter;`
- `use opentelemetry::metrics::Histogram;`
- `use opentelemetry::metrics::Meter;`
- `use opentelemetry::metrics::MeterProvider as _;`
- `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_METRICS_TIMEOUT;`
- `use opentelemetry_otlp::Protocol;`
- `use opentelemetry_otlp::WithExportConfig;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
