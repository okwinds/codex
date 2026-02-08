# `codex-rs/protocol/src/approvals.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3339`
- sha256: `d10e3556f4492f03dae69dd108aa1b1c93d94358e96a6c5abd564ecc3d93d7de`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/protocol/src/approvals.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ExecPolicyAmendment {`
- `pub fn new(command: Vec<String>) -> Self {`
- `pub fn command(&self) -> &[String] {`
- `pub struct ExecApprovalRequestEvent {`
- `pub struct ElicitationRequestEvent {`
- `pub enum ElicitationAction {`
- `pub struct ApplyPatchApprovalRequestEvent {`

## Definitions (auto, per-file)
- `use` `codex-rs/protocol/src/approvals.rs:1` `use std::collections::HashMap;`
- `use` `codex-rs/protocol/src/approvals.rs:2` `use std::path::PathBuf;`
- `use` `codex-rs/protocol/src/approvals.rs:4` `use crate::mcp::RequestId;`
- `use` `codex-rs/protocol/src/approvals.rs:5` `use crate::parse_command::ParsedCommand;`
- `use` `codex-rs/protocol/src/approvals.rs:6` `use crate::protocol::FileChange;`
- `use` `codex-rs/protocol/src/approvals.rs:7` `use schemars::JsonSchema;`
- `use` `codex-rs/protocol/src/approvals.rs:8` `use serde::Deserialize;`
- `use` `codex-rs/protocol/src/approvals.rs:9` `use serde::Serialize;`
- `use` `codex-rs/protocol/src/approvals.rs:10` `use ts_rs::TS;`
- `struct` `codex-rs/protocol/src/approvals.rs:20` `pub struct ExecPolicyAmendment {`
- `impl` `codex-rs/protocol/src/approvals.rs:24` `impl ExecPolicyAmendment {`
- `fn` `codex-rs/protocol/src/approvals.rs:25` `pub fn new(command: Vec<String>) -> Self {`
- `fn` `codex-rs/protocol/src/approvals.rs:29` `pub fn command(&self) -> &[String] {`
- `impl` `codex-rs/protocol/src/approvals.rs:34` `impl From<Vec<String>> for ExecPolicyAmendment {`
- `fn` `codex-rs/protocol/src/approvals.rs:35` `fn from(command: Vec<String>) -> Self {`
- `struct` `codex-rs/protocol/src/approvals.rs:41` `pub struct ExecApprovalRequestEvent {`
- `struct` `codex-rs/protocol/src/approvals.rs:63` `pub struct ElicitationRequestEvent {`
- `enum` `codex-rs/protocol/src/approvals.rs:75` `pub enum ElicitationAction {`
- `struct` `codex-rs/protocol/src/approvals.rs:82` `pub struct ApplyPatchApprovalRequestEvent {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use crate::mcp::RequestId;`
- `use crate::parse_command::ParsedCommand;`
- `use crate::protocol::FileChange;`
- `use schemars::JsonSchema;`
- `use serde::Deserialize;`
- `use serde::Serialize;`
- `use ts_rs::TS;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic

## Spec Links
- `docs/workdocjcl/spec/02_Data/ROLLOUT_FORMAT.md`
