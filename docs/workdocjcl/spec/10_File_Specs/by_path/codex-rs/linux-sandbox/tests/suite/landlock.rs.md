# `codex-rs/linux-sandbox/tests/suite/landlock.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `12953`
- sha256: `657c7b92a7b8ff21ff0740483cd134dcca3bd4d94bdde806943bd1085d19e3f7`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/linux-sandbox/tests/suite/landlock.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::types::ShellEnvironmentPolicy;`
- `use codex_core::error::CodexErr;`
- `use codex_core::error::Result;`
- `use codex_core::error::SandboxErr;`
- `use codex_core::exec::ExecParams;`
- `use codex_core::exec::process_exec_tool_call;`
- `use codex_core::exec_env::create_env;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol_config_types::WindowsSandboxLevel;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use tempfile::NamedTempFile;`
- `use std::os::unix::fs::symlink;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
