# `codex-rs/network-proxy/src/runtime.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `33172`
- sha256: `89a5a3c9d8fcc4c81b1964476f1062b9145338360f833cf3c758d47771f607d0`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/runtime.rs` (read)

### Outputs / Side Effects
- writes to filesystem

## Public Surface (auto)
- `pub enum HostBlockReason {`
- `pub enum HostBlockDecision {`
- `pub struct BlockedRequest {`
- `pub struct BlockedRequestArgs {`
- `pub fn new(args: BlockedRequestArgs) -> Self {`
- `pub struct NetworkProxyState {`

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/runtime.rs:1` `use crate::config::NetworkMode;`
- `use` `codex-rs/network-proxy/src/runtime.rs:2` `use crate::config::NetworkProxyConfig;`
- `use` `codex-rs/network-proxy/src/runtime.rs:3` `use crate::policy::Host;`
- `use` `codex-rs/network-proxy/src/runtime.rs:4` `use crate::policy::is_loopback_host;`
- `use` `codex-rs/network-proxy/src/runtime.rs:5` `use crate::policy::is_non_public_ip;`
- `use` `codex-rs/network-proxy/src/runtime.rs:6` `use crate::policy::normalize_host;`
- `use` `codex-rs/network-proxy/src/runtime.rs:7` `use crate::reasons::REASON_DENIED;`
- `use` `codex-rs/network-proxy/src/runtime.rs:8` `use crate::reasons::REASON_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/runtime.rs:9` `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use` `codex-rs/network-proxy/src/runtime.rs:10` `use crate::state::NetworkProxyConstraints;`
- `use` `codex-rs/network-proxy/src/runtime.rs:11` `use crate::state::build_config_state;`
- `use` `codex-rs/network-proxy/src/runtime.rs:12` `use crate::state::validate_policy_against_constraints;`
- `use` `codex-rs/network-proxy/src/runtime.rs:13` `use anyhow::Context;`
- `use` `codex-rs/network-proxy/src/runtime.rs:14` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/runtime.rs:15` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/network-proxy/src/runtime.rs:16` `use globset::GlobSet;`
- `use` `codex-rs/network-proxy/src/runtime.rs:17` `use serde::Serialize;`
- `use` `codex-rs/network-proxy/src/runtime.rs:18` `use std::collections::HashSet;`
- `use` `codex-rs/network-proxy/src/runtime.rs:19` `use std::collections::VecDeque;`
- `use` `codex-rs/network-proxy/src/runtime.rs:20` `use std::net::IpAddr;`
- `use` `codex-rs/network-proxy/src/runtime.rs:21` `use std::path::Path;`
- `use` `codex-rs/network-proxy/src/runtime.rs:22` `use std::path::PathBuf;`
- `use` `codex-rs/network-proxy/src/runtime.rs:23` `use std::sync::Arc;`
- `use` `codex-rs/network-proxy/src/runtime.rs:24` `use std::time::Duration;`
- `use` `codex-rs/network-proxy/src/runtime.rs:25` `use std::time::SystemTime;`
- `use` `codex-rs/network-proxy/src/runtime.rs:26` `use time::OffsetDateTime;`
- `use` `codex-rs/network-proxy/src/runtime.rs:27` `use tokio::net::lookup_host;`
- `use` `codex-rs/network-proxy/src/runtime.rs:28` `use tokio::sync::RwLock;`
- `use` `codex-rs/network-proxy/src/runtime.rs:29` `use tokio::time::timeout;`
- `use` `codex-rs/network-proxy/src/runtime.rs:30` `use tracing::info;`
- `use` `codex-rs/network-proxy/src/runtime.rs:31` `use tracing::warn;`
- `const` `codex-rs/network-proxy/src/runtime.rs:33` `const MAX_BLOCKED_EVENTS: usize = 200;`
- `const` `codex-rs/network-proxy/src/runtime.rs:34` `const DNS_LOOKUP_TIMEOUT: Duration = Duration::from_secs(2);`
- `enum` `codex-rs/network-proxy/src/runtime.rs:37` `pub enum HostBlockReason {`
- `impl` `codex-rs/network-proxy/src/runtime.rs:43` `impl HostBlockReason {`
- `const` `codex-rs/network-proxy/src/runtime.rs:44` `pub const fn as_str(self) -> &'static str {`
- `impl` `codex-rs/network-proxy/src/runtime.rs:53` `impl std::fmt::Display for HostBlockReason {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:54` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `enum` `codex-rs/network-proxy/src/runtime.rs:60` `pub enum HostBlockDecision {`
- `struct` `codex-rs/network-proxy/src/runtime.rs:66` `pub struct BlockedRequest {`
- `struct` `codex-rs/network-proxy/src/runtime.rs:76` `pub struct BlockedRequestArgs {`
- `impl` `codex-rs/network-proxy/src/runtime.rs:85` `impl BlockedRequest {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:86` `pub fn new(args: BlockedRequestArgs) -> Self {`
- `impl` `codex-rs/network-proxy/src/runtime.rs:124` `impl LayerMtime {`
- `struct` `codex-rs/network-proxy/src/runtime.rs:132` `pub struct NetworkProxyState {`
- `impl` `codex-rs/network-proxy/src/runtime.rs:136` `impl std::fmt::Debug for NetworkProxyState {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:137` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `impl` `codex-rs/network-proxy/src/runtime.rs:144` `impl NetworkProxyState {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:145` `pub async fn new() -> Result<Self> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:152` `pub async fn current_cfg(&self) -> Result<NetworkProxyConfig> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:160` `pub async fn current_patterns(&self) -> Result<(Vec<String>, Vec<String>)> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:169` `pub async fn enabled(&self) -> Result<bool> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:175` `pub async fn force_reload(&self) -> Result<()> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:201` `pub async fn host_blocked(&self, host: &str, port: u16) -> Result<HostBlockDecision> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:268` `pub async fn record_blocked(&self, entry: BlockedRequest) -> Result<()> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:279` `pub async fn drain_blocked(&self) -> Result<Vec<BlockedRequest>> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:288` `pub async fn is_unix_socket_allowed(&self, path: &str) -> Result<bool> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:327` `pub async fn method_allowed(&self, method: &str) -> Result<bool> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:333` `pub async fn allow_upstream_proxy(&self) -> Result<bool> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:339` `pub async fn network_mode(&self) -> Result<NetworkMode> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:345` `pub async fn set_network_mode(&self, mode: NetworkMode) -> Result<()> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:369` `async fn reload_if_needed(&self) -> Result<()> {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:395` `async fn host_resolves_to_non_public_ip(host: &str, port: u16) -> bool {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:417` `fn log_policy_changes(previous: &NetworkProxyConfig, next: &NetworkProxyConfig) {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:430` `fn log_domain_list_changes(list_name: &str, previous: &[String], next: &[String]) {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:466` `fn is_explicit_local_allowlisted(allowed_domains: &[String], host: &Host) -> bool {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:480` `fn unix_timestamp() -> i64 {`
- `use` `codex-rs/network-proxy/src/runtime.rs:512` `use super::*;`
- `use` `codex-rs/network-proxy/src/runtime.rs:514` `use crate::config::NetworkProxyConfig;`
- `use` `codex-rs/network-proxy/src/runtime.rs:515` `use crate::config::NetworkProxySettings;`
- `use` `codex-rs/network-proxy/src/runtime.rs:516` `use crate::policy::compile_globset;`
- `use` `codex-rs/network-proxy/src/runtime.rs:517` `use crate::state::NetworkProxyConstraints;`
- `use` `codex-rs/network-proxy/src/runtime.rs:518` `use crate::state::validate_policy_against_constraints;`
- `use` `codex-rs/network-proxy/src/runtime.rs:519` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/network-proxy/src/runtime.rs:522` `async fn host_blocked_denied_wins_over_allowed() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:536` `async fn host_blocked_requires_allowlist_match() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:555` `async fn host_blocked_subdomain_wildcards_exclude_apex() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:572` `async fn host_blocked_rejects_loopback_when_local_binding_disabled() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:590` `async fn host_blocked_rejects_loopback_when_allowlist_is_wildcard() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:604` `async fn host_blocked_rejects_private_ip_literal_when_allowlist_is_wildcard() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:618` `async fn host_blocked_allows_loopback_when_explicitly_allowlisted_and_local_binding_disabled() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:632` `async fn host_blocked_allows_private_ip_literal_when_explicitly_allowlisted() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:646` `async fn host_blocked_rejects_scoped_ipv6_literal_when_not_allowlisted() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:660` `async fn host_blocked_allows_scoped_ipv6_literal_when_explicitly_allowlisted() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:674` `async fn host_blocked_rejects_private_ip_literals_when_local_binding_disabled() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:688` `async fn host_blocked_rejects_loopback_when_allowlist_empty() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:702` `fn validate_policy_against_constraints_disallows_widening_allowed_domains() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:720` `fn validate_policy_against_constraints_disallows_widening_mode() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:738` `fn validate_policy_against_constraints_allows_narrowing_wildcard_allowlist() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:756` `fn validate_policy_against_constraints_rejects_widening_wildcard_allowlist() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:774` `fn validate_policy_against_constraints_requires_managed_denied_domains_entries() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:792` `fn validate_policy_against_constraints_disallows_enabling_when_managed_disabled() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:809` `fn validate_policy_against_constraints_disallows_allow_local_binding_when_managed_disabled() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:827` `fn validate_policy_against_constraints_disallows_non_loopback_admin_without_managed_opt_in() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:845` `fn validate_policy_against_constraints_allows_non_loopback_admin_with_managed_opt_in() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:863` `fn compile_globset_is_case_insensitive() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:871` `fn compile_globset_excludes_apex_for_subdomain_patterns() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:880` `fn compile_globset_includes_apex_for_double_wildcard_patterns() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:889` `fn compile_globset_matches_all_with_star() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:897` `fn compile_globset_dedupes_patterns_without_changing_behavior() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:906` `fn compile_globset_rejects_invalid_patterns() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:913` `async fn unix_socket_allowlist_is_respected_on_macos() {`
- `fn` `codex-rs/network-proxy/src/runtime.rs:932` `async fn unix_socket_allowlist_resolves_symlinks() {`
- `use` `codex-rs/network-proxy/src/runtime.rs:933` `use std::os::unix::fs::symlink;`
- `use` `codex-rs/network-proxy/src/runtime.rs:934` `use tempfile::tempdir;`
- `fn` `codex-rs/network-proxy/src/runtime.rs:961` `async fn unix_socket_allowlist_is_rejected_on_non_macos() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::NetworkMode;`
- `use crate::config::NetworkProxyConfig;`
- `use crate::policy::Host;`
- `use crate::policy::is_loopback_host;`
- `use crate::policy::is_non_public_ip;`
- `use crate::policy::normalize_host;`
- `use crate::reasons::REASON_DENIED;`
- `use crate::reasons::REASON_NOT_ALLOWED;`
- `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use crate::state::NetworkProxyConstraints;`
- `use crate::state::build_config_state;`
- `use crate::state::validate_policy_against_constraints;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use globset::GlobSet;`
- `use serde::Serialize;`
- `use std::collections::HashSet;`
- `use std::collections::VecDeque;`
- `use std::net::IpAddr;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
