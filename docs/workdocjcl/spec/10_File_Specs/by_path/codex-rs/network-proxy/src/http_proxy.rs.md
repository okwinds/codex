# `codex-rs/network-proxy/src/http_proxy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `25081`
- sha256: `8e3bf6f21f6c127af75de8c58d789039c787699e336d6908594797206afb3370`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/http_proxy.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/http_proxy.rs:1` `use crate::config::NetworkMode;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:2` `use crate::network_policy::NetworkDecision;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:3` `use crate::network_policy::NetworkDecisionSource;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:4` `use crate::network_policy::NetworkPolicyDecider;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:5` `use crate::network_policy::NetworkPolicyDecision;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:6` `use crate::network_policy::NetworkPolicyRequest;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:7` `use crate::network_policy::NetworkPolicyRequestArgs;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:8` `use crate::network_policy::NetworkProtocol;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:9` `use crate::network_policy::evaluate_host_policy;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:10` `use crate::policy::normalize_host;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:11` `use crate::reasons::REASON_METHOD_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:12` `use crate::reasons::REASON_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:13` `use crate::reasons::REASON_PROXY_DISABLED;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:14` `use crate::responses::PolicyDecisionDetails;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:15` `use crate::responses::blocked_header_value;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:16` `use crate::responses::blocked_message_with_policy;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:17` `use crate::responses::blocked_text_response_with_policy;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:18` `use crate::responses::json_response;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:19` `use crate::responses::policy_decision_prefix;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:20` `use crate::runtime::unix_socket_permissions_supported;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:21` `use crate::state::BlockedRequest;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:22` `use crate::state::BlockedRequestArgs;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:23` `use crate::state::NetworkProxyState;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:24` `use crate::upstream::UpstreamClient;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:25` `use crate::upstream::proxy_for_connect;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:26` `use anyhow::Context as _;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:27` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:28` `use rama_core::Layer;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:29` `use rama_core::Service;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:30` `use rama_core::error::BoxError;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:31` `use rama_core::error::ErrorExt as _;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:32` `use rama_core::error::OpaqueError;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:33` `use rama_core::extensions::ExtensionsMut;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:34` `use rama_core::extensions::ExtensionsRef;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:35` `use rama_core::layer::AddInputExtensionLayer;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:36` `use rama_core::rt::Executor;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:37` `use rama_core::service::service_fn;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:38` `use rama_http::Body;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:39` `use rama_http::HeaderValue;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:40` `use rama_http::Request;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:41` `use rama_http::Response;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:42` `use rama_http::StatusCode;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:43` `use rama_http::layer::remove_header::RemoveRequestHeaderLayer;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:44` `use rama_http::layer::remove_header::RemoveResponseHeaderLayer;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:45` `use rama_http::matcher::MethodMatcher;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:46` `use rama_http_backend::client::proxy::layer::HttpProxyConnector;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:47` `use rama_http_backend::server::HttpServer;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:48` `use rama_http_backend::server::layer::upgrade::UpgradeLayer;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:49` `use rama_http_backend::server::layer::upgrade::Upgraded;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:50` `use rama_net::Protocol;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:51` `use rama_net::address::ProxyAddress;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:52` `use rama_net::client::ConnectorService;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:53` `use rama_net::client::EstablishedClientConnection;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:54` `use rama_net::http::RequestContext;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:55` `use rama_net::proxy::ProxyRequest;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:56` `use rama_net::proxy::ProxyTarget;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:57` `use rama_net::proxy::StreamForwardService;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:58` `use rama_net::stream::SocketInfo;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:59` `use rama_tcp::client::Request as TcpRequest;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:60` `use rama_tcp::client::service::TcpConnector;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:61` `use rama_tcp::server::TcpListener;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:62` `use rama_tls_rustls::client::TlsConnectorDataBuilder;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:63` `use rama_tls_rustls::client::TlsConnectorLayer;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:64` `use serde::Serialize;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:65` `use std::convert::Infallible;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:66` `use std::net::SocketAddr;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:67` `use std::sync::Arc;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:68` `use tracing::error;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:69` `use tracing::info;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:70` `use tracing::warn;`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:72` `pub async fn run_http_proxy(`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:115` `async fn http_connect_accept(`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:250` `async fn http_connect_proxy(upgraded: Upgraded) -> Result<(), Infallible> {`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:286` `async fn forward_connect_tunnel(`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:331` `async fn http_plain_proxy(`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:567` `async fn proxy_via_unix_socket(req: Request, socket_path: &str) -> Result<Response> {`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:601` `fn json_blocked(host: &str, reason: &str, details: Option<&PolicyDecisionDetails<'_>>) -> Response {`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:626` `fn blocked_text_with_details(reason: &str, details: &PolicyDecisionDetails<'_>) -> Response {`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:630` `async fn proxy_disabled_response(`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:664` `fn internal_error(context: &str, err: impl std::fmt::Display) -> Response {`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:669` `fn text_response(status: StatusCode, body: &str) -> Response {`
- `struct` `codex-rs/network-proxy/src/http_proxy.rs:678` `struct BlockedResponse<'a> {`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:690` `use super::*;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:692` `use crate::config::NetworkMode;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:693` `use crate::config::NetworkProxySettings;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:694` `use crate::runtime::network_proxy_state_for_policy;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:695` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:696` `use rama_http::Method;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:697` `use rama_http::Request;`
- `use` `codex-rs/network-proxy/src/http_proxy.rs:698` `use std::sync::Arc;`
- `fn` `codex-rs/network-proxy/src/http_proxy.rs:701` `async fn http_connect_accept_blocks_in_limited_mode() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::NetworkMode;`
- `use crate::network_policy::NetworkDecision;`
- `use crate::network_policy::NetworkDecisionSource;`
- `use crate::network_policy::NetworkPolicyDecider;`
- `use crate::network_policy::NetworkPolicyDecision;`
- `use crate::network_policy::NetworkPolicyRequest;`
- `use crate::network_policy::NetworkPolicyRequestArgs;`
- `use crate::network_policy::NetworkProtocol;`
- `use crate::network_policy::evaluate_host_policy;`
- `use crate::policy::normalize_host;`
- `use crate::reasons::REASON_METHOD_NOT_ALLOWED;`
- `use crate::reasons::REASON_NOT_ALLOWED;`
- `use crate::reasons::REASON_PROXY_DISABLED;`
- `use crate::responses::PolicyDecisionDetails;`
- `use crate::responses::blocked_header_value;`
- `use crate::responses::blocked_message_with_policy;`
- `use crate::responses::blocked_text_response_with_policy;`
- `use crate::responses::json_response;`
- `use crate::responses::policy_decision_prefix;`
- `use crate::runtime::unix_socket_permissions_supported;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
