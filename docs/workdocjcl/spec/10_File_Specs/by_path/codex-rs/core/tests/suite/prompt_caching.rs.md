# `codex-rs/core/tests/suite/prompt_caching.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `29038`
- sha256: `a1000f9376ca1464ac3d79d924037eef668deaa8edd125c8ca919571fc7c6599`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/prompt_caching.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_apply_patch::APPLY_PATCH_TOOL_INSTRUCTIONS;`
- `use codex_core::features::Feature;`
- `use codex_core::models_manager::model_info::BASE_INSTRUCTIONS;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::ENVIRONMENT_CONTEXT_OPEN_TAG;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_core::protocol_config_types::ReasoningSummary;`
- `use codex_core::shell::Shell;`
- `use codex_core::shell::default_user_shell;`
- `use codex_protocol::config_types::CollaborationMode;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::config_types::Settings;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::user_input::UserInput;`
- `use codex_utils_absolute_path::AbsolutePathBuf;`
- `use core_test_support::load_sse_fixture_with_id;`
- `use core_test_support::responses::mount_sse_once;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
