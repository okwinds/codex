# `codex-rs/core/tests/suite/live_reload.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5096`
- sha256: `84d09d7342338edde40ebbba204732c8d32d210a56a69fbe8cae09b962d39b22`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/live_reload.rs` (read)

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
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use anyhow::Result;`
- `use codex_core::config::ProjectConfig;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::config_types::TrustLevel;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses;`
- `use core_test_support::responses::ResponsesRequest;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::test_codex::TestCodex;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
