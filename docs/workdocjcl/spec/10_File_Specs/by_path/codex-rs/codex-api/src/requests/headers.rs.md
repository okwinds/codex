# `codex-rs/codex-api/src/requests/headers.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1199`
- sha256: `0fa2c0f03d251758dd1a5344cd6bca6aaba97eea44df5ae9c354c7a37fdf4345`
- generated_utc: `2026-02-08T10:45:16Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-api/src/requests/headers.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn build_conversation_headers(conversation_id: Option<String>) -> HeaderMap {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-api/src/requests/headers.rs:1` `use codex_protocol::protocol::SessionSource;`
- `use` `codex-rs/codex-api/src/requests/headers.rs:2` `use http::HeaderMap;`
- `use` `codex-rs/codex-api/src/requests/headers.rs:3` `use http::HeaderValue;`
- `fn` `codex-rs/codex-api/src/requests/headers.rs:5` `pub fn build_conversation_headers(conversation_id: Option<String>) -> HeaderMap {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::protocol::SessionSource;`
- `use http::HeaderMap;`
- `use http::HeaderValue;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
