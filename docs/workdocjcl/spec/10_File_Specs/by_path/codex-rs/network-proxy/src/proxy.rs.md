# `codex-rs/network-proxy/src/proxy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `6132`
- sha256: `075ebab4eabb84c4a4d53d5204ae29fb8f9928ab20ead3ce06fa70e8d461b3a1`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/proxy.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct Args {}`
- `pub struct NetworkProxyBuilder {`
- `pub fn state(mut self, state: Arc<NetworkProxyState>) -> Self {`
- `pub fn http_addr(mut self, addr: SocketAddr) -> Self {`
- `pub fn admin_addr(mut self, addr: SocketAddr) -> Self {`
- `pub fn policy_decider_arc(mut self, decider: Arc<dyn NetworkPolicyDecider>) -> Self {`
- `pub struct NetworkProxy {`
- `pub fn builder() -> NetworkProxyBuilder {`
- `pub struct NetworkProxyHandle {`

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/proxy.rs:1` `use crate::admin;`
- `use` `codex-rs/network-proxy/src/proxy.rs:2` `use crate::config;`
- `use` `codex-rs/network-proxy/src/proxy.rs:3` `use crate::http_proxy;`
- `use` `codex-rs/network-proxy/src/proxy.rs:4` `use crate::network_policy::NetworkPolicyDecider;`
- `use` `codex-rs/network-proxy/src/proxy.rs:5` `use crate::runtime::unix_socket_permissions_supported;`
- `use` `codex-rs/network-proxy/src/proxy.rs:6` `use crate::socks5;`
- `use` `codex-rs/network-proxy/src/proxy.rs:7` `use crate::state::NetworkProxyState;`
- `use` `codex-rs/network-proxy/src/proxy.rs:8` `use anyhow::Context;`
- `use` `codex-rs/network-proxy/src/proxy.rs:9` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/proxy.rs:10` `use clap::Parser;`
- `use` `codex-rs/network-proxy/src/proxy.rs:11` `use std::net::SocketAddr;`
- `use` `codex-rs/network-proxy/src/proxy.rs:12` `use std::sync::Arc;`
- `use` `codex-rs/network-proxy/src/proxy.rs:13` `use tokio::task::JoinHandle;`
- `use` `codex-rs/network-proxy/src/proxy.rs:14` `use tracing::warn;`
- `struct` `codex-rs/network-proxy/src/proxy.rs:18` `pub struct Args {}`
- `struct` `codex-rs/network-proxy/src/proxy.rs:21` `pub struct NetworkProxyBuilder {`
- `impl` `codex-rs/network-proxy/src/proxy.rs:28` `impl NetworkProxyBuilder {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:29` `pub fn state(mut self, state: Arc<NetworkProxyState>) -> Self {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:34` `pub fn http_addr(mut self, addr: SocketAddr) -> Self {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:39` `pub fn admin_addr(mut self, addr: SocketAddr) -> Self {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:52` `pub fn policy_decider_arc(mut self, decider: Arc<dyn NetworkPolicyDecider>) -> Self {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:57` `pub async fn build(self) -> Result<NetworkProxy> {`
- `struct` `codex-rs/network-proxy/src/proxy.rs:83` `pub struct NetworkProxy {`
- `impl` `codex-rs/network-proxy/src/proxy.rs:91` `impl NetworkProxy {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:92` `pub fn builder() -> NetworkProxyBuilder {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:96` `pub async fn run(&self) -> Result<NetworkProxyHandle> {`
- `struct` `codex-rs/network-proxy/src/proxy.rs:133` `pub struct NetworkProxyHandle {`
- `impl` `codex-rs/network-proxy/src/proxy.rs:140` `impl NetworkProxyHandle {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:141` `fn noop() -> Self {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:150` `pub async fn wait(mut self) -> Result<()> {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:169` `pub async fn shutdown(mut self) -> Result<()> {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:181` `async fn abort_task(task: Option<JoinHandle<Result<()>>>) {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:188` `async fn abort_tasks(`
- `impl` `codex-rs/network-proxy/src/proxy.rs:198` `impl Drop for NetworkProxyHandle {`
- `fn` `codex-rs/network-proxy/src/proxy.rs:199` `fn drop(&mut self) {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::admin;`
- `use crate::config;`
- `use crate::http_proxy;`
- `use crate::network_policy::NetworkPolicyDecider;`
- `use crate::runtime::unix_socket_permissions_supported;`
- `use crate::socks5;`
- `use crate::state::NetworkProxyState;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use clap::Parser;`
- `use std::net::SocketAddr;`
- `use std::sync::Arc;`
- `use tokio::task::JoinHandle;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
