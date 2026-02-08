# `codex-rs/core/tests/suite/compact.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `80804`
- sha256: `94ea78d4caa13880ba9ed512a5577470927b3bee36a909b406789ef3d55c5813`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/compact.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::CodexAuth;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::built_in_model_providers;`
- `use codex_core::compact::SUMMARIZATION_PROMPT;`
- `use codex_core::compact::SUMMARY_PREFIX;`
- `use codex_core::config::Config;`
- `use codex_core::features::Feature;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ItemCompletedEvent;`
- `use codex_core::protocol::ItemStartedEvent;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::RolloutItem;`
- `use codex_core::protocol::RolloutLine;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol::WarningEvent;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::items::TurnItem;`
- `use codex_protocol::user_input::UserInput;`
- `use core_test_support::responses::ev_local_shell_call;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
