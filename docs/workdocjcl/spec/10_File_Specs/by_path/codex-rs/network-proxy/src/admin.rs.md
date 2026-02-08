# `codex-rs/network-proxy/src/admin.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5551`
- sha256: `a6a0859fb58afc3d3102121ea71f681793c66db9ffaf268a26066c109133db52`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/admin.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/admin.rs:1` `use crate::config::NetworkMode;`
- `use` `codex-rs/network-proxy/src/admin.rs:2` `use crate::responses::json_response;`
- `use` `codex-rs/network-proxy/src/admin.rs:3` `use crate::responses::text_response;`
- `use` `codex-rs/network-proxy/src/admin.rs:4` `use crate::state::NetworkProxyState;`
- `use` `codex-rs/network-proxy/src/admin.rs:5` `use anyhow::Context;`
- `use` `codex-rs/network-proxy/src/admin.rs:6` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/admin.rs:7` `use rama_core::rt::Executor;`
- `use` `codex-rs/network-proxy/src/admin.rs:8` `use rama_core::service::service_fn;`
- `use` `codex-rs/network-proxy/src/admin.rs:9` `use rama_http::Body;`
- `use` `codex-rs/network-proxy/src/admin.rs:10` `use rama_http::Request;`
- `use` `codex-rs/network-proxy/src/admin.rs:11` `use rama_http::Response;`
- `use` `codex-rs/network-proxy/src/admin.rs:12` `use rama_http::StatusCode;`
- `use` `codex-rs/network-proxy/src/admin.rs:13` `use rama_http_backend::server::HttpServer;`
- `use` `codex-rs/network-proxy/src/admin.rs:14` `use rama_tcp::server::TcpListener;`
- `use` `codex-rs/network-proxy/src/admin.rs:15` `use serde::Deserialize;`
- `use` `codex-rs/network-proxy/src/admin.rs:16` `use serde::Serialize;`
- `use` `codex-rs/network-proxy/src/admin.rs:17` `use std::convert::Infallible;`
- `use` `codex-rs/network-proxy/src/admin.rs:18` `use std::net::SocketAddr;`
- `use` `codex-rs/network-proxy/src/admin.rs:19` `use std::sync::Arc;`
- `use` `codex-rs/network-proxy/src/admin.rs:20` `use tracing::error;`
- `use` `codex-rs/network-proxy/src/admin.rs:21` `use tracing::info;`
- `fn` `codex-rs/network-proxy/src/admin.rs:23` `pub async fn run_admin_api(state: Arc<NetworkProxyState>, addr: SocketAddr) -> Result<()> {`
- `fn` `codex-rs/network-proxy/src/admin.rs:44` `async fn handle_admin_request(`
- `const` `codex-rs/network-proxy/src/admin.rs:48` `const MODE_BODY_LIMIT: usize = 8 * 1024;`
- `struct` `codex-rs/network-proxy/src/admin.rs:136` `struct ModeUpdate {`
- `struct` `codex-rs/network-proxy/src/admin.rs:141` `struct PatternsResponse {`
- `struct` `codex-rs/network-proxy/src/admin.rs:147` `struct BlockedResponse<T> {`
- `struct` `codex-rs/network-proxy/src/admin.rs:152` `struct ModeUpdateResponse {`
- `struct` `codex-rs/network-proxy/src/admin.rs:158` `struct ReloadResponse {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::NetworkMode;`
- `use crate::responses::json_response;`
- `use crate::responses::text_response;`
- `use crate::state::NetworkProxyState;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use rama_core::rt::Executor;`
- `use rama_core::service::service_fn;`
- `use rama_http::Body;`
- `use rama_http::Request;`
- `use rama_http::Response;`
- `use rama_http::StatusCode;`
- `use rama_http_backend::server::HttpServer;`
- `use rama_tcp::server::TcpListener;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::convert::Infallible;`
- `use std::net::SocketAddr;`
- `use std::sync::Arc;`
- `use tracing::error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
