# `codex-rs/linux-sandbox/tests/suite/landlock.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `8561`
- sha256: `007ee06ec55fcf0419344385cba95f262ad335f8e20044c3e2df2fe94d6a7c76`
- generated_utc: `2026-02-03T16:08:30Z`

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
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
