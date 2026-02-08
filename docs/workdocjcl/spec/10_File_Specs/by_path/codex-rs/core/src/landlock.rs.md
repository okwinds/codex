# `codex-rs/core/src/landlock.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3462`
- sha256: `be18e4562dd9c80d44aafdea5f650ef7c17cfdd7e68784d68cd3ba352b3c0886`
- generated_utc: `2026-02-08T10:45:32Z`

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
- `use` `codex-rs/core/src/landlock.rs:92` `use super::*;`
- `use` `codex-rs/core/src/landlock.rs:93` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/landlock.rs:96` `fn bwrap_flags_are_feature_gated() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::protocol::SandboxPolicy;`
- `use crate::spawn::StdioPolicy;`
- `use crate::spawn::spawn_child_async;`
- `use std::collections::HashMap;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use tokio::process::Child;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
