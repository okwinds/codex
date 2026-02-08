# `codex-rs/common/src/approval_presets.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1884`
- sha256: `ef9d94e8668bc72ab0a7f0ed31c6324bb3995b5e81509b2fa9565663b4bc55d3`
- generated_utc: `2026-02-08T10:45:25Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/approval_presets.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub struct ApprovalPreset {`
- `pub fn builtin_approval_presets() -> Vec<ApprovalPreset> {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/approval_presets.rs:1` `use codex_core::protocol::AskForApproval;`
- `use` `codex-rs/common/src/approval_presets.rs:2` `use codex_core::protocol::SandboxPolicy;`
- `struct` `codex-rs/common/src/approval_presets.rs:6` `pub struct ApprovalPreset {`
- `fn` `codex-rs/common/src/approval_presets.rs:22` `pub fn builtin_approval_presets() -> Vec<ApprovalPreset> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::SandboxPolicy;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
