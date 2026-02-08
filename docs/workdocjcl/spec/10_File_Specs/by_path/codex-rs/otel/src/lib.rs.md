# `codex-rs/otel/src/lib.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6982`
- sha256: `1b53f13b232961bf4e40cff397310d61133a201dbdb78ff9a2c3299dc87dc27d`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/lib.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
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
- `use` `codex-rs/otel/src/lib.rs:17` `use opentelemetry_sdk::metrics::data::ResourceMetrics;`
- `use` `codex-rs/otel/src/lib.rs:18` `use serde::Serialize;`
- `use` `codex-rs/otel/src/lib.rs:19` `use std::time::Duration;`
- `use` `codex-rs/otel/src/lib.rs:20` `use strum_macros::Display;`
- `use` `codex-rs/otel/src/lib.rs:21` `use tracing::debug;`
- `enum` `codex-rs/otel/src/lib.rs:28` `pub enum ToolDecisionSource {`
- `struct` `codex-rs/otel/src/lib.rs:34` `pub struct OtelEventMetadata {`
- `struct` `codex-rs/otel/src/lib.rs:48` `pub struct OtelManager {`
- `impl` `codex-rs/otel/src/lib.rs:54` `impl OtelManager {`
- `fn` `codex-rs/otel/src/lib.rs:55` `pub fn with_model(mut self, model: &str, slug: &str) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:61` `pub fn with_metrics(mut self, metrics: MetricsClient) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:67` `pub fn with_metrics_without_metadata_tags(mut self, metrics: MetricsClient) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:73` `pub fn with_metrics_config(self, config: MetricsConfig) -> MetricsResult<Self> {`
- `fn` `codex-rs/otel/src/lib.rs:78` `pub fn with_provider_metrics(self, provider: &OtelProvider) -> Self {`
- `fn` `codex-rs/otel/src/lib.rs:85` `pub fn counter(&self, name: &str, inc: i64, tags: &[(&str, &str)]) {`
- `fn` `codex-rs/otel/src/lib.rs:100` `pub fn histogram(&self, name: &str, value: i64, tags: &[(&str, &str)]) {`
- `fn` `codex-rs/otel/src/lib.rs:115` `pub fn record_duration(&self, name: &str, duration: Duration, tags: &[(&str, &str)]) {`
- `fn` `codex-rs/otel/src/lib.rs:130` `pub fn start_timer(&self, name: &str, tags: &[(&str, &str)]) -> Result<Timer, MetricsError> {`
- `fn` `codex-rs/otel/src/lib.rs:138` `pub fn shutdown_metrics(&self) -> MetricsResult<()> {`
- `fn` `codex-rs/otel/src/lib.rs:145` `pub fn snapshot_metrics(&self) -> MetricsResult<ResourceMetrics> {`
- `fn` `codex-rs/otel/src/lib.rs:153` `pub fn reset_runtime_metrics(&self) {`
- `fn` `codex-rs/otel/src/lib.rs:163` `pub fn runtime_metrics_summary(&self) -> Option<RuntimeMetricsSummary> {`
- `fn` `codex-rs/otel/src/lib.rs:187` `fn metadata_tag_refs(&self) -> MetricsResult<Vec<(&str, &str)>> {`
- `fn` `codex-rs/otel/src/lib.rs:219` `pub fn start_global_timer(name: &str, tags: &[(&str, &str)]) -> MetricsResult<Timer> {`

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
