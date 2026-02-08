# `codex-rs/codex-api/src/rate_limits.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5229`
- sha256: `4618d05f4050f9a8c696258be5cf3542677ae0946e25ae3d463bd5d0f4602f75`
- generated_utc: `2026-02-08T10:45:16Z`

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
- `pub fn parse_rate_limit_event(payload: &str) -> Option<RateLimitSnapshot> {`
- `pub fn parse_promo_message(headers: &HeaderMap) -> Option<String> {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/rate_limits.rs:1` `use codex_protocol::account::PlanType;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:2` `use codex_protocol::protocol::CreditsSnapshot;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:3` `use codex_protocol::protocol::RateLimitSnapshot;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:4` `use codex_protocol::protocol::RateLimitWindow;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:5` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:6` `use serde::Deserialize;`
- `use` `codex-rs/codex-api/src/rate_limits.rs:7` `use std::fmt::Display;`
- `struct` `codex-rs/codex-api/src/rate_limits.rs:10` `pub struct RateLimitError {`
- `impl` `codex-rs/codex-api/src/rate_limits.rs:14` `impl Display for RateLimitError {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:15` `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:21` `pub fn parse_rate_limit(headers: &HeaderMap) -> Option<RateLimitSnapshot> {`
- `struct` `codex-rs/codex-api/src/rate_limits.rs:47` `struct RateLimitEventWindow {`
- `struct` `codex-rs/codex-api/src/rate_limits.rs:54` `struct RateLimitEventDetails {`
- `struct` `codex-rs/codex-api/src/rate_limits.rs:60` `struct RateLimitEventCredits {`
- `struct` `codex-rs/codex-api/src/rate_limits.rs:67` `struct RateLimitEvent {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:75` `pub fn parse_rate_limit_event(payload: &str) -> Option<RateLimitSnapshot> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:101` `fn map_event_window(window: Option<&RateLimitEventWindow>) -> Option<RateLimitWindow> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:111` `pub fn parse_promo_message(headers: &HeaderMap) -> Option<String> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:118` `fn parse_rate_limit_window(`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:142` `fn parse_credits_snapshot(headers: &HeaderMap) -> Option<CreditsSnapshot> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:156` `fn parse_header_f64(headers: &HeaderMap, name: &str) -> Option<f64> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:163` `fn parse_header_i64(headers: &HeaderMap, name: &str) -> Option<i64> {`
- `fn` `codex-rs/codex-api/src/rate_limits.rs:167` `fn parse_header_bool(headers: &HeaderMap, name: &str) -> Option<bool> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::account::PlanType;`
- `use codex_protocol::protocol::CreditsSnapshot;`
- `use codex_protocol::protocol::RateLimitSnapshot;`
- `use codex_protocol::protocol::RateLimitWindow;`
- `use http::HeaderMap;`
- `use serde::Deserialize;`
- `use std::fmt::Display;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
