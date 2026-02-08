# `codex-rs/core/tests/suite/models_etag_responses.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5320`
- sha256: `9aa8b961cc6c966bcc56871e8b888448f7df79617568cd21033603fb74bf50b0`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/models_etag_responses.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use anyhow::Result;`
- `use codex_core::CodexAuth;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::openai_models::ModelsResponse;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_local_shell_call;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::sse_response;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::test_codex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
