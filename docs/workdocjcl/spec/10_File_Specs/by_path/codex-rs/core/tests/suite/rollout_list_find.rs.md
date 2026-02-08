# `codex-rs/core/tests/suite/rollout_list_find.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5069`
- sha256: `533956b712cb5061bc008ff7ca643f30d9936a7489a6965dccd414fa8b68352f`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/rollout_list_find.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::io::Write;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_core::RolloutRecorder;`
- `use codex_core::RolloutRecorderParams;`
- `use codex_core::config::ConfigBuilder;`
- `use codex_core::find_archived_thread_path_by_id_str;`
- `use codex_core::find_thread_path_by_id_str;`
- `use codex_core::find_thread_path_by_name_str;`
- `use codex_core::protocol::SessionSource;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::models::BaseInstructions;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
- `use uuid::Uuid;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
