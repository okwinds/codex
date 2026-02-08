# `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `711`
- sha256: `0175555e58be66fc6cf795471dcf00525c98ddcdda846c4c404a2b02c05c7bd1`
- generated_utc: `2026-02-08T10:45:17Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct PaginatedListTaskListItem {`
- `pub fn new(items: Vec<models::TaskListItem>) -> PaginatedListTaskListItem {`

## Definitions (auto, per-file)
- `use` `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:11` `use crate::models;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:12` `use serde::Deserialize;`
- `use` `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:13` `use serde::Serialize;`
- `struct` `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:16` `pub struct PaginatedListTaskListItem {`
- `impl` `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:23` `impl PaginatedListTaskListItem {`
- `fn` `codex-rs/codex-backend-openapi-models/src/models/paginated_list_task_list_item_.rs:24` `pub fn new(items: Vec<models::TaskListItem>) -> PaginatedListTaskListItem {`

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
