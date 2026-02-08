# `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1433`
- sha256: `519cf69bc9d0ddcf59f517cdadab8bf14e7d051ae6cec572501ab26430c0a556`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CreditStatusDetails {`
- `pub fn new(has_credits: bool, unlimited: bool) -> CreditStatusDetails {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs:10` `use serde::Deserialize;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs:11` `use serde::Serialize;`
- `struct` `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs:14` `pub struct CreditStatusDetails {`
- `impl` `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs:42` `impl CreditStatusDetails {`
- `fn` `codex-rs/codex-backend-openapi-models/src/models/credit_status_details.rs:43` `pub fn new(has_credits: bool, unlimited: bool) -> CreditStatusDetails {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Deserialize;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
