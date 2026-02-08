# `codex-client`

- path: `codex-rs/codex-client`
- generated_utc: `2026-02-03T09:48:37Z`
- role: crate

## Build Targets
- has_lib_rs: `true`
- has_main_rs: `false`
- explicit_bins: (none)

## Key Dependencies (direct, from Cargo.toml)
- `async-trait`
- `bytes`
- `eventsource-stream`
- `futures`
- `http`
- `opentelemetry`
- `rand`
- `reqwest`
- `serde`
- `serde_json`
- `thiserror`
- `tokio`
- `tracing`
- `tracing-opentelemetry`
- `zstd`

## Features
- (none)

## Public Surface (auto, from src/lib.rs or src/main.rs)
- `pub use crate::default_client::CodexHttpClient;`
- `pub use crate::default_client::CodexRequestBuilder;`
- `pub use crate::error::StreamError;`
- `pub use crate::error::TransportError;`
- `pub use crate::request::Request;`
- `pub use crate::request::RequestCompression;`
- `pub use crate::request::Response;`
- `pub use crate::retry::RetryOn;`
- `pub use crate::retry::RetryPolicy;`
- `pub use crate::retry::backoff;`
- `pub use crate::retry::run_with_retry;`
- `pub use crate::sse::sse_stream;`
- `pub use crate::telemetry::RequestTelemetry;`
- `pub use crate::transport::ByteStream;`
- `pub use crate::transport::HttpTransport;`
- `pub use crate::transport::ReqwestTransport;`
- `pub use crate::transport::StreamResponse;`

## Spec Links
- `workdocjcl/spec/00_Overview/MODULE_MAP.md`
- `workdocjcl/spec/09_Verification/CODE_TO_SPEC_MAP.md`
