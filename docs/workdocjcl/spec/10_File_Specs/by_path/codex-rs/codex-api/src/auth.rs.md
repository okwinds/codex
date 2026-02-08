# `codex-rs/codex-api/src/auth.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `885`
- sha256: `d5a2e2c2f033ded97bf037649f64887fd081c1d5620fd9d135b8e9c9d08509dc`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `trait` `codex-rs/codex-api/src/auth.rs:8` `pub trait AuthProvider: Send + Sync {`
- `fn` `codex-rs/codex-api/src/auth.rs:9` `fn bearer_token(&self) -> Option<String>;`
- `fn` `codex-rs/codex-api/src/auth.rs:10` `fn account_id(&self) -> Option<String> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_client::Request;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
