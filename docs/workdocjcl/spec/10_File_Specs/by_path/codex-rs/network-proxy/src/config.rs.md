# `codex-rs/network-proxy/src/config.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15031`
- sha256: `dbfe245bfa6495b14be4afd7234943527a1c4730e273799055b3713a5d2d1a7c`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/config.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct NetworkProxyConfig {`
- `pub struct NetworkProxySettings {`
- `pub struct NetworkPolicy {`
- `pub enum NetworkMode {`
- `pub fn allows_method(self, method: &str) -> bool {`
- `pub struct RuntimeConfig {`
- `pub fn resolve_runtime(cfg: &NetworkProxyConfig) -> Result<RuntimeConfig> {`

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/config.rs:1` `use anyhow::Context;`
- `use` `codex-rs/network-proxy/src/config.rs:2` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/config.rs:3` `use anyhow::bail;`
- `use` `codex-rs/network-proxy/src/config.rs:4` `use serde::Deserialize;`
- `use` `codex-rs/network-proxy/src/config.rs:5` `use serde::Serialize;`
- `use` `codex-rs/network-proxy/src/config.rs:6` `use std::net::IpAddr;`
- `use` `codex-rs/network-proxy/src/config.rs:7` `use std::net::SocketAddr;`
- `use` `codex-rs/network-proxy/src/config.rs:8` `use tracing::warn;`
- `use` `codex-rs/network-proxy/src/config.rs:9` `use url::Url;`
- `struct` `codex-rs/network-proxy/src/config.rs:12` `pub struct NetworkProxyConfig {`
- `struct` `codex-rs/network-proxy/src/config.rs:18` `pub struct NetworkProxySettings {`
- `impl` `codex-rs/network-proxy/src/config.rs:43` `impl Default for NetworkProxySettings {`
- `fn` `codex-rs/network-proxy/src/config.rs:44` `fn default() -> Self {`
- `struct` `codex-rs/network-proxy/src/config.rs:62` `pub struct NetworkPolicy {`
- `enum` `codex-rs/network-proxy/src/config.rs:75` `pub enum NetworkMode {`
- `impl` `codex-rs/network-proxy/src/config.rs:85` `impl NetworkMode {`
- `fn` `codex-rs/network-proxy/src/config.rs:86` `pub fn allows_method(self, method: &str) -> bool {`
- `fn` `codex-rs/network-proxy/src/config.rs:94` `fn default_proxy_url() -> String {`
- `fn` `codex-rs/network-proxy/src/config.rs:98` `fn default_admin_url() -> String {`
- `fn` `codex-rs/network-proxy/src/config.rs:102` `fn default_socks_url() -> String {`
- `fn` `codex-rs/network-proxy/src/config.rs:107` `fn clamp_non_loopback(addr: SocketAddr, allow_non_loopback: bool, name: &str) -> SocketAddr {`
- `struct` `codex-rs/network-proxy/src/config.rs:175` `pub struct RuntimeConfig {`
- `fn` `codex-rs/network-proxy/src/config.rs:181` `pub fn resolve_runtime(cfg: &NetworkProxyConfig) -> Result<RuntimeConfig> {`
- `fn` `codex-rs/network-proxy/src/config.rs:210` `fn resolve_addr(url: &str, default_port: u16) -> Result<SocketAddr> {`
- `struct` `codex-rs/network-proxy/src/config.rs:224` `struct SocketAddressParts {`
- `fn` `codex-rs/network-proxy/src/config.rs:229` `fn parse_host_port(url: &str, default_port: u16) -> Result<SocketAddressParts> {`
- `fn` `codex-rs/network-proxy/src/config.rs:266` `fn parse_host_port_fallback(input: &str, default_port: u16) -> Result<SocketAddressParts> {`
- `use` `codex-rs/network-proxy/src/config.rs:320` `use super::*;`
- `use` `codex-rs/network-proxy/src/config.rs:322` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/network-proxy/src/config.rs:325` `fn parse_host_port_defaults_for_empty_string() {`
- `fn` `codex-rs/network-proxy/src/config.rs:330` `fn parse_host_port_defaults_for_whitespace() {`
- `fn` `codex-rs/network-proxy/src/config.rs:335` `fn parse_host_port_parses_host_port_without_scheme() {`
- `fn` `codex-rs/network-proxy/src/config.rs:346` `fn parse_host_port_parses_host_port_with_scheme_and_path() {`
- `fn` `codex-rs/network-proxy/src/config.rs:357` `fn parse_host_port_strips_userinfo() {`
- `fn` `codex-rs/network-proxy/src/config.rs:368` `fn parse_host_port_parses_ipv6_with_brackets() {`
- `fn` `codex-rs/network-proxy/src/config.rs:379` `fn parse_host_port_does_not_treat_unbracketed_ipv6_as_host_port() {`
- `fn` `codex-rs/network-proxy/src/config.rs:390` `fn parse_host_port_falls_back_to_default_port_when_port_is_invalid() {`
- `fn` `codex-rs/network-proxy/src/config.rs:401` `fn resolve_addr_maps_localhost_to_loopback() {`
- `fn` `codex-rs/network-proxy/src/config.rs:409` `fn resolve_addr_parses_ip_literals() {`
- `fn` `codex-rs/network-proxy/src/config.rs:417` `fn resolve_addr_parses_ipv6_literals() {`
- `fn` `codex-rs/network-proxy/src/config.rs:425` `fn resolve_addr_falls_back_to_loopback_for_hostnames() {`
- `fn` `codex-rs/network-proxy/src/config.rs:433` `fn clamp_bind_addrs_allows_non_loopback_when_enabled() {`
- `fn` `codex-rs/network-proxy/src/config.rs:452` `fn clamp_bind_addrs_forces_loopback_when_unix_sockets_enabled() {`

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::bail;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use std::net::IpAddr;`
- `use std::net::SocketAddr;`
- `use tracing::warn;`
- `use url::Url;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
