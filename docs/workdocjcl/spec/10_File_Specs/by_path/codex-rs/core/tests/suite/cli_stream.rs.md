# `codex-rs/core/tests/suite/cli_stream.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `19653`
- sha256: `78344ba6f55a5be31e3d7515bcabd9d0b03f872851321c14c4fb97b01301a08c`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use core_test_support::skip_if_no_network;`
- `use std::time::Duration;`
- `use tempfile::TempDir;`
- `use uuid::Uuid;`
- `use wiremock::Mock;`
- `use wiremock::MockServer;`
- `use wiremock::ResponseTemplate;`
- `use wiremock::matchers::method;`
- `use wiremock::matchers::path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
