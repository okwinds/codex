# `codex-rs/core/src/user_notification.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2933`
- sha256: `f1c9c8b0e395b5955bdc22f18662d0b466755ec2b4399f9d7627dc6c59a2548c`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/user_notification.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/user_notification.rs:1` `use serde::Serialize;`
- `use` `codex-rs/core/src/user_notification.rs:2` `use tracing::error;`
- `use` `codex-rs/core/src/user_notification.rs:3` `use tracing::warn;`
- `impl` `codex-rs/core/src/user_notification.rs:10` `impl UserNotifier {`
- `fn` `codex-rs/core/src/user_notification.rs:19` `fn invoke_notify(&self, notify_command: &[String], notification: &UserNotification) {`
- `use` `codex-rs/core/src/user_notification.rs:66` `use super::*;`
- `use` `codex-rs/core/src/user_notification.rs:67` `use anyhow::Result;`
- `fn` `codex-rs/core/src/user_notification.rs:70` `fn test_user_notification() -> Result<()> {`

## Dependencies (auto sample)
### Imports / Includes
- `use serde::Serialize;`
- `use tracing::error;`
- `use tracing::warn;`
- `use super::*;`
- `use anyhow::Result;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
