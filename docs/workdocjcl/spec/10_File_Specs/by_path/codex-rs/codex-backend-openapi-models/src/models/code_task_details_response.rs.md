# `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1283`
- sha256: `c793eecb2934eb459f9a164fb6aea27fbf220beb95d50f2591149d32e55ed6eb`
- generated_utc: `2026-02-08T10:45:17Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct CodeTaskDetailsResponse {`
- `pub fn new(task: models::TaskResponse) -> CodeTaskDetailsResponse {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:11` `use crate::models;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:12` `use serde::Deserialize;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:13` `use serde::Serialize;`
- `struct` `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:16` `pub struct CodeTaskDetailsResponse {`
- `impl` `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:33` `impl CodeTaskDetailsResponse {`
- `fn` `codex-rs/codex-backend-openapi-models/src/models/code_task_details_response.rs:34` `pub fn new(task: models::TaskResponse) -> CodeTaskDetailsResponse {`

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
