# `codex-rs/core/tests/suite/image_rollout.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `8244`
- sha256: `0ece8ace05e616576752bc75527dcd88b4ec2156520a5d8f9d327537e1415cbc`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/image_rollout.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::RolloutItem;`
- `use codex_core::protocol::RolloutLine;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::models::ContentItem;`
- `use codex_protocol::models::ResponseItem;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::ev_response_created;`
- `use core_test_support::responses::sse;`
- `use core_test_support::responses::start_mock_server;`
- `use core_test_support::skip_if_no_network;`
- `use core_test_support::test_codex::TestCodex;`
- `use core_test_support::test_codex::test_codex;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
