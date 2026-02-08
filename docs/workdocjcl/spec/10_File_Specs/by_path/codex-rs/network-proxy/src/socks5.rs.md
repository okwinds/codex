# `codex-rs/network-proxy/src/socks5.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `13683`
- sha256: `f4cc44ccc0f6399e21e1316e63d9341502bf0782895b7a18f9a93543d60f9b09`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/socks5.rs` (read)

### Outputs / Side Effects
- performs network I/O

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/socks5.rs:1` `use crate::config::NetworkMode;`
- `use` `codex-rs/network-proxy/src/socks5.rs:2` `use crate::network_policy::NetworkDecision;`
- `use` `codex-rs/network-proxy/src/socks5.rs:3` `use crate::network_policy::NetworkDecisionSource;`
- `use` `codex-rs/network-proxy/src/socks5.rs:4` `use crate::network_policy::NetworkPolicyDecider;`
- `use` `codex-rs/network-proxy/src/socks5.rs:5` `use crate::network_policy::NetworkPolicyDecision;`
- `use` `codex-rs/network-proxy/src/socks5.rs:6` `use crate::network_policy::NetworkPolicyRequest;`
- `use` `codex-rs/network-proxy/src/socks5.rs:7` `use crate::network_policy::NetworkPolicyRequestArgs;`
- `use` `codex-rs/network-proxy/src/socks5.rs:8` `use crate::network_policy::NetworkProtocol;`
- `use` `codex-rs/network-proxy/src/socks5.rs:9` `use crate::network_policy::evaluate_host_policy;`
- `use` `codex-rs/network-proxy/src/socks5.rs:10` `use crate::policy::normalize_host;`
- `use` `codex-rs/network-proxy/src/socks5.rs:11` `use crate::reasons::REASON_METHOD_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/socks5.rs:12` `use crate::reasons::REASON_PROXY_DISABLED;`
- `use` `codex-rs/network-proxy/src/socks5.rs:13` `use crate::responses::PolicyDecisionDetails;`
- `use` `codex-rs/network-proxy/src/socks5.rs:14` `use crate::responses::blocked_message_with_policy;`
- `use` `codex-rs/network-proxy/src/socks5.rs:15` `use crate::state::BlockedRequest;`
- `use` `codex-rs/network-proxy/src/socks5.rs:16` `use crate::state::BlockedRequestArgs;`
- `use` `codex-rs/network-proxy/src/socks5.rs:17` `use crate::state::NetworkProxyState;`
- `use` `codex-rs/network-proxy/src/socks5.rs:18` `use anyhow::Context as _;`
- `use` `codex-rs/network-proxy/src/socks5.rs:19` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/socks5.rs:20` `use rama_core::Layer;`
- `use` `codex-rs/network-proxy/src/socks5.rs:21` `use rama_core::Service;`
- `use` `codex-rs/network-proxy/src/socks5.rs:22` `use rama_core::error::BoxError;`
- `use` `codex-rs/network-proxy/src/socks5.rs:23` `use rama_core::extensions::ExtensionsRef;`
- `use` `codex-rs/network-proxy/src/socks5.rs:24` `use rama_core::layer::AddInputExtensionLayer;`
- `use` `codex-rs/network-proxy/src/socks5.rs:25` `use rama_core::service::service_fn;`
- `use` `codex-rs/network-proxy/src/socks5.rs:26` `use rama_net::client::EstablishedClientConnection;`
- `use` `codex-rs/network-proxy/src/socks5.rs:27` `use rama_net::stream::SocketInfo;`
- `use` `codex-rs/network-proxy/src/socks5.rs:28` `use rama_socks5::Socks5Acceptor;`
- `use` `codex-rs/network-proxy/src/socks5.rs:29` `use rama_socks5::server::DefaultConnector;`
- `use` `codex-rs/network-proxy/src/socks5.rs:30` `use rama_socks5::server::DefaultUdpRelay;`
- `use` `codex-rs/network-proxy/src/socks5.rs:31` `use rama_socks5::server::udp::RelayRequest;`
- `use` `codex-rs/network-proxy/src/socks5.rs:32` `use rama_socks5::server::udp::RelayResponse;`
- `use` `codex-rs/network-proxy/src/socks5.rs:33` `use rama_tcp::TcpStream;`
- `use` `codex-rs/network-proxy/src/socks5.rs:34` `use rama_tcp::client::Request as TcpRequest;`
- `use` `codex-rs/network-proxy/src/socks5.rs:35` `use rama_tcp::client::service::TcpConnector;`
- `use` `codex-rs/network-proxy/src/socks5.rs:36` `use rama_tcp::server::TcpListener;`
- `use` `codex-rs/network-proxy/src/socks5.rs:37` `use std::io;`
- `use` `codex-rs/network-proxy/src/socks5.rs:38` `use std::net::SocketAddr;`
- `use` `codex-rs/network-proxy/src/socks5.rs:39` `use std::sync::Arc;`
- `use` `codex-rs/network-proxy/src/socks5.rs:40` `use tracing::error;`
- `use` `codex-rs/network-proxy/src/socks5.rs:41` `use tracing::info;`
- `use` `codex-rs/network-proxy/src/socks5.rs:42` `use tracing::warn;`
- `fn` `codex-rs/network-proxy/src/socks5.rs:44` `pub async fn run_socks5(`
- `fn` `codex-rs/network-proxy/src/socks5.rs:105` `async fn handle_socks5_tcp(`
- `fn` `codex-rs/network-proxy/src/socks5.rs:242` `async fn inspect_socks5_udp(`
- `fn` `codex-rs/network-proxy/src/socks5.rs:373` `fn policy_denied_error(reason: &str, details: &PolicyDecisionDetails<'_>) -> io::Error {`

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
- `use crate::reasons::REASON_PROXY_DISABLED;`
- `use crate::responses::PolicyDecisionDetails;`
- `use crate::responses::blocked_message_with_policy;`
- `use crate::state::BlockedRequest;`
- `use crate::state::BlockedRequestArgs;`
- `use crate::state::NetworkProxyState;`
- `use anyhow::Context as _;`
- `use anyhow::Result;`
- `use rama_core::Layer;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
