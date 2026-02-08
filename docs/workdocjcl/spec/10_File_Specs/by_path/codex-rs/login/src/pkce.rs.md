# `codex-rs/login/src/pkce.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `750`
- sha256: `1b000282c7741f4c7241a2eaa82fd2b332d5e1e83b3e69dd13f3260595418c92`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/login/src/pkce.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PkceCodes {`
- `pub fn generate_pkce() -> PkceCodes {`

## Definitions (auto, per-file)
- `use` `codex-rs/login/src/pkce.rs:1` `use base64::Engine;`
- `use` `codex-rs/login/src/pkce.rs:2` `use rand::RngCore;`
- `use` `codex-rs/login/src/pkce.rs:3` `use sha2::Digest;`
- `use` `codex-rs/login/src/pkce.rs:4` `use sha2::Sha256;`
- `struct` `codex-rs/login/src/pkce.rs:7` `pub struct PkceCodes {`
- `fn` `codex-rs/login/src/pkce.rs:12` `pub fn generate_pkce() -> PkceCodes {`

## Dependencies (auto sample)
### Imports / Includes
- `use base64::Engine;`
- `use rand::RngCore;`
- `use sha2::Digest;`
- `use sha2::Sha256;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
