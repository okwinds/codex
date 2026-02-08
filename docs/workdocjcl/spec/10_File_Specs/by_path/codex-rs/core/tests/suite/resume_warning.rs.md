# `codex-rs/core/tests/suite/resume_warning.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3298`
- sha256: `2cfe58f136afe959ca8355b6e81d544a70844e43b06c685b953f7a4ab3e8a40d`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/resume_warning.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::AuthManager;`
- `use codex_core::CodexAuth;`
- `use codex_core::NewThread;`
- `use codex_core::ThreadManager;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::InitialHistory;`
- `use codex_core::protocol::ResumedHistory;`
- `use codex_core::protocol::RolloutItem;`
- `use codex_core::protocol::TurnContextItem;`
- `use codex_core::protocol::WarningEvent;`
- `use codex_protocol::ThreadId;`
- `use core::time::Duration;`
- `use core_test_support::load_default_config_for_test;`
- `use core_test_support::wait_for_event;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
