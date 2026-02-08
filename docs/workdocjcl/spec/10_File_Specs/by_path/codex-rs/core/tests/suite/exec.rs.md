# `codex-rs/core/tests/suite/exec.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3871`
- sha256: `6d61af471b394b8d17bd2c2f783d846d5cd0881482932605e1fe0c371430c67d`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/exec.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::string::ToString;`
- `use codex_core::exec::ExecParams;`
- `use codex_core::exec::ExecToolCallOutput;`
- `use codex_core::exec::SandboxType;`
- `use codex_core::exec::process_exec_tool_call;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use codex_core::spawn::CODEX_SANDBOX_ENV_VAR;`
- `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use tempfile::TempDir;`
- `use codex_core::error::Result;`
- `use codex_core::get_platform_sandbox;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
