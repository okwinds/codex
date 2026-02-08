# `codex-rs/codex-api/src/endpoint/session.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3296`
- sha256: `1d7928dcc9074b5a10e0a88fed6d8b85163d703271c6e7e0722b6adfe69f2924`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/endpoint/session.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/endpoint/session.rs:1` `use crate::auth::AuthProvider;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:2` `use crate::auth::add_auth_headers;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:3` `use crate::error::ApiError;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:4` `use crate::provider::Provider;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:5` `use crate::telemetry::run_with_request_telemetry;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:6` `use codex_client::HttpTransport;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:7` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:8` `use codex_client::RequestTelemetry;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:9` `use codex_client::Response;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:10` `use codex_client::StreamResponse;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:11` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:12` `use http::Method;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:13` `use serde_json::Value;`
- `use` `codex-rs/codex-api/src/endpoint/session.rs:14` `use std::sync::Arc;`
- `impl` `codex-rs/codex-api/src/endpoint/session.rs:23` `impl<T: HttpTransport, A: AuthProvider> EndpointSession<T, A> {`
- `fn` `codex-rs/codex-api/src/endpoint/session.rs:45` `fn make_request(`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthProvider;`
- `use crate::auth::add_auth_headers;`
- `use crate::error::ApiError;`
- `use crate::provider::Provider;`
- `use crate::telemetry::run_with_request_telemetry;`
- `use codex_client::HttpTransport;`
- `use codex_client::Request;`
- `use codex_client::RequestTelemetry;`
- `use codex_client::Response;`
- `use codex_client::StreamResponse;`
- `use http::HeaderMap;`
- `use http::Method;`
- `use serde_json::Value;`
- `use std::sync::Arc;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
