# `codex-rs/core/src/landlock.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2258`
- sha256: `992ba02451d2e28a31ead2841fa98ed8ef73533c5db8637aa512e96b5e7d55ab`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/landlock.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/landlock.rs:1` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/landlock.rs:2` `use crate::spawn::StdioPolicy;`
- `use` `codex-rs/core/src/landlock.rs:3` `use crate::spawn::spawn_child_async;`
- `use` `codex-rs/core/src/landlock.rs:4` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/landlock.rs:5` `use std::path::Path;`
- `use` `codex-rs/core/src/landlock.rs:6` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/landlock.rs:7` `use tokio::process::Child;`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::protocol::SandboxPolicy;`
- `use crate::spawn::StdioPolicy;`
- `use crate::spawn::spawn_child_async;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tokio::process::Child;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
