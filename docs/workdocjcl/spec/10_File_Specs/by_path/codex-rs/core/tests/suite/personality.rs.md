# `codex-rs/core/tests/suite/personality.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `35698`
- sha256: `394f1c0b8f32b0948a60d367924b79e290478f29973b2797925de436d8b060a1`
- generated_utc: `2026-02-08T10:45:36Z`

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
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
