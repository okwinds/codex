# `codex-rs/core/tests/suite/override_updates.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `7336`
- sha256: `434f7f51a340dd8aadbf3f851f73e4bb54fc239d9529386b36cd4ae7a033b1bc`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/override_updates.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_core::config::Constrained;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::COLLABORATION_MODE_CLOSE_TAG;`
- `use codex_core::protocol::COLLABORATION_MODE_OPEN_TAG;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::RolloutItem;`
- `use codex_core::protocol::RolloutLine;`
- `use codex_core::protocol::ENVIRONMENT_CONTEXT_OPEN_TAG;`
- `use codex_protocol::config_types::CollaborationMode;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::config_types::Settings;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
