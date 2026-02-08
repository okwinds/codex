# `codex-rs/core/tests/suite/unified_exec.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `88836`
- sha256: `b7b918c55d5e6d7b74bc306ed4ed1a9e5c5787b7afc3b2719c2430e06e3ad8e1`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/unified_exec.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::collections::HashMap;`
- `use std::ffi::OsStr;`
- `use std::fs;`
- `use std::sync::OnceLock;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecCommandSource;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::process::wait_for_pid_file;`
- `use core_test_support::process::wait_for_process_exit;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_function_call;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
