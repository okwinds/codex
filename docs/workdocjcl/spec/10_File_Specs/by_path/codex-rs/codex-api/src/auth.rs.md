# `codex-rs/codex-api/src/auth.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1115`
- sha256: `1d711f3594972b96901968d31008543400493b6be3b5d71eb41a324db1729ed6`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/auth.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub trait AuthProvider: Send + Sync {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/auth.rs:1` `use codex_client::Request;`
- `use` `codex-rs/codex-api/src/auth.rs:2` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/auth.rs:3` `use http::HeaderValue;`
- `trait` `codex-rs/codex-api/src/auth.rs:10` `pub trait AuthProvider: Send + Sync {`
- `fn` `codex-rs/codex-api/src/auth.rs:11` `fn bearer_token(&self) -> Option<String>;`
- `fn` `codex-rs/codex-api/src/auth.rs:12` `fn account_id(&self) -> Option<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_client::Request;`
- `use http::HeaderMap;`
- `use http::HeaderValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
