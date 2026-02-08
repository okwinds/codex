# `codex-rs/core/tests/suite/apply_patch_cli.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `50113`
- sha256: `e176a5f8c1b0efc3ab70d6a9a6c37a7d3042dd8b6d8701110af7a03513064dc7`
- generated_utc: `2026-02-08T10:45:34Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/apply_patch_cli.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use core_test_support::responses::ev_apply_patch_call;`
- `use core_test_support::responses::ev_apply_patch_custom_tool_call;`
- `use core_test_support::responses::ev_shell_command_call;`
- `use core_test_support::test_codex::ApplyPatchModelOutput;`
- `use pretty_assertions::assert_eq;`
- `use std::fs;`
- `use std::sync::atomic::AtomicI32;`
- `use std::sync::atomic::Ordering;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::responses::ev_apply_patch_function_call;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
