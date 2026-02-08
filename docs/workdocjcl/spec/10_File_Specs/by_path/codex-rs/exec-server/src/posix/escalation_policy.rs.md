# `codex-rs/exec-server/src/posix/escalation_policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `401`
- sha256: `88cfcbdbdfa73c233b5ebc3cac338f1d0d25857ba80c8510b7d851d99d77df55`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/escalation_policy.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/escalation_policy.rs:1` `use std::path::Path;`
- `use` `codex-rs/exec-server/src/posix/escalation_policy.rs:3` `use crate::posix::escalate_protocol::EscalateAction;`
- `fn` `codex-rs/exec-server/src/posix/escalation_policy.rs:8` `async fn determine_action(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use crate::posix::escalate_protocol::EscalateAction;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
