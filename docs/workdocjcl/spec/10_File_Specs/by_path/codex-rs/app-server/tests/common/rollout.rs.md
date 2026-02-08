# `codex-rs/app-server/tests/common/rollout.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5982`
- sha256: `748aae9dad7ee35f7a6c37d5d89d6992aac506f28af1c3ed704de29112fb4064`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/common/rollout.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub fn rollout_path(codex_home: &Path, filename_ts: &str, thread_id: &str) -> PathBuf {`
- `pub fn create_fake_rollout(`
- `pub fn create_fake_rollout_with_source(`
- `pub fn create_fake_rollout_with_text_elements(`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::GitInfo;`
- `use codex_protocol::protocol::SessionMeta;`
- `use codex_protocol::protocol::SessionMetaLine;`
- `use codex_protocol::protocol::SessionSource;`
- `use serde_json::json;`
- `use std::fs;`
- `use std::fs::FileTimes;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use uuid::Uuid;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
