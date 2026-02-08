# `codex-rs/core/tests/suite/unstable_features_warning.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3417`
- sha256: `4dbd3e6a371d8d426550f4b6cc91ea8587e105a0478224b854865dd86554053b`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/unstable_features_warning.rs` (read)

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
- `use codex_core::config::CONFIG_TOML_FILE;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::InitialHistory;`
- `use codex_core::protocol::WarningEvent;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use core::time::Duration;`
- `use core_test_support::load_default_config_for_test;`
- `use core_test_support::wait_for_event;`
- `use tempfile::TempDir;`
- `use tokio::time::timeout;`
- `use toml::toml;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
