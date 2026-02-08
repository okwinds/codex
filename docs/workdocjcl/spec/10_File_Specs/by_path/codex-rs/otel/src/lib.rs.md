# `codex-rs/otel/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7255`
- sha256: `19c7ded27082eb1866fa100641f192680f3ab4b000de9a9cdcc8c8985682579c`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ToolDecisionSource {`
- `pub enum TelemetryAuthMode {`
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

## Definitions (auto, per-file)
- `mod` `codex-rs/otel/src/lib.rs:1` `pub mod config;`
- `mod` `codex-rs/otel/src/lib.rs:2` `pub mod metrics;`
- `mod` `codex-rs/otel/src/lib.rs:3` `pub mod otel_provider;`
- `mod` `codex-rs/otel/src/lib.rs:4` `pub mod traces;`
- `mod` `codex-rs/otel/src/lib.rs:6` `mod otlp;`
- `use` `codex-rs/otel/src/lib.rs:8` `use crate::metrics::MetricsClient;`
- `use` `codex-rs/otel/src/lib.rs:9` `use crate::metrics::MetricsConfig;`
- `use` `codex-rs/otel/src/lib.rs:10` `use crate::metrics::MetricsError;`
- `use` `codex-rs/otel/src/lib.rs:11` `use crate::metrics::Result as MetricsResult;`
- `use` `codex-rs/otel/src/lib.rs:13` `use crate::metrics::validation::validate_tag_key;`
- `use` `codex-rs/otel/src/lib.rs:14` `use crate::metrics::validation::validate_tag_value;`
- `use` `codex-rs/otel/src/lib.rs:15` `use crate::otel_provider::OtelProvider;`
- `use` `codex-rs/otel/src/lib.rs:16` `use codex_protocol::ThreadId;`
- `use` `codex-rs/otel/src/lib.rs:18` `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
- `use` `codex-rs/otel/src/lib.rs:19` `use serde::Serialize;`
- `use` `codex-rs/otel/src/lib.rs:20` `use std::time::Duration;`
- `use` `codex-rs/otel/src/lib.rs:21` `use strum_macros::Display;`
- `use` `codex-rs/otel/src/lib.rs:22` `use tracing::debug;`
- `enum` `codex-rs/otel/src/lib.rs:29` `pub enum ToolDecisionSource {`
- `enum` `codex-rs/otel/src/lib.rs:36` `pub enum TelemetryAuthMode {`
- `struct` `codex-rs/otel/src/lib.rs:42` `pub struct OtelEventMetadata {`
- `struct` `codex-rs/otel/src/lib.rs:57` `pub struct OtelManager {`
- `impl` `codex-rs/otel/src/lib.rs:63` `impl OtelManager {`
- `fn` `codex-rs/otel/src/lib.rs:64` `pub fn with_model(mut self, model: &str, slug: &str) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:70` `pub fn with_metrics(mut self, metrics: MetricsClient) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:76` `pub fn with_metrics_without_metadata_tags(mut self, metrics: MetricsClient) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:82` `pub fn with_metrics_config(self, config: MetricsConfig) -> MetricsResult<Self> {`
- `fn` `codex-rs/otel/src/lib.rs:87` `pub fn with_provider_metrics(self, provider: &OtelProvider) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:94` `pub fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) {`
- `fn` `codex-rs/otel/src/lib.rs:109` `pub fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) {`
- `fn` `codex-rs/otel/src/lib.rs:124` `pub fn record_duration(&self, name: &str, duration: Duration, tags: &[(&str, &str)]) {`
- `fn` `codex-rs/otel/src/lib.rs:139` `pub fn start_timer(&self, name: &str, tags: &[(&str, &str)]) -> Result<Timer, MetricsError> {`
- `fn` `codex-rs/otel/src/lib.rs:147` `pub fn shutdown_metrics(&self) -> MetricsResult<()> {`
- `fn` `codex-rs/otel/src/lib.rs:154` `pub fn snapshot_metrics(&self) -> MetricsResult<ResourceMetrics> {`
- `fn` `codex-rs/otel/src/lib.rs:162` `pub fn reset_runtime_metrics(&self) {`
- `fn` `codex-rs/otel/src/lib.rs:172` `pub fn runtime_metrics_summary(&self) -> Option<RuntimeMetricsSummary> {`
- `fn` `codex-rs/otel/src/lib.rs:196` `fn metadata_tag_refs(&self) -> MetricsResult<Vec<(&str, &str)>> {`
- `fn` `codex-rs/otel/src/lib.rs:228` `pub fn start_global_timer(name: &str, tags: &[(&str, &str)]) -> MetricsResult<Timer> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::metrics::MetricsClient;`
- `use crate::metrics::MetricsConfig;`
- `use crate::metrics::MetricsError;`
- `use crate::metrics::Result as MetricsResult;`
- `use crate::metrics::validation::validate_tag_key;`
- `use crate::metrics::validation::validate_tag_value;`
- `use crate::otel_provider::OtelProvider;`
- `use codex_protocol::ThreadId;`
- `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
- `use serde::Serialize;`
- `use std::time::Duration;`
- `use strum_macros::Display;`
- `use tracing::debug;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
