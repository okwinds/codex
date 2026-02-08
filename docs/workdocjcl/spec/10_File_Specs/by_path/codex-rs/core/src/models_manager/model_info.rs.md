# `codex-rs/core/src/models_manager/model_info.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `17631`
- sha256: `27a84312f920d794b29732cade0a26e73a1a28b32a28599952d1014a6e28c603`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/models_manager/model_info.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/models_manager/model_info.rs:1` `use codex_protocol::config_types::Verbosity;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:2` `use codex_protocol::openai_models::ApplyPatchToolType;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:3` `use codex_protocol::openai_models::ConfigShellToolType;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:4` `use codex_protocol::openai_models::ModelInfo;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:5` `use codex_protocol::openai_models::ModelInstructionsVariables;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:6` `use codex_protocol::openai_models::ModelMessages;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:7` `use codex_protocol::openai_models::ModelVisibility;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:8` `use codex_protocol::openai_models::ReasoningEffort;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:9` `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:10` `use codex_protocol::openai_models::TruncationMode;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:11` `use codex_protocol::openai_models::TruncationPolicyConfig;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:12` `use codex_protocol::openai_models::default_input_modalities;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:14` `use crate::config::Config;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:15` `use crate::features::Feature;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:16` `use crate::truncate::approx_bytes_for_tokens;`
- `use` `codex-rs/core/src/models_manager/model_info.rs:17` `use tracing::warn;`
- `const` `codex-rs/core/src/models_manager/model_info.rs:19` `pub const BASE_INSTRUCTIONS: &str = include_str!("../../prompt.md");`
- `const` `codex-rs/core/src/models_manager/model_info.rs:20` `const BASE_INSTRUCTIONS_WITH_APPLY_PATCH: &str =`
- `const` `codex-rs/core/src/models_manager/model_info.rs:23` `const GPT_5_CODEX_INSTRUCTIONS: &str = include_str!("../../gpt_5_codex_prompt.md");`
- `const` `codex-rs/core/src/models_manager/model_info.rs:24` `const GPT_5_1_INSTRUCTIONS: &str = include_str!("../../gpt_5_1_prompt.md");`
- `const` `codex-rs/core/src/models_manager/model_info.rs:25` `const GPT_5_2_INSTRUCTIONS: &str = include_str!("../../gpt_5_2_prompt.md");`
- `const` `codex-rs/core/src/models_manager/model_info.rs:26` `const GPT_5_1_CODEX_MAX_INSTRUCTIONS: &str = include_str!("../../gpt-5.1-codex-max_prompt.md");`
- `const` `codex-rs/core/src/models_manager/model_info.rs:28` `const GPT_5_2_CODEX_INSTRUCTIONS: &str = include_str!("../../gpt-5.2-codex_prompt.md");`
- `const` `codex-rs/core/src/models_manager/model_info.rs:29` `const GPT_5_2_CODEX_INSTRUCTIONS_TEMPLATE: &str =`
- `const` `codex-rs/core/src/models_manager/model_info.rs:32` `const GPT_5_2_CODEX_PERSONALITY_FRIENDLY: &str =`
- `const` `codex-rs/core/src/models_manager/model_info.rs:34` `const GPT_5_2_CODEX_PERSONALITY_PRAGMATIC: &str =`
- `fn` `codex-rs/core/src/models_manager/model_info.rs:326` `fn supported_reasoning_level_low_medium_high() -> Vec<ReasoningEffortPreset> {`
- `fn` `codex-rs/core/src/models_manager/model_info.rs:343` `fn supported_reasoning_level_low_medium_high_non_codex() -> Vec<ReasoningEffortPreset> {`
- `fn` `codex-rs/core/src/models_manager/model_info.rs:360` `fn supported_reasoning_level_low_medium_high_xhigh() -> Vec<ReasoningEffortPreset> {`
- `fn` `codex-rs/core/src/models_manager/model_info.rs:381` `fn supported_reasoning_level_low_medium_high_xhigh_non_codex() -> Vec<ReasoningEffortPreset> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::config_types::Verbosity;`
- `use codex_protocol::openai_models::ApplyPatchToolType;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelInstructionsVariables;`
- `use codex_protocol::openai_models::ModelMessages;`
- `use codex_protocol::openai_models::ModelVisibility;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use codex_protocol::openai_models::TruncationMode;`
- `use codex_protocol::openai_models::TruncationPolicyConfig;`
- `use codex_protocol::openai_models::default_input_modalities;`
- `use crate::config::Config;`
- `use crate::features::Feature;`
- `use crate::truncate::approx_bytes_for_tokens;`
- `use tracing::warn;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
