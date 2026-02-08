# `codex-rs/tui/src/collaboration_modes.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1996`
- sha256: `7727c529b03cb0be00c321d85c7c6b1c923b09f3ec3c5ca3dd6e2e641b938406`
- generated_utc: `2026-02-08T10:45:40Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/tui/src/collaboration_modes.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/tui/src/collaboration_modes.rs:1` `use codex_core::models_manager::manager::ModelsManager;`
- `use` `codex-rs/tui/src/collaboration_modes.rs:2` `use codex_protocol::config_types::CollaborationModeMask;`
- `use` `codex-rs/tui/src/collaboration_modes.rs:3` `use codex_protocol::config_types::ModeKind;`
- `fn` `codex-rs/tui/src/collaboration_modes.rs:5` `fn filtered_presets(models_manager: &ModelsManager) -> Vec<CollaborationModeMask> {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_protocol::config_types::CollaborationModeMask;`
- `use codex_protocol::config_types::ModeKind;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- `docs/workdocjcl/spec/06_UI/TUI.md`
