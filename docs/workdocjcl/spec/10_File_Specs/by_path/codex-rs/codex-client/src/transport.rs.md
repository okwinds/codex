# `codex-rs/codex-client/src/transport.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6161`
- sha256: `a866fea696a5d1dfaca8026a236242839d2472a1bfdb319d0239e3d03cc77478`
- generated_utc: `2026-02-08T10:45:22Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-client/src/transport.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- `pub struct StreamResponse {`
- `pub trait HttpTransport: Send + Sync {`
- `pub struct ReqwestTransport {`
- `pub fn new(client: reqwest::Client) -> Self {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-client/src/transport.rs:1` `use crate::default_client::CodexHttpClient;`
- `use` `codex-rs/codex-client/src/transport.rs:2` `use crate::default_client::CodexRequestBuilder;`
- `use` `codex-rs/codex-client/src/transport.rs:3` `use crate::error::TransportError;`
- `use` `codex-rs/codex-client/src/transport.rs:4` `use crate::request::Request;`
- `use` `codex-rs/codex-client/src/transport.rs:5` `use crate::request::RequestCompression;`
- `use` `codex-rs/codex-client/src/transport.rs:6` `use crate::request::Response;`
- `use` `codex-rs/codex-client/src/transport.rs:7` `use async_trait::async_trait;`
- `use` `codex-rs/codex-client/src/transport.rs:8` `use bytes::Bytes;`
- `use` `codex-rs/codex-client/src/transport.rs:9` `use futures::StreamExt;`
- `use` `codex-rs/codex-client/src/transport.rs:10` `use futures::stream::BoxStream;`
- `use` `codex-rs/codex-client/src/transport.rs:11` `use http::HeaderMap;`
- `use` `codex-rs/codex-client/src/transport.rs:12` `use http::Method;`
- `use` `codex-rs/codex-client/src/transport.rs:13` `use http::StatusCode;`
- `use` `codex-rs/codex-client/src/transport.rs:14` `use tracing::Level;`
- `use` `codex-rs/codex-client/src/transport.rs:15` `use tracing::enabled;`
- `use` `codex-rs/codex-client/src/transport.rs:16` `use tracing::trace;`
- `type` `codex-rs/codex-client/src/transport.rs:18` `pub type ByteStream = BoxStream<'static, Result<Bytes, TransportError>>;`
- `struct` `codex-rs/codex-client/src/transport.rs:20` `pub struct StreamResponse {`
- `trait` `codex-rs/codex-client/src/transport.rs:27` `pub trait HttpTransport: Send + Sync {`
- `fn` `codex-rs/codex-client/src/transport.rs:28` `async fn execute(&self, req: Request) -> Result<Response, TransportError>;`
- `fn` `codex-rs/codex-client/src/transport.rs:29` `async fn stream(&self, req: Request) -> Result<StreamResponse, TransportError>;`
- `struct` `codex-rs/codex-client/src/transport.rs:33` `pub struct ReqwestTransport {`
- `impl` `codex-rs/codex-client/src/transport.rs:37` `impl ReqwestTransport {`
- `fn` `codex-rs/codex-client/src/transport.rs:38` `pub fn new(client: reqwest::Client) -> Self {`
- `fn` `codex-rs/codex-client/src/transport.rs:44` `fn build(&self, req: Request) -> Result<CodexRequestBuilder, TransportError> {`
- `fn` `codex-rs/codex-client/src/transport.rs:113` `fn map_error(err: reqwest::Error) -> TransportError {`
- `impl` `codex-rs/codex-client/src/transport.rs:123` `impl HttpTransport for ReqwestTransport {`
- `fn` `codex-rs/codex-client/src/transport.rs:124` `async fn execute(&self, req: Request) -> Result<Response, TransportError> {`
- `fn` `codex-rs/codex-client/src/transport.rs:156` `async fn stream(&self, req: Request) -> Result<StreamResponse, TransportError> {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::default_client::CodexHttpClient;`
- `use crate::default_client::CodexRequestBuilder;`
- `use crate::error::TransportError;`
- `use crate::request::Request;`
- `use crate::request::RequestCompression;`
- `use crate::request::Response;`
- `use async_trait::async_trait;`
- `use bytes::Bytes;`
- `use futures::StreamExt;`
- `use futures::stream::BoxStream;`
- `use http::HeaderMap;`
- `use http::Method;`
- `use http::StatusCode;`
- `use tracing::Level;`
- `use tracing::enabled;`
- `use tracing::trace;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
