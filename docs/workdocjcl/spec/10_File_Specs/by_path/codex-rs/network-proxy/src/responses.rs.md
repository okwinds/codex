# `codex-rs/network-proxy/src/responses.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2355`
- sha256: `7f334ef5ac948e4f1aa6d71329268cb2103c999137e2057c280baf366225daff`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/network-proxy/src/responses.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn text_response(status: StatusCode, body: &str) -> Response {`
- `pub fn blocked_header_value(reason: &str) -> &'static str {`
- `pub fn blocked_message(reason: &str) -> &'static str {`
- `pub fn blocked_text_response(reason: &str) -> Response {`

## Definitions (auto, per-file)
- `use` `codex-rs/network-proxy/src/responses.rs:1` `use crate::reasons::REASON_DENIED;`
- `use` `codex-rs/network-proxy/src/responses.rs:2` `use crate::reasons::REASON_METHOD_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/responses.rs:3` `use crate::reasons::REASON_NOT_ALLOWED;`
- `use` `codex-rs/network-proxy/src/responses.rs:4` `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use` `codex-rs/network-proxy/src/responses.rs:5` `use rama_http::Body;`
- `use` `codex-rs/network-proxy/src/responses.rs:6` `use rama_http::Response;`
- `use` `codex-rs/network-proxy/src/responses.rs:7` `use rama_http::StatusCode;`
- `use` `codex-rs/network-proxy/src/responses.rs:8` `use serde::Serialize;`
- `use` `codex-rs/network-proxy/src/responses.rs:9` `use tracing::error;`
- `fn` `codex-rs/network-proxy/src/responses.rs:11` `pub fn text_response(status: StatusCode, body: &str) -> Response {`
- `fn` `codex-rs/network-proxy/src/responses.rs:37` `pub fn blocked_header_value(reason: &str) -> &'static str {`
- `fn` `codex-rs/network-proxy/src/responses.rs:46` `pub fn blocked_message(reason: &str) -> &'static str {`
- `fn` `codex-rs/network-proxy/src/responses.rs:60` `pub fn blocked_text_response(reason: &str) -> Response {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::reasons::REASON_DENIED;`
- `use crate::reasons::REASON_METHOD_NOT_ALLOWED;`
- `use crate::reasons::REASON_NOT_ALLOWED;`
- `use crate::reasons::REASON_NOT_ALLOWED_LOCAL;`
- `use rama_http::Body;`
- `use rama_http::Response;`
- `use rama_http::StatusCode;`
- `use serde::Serialize;`
- `use tracing::error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
