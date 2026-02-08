# `codex-rs/exec/tests/suite/sandbox.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `13638`
- sha256: `4ae4c86cff68eaad8c5533ac7c84b43323681282f617354b2a09bdf1a507ed2c`
- generated_utc: `2026-02-08T10:45:37Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec/tests/suite/sandbox.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::spawn::StdioPolicy;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use std::collections::HashMap;`
- `use std::future::Future;`
- `use std::io;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use std::process::ExitStatus;`
- `use tokio::fs::create_dir_all;`
- `use tokio::process::Child;`
- `use codex_core::seatbelt::spawn_command_under_seatbelt;`
- `use codex_core::landlock::spawn_command_under_linux_sandbox;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
