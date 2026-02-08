# `codex-rs/core/src/models_manager/collaboration_mode_presets.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2252`
- sha256: `444baecdbc1e757c07cc66661744feea5f37a22a6383b7358661e158b997cd93`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:3` `use codex_protocol::openai_models::ReasoningEffort;`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:5` `const COLLABORATION_MODE_PLAN: &str = include_str!("../../templates/collaboration_mode/plan.md");`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:6` `const COLLABORATION_MODE_CODE: &str = include_str!("../../templates/collaboration_mode/code.md");`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:7` `const COLLABORATION_MODE_PAIR_PROGRAMMING: &str =`
- `const` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:9` `const COLLABORATION_MODE_EXECUTE: &str =`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:22` `pub fn test_builtin_collaboration_mode_presets() -> Vec<CollaborationModeMask> {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:26` `fn plan_preset() -> CollaborationModeMask {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:36` `fn code_preset() -> CollaborationModeMask {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:46` `fn pair_programming_preset() -> CollaborationModeMask {`
- `fn` `codex-rs/core/src/models_manager/collaboration_mode_presets.rs:56` `fn execute_preset() -> CollaborationModeMask {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_protocol::config_types::CollaborationModeMask;`
- `use codex_protocol::config_types::ModeKind;`
- `use codex_protocol::openai_models::ReasoningEffort;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
