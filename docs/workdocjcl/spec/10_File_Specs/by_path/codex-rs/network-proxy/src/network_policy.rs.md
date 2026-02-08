# `codex-rs/network-proxy/src/network_policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `7604`
- sha256: `4e52b609c8a3e5acaa8ca2a4515eb8a54749053db2bf2feb5818d8e7ade45cb1`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/network_policy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum NetworkProtocol {`
- `pub struct NetworkPolicyRequest {`
- `pub struct NetworkPolicyRequestArgs {`
- `pub fn new(args: NetworkPolicyRequestArgs) -> Self {`
- `pub enum NetworkDecision {`
- `pub fn deny(reason: impl Into<String>) -> Self {`
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
- `struct` `codex-rs/network-proxy/src/network_policy.rs:19` `pub struct NetworkPolicyRequest {`
- `struct` `codex-rs/network-proxy/src/network_policy.rs:29` `pub struct NetworkPolicyRequestArgs {`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:39` `impl NetworkPolicyRequest {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:40` `pub fn new(args: NetworkPolicyRequestArgs) -> Self {`
- `enum` `codex-rs/network-proxy/src/network_policy.rs:63` `pub enum NetworkDecision {`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:68` `impl NetworkDecision {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:69` `pub fn deny(reason: impl Into<String>) -> Self {`
- `trait` `codex-rs/network-proxy/src/network_policy.rs:86` `pub trait NetworkPolicyDecider: Send + Sync + 'static {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:87` `async fn decide(&self, req: NetworkPolicyRequest) -> NetworkDecision;`
- `impl` `codex-rs/network-proxy/src/network_policy.rs:91` `impl<D: NetworkPolicyDecider + ?Sized> NetworkPolicyDecider for Arc<D> {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:92` `async fn decide(&self, req: NetworkPolicyRequest) -> NetworkDecision {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:103` `async fn decide(&self, req: NetworkPolicyRequest) -> NetworkDecision {`
- `use` `codex-rs/network-proxy/src/network_policy.rs:128` `use super::*;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:130` `use crate::config::NetworkPolicy;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:131` `use crate::reasons::REASON_DENIED;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:132` `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:133` `use crate::state::network_proxy_state_for_policy;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:134` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:135` `use std::sync::Arc;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:136` `use std::sync::atomic::AtomicUsize;`
- `use` `codex-rs/network-proxy/src/network_policy.rs:137` `use std::sync::atomic::Ordering;`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:140` `async fn evaluate_host_policy_invokes_decider_for_not_allowed() {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:171` `async fn evaluate_host_policy_skips_decider_for_denied() {`
- `fn` `codex-rs/network-proxy/src/network_policy.rs:209` `async fn evaluate_host_policy_skips_decider_for_not_allowed_local() {`

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
- `use crate::config::NetworkPolicy;`
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
