# `codex-rs/exec-server/src/posix/escalate_protocol.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1772`
- sha256: `b5dcd1931043d5301b81e54381c3227d0c355152b1f3817c0127c29bce00f75e`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/escalate_protocol.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/escalate_protocol.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/exec-server/src/posix/escalate_protocol.rs:2` `use std::os::fd::RawFd;`
- `use` `codex-rs/exec-server/src/posix/escalate_protocol.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/exec-server/src/posix/escalate_protocol.rs:5` `use serde::Deserialize;`
- `use` `codex-rs/exec-server/src/posix/escalate_protocol.rs:6` `use serde::Serialize;`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::os::fd::RawFd;`
- `use std::path::PathBuf;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
