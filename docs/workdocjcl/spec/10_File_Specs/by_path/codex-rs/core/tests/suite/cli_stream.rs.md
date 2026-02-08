# `codex-rs/core/tests/suite/cli_stream.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `18973`
- sha256: `3a827a99cfc3e566469a4642fd9167eb8ab0485a00dffc16c408e516e25dda92`
- generated_utc: `2026-02-08T10:45:35Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/cli_stream.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use assert_cmd::Command as AssertCommand;`
- `use codex_core::RolloutRecorder;`
- `use codex_core::auth::CODEX_API_KEY_ENV_VAR;`
- `use codex_core::protocol::GitInfo;`
- `use codex_utils_cargo_bin::find_resource;`
- `use core_test_support::fs_wait;`
- `use core_test_support::responses;`
- `use core_test_support::skip_if_no_network;`
- `use std::time::Duration;`
- `use tempfile::TempDir;`
- `use uuid::Uuid;`
- `use wiremock::MockServer;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
