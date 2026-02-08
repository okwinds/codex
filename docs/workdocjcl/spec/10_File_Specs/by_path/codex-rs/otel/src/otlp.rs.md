# `codex-rs/otel/src/otlp.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5640`
- sha256: `12f007998f9ec42b88a98905fb144889ef8a0fdaaced3c07128ac6d63ded09a2`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/src/otlp.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/otel/src/otlp.rs:1` `use crate::config::OtelTlsConfig;`
- `use` `codex-rs/otel/src/otlp.rs:2` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/otel/src/otlp.rs:3` `use http::Uri;`
- `use` `codex-rs/otel/src/otlp.rs:4` `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_TIMEOUT;`
- `use` `codex-rs/otel/src/otlp.rs:5` `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_TIMEOUT_DEFAULT;`
- `use` `codex-rs/otel/src/otlp.rs:6` `use opentelemetry_otlp::tonic_types::transport::Certificate as TonicCertificate;`
- `use` `codex-rs/otel/src/otlp.rs:7` `use opentelemetry_otlp::tonic_types::transport::ClientTlsConfig;`
- `use` `codex-rs/otel/src/otlp.rs:8` `use opentelemetry_otlp::tonic_types::transport::Identity as TonicIdentity;`
- `use` `codex-rs/otel/src/otlp.rs:9` `use reqwest::Certificate as ReqwestCertificate;`
- `use` `codex-rs/otel/src/otlp.rs:10` `use reqwest::Identity as ReqwestIdentity;`
- `use` `codex-rs/otel/src/otlp.rs:11` `use reqwest::header::HeaderMap;`
- `use` `codex-rs/otel/src/otlp.rs:12` `use reqwest::header::HeaderName;`
- `use` `codex-rs/otel/src/otlp.rs:13` `use reqwest::header::HeaderValue;`
- `use` `codex-rs/otel/src/otlp.rs:14` `use std::env;`
- `use` `codex-rs/otel/src/otlp.rs:15` `use std::error::Error;`
- `use` `codex-rs/otel/src/otlp.rs:16` `use std::fs;`
- `use` `codex-rs/otel/src/otlp.rs:17` `use std::io;`
- `use` `codex-rs/otel/src/otlp.rs:18` `use std::io::ErrorKind;`
- `use` `codex-rs/otel/src/otlp.rs:19` `use std::path::PathBuf;`
- `use` `codex-rs/otel/src/otlp.rs:20` `use std::time::Duration;`
- `fn` `codex-rs/otel/src/otlp.rs:85` `fn build_http_client_inner(`
- `fn` `codex-rs/otel/src/otlp.rs:142` `fn read_timeout_env(var: &str) -> Option<Duration> {`
- `fn` `codex-rs/otel/src/otlp.rs:151` `fn read_bytes(path: &AbsolutePathBuf) -> Result<(Vec<u8>, PathBuf), Box<dyn Error>> {`
- `fn` `codex-rs/otel/src/otlp.rs:161` `fn config_error(message: impl Into<String>) -> Box<dyn Error> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::OtelTlsConfig;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use http::Uri;`
- `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_TIMEOUT;`
- `use opentelemetry_otlp::OTEL_EXPORTER_OTLP_TIMEOUT_DEFAULT;`
- `use opentelemetry_otlp::tonic_types::transport::Certificate as TonicCertificate;`
- `use opentelemetry_otlp::tonic_types::transport::ClientTlsConfig;`
- `use opentelemetry_otlp::tonic_types::transport::Identity as TonicIdentity;`
- `use reqwest::Certificate as ReqwestCertificate;`
- `use reqwest::Identity as ReqwestIdentity;`
- `use reqwest::header::HeaderMap;`
- `use reqwest::header::HeaderName;`
- `use reqwest::header::HeaderValue;`
- `use std::env;`
- `use std::error::Error;`
- `use std::fs;`
- `use std::io;`
- `use std::io::ErrorKind;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
