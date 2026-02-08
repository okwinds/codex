# `codex-rs/common/src/sandbox_summary.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3022`
- sha256: `b478b7552292ed2f7d9e9c5fcc5a105b25470dd9ff12ca5781589fe5f479cb54`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/sandbox_summary.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn summarize_sandbox_policy(sandbox_policy: &SandboxPolicy) -> String {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/sandbox_summary.rs:1` `use codex_core::protocol::NetworkAccess;`
- `use` `codex-rs/common/src/sandbox_summary.rs:2` `use codex_core::protocol::SandboxPolicy;`
- `fn` `codex-rs/common/src/sandbox_summary.rs:4` `pub fn summarize_sandbox_policy(sandbox_policy: &SandboxPolicy) -> String {`
- `use` `codex-rs/common/src/sandbox_summary.rs:48` `use super::*;`
- `use` `codex-rs/common/src/sandbox_summary.rs:49` `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use` `codex-rs/common/src/sandbox_summary.rs:50` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/common/src/sandbox_summary.rs:53` `fn summarizes_external_sandbox_without_network_access_suffix() {`
- `fn` `codex-rs/common/src/sandbox_summary.rs:61` `fn summarizes_external_sandbox_with_enabled_network() {`
- `fn` `codex-rs/common/src/sandbox_summary.rs:69` `fn workspace_write_summary_still_includes_network_access() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::protocol::NetworkAccess;`
- `use codex_core::protocol::SandboxPolicy;`
- `use super::*;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
