# `codex-rs/network-proxy/src/responses.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5521`
- sha256: `de3d74d6837729547b496163e9de1a1dc4ba49c3664adb0ff3ac5f1f7b5529c1`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/responses.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PolicyDecisionDetails<'a> {`
- `pub fn text_response(status: StatusCode, body: &str) -> Response {`
- `pub fn blocked_header_value(reason: &str) -> &'static str {`
- `pub fn blocked_message(reason: &str) -> &'static str {`
- `pub fn policy_decision_prefix(details: &PolicyDecisionDetails<'_>) -> String {`
- `pub fn blocked_message_with_policy(reason: &str, details: &PolicyDecisionDetails<'_>) -> String {`
- `pub fn blocked_text_response_with_policy(`

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/responses.rs:1` `use crate::network_policy::NetworkDecisionSource;`
- `use` `codex-rs/network-proxy/src/responses.rs:2` `use crate::network_policy::NetworkPolicyDecision;`
- `use` `codex-rs/network-proxy/src/responses.rs:3` `use crate::network_policy::NetworkProtocol;`
- `use` `codex-rs/network-proxy/src/responses.rs:4` `use crate::reasons::REASON_DENIED;`
- `use` `codex-rs/network-proxy/src/responses.rs:5` `use crate::reasons::REASON_METHOD_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/responses.rs:6` `use crate::reasons::REASON_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/responses.rs:7` `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use` `codex-rs/network-proxy/src/responses.rs:8` `use rama_http::Body;`
- `use` `codex-rs/network-proxy/src/responses.rs:9` `use rama_http::Response;`
- `use` `codex-rs/network-proxy/src/responses.rs:10` `use rama_http::StatusCode;`
- `use` `codex-rs/network-proxy/src/responses.rs:11` `use serde::Serialize;`
- `use` `codex-rs/network-proxy/src/responses.rs:12` `use tracing::error;`
- `const` `codex-rs/network-proxy/src/responses.rs:14` `const NETWORK_POLICY_DECISION_PREFIX: &str = "CODEX_NETWORK_POLICY_DECISION";`
- `struct` `codex-rs/network-proxy/src/responses.rs:16` `pub struct PolicyDecisionDetails<'a> {`
- `struct` `codex-rs/network-proxy/src/responses.rs:27` `struct PolicyDecisionPayload<'a> {`
- `fn` `codex-rs/network-proxy/src/responses.rs:36` `pub fn text_response(status: StatusCode, body: &str) -> Response {`
- `fn` `codex-rs/network-proxy/src/responses.rs:62` `pub fn blocked_header_value(reason: &str) -> &'static str {`
- `fn` `codex-rs/network-proxy/src/responses.rs:71` `pub fn blocked_message(reason: &str) -> &'static str {`
- `fn` `codex-rs/network-proxy/src/responses.rs:85` `pub fn policy_decision_prefix(details: &PolicyDecisionDetails<'_>) -> String {`
- `fn` `codex-rs/network-proxy/src/responses.rs:104` `pub fn blocked_message_with_policy(reason: &str, details: &PolicyDecisionDetails<'_>) -> String {`
- `fn` `codex-rs/network-proxy/src/responses.rs:112` `pub fn blocked_text_response_with_policy(`
- `use` `codex-rs/network-proxy/src/responses.rs:126` `use super::*;`
- `use` `codex-rs/network-proxy/src/responses.rs:127` `use crate::reasons::REASON_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/responses.rs:128` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/network-proxy/src/responses.rs:131` `fn policy_decision_prefix_serializes_expected_payload() {`
- `fn` `codex-rs/network-proxy/src/responses.rs:149` `fn blocked_message_with_policy_includes_prefix_and_human_message() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::network_policy::NetworkDecisionSource;`
- `use crate::network_policy::NetworkPolicyDecision;`
- `use crate::network_policy::NetworkProtocol;`
- `use crate::reasons::REASON_DENIED;`
- `use crate::reasons::REASON_METHOD_NOT_ALLOWED;`
- `use crate::reasons::REASON_NOT_ALLOWED;`
- `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use rama_http::Body;`
- `use rama_http::Response;`
- `use rama_http::StatusCode;`
- `use serde::Serialize;`
- `use tracing::error;`
- `use super::*;`
- `use crate::reasons::REASON_NOT_ALLOWED;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
