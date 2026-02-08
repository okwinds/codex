# `codex-rs/network-proxy/src/network_policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10253`
- sha256: `e89ab4245b46443e76053e73e2ababb68655f7883a772da5c8e0ad83f68997b0`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/network_policy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum NetworkProtocol {`
- `pub enum NetworkPolicyDecision {`
- `pub enum NetworkDecisionSource {`
- `pub struct NetworkPolicyRequest {`
- `pub struct NetworkPolicyRequestArgs {`
- `pub fn new(args: NetworkPolicyRequestArgs) -> Self {`
- `pub enum NetworkDecision {`
- `pub fn deny(reason: impl Into<String>) -> Self {`
- `pub fn deny_with_source(reason: impl Into<String>, source: NetworkDecisionSource) -> Self {`
- `pub fn ask_with_source(reason: impl Into<String>, source: NetworkDecisionSource) -> Self {`
- `pub trait NetworkPolicyDecider: Send + Sync + 'static {`

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/network_policy.rs:1` `use crate::reasons::REASON_POLICY_DENIED;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:2` `use crate::runtime::HostBlockDecision;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:3` `use crate::runtime::HostBlockReason;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:4` `use crate::state::NetworkProxyState;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:5` `use anyhow::Result;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:6` `use async_trait::async_trait;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:7` `use std::future::Future;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:8` `use std::sync::Arc;`
- `enum` `codex-rs/network-proxy/src/network_policy.rs:11` `pub enum NetworkProtocol {`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:18` `impl NetworkProtocol {`
- `const` `codex-rs/network-proxy/src/network_policy.rs:19` `pub const fn as_policy_protocol(self) -> &'static str {`
- `enum` `codex-rs/network-proxy/src/network_policy.rs:30` `pub enum NetworkPolicyDecision {`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:35` `impl NetworkPolicyDecision {`
- `const` `codex-rs/network-proxy/src/network_policy.rs:36` `pub const fn as_str(self) -> &'static str {`
- `enum` `codex-rs/network-proxy/src/network_policy.rs:45` `pub enum NetworkDecisionSource {`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:52` `impl NetworkDecisionSource {`
- `const` `codex-rs/network-proxy/src/network_policy.rs:53` `pub const fn as_str(self) -> &'static str {`
- `struct` `codex-rs/network-proxy/src/network_policy.rs:64` `pub struct NetworkPolicyRequest {`
- `struct` `codex-rs/network-proxy/src/network_policy.rs:74` `pub struct NetworkPolicyRequestArgs {`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:84` `impl NetworkPolicyRequest {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:85` `pub fn new(args: NetworkPolicyRequestArgs) -> Self {`
- `enum` `codex-rs/network-proxy/src/network_policy.rs:108` `pub enum NetworkDecision {`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:117` `impl NetworkDecision {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:118` `pub fn deny(reason: impl Into<String>) -> Self {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:122` `pub fn deny_with_source(reason: impl Into<String>, source: NetworkDecisionSource) -> Self {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:136` `pub fn ask_with_source(reason: impl Into<String>, source: NetworkDecisionSource) -> Self {`
- `trait` `codex-rs/network-proxy/src/network_policy.rs:157` `pub trait NetworkPolicyDecider: Send + Sync + 'static {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:158` `async fn decide(&self, req: NetworkPolicyRequest) -> NetworkDecision;`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:162` `impl<D: NetworkPolicyDecider + ?Sized> NetworkPolicyDecider for Arc<D> {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:163` `async fn decide(&self, req: NetworkPolicyRequest) -> NetworkDecision {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:174` `async fn decide(&self, req: NetworkPolicyRequest) -> NetworkDecision {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:203` `fn map_decider_decision(decision: NetworkDecision) -> NetworkDecision {`
- `use` `codex-rs/network-proxy/src/network_policy.rs:218` `use super::*;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:220` `use crate::config::NetworkProxySettings;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:221` `use crate::reasons::REASON_DENIED;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:222` `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:223` `use crate::state::network_proxy_state_for_policy;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:224` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:225` `use std::sync::Arc;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:226` `use std::sync::atomic::AtomicUsize;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:227` `use std::sync::atomic::Ordering;`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:230` `async fn evaluate_host_policy_invokes_decider_for_not_allowed() {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:261` `async fn evaluate_host_policy_skips_decider_for_denied() {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:301` `async fn evaluate_host_policy_skips_decider_for_not_allowed_local() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::reasons::REASON_POLICY_DENIED;`
- `use crate::runtime::HostBlockDecision;`
- `use crate::runtime::HostBlockReason;`
- `use crate::state::NetworkProxyState;`
- `use anyhow::Result;`
- `use async_trait::async_trait;`
- `use std::future::Future;`
- `use std::sync::Arc;`
- `use super::*;`
- `use crate::config::NetworkProxySettings;`
- `use crate::reasons::REASON_DENIED;`
- `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use crate::state::network_proxy_state_for_policy;`
- `use pretty_assertions::assert_eq;`
- `use std::sync::Arc;`
- `use std::sync::atomic::AtomicUsize;`
- `use std::sync::atomic::Ordering;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
