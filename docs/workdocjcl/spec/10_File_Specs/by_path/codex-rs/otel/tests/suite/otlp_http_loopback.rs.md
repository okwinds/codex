# `codex-rs/otel/tests/suite/otlp_http_loopback.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `7029`
- sha256: `75c35941237ae1d6e40214fd0591473360fd5e8109b81c5564ab41f3a64d695b`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/tests/suite/otlp_http_loopback.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_otel::config::OtelExporter;`
- `use codex_otel::config::OtelHttpProtocol;`
- `use codex_otel::metrics::MetricsClient;`
- `use codex_otel::metrics::MetricsConfig;`
- `use codex_otel::metrics::Result;`
- `use std::collections::HashMap;`
- `use std::io::Read as _;`
- `use std::io::Write as _;`
- `use std::net::TcpListener;`
- `use std::net::TcpStream;`
- `use std::sync::mpsc;`
- `use std::thread;`
- `use std::time::Duration;`
- `use std::time::Instant;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
