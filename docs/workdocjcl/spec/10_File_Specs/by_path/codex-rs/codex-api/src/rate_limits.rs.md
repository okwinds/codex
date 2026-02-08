# `codex-rs/codex-api/src/rate_limits.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3437`
- sha256: `56164abc878a0484681729eaee5a1a9841e70113d09477062fd8420962cf114f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/rate_limits.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RateLimitError {`
- `pub fn parse_rate_limit(headers: &HeaderMap) -> Option<RateLimitSnapshot> {`
- `pub fn parse_promo_message(headers: &HeaderMap) -> Option<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/rate_limits.rs:1` `use codex_protocol::protocol::CreditsSnapshot;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:2` `use codex_protocol::protocol::RateLimitSnapshot;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:3` `use codex_protocol::protocol::RateLimitWindow;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:4` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:5` `use std::fmt::Display;`
- `struct` `codex-rs/codex-api/src/rate_limits.rs:8` `pub struct RateLimitError {`
- `impl` `codex-rs/codex-api/src/rate_limits.rs:12` `impl Display for RateLimitError {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:13` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:19` `pub fn parse_rate_limit(headers: &HeaderMap) -> Option<RateLimitSnapshot> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:45` `pub fn parse_promo_message(headers: &HeaderMap) -> Option<String> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:52` `fn parse_rate_limit_window(`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:76` `fn parse_credits_snapshot(headers: &HeaderMap) -> Option<CreditsSnapshot> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:90` `fn parse_header_f64(headers: &HeaderMap, name: &str) -> Option<f64> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:97` `fn parse_header_i64(headers: &HeaderMap, name: &str) -> Option<i64> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:101` `fn parse_header_bool(headers: &HeaderMap, name: &str) -> Option<bool> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::protocol::CreditsSnapshot;`
- `use codex_protocol::protocol::RateLimitSnapshot;`
- `use codex_protocol::protocol::RateLimitWindow;`
- `use http::HeaderMap;`
- `use std::fmt::Display;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
