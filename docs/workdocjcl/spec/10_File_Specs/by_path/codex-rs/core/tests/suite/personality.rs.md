# `codex-rs/core/tests/suite/personality.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `32084`
- sha256: `f20de7b2c11098766157b89cc50a1bad9f8edc4dfda3e17acabd4890c7ef7afb`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/personality.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::config::types::Personality;`
- `use codex_core::features::Feature;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_core::models_manager::manager::RefreshStrategy;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelInstructionsVariables;`
- `use codex_protocol::openai_models::ModelMessages;`
- `use codex_protocol::openai_models::ModelVisibility;`
- `use codex_protocol::openai_models::ModelsResponse;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use codex_protocol::openai_models::TruncationPolicyConfig;`
- `use codex_protocol::openai_models::default_input_modalities;`
- `use codex_protocol::user_input::UserInput;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
