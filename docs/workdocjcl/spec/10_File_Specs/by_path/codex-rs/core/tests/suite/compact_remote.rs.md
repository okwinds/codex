# `codex-rs/core/tests/suite/compact_remote.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `42942`
- sha256: `3d40c3beeb276c925672189dad1c5aeeea30f5b50ad696859289792e9aa69434`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/compact_remote.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs;`
- `use anyhow::Result;`
- `use codex_core::CodexAuth;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ItemCompletedEvent;`
- `use codex_core::protocol::ItemStartedEvent;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::RolloutItem;`
- `use codex_core::protocol::RolloutLine;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::sse;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::TestCodexHarness;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
