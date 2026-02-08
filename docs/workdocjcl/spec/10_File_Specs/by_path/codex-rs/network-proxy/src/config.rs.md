# `codex-rs/network-proxy/src/config.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `14722`
- sha256: `67d582b94785bcfa09d34a7b86fabc6b5131576ed10ddd941a3c6585daa3d78d`
- generated_utc: `2026-02-08T10:45:38Z`

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
- `impl` `codex-rs/network-proxy/src/config.rs:49` `impl Default for NetworkProxySettings {`
- `fn` `codex-rs/network-proxy/src/config.rs:50` `fn default() -> Self {`
- `enum` `codex-rs/network-proxy/src/config.rs:72` `pub enum NetworkMode {`
- `impl` `codex-rs/network-proxy/src/config.rs:82` `impl NetworkMode {`
- `fn` `codex-rs/network-proxy/src/config.rs:83` `pub fn allows_method(self, method: &str) -> bool {`
- `fn` `codex-rs/network-proxy/src/config.rs:91` `fn default_proxy_url() -> String {`
- `fn` `codex-rs/network-proxy/src/config.rs:95` `fn default_admin_url() -> String {`
- `fn` `codex-rs/network-proxy/src/config.rs:99` `fn default_socks_url() -> String {`
- `fn` `codex-rs/network-proxy/src/config.rs:104` `fn clamp_non_loopback(addr: SocketAddr, allow_non_loopback: bool, name: &str) -> SocketAddr {`
- `struct` `codex-rs/network-proxy/src/config.rs:172` `pub struct RuntimeConfig {`
- `fn` `codex-rs/network-proxy/src/config.rs:178` `pub fn resolve_runtime(cfg: &NetworkProxyConfig) -> Result<RuntimeConfig> {`
- `fn` `codex-rs/network-proxy/src/config.rs:195` `fn resolve_addr(url: &str, default_port: u16) -> Result<SocketAddr> {`
- `struct` `codex-rs/network-proxy/src/config.rs:209` `struct SocketAddressParts {`
- `fn` `codex-rs/network-proxy/src/config.rs:214` `fn parse_host_port(url: &str, default_port: u16) -> Result<SocketAddressParts> {`
- `fn` `codex-rs/network-proxy/src/config.rs:251` `fn parse_host_port_fallback(input: &str, default_port: u16) -> Result<SocketAddressParts> {`
- `use` `codex-rs/network-proxy/src/config.rs:305` `use super::*;`
- `use` `codex-rs/network-proxy/src/config.rs:307` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/network-proxy/src/config.rs:310` `fn parse_host_port_defaults_for_empty_string() {`
- `fn` `codex-rs/network-proxy/src/config.rs:315` `fn parse_host_port_defaults_for_whitespace() {`
- `fn` `codex-rs/network-proxy/src/config.rs:320` `fn parse_host_port_parses_host_port_without_scheme() {`
- `fn` `codex-rs/network-proxy/src/config.rs:331` `fn parse_host_port_parses_host_port_with_scheme_and_path() {`
- `fn` `codex-rs/network-proxy/src/config.rs:342` `fn parse_host_port_strips_userinfo() {`
- `fn` `codex-rs/network-proxy/src/config.rs:353` `fn parse_host_port_parses_ipv6_with_brackets() {`
- `fn` `codex-rs/network-proxy/src/config.rs:364` `fn parse_host_port_does_not_treat_unbracketed_ipv6_as_host_port() {`
- `fn` `codex-rs/network-proxy/src/config.rs:375` `fn parse_host_port_falls_back_to_default_port_when_port_is_invalid() {`
- `fn` `codex-rs/network-proxy/src/config.rs:386` `fn resolve_addr_maps_localhost_to_loopback() {`
- `fn` `codex-rs/network-proxy/src/config.rs:394` `fn resolve_addr_parses_ip_literals() {`
- `fn` `codex-rs/network-proxy/src/config.rs:402` `fn resolve_addr_parses_ipv6_literals() {`
- `fn` `codex-rs/network-proxy/src/config.rs:410` `fn resolve_addr_falls_back_to_loopback_for_hostnames() {`
- `fn` `codex-rs/network-proxy/src/config.rs:418` `fn clamp_bind_addrs_allows_non_loopback_when_enabled() {`
- `fn` `codex-rs/network-proxy/src/config.rs:437` `fn clamp_bind_addrs_forces_loopback_when_unix_sockets_enabled() {`

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
