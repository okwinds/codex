# `codex-rs/network-proxy/src/policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `15003`
- sha256: `74368f64b1909425d39b1f5394136728b4994f948f8f745f461412434873f0cc`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/policy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct Host(String);`
- `pub fn parse(input: &str) -> Result<Self> {`
- `pub fn as_str(&self) -> &str {`
- `pub fn is_loopback_host(host: &Host) -> bool {`
- `pub fn is_non_public_ip(ip: IpAddr) -> bool {`
- `pub fn normalize_host(host: &str) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/policy.rs:2` `use crate::config::NetworkMode;`
- `use` `codex-rs/network-proxy/src/policy.rs:3` `use anyhow::Context;`
- `use` `codex-rs/network-proxy/src/policy.rs:4` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/policy.rs:5` `use anyhow::ensure;`
- `use` `codex-rs/network-proxy/src/policy.rs:6` `use globset::GlobBuilder;`
- `use` `codex-rs/network-proxy/src/policy.rs:7` `use globset::GlobSet;`
- `use` `codex-rs/network-proxy/src/policy.rs:8` `use globset::GlobSetBuilder;`
- `use` `codex-rs/network-proxy/src/policy.rs:9` `use std::collections::HashSet;`
- `use` `codex-rs/network-proxy/src/policy.rs:10` `use std::net::IpAddr;`
- `use` `codex-rs/network-proxy/src/policy.rs:11` `use std::net::Ipv4Addr;`
- `use` `codex-rs/network-proxy/src/policy.rs:12` `use std::net::Ipv6Addr;`
- `use` `codex-rs/network-proxy/src/policy.rs:13` `use url::Host as UrlHost;`
- `struct` `codex-rs/network-proxy/src/policy.rs:17` `pub struct Host(String);`
- `impl` `codex-rs/network-proxy/src/policy.rs:19` `impl Host {`
- `fn` `codex-rs/network-proxy/src/policy.rs:20` `pub fn parse(input: &str) -> Result<Self> {`
- `fn` `codex-rs/network-proxy/src/policy.rs:26` `pub fn as_str(&self) -> &str {`
- `fn` `codex-rs/network-proxy/src/policy.rs:32` `pub fn is_loopback_host(host: &Host) -> bool {`
- `fn` `codex-rs/network-proxy/src/policy.rs:44` `pub fn is_non_public_ip(ip: IpAddr) -> bool {`
- `fn` `codex-rs/network-proxy/src/policy.rs:51` `fn is_non_public_ipv4(ip: Ipv4Addr) -> bool {`
- `fn` `codex-rs/network-proxy/src/policy.rs:71` `fn ipv4_in_cidr(ip: Ipv4Addr, base: [u8; 4], prefix: u8) -> bool {`
- `fn` `codex-rs/network-proxy/src/policy.rs:82` `fn is_non_public_ipv6(ip: Ipv6Addr) -> bool {`
- `fn` `codex-rs/network-proxy/src/policy.rs:100` `pub fn normalize_host(host: &str) -> String {`
- `fn` `codex-rs/network-proxy/src/policy.rs:120` `fn normalize_dns_host(host: &str) -> String {`
- `fn` `codex-rs/network-proxy/src/policy.rs:125` `fn normalize_pattern(pattern: &str) -> String {`
- `impl` `codex-rs/network-proxy/src/policy.rs:179` `impl DomainPattern {`
- `fn` `codex-rs/network-proxy/src/policy.rs:218` `fn parse_domain(domain: &str, build: impl FnOnce(String) -> Self) -> Self {`
- `fn` `codex-rs/network-proxy/src/policy.rs:257` `fn parse_domain_for_constraints(domain: &str) -> String {`
- `fn` `codex-rs/network-proxy/src/policy.rs:276` `fn expand_domain_pattern(pattern: &str) -> Vec<String> {`
- `fn` `codex-rs/network-proxy/src/policy.rs:289` `fn normalize_domain(domain: &str) -> String {`
- `fn` `codex-rs/network-proxy/src/policy.rs:293` `fn domain_eq(left: &str, right: &str) -> bool {`
- `fn` `codex-rs/network-proxy/src/policy.rs:297` `fn is_subdomain_or_equal(child: &str, parent: &str) -> bool {`
- `fn` `codex-rs/network-proxy/src/policy.rs:306` `fn is_strict_subdomain(child: &str, parent: &str) -> bool {`
- `use` `codex-rs/network-proxy/src/policy.rs:314` `use super::*;`
- `use` `codex-rs/network-proxy/src/policy.rs:316` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/network-proxy/src/policy.rs:319` `fn method_allowed_full_allows_everything() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:326` `fn method_allowed_limited_allows_only_safe_methods() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:335` `fn compile_globset_normalizes_trailing_dots() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:343` `fn compile_globset_normalizes_wildcards() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:351` `fn compile_globset_normalizes_apex_and_subdomains() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:359` `fn compile_globset_normalizes_bracketed_ipv6_literals() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:366` `fn is_loopback_host_handles_localhost_variants() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:374` `fn is_loopback_host_handles_ip_literals() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:381` `fn is_non_public_ip_rejects_private_and_loopback_ranges() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:405` `fn normalize_host_lowercases_and_trims() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:410` `fn normalize_host_strips_port_for_host_port() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:415` `fn normalize_host_preserves_unbracketed_ipv6() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:420` `fn normalize_host_strips_trailing_dot() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:426` `fn normalize_host_strips_trailing_dot_with_port() {`
- `fn` `codex-rs/network-proxy/src/policy.rs:431` `fn normalize_host_strips_brackets_for_ipv6() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::NetworkMode;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::ensure;`
- `use globset::GlobBuilder;`
- `use globset::GlobSet;`
- `use globset::GlobSetBuilder;`
- `use std::collections::HashSet;`
- `use std::net::IpAddr;`
- `use std::net::Ipv4Addr;`
- `use std::net::Ipv6Addr;`
- `use url::Host as UrlHost;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
