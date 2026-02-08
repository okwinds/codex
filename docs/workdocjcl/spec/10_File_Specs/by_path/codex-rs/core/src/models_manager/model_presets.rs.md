# `codex-rs/core/src/models_manager/model_presets.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17182`
- sha256: `8d2f10bcea92a474b96dc2ded8a699477f4f8d6f444311bd9c4d7e99d4deb2b4`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/models_manager/model_presets.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn all_model_presets() -> &'static Vec<ModelPreset> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/models_manager/model_presets.rs:1` `use crate::auth::AuthMode;`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:2` `use codex_protocol::openai_models::ModelPreset;`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:3` `use codex_protocol::openai_models::ModelUpgrade;`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:4` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:5` `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:6` `use codex_protocol::openai_models::default_input_modalities;`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:7` `use indoc::indoc;`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:8` `use once_cell::sync::Lazy;`
- `const` `codex-rs/core/src/models_manager/model_presets.rs:10` `pub const HIDE_GPT5_1_MIGRATION_PROMPT_CONFIG: &str = "hide_gpt5_1_migration_prompt";`
- `const` `codex-rs/core/src/models_manager/model_presets.rs:11` `pub const HIDE_GPT_5_1_CODEX_MAX_MIGRATION_PROMPT_CONFIG: &str =`
- `static` `codex-rs/core/src/models_manager/model_presets.rs:14` `static PRESETS: Lazy<Vec<ModelPreset>> = Lazy::new(|| {`
- `fn` `codex-rs/core/src/models_manager/model_presets.rs:335` `fn gpt_52_codex_upgrade() -> ModelUpgrade {`
- `fn` `codex-rs/core/src/models_manager/model_presets.rs:363` `pub fn all_model_presets() -> &'static Vec<ModelPreset> {`
- `use` `codex-rs/core/src/models_manager/model_presets.rs:369` `use super::*;`
- `fn` `codex-rs/core/src/models_manager/model_presets.rs:372` `fn only_one_default_model_is_configured() {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::auth::AuthMode;`
- `use codex_protocol::openai_models::ModelPreset;`
- `use codex_protocol::openai_models::ModelUpgrade;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use codex_protocol::openai_models::default_input_modalities;`
- `use indoc::indoc;`
- `use once_cell::sync::Lazy;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
