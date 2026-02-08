# `codex-rs/core/tests/suite/undo.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `18277`
- sha256: `dc203663bd07e316b9c17de9a167d82a3bc52500ca981407536866076d209197`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/undo.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs;`
- `use std::path::Path;`
- `use std::process::Command;`
- `use std::sync::Arc;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use anyhow::bail;`
- `use codex_core::CodexThread;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::UndoCompletedEvent;`
- `use core_test_support::responses::ev_apply_patch_function_call;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::TestCodexHarness;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
