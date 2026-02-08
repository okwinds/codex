# `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1791`
- sha256: `1c255217bafdda0cf50adce97afa2dcce6181a681a1fc725ca69f3fe6be7f62a`
- generated_utc: `2026-02-08T10:45:18Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct RateLimitStatusPayload {`
- `pub fn new(plan_type: PlanType) -> RateLimitStatusPayload {`
- `pub enum PlanType {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:11` `use crate::models;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:12` `use serde::Deserialize;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:13` `use serde::Serialize;`
- `struct` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:16` `pub struct RateLimitStatusPayload {`
- `impl` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:35` `impl RateLimitStatusPayload {`
- `fn` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:36` `pub fn new(plan_type: PlanType) -> RateLimitStatusPayload {`
- `enum` `codex-rs/codex-backend-openapi-models/src/models/rate_limit_status_payload.rs:48` `pub enum PlanType {`

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
