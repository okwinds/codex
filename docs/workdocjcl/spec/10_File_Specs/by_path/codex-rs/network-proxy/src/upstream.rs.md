# `codex-rs/network-proxy/src/upstream.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5528`
- sha256: `d703342854bb7acd44a3e945c53f57279409efd0529ad9f79944ea935eef3298`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/upstream.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/upstream.rs:1` `use rama_core::Layer;`
- `use` `codex-rs/network-proxy/src/upstream.rs:2` `use rama_core::Service;`
- `use` `codex-rs/network-proxy/src/upstream.rs:3` `use rama_core::error::BoxError;`
- `use` `codex-rs/network-proxy/src/upstream.rs:4` `use rama_core::error::ErrorContext as _;`
- `use` `codex-rs/network-proxy/src/upstream.rs:5` `use rama_core::error::OpaqueError;`
- `use` `codex-rs/network-proxy/src/upstream.rs:6` `use rama_core::extensions::ExtensionsMut;`
- `use` `codex-rs/network-proxy/src/upstream.rs:7` `use rama_core::extensions::ExtensionsRef;`
- `use` `codex-rs/network-proxy/src/upstream.rs:8` `use rama_core::service::BoxService;`
- `use` `codex-rs/network-proxy/src/upstream.rs:9` `use rama_http::Body;`
- `use` `codex-rs/network-proxy/src/upstream.rs:10` `use rama_http::Request;`
- `use` `codex-rs/network-proxy/src/upstream.rs:11` `use rama_http::Response;`
- `use` `codex-rs/network-proxy/src/upstream.rs:12` `use rama_http::layer::version_adapter::RequestVersionAdapter;`
- `use` `codex-rs/network-proxy/src/upstream.rs:13` `use rama_http_backend::client::HttpClientService;`
- `use` `codex-rs/network-proxy/src/upstream.rs:14` `use rama_http_backend::client::HttpConnector;`
- `use` `codex-rs/network-proxy/src/upstream.rs:15` `use rama_http_backend::client::proxy::layer::HttpProxyConnectorLayer;`
- `use` `codex-rs/network-proxy/src/upstream.rs:16` `use rama_net::address::ProxyAddress;`
- `use` `codex-rs/network-proxy/src/upstream.rs:17` `use rama_net::client::EstablishedClientConnection;`
- `use` `codex-rs/network-proxy/src/upstream.rs:18` `use rama_net::http::RequestContext;`
- `use` `codex-rs/network-proxy/src/upstream.rs:19` `use rama_tcp::client::service::TcpConnector;`
- `use` `codex-rs/network-proxy/src/upstream.rs:20` `use rama_tls_boring::client::TlsConnectorDataBuilder;`
- `use` `codex-rs/network-proxy/src/upstream.rs:21` `use rama_tls_boring::client::TlsConnectorLayer;`
- `use` `codex-rs/network-proxy/src/upstream.rs:22` `use tracing::warn;`
- `use` `codex-rs/network-proxy/src/upstream.rs:25` `use rama_unix::client::UnixConnector;`
- `struct` `codex-rs/network-proxy/src/upstream.rs:28` `struct ProxyConfig {`
- `impl` `codex-rs/network-proxy/src/upstream.rs:34` `impl ProxyConfig {`
- `fn` `codex-rs/network-proxy/src/upstream.rs:35` `fn from_env() -> Self {`
- `fn` `codex-rs/network-proxy/src/upstream.rs:42` `fn proxy_for_request(&self, req: &Request) -> Option<ProxyAddress> {`
- `fn` `codex-rs/network-proxy/src/upstream.rs:49` `fn proxy_for_protocol(&self, is_secure: bool) -> Option<ProxyAddress> {`
- `fn` `codex-rs/network-proxy/src/upstream.rs:61` `fn read_proxy_env(keys: &[&str]) -> Option<ProxyAddress> {`
- `impl` `codex-rs/network-proxy/src/upstream.rs:104` `impl UpstreamClient {`
- `fn` `codex-rs/network-proxy/src/upstream.rs:122` `fn new(proxy_config: ProxyConfig) -> Self {`
- `impl` `codex-rs/network-proxy/src/upstream.rs:131` `impl Service<Request<Body>> for UpstreamClient {`
- `type` `codex-rs/network-proxy/src/upstream.rs:132` `type Output = Response;`
- `type` `codex-rs/network-proxy/src/upstream.rs:133` `type Error = OpaqueError;`
- `fn` `codex-rs/network-proxy/src/upstream.rs:135` `async fn serve(&self, mut req: Request<Body>) -> Result<Self::Output, Self::Error> {`
- `fn` `codex-rs/network-proxy/src/upstream.rs:161` `fn build_http_connector() -> BoxService<`
- `fn` `codex-rs/network-proxy/src/upstream.rs:178` `fn build_unix_connector(`

## Dependencies (auto sample)
### Imports / Includes
- `use rama_core::Layer;`
- `use rama_core::Service;`
- `use rama_core::error::BoxError;`
- `use rama_core::error::ErrorContext as _;`
- `use rama_core::error::OpaqueError;`
- `use rama_core::extensions::ExtensionsMut;`
- `use rama_core::extensions::ExtensionsRef;`
- `use rama_core::service::BoxService;`
- `use rama_http::Body;`
- `use rama_http::Request;`
- `use rama_http::Response;`
- `use rama_http::layer::version_adapter::RequestVersionAdapter;`
- `use rama_http_backend::client::HttpClientService;`
- `use rama_http_backend::client::HttpConnector;`
- `use rama_http_backend::client::proxy::layer::HttpProxyConnectorLayer;`
- `use rama_net::address::ProxyAddress;`
- `use rama_net::client::EstablishedClientConnection;`
- `use rama_net::http::RequestContext;`
- `use rama_tcp::client::service::TcpConnector;`
- `use rama_tls_boring::client::TlsConnectorDataBuilder;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
