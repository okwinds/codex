# `codex-rs/core/src/tools/runtimes/mod.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2410`
- sha256: `50b139552597de12f69210b36b63115d2804cbef9cf039f40502f154acd2c32c`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/tools/runtimes/mod.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:7` `use crate::exec::ExecExpiration;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:8` `use crate::sandboxing::CommandSpec;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:9` `use crate::sandboxing::SandboxPermissions;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:10` `use crate::shell::Shell;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:11` `use crate::tools::sandboxing::ToolError;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:12` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/tools/runtimes/mod.rs:13` `use std::path::Path;`
- `mod` `codex-rs/core/src/tools/runtimes/mod.rs:15` `pub mod apply_patch;`
- `mod` `codex-rs/core/src/tools/runtimes/mod.rs:16` `pub mod shell;`
- `mod` `codex-rs/core/src/tools/runtimes/mod.rs:17` `pub mod unified_exec;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::exec::ExecExpiration;`
- `use crate::sandboxing::CommandSpec;`
- `use crate::sandboxing::SandboxPermissions;`
- `use crate::shell::Shell;`
- `use crate::tools::sandboxing::ToolError;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
