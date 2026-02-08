# `codex-rs/core/tests/suite/remote_models.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `26652`
- sha256: `3a47dea4f70e9c9b5bd0a2c3809650d59ffa1444bb457b0f04d8e021b4ec62b7`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/remote_models.rs` (read)

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
- `use codex_core::ModelProviderInfo;`
- `use codex_core::built_in_model_providers;`
- `use codex_core::config::Config;`
- `use codex_core::features::Feature;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_core::models_manager::manager::RefreshStrategy;`
- `use codex_core::protocol::AskForApproval;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::ExecCommandSource;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelPreset;`
- `use codex_protocol::openai_models::ModelVisibility;`
- `use codex_protocol::openai_models::ModelsResponse;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
