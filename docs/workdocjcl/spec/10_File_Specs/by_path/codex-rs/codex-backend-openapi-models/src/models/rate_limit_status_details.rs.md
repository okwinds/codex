# `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1224`
- sha256: `38935bb0f24cbb60bb9def3426fdd44bdec75dee92d8c0396698e851f122c00a`
- generated_utc: `2026-02-08T10:45:18Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RateLimitStatusDetails {`
- `pub fn new(allowed: bool, limit_reached: bool) -> RateLimitStatusDetails {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:11` `use crate::models;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:12` `use serde::Deserialize;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:13` `use serde::Serialize;`
- `struct` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:16` `pub struct RateLimitStatusDetails {`
- `impl` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:37` `impl RateLimitStatusDetails {`
- `fn` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_details.rs:38` `pub fn new(allowed: bool, limit_reached: bool) -> RateLimitStatusDetails {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::models;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
