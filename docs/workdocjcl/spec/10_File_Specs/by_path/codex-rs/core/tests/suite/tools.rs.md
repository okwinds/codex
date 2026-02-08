# `codex-rs/core/tests/suite/tools.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `17896`
- sha256: `4376f9746d9e29a1a03d84acb6daa95a2ff96d539f63bcc575e42a06390f1209`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/tools.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::fs;`
- `use std::time::Duration;`
- `use std::time::Instant;`
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use core_test_support::assert_regex_match;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_custom_tool_call;`
- `use core_test_support::responses::ev_function_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::mount_sse_once;`
- `use core_test_support::responses::mount_sse_sequence;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
