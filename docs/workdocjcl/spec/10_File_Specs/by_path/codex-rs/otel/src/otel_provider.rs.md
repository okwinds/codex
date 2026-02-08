# `codex-rs/otel/src/otel_provider.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13357`
- sha256: `2e07497fbae4aee47a17922ae08fb9b6c7cbc29c8685424a5431191692a8efd7`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/otel_provider.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct OtelProvider {`
- `pub fn shutdown(&self) {`
- `pub fn from(settings: &OtelSettings) -> Result<Option<Self>, Box<dyn Error>> {`
- `pub fn codex_export_filter(meta: &tracing::Metadata<'_>) -> bool {`
- `pub fn metrics(&self) -> Option<&MetricsClient> {`

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/otel_provider.rs:1` `use crate::config::OtelExporter;`
- `use` `codex-rs/otel/src/otel_provider.rs:2` `use crate::config::OtelHttpProtocol;`
- `use` `codex-rs/otel/src/otel_provider.rs:3` `use crate::config::OtelSettings;`
- `use` `codex-rs/otel/src/otel_provider.rs:4` `use crate::metrics::MetricsClient;`
- `use` `codex-rs/otel/src/otel_provider.rs:5` `use crate::metrics::MetricsConfig;`
- `use` `codex-rs/otel/src/otel_provider.rs:6` `use opentelemetry::Context;`
- `use` `codex-rs/otel/src/otel_provider.rs:7` `use opentelemetry::KeyValue;`
- `use` `codex-rs/otel/src/otel_provider.rs:8` `use opentelemetry::context::ContextGuard;`
- `use` `codex-rs/otel/src/otel_provider.rs:9` `use opentelemetry::global;`
- `use` `codex-rs/otel/src/otel_provider.rs:10` `use opentelemetry::propagation::TextMapPropagator;`
- `use` `codex-rs/otel/src/otel_provider.rs:11` `use opentelemetry::trace::TraceContextExt;`
- `use` `codex-rs/otel/src/otel_provider.rs:12` `use opentelemetry::trace::TracerProvider as _;`
- `use` `codex-rs/otel/src/otel_provider.rs:13` `use opentelemetry_appender_tracing::layer::OpenTelemetryTracingBridge;`
- `use` `codex-rs/otel/src/otel_provider.rs:14` `use opentelemetry_otlp::LogExporter;`
- `use` `codex-rs/otel/src/otel_provider.rs:15` `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_LOGS_TIMEOUT;`
- `use` `codex-rs/otel/src/otel_provider.rs:16` `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_TRACES_TIMEOUT;`
- `use` `codex-rs/otel/src/otel_provider.rs:17` `use opentelemetry_otlp::Protocol;`
- `use` `codex-rs/otel/src/otel_provider.rs:18` `use opentelemetry_otlp::SpanExporter;`
- `use` `codex-rs/otel/src/otel_provider.rs:19` `use opentelemetry_otlp::WithExportConfig;`
- `use` `codex-rs/otel/src/otel_provider.rs:20` `use opentelemetry_otlp::WithHttpConfig;`
- `use` `codex-rs/otel/src/otel_provider.rs:21` `use opentelemetry_otlp::WithTonicConfig;`
- `use` `codex-rs/otel/src/otel_provider.rs:22` `use opentelemetry_otlp::tonic_types::metadata::MetadataMap;`
- `use` `codex-rs/otel/src/otel_provider.rs:23` `use opentelemetry_otlp::tonic_types::transport::ClientTlsConfig;`
- `use` `codex-rs/otel/src/otel_provider.rs:24` `use opentelemetry_sdk::Resource;`
- `use` `codex-rs/otel/src/otel_provider.rs:25` `use opentelemetry_sdk::logs::SdkLoggerProvider;`
- `use` `codex-rs/otel/src/otel_provider.rs:26` `use opentelemetry_sdk::propagation::TraceContextPropagator;`
- `use` `codex-rs/otel/src/otel_provider.rs:27` `use opentelemetry_sdk::trace::BatchSpanProcessor;`
- `use` `codex-rs/otel/src/otel_provider.rs:28` `use opentelemetry_sdk::trace::SdkTracerProvider;`
- `use` `codex-rs/otel/src/otel_provider.rs:29` `use opentelemetry_sdk::trace::Tracer;`
- `use` `codex-rs/otel/src/otel_provider.rs:30` `use opentelemetry_semantic_conventions as semconv;`
- `use` `codex-rs/otel/src/otel_provider.rs:31` `use std::cell::RefCell;`
- `use` `codex-rs/otel/src/otel_provider.rs:32` `use std::collections::HashMap;`
- `use` `codex-rs/otel/src/otel_provider.rs:33` `use std::env;`
- `use` `codex-rs/otel/src/otel_provider.rs:34` `use std::error::Error;`
- `use` `codex-rs/otel/src/otel_provider.rs:35` `use std::sync::OnceLock;`
- `use` `codex-rs/otel/src/otel_provider.rs:36` `use tracing::debug;`
- `use` `codex-rs/otel/src/otel_provider.rs:37` `use tracing::level_filters::LevelFilter;`
- `use` `codex-rs/otel/src/otel_provider.rs:38` `use tracing::warn;`
- `use` `codex-rs/otel/src/otel_provider.rs:39` `use tracing_subscriber::Layer;`
- `use` `codex-rs/otel/src/otel_provider.rs:40` `use tracing_subscriber::registry::LookupSpan;`
- `const` `codex-rs/otel/src/otel_provider.rs:42` `const ENV_ATTRIBUTE: &str = "env";`
- `const` `codex-rs/otel/src/otel_provider.rs:43` `const TRACEPARENT_ENV_VAR: &str = "TRACEPARENT";`
- `const` `codex-rs/otel/src/otel_provider.rs:44` `const TRACESTATE_ENV_VAR: &str = "TRACESTATE";`
- `static` `codex-rs/otel/src/otel_provider.rs:45` `static TRACEPARENT_CONTEXT: OnceLock<Option<Context>> = OnceLock::new();`
- `static` `codex-rs/otel/src/otel_provider.rs:48` `static TRACEPARENT_GUARD: RefCell<Option<ContextGuard>> = const { RefCell::new(None) };`
- `struct` `codex-rs/otel/src/otel_provider.rs:50` `pub struct OtelProvider {`
- `impl` `codex-rs/otel/src/otel_provider.rs:57` `impl OtelProvider {`
- `fn` `codex-rs/otel/src/otel_provider.rs:58` `pub fn shutdown(&self) {`
- `fn` `codex-rs/otel/src/otel_provider.rs:70` `pub fn from(settings: &OtelSettings) -> Result<Option<Self>, Box<dyn Error>> {`
- `fn` `codex-rs/otel/src/otel_provider.rs:150` `pub fn codex_export_filter(meta: &tracing::Metadata<'_>) -> bool {`
- `fn` `codex-rs/otel/src/otel_provider.rs:154` `pub fn metrics(&self) -> Option<&MetricsClient> {`
- `impl` `codex-rs/otel/src/otel_provider.rs:159` `impl Drop for OtelProvider {`
- `fn` `codex-rs/otel/src/otel_provider.rs:160` `fn drop(&mut self) {`
- `fn` `codex-rs/otel/src/otel_provider.rs:179` `fn attach_traceparent_context() {`
- `fn` `codex-rs/otel/src/otel_provider.rs:191` `fn load_traceparent_context() -> Option<Context> {`
- `fn` `codex-rs/otel/src/otel_provider.rs:207` `fn extract_traceparent_context(traceparent: String, tracestate: Option<String>) -> Option<Context> {`
- `fn` `codex-rs/otel/src/otel_provider.rs:223` `fn make_resource(settings: &OtelSettings) -> Resource {`
- `fn` `codex-rs/otel/src/otel_provider.rs:236` `fn build_logger(`
- `fn` `codex-rs/otel/src/otel_provider.rs:305` `fn build_tracer_provider(`
- `use` `codex-rs/otel/src/otel_provider.rs:376` `use super::*;`
- `use` `codex-rs/otel/src/otel_provider.rs:377` `use opentelemetry::trace::SpanId;`
- `use` `codex-rs/otel/src/otel_provider.rs:378` `use opentelemetry::trace::TraceContextExt;`
- `use` `codex-rs/otel/src/otel_provider.rs:379` `use opentelemetry::trace::TraceId;`
- `fn` `codex-rs/otel/src/otel_provider.rs:382` `fn parses_valid_traceparent() {`
- `fn` `codex-rs/otel/src/otel_provider.rs:398` `fn invalid_traceparent_returns_none() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::OtelExporter;`
- `use crate::config::OtelHttpProtocol;`
- `use crate::config::OtelSettings;`
- `use crate::metrics::MetricsClient;`
- `use crate::metrics::MetricsConfig;`
- `use opentelemetry::Context;`
- `use opentelemetry::KeyValue;`
- `use opentelemetry::context::ContextGuard;`
- `use opentelemetry::global;`
- `use opentelemetry::propagation::TextMapPropagator;`
- `use opentelemetry::trace::TraceContextExt;`
- `use opentelemetry::trace::TracerProvider as _;`
- `use opentelemetry_appender_tracing::layer::OpenTelemetryTracingBridge;`
- `use opentelemetry_otlp::LogExporter;`
- `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_LOGS_TIMEOUT;`
- `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_TRACES_TIMEOUT;`
- `use opentelemetry_otlp::Protocol;`
- `use opentelemetry_otlp::SpanExporter;`
- `use opentelemetry_otlp::WithExportConfig;`
- `use opentelemetry_otlp::WithHttpConfig;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
