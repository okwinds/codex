# `codex-rs/core/tests/suite/compact_resume_fork.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `30961`
- sha256: `197703b146cf69dd5a53dd5641cf43c5b86668d263065f754e5b7777c70ad7c5`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/compact_resume_fork.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use super::compact::COMPACT_WARNING_MESSAGE;`
- `use super::compact::FIRST_REPLY;`
- `use super::compact::SUMMARY_TEXT;`
- `use codex_core::CodexThread;`
- `use codex_core::ThreadManager;`
- `use codex_core::compact::SUMMARIZATION_PROMPT;`
- `use codex_core::config::Config;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::WarningEvent;`
- `use codex_core::spawn::CODEX_SANDBOX_NETWORK_DISABLED_ENV_VAR;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ResponseMock;`
- `use core_test_support::responses::ev_assistant_message;`
- `use core_test_support::responses::ev_completed;`
- `use core_test_support::responses::mount_sse_once_match;`
- `use core_test_support::responses::sse;`
- `use core_test_support::test_codex::test_codex;`
- `use core_test_support::wait_for_event;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
