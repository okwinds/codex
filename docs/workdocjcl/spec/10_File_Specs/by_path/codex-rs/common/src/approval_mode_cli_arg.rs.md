# `codex-rs/common/src/approval_mode_cli_arg.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1354`
- sha256: `17a713561dc7302227dc01b1ed8e1811ac4420afda1f607ca07067ae965948d3`
- generated_utc: `2026-02-08T10:45:25Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/approval_mode_cli_arg.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum ApprovalModeCliArg {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/approval_mode_cli_arg.rs:4` `use clap::ValueEnum;`
- `use` `codex-rs/common/src/approval_mode_cli_arg.rs:6` `use codex_core::protocol::AskForApproval;`
- `enum` `codex-rs/common/src/approval_mode_cli_arg.rs:10` `pub enum ApprovalModeCliArg {`
- `impl` `codex-rs/common/src/approval_mode_cli_arg.rs:29` `impl From<ApprovalModeCliArg> for AskForApproval {`
- `fn` `codex-rs/common/src/approval_mode_cli_arg.rs:30` `fn from(value: ApprovalModeCliArg) -> Self {`

## Dependencies (auto sample)
### Imports / Includes
- `use clap::ValueEnum;`
- `use codex_core::protocol::AskForApproval;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
