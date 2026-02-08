# `codex-rs/core/src/models_manager/collaboration_mode_presets.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4004`
- sha256: `0646f8acb83b296c01bcce5f1f806f625d1b7d880f2f228e474a1aea10cad4c0`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/models_manager/collaboration_mode_presets.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn test_builtin_collaboration_mode_presets() -> Vec<CollaborationModeMask> {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:1` `use codex_protocol::config_types::CollaborationModeMask;`
- `use` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:2` `use codex_protocol::config_types::ModeKind;`
- `use` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:3` `use codex_protocol::config_types::TUI_VISIBLE_COLLABORATION_MODES;`
- `use` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:4` `use codex_protocol::openai_models::ReasoningEffort;`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:6` `const COLLABORATION_MODE_PLAN: &str = include_str!("../../templates/collaboration_mode/plan.md");`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:7` `const COLLABORATION_MODE_DEFAULT: &str =`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:9` `const KNOWN_MODE_NAMES_PLACEHOLDER: &str = "{{KNOWN_MODE_NAMES}}";`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:10` `const REQUEST_USER_INPUT_AVAILABILITY_PLACEHOLDER: &str = "{{REQUEST_USER_INPUT_AVAILABILITY}}";`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:17` `pub fn test_builtin_collaboration_mode_presets() -> Vec<CollaborationModeMask> {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:21` `fn plan_preset() -> CollaborationModeMask {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:31` `fn default_preset() -> CollaborationModeMask {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:41` `fn default_mode_instructions() -> String {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:53` `fn format_mode_names(modes: &[ModeKind]) -> String {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:63` `fn request_user_input_availability_message(mode: ModeKind) -> String {`
- `use` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:76` `use super::*;`
- `use` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:77` `use pretty_assertions::assert_eq;`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:80` `fn preset_names_use_mode_display_names() {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:86` `fn default_mode_instructions_replace_mode_names_placeholder() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::config_types::CollaborationModeMask;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::config_types::TUI_VISIBLE_COLLABORATION_MODES;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use super::*;`
- `use pretty_assertions::assert_eq;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
