# `codex-rs/core/src/safety.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `8353`
- sha256: `2e5f976f2c73f7e10c619dc5f14e8621db717aa7d07a0e970044206593fd5620`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/safety.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub enum SafetyCheck {`
- `pub fn assess_patch_safety(`
- `pub fn get_platform_sandbox(windows_sandbox_enabled: bool) -> Option<SandboxType> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/safety.rs:1` `use std::path::Component;`
- `use` `codex-rs/core/src/safety.rs:2` `use std::path::Path;`
- `use` `codex-rs/core/src/safety.rs:3` `use std::path::PathBuf;`
- `use` `codex-rs/core/src/safety.rs:5` `use codex_apply_patch::ApplyPatchAction;`
- `use` `codex-rs/core/src/safety.rs:6` `use codex_apply_patch::ApplyPatchFileChange;`
- `use` `codex-rs/core/src/safety.rs:8` `use crate::exec::SandboxType;`
- `use` `codex-rs/core/src/safety.rs:9` `use crate::util::resolve_path;`
- `use` `codex-rs/core/src/safety.rs:11` `use crate::protocol::AskForApproval;`
- `use` `codex-rs/core/src/safety.rs:12` `use crate::protocol::SandboxPolicy;`
- `use` `codex-rs/core/src/safety.rs:13` `use codex_protocol::config_types::WindowsSandboxLevel;`
- `enum` `codex-rs/core/src/safety.rs:16` `pub enum SafetyCheck {`
- `fn` `codex-rs/core/src/safety.rs:27` `pub fn assess_patch_safety(`
- `fn` `codex-rs/core/src/safety.rs:88` `pub fn get_platform_sandbox(windows_sandbox_enabled: bool) -> Option<SandboxType> {`
- `fn` `codex-rs/core/src/safety.rs:104` `fn is_write_patch_constrained_to_writable_paths(`
- `fn` `codex-rs/core/src/safety.rs:122` `fn normalize(path: &Path) -> Option<PathBuf> {`
- `use` `codex-rs/core/src/safety.rs:176` `use super::*;`
- `use` `codex-rs/core/src/safety.rs:177` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/core/src/safety.rs:178` `use tempfile::TempDir;`
- `fn` `codex-rs/core/src/safety.rs:181` `fn test_writable_roots_constraint() {`
- `fn` `codex-rs/core/src/safety.rs:231` `fn external_sandbox_auto_approves_in_on_request() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Component;`
- `use std::path::Path;`
- `use std::path::PathBuf;`
- `use codex_apply_patch::ApplyPatchAction;`
- `use codex_apply_patch::ApplyPatchFileChange;`
- `use crate::exec::SandboxType;`
- `use crate::util::resolve_path;`
- `use crate::protocol::AskForApproval;`
- `use crate::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::WindowsSandboxLevel;`
- `use super::*;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
