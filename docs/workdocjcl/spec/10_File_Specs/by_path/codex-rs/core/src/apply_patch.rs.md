# `codex-rs/core/src/apply_patch.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4520`
- sha256: `dd011994b963a8bf128110ee0f05cd88ba32c8beaa63d3dc9c8a2c13b15cb055`
- generated_utc: `2026-02-08T10:45:26Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/apply_patch.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/apply_patch.rs:1` `use crate::codex::TurnContext;`
- `use` `codex-rs/core/src/apply_patch.rs:2` `use crate::function_tool::FunctionCallError;`
- `use` `codex-rs/core/src/apply_patch.rs:3` `use crate::protocol::FileChange;`
- `use` `codex-rs/core/src/apply_patch.rs:4` `use crate::safety::SafetyCheck;`
- `use` `codex-rs/core/src/apply_patch.rs:5` `use crate::safety::assess_patch_safety;`
- `use` `codex-rs/core/src/apply_patch.rs:6` `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use` `codex-rs/core/src/apply_patch.rs:7` `use codex_apply_patch::ApplyPatchAction;`
- `use` `codex-rs/core/src/apply_patch.rs:8` `use codex_apply_patch::ApplyPatchFileChange;`
- `use` `codex-rs/core/src/apply_patch.rs:9` `use std::collections::HashMap;`
- `use` `codex-rs/core/src/apply_patch.rs:10` `use std::path::PathBuf;`
- `const` `codex-rs/core/src/apply_patch.rs:12` `pub const CODEX_APPLY_PATCH_ARG1: &str = "--codex-run-as-apply-patch";`
- `use` `codex-rs/core/src/apply_patch.rs:106` `use super::*;`
- `use` `codex-rs/core/src/apply_patch.rs:107` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/core/src/apply_patch.rs:109` `use tempfile::tempdir;`
- `fn` `codex-rs/core/src/apply_patch.rs:112` `fn convert_apply_patch_maps_add_variant() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::codex::TurnContext;`
- `use crate::function_tool::FunctionCallError;`
- `use crate::protocol::FileChange;`
- `use crate::safety::SafetyCheck;`
- `use crate::safety::assess_patch_safety;`
- `use crate::tools::sandboxing::ExecApprovalRequirement;`
- `use codex_apply_patch::ApplyPatchAction;`
- `use codex_apply_patch::ApplyPatchFileChange;`
- `use std::collections::HashMap;`
- `use std::path::PathBuf;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
