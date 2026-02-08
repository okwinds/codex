# `codex-rs/codex-client/src/default_client.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6218`
- sha256: `56aee943e52149f53e1f513d9eef0576d83696a5f2ff3eb9d95643377efaefc0`
- generated_utc: `2026-02-08T10:45:20Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/default_client.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub struct CodexHttpClient {`
- `pub fn new(inner: reqwest::Client) -> Self {`
- `pub struct CodexRequestBuilder {`
- `pub fn headers(self, headers: HeaderMap) -> Self {`
- `pub fn timeout(self, timeout: Duration) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-client/src/default_client.rs:1` `use http::Error as HttpError;`
- `use` `codex-rs/codex-client/src/default_client.rs:2` `use opentelemetry::global;`
- `use` `codex-rs/codex-client/src/default_client.rs:3` `use opentelemetry::propagation::Injector;`
- `use` `codex-rs/codex-client/src/default_client.rs:4` `use reqwest::IntoUrl;`
- `use` `codex-rs/codex-client/src/default_client.rs:5` `use reqwest::Method;`
- `use` `codex-rs/codex-client/src/default_client.rs:6` `use reqwest::Response;`
- `use` `codex-rs/codex-client/src/default_client.rs:7` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/codex-client/src/default_client.rs:8` `use reqwest::header::HeaderName;`
- `use` `codex-rs/codex-client/src/default_client.rs:9` `use reqwest::header::HeaderValue;`
- `use` `codex-rs/codex-client/src/default_client.rs:10` `use serde::Serialize;`
- `use` `codex-rs/codex-client/src/default_client.rs:11` `use std::fmt::Display;`
- `use` `codex-rs/codex-client/src/default_client.rs:12` `use std::time::Duration;`
- `use` `codex-rs/codex-client/src/default_client.rs:13` `use tracing::Span;`
- `use` `codex-rs/codex-client/src/default_client.rs:14` `use tracing_opentelemetry::OpenTelemetrySpanExt;`
- `struct` `codex-rs/codex-client/src/default_client.rs:17` `pub struct CodexHttpClient {`
- `impl` `codex-rs/codex-client/src/default_client.rs:21` `impl CodexHttpClient {`
- `fn` `codex-rs/codex-client/src/default_client.rs:22` `pub fn new(inner: reqwest::Client) -> Self {`
- `struct` `codex-rs/codex-client/src/default_client.rs:51` `pub struct CodexRequestBuilder {`
- `impl` `codex-rs/codex-client/src/default_client.rs:57` `impl CodexRequestBuilder {`
- `fn` `codex-rs/codex-client/src/default_client.rs:58` `fn new(builder: reqwest::RequestBuilder, method: Method, url: String) -> Self {`
- `fn` `codex-rs/codex-client/src/default_client.rs:66` `fn map(self, f: impl FnOnce(reqwest::RequestBuilder) -> reqwest::RequestBuilder) -> Self {`
- `fn` `codex-rs/codex-client/src/default_client.rs:74` `pub fn headers(self, headers: HeaderMap) -> Self {`
- `fn` `codex-rs/codex-client/src/default_client.rs:95` `pub fn timeout(self, timeout: Duration) -> Self {`
- `fn` `codex-rs/codex-client/src/default_client.rs:113` `pub async fn send(self) -> Result<Response, reqwest::Error> {`
- `struct` `codex-rs/codex-client/src/default_client.rs:144` `struct HeaderMapInjector<'a>(&'a mut HeaderMap);`
- `impl` `codex-rs/codex-client/src/default_client.rs:146` `impl<'a> Injector for HeaderMapInjector<'a> {`
- `fn` `codex-rs/codex-client/src/default_client.rs:147` `fn set(&mut self, key: &str, value: String) {`
- `fn` `codex-rs/codex-client/src/default_client.rs:157` `fn trace_headers() -> HeaderMap {`
- `use` `codex-rs/codex-client/src/default_client.rs:170` `use super::*;`
- `use` `codex-rs/codex-client/src/default_client.rs:171` `use opentelemetry::propagation::Extractor;`
- `use` `codex-rs/codex-client/src/default_client.rs:172` `use opentelemetry::propagation::TextMapPropagator;`
- `use` `codex-rs/codex-client/src/default_client.rs:173` `use opentelemetry::trace::TraceContextExt;`
- `use` `codex-rs/codex-client/src/default_client.rs:174` `use opentelemetry::trace::TracerProvider;`
- `use` `codex-rs/codex-client/src/default_client.rs:175` `use opentelemetry_sdk::propagation::TraceContextPropagator;`
- `use` `codex-rs/codex-client/src/default_client.rs:176` `use opentelemetry_sdk::trace::SdkTracerProvider;`
- `use` `codex-rs/codex-client/src/default_client.rs:177` `use tracing::trace_span;`
- `use` `codex-rs/codex-client/src/default_client.rs:178` `use tracing_subscriber::layer::SubscriberExt;`
- `use` `codex-rs/codex-client/src/default_client.rs:179` `use tracing_subscriber::util::SubscriberInitExt;`
- `fn` `codex-rs/codex-client/src/default_client.rs:182` `fn inject_trace_headers_uses_current_span_context() {`
- `struct` `codex-rs/codex-client/src/default_client.rs:207` `struct HeaderMapExtractor<'a>(&'a HeaderMap);`
- `impl` `codex-rs/codex-client/src/default_client.rs:209` `impl<'a> Extractor for HeaderMapExtractor<'a> {`
- `fn` `codex-rs/codex-client/src/default_client.rs:210` `fn get(&self, key: &str) -> Option<&str> {`
- `fn` `codex-rs/codex-client/src/default_client.rs:214` `fn keys(&self) -> Vec<&str> {`

## Dependencies (auto sample)
### Imports / Includes
- `use http::Error as HttpError;`
- `use opentelemetry::global;`
- `use opentelemetry::propagation::Injector;`
- `use reqwest::IntoUrl;`
- `use reqwest::Method;`
- `use reqwest::Response;`
- `use reqwest::header::HeaderMap;`
- `use reqwest::header::HeaderName;`
- `use reqwest::header::HeaderValue;`
- `use serde::Serialize;`
- `use std::fmt::Display;`
- `use std::time::Duration;`
- `use tracing::Span;`
- `use tracing_opentelemetry::OpenTelemetrySpanExt;`
- `use super::*;`
- `use opentelemetry::propagation::Extractor;`
- `use opentelemetry::propagation::TextMapPropagator;`
- `use opentelemetry::trace::TraceContextExt;`
- `use opentelemetry::trace::TracerProvider;`
- `use opentelemetry_sdk::propagation::TraceContextPropagator;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
