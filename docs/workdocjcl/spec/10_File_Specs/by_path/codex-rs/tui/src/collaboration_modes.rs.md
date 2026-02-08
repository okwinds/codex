# `codex-rs/tui/src/collaboration_modes.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2061`
- sha256: `11fff90650dc2fa756f76225c6b859f1f436f8a4ffc8563f5c4f436675155ee3`
- generated_utc: `2026-02-03T16:08:30Z`

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
- `fn` `codex-rs/tui/src/collaboration_modes.rs:5` `fn is_tui_mode(kind: ModeKind) -> bool {`
- `fn` `codex-rs/tui/src/collaboration_modes.rs:9` `fn filtered_presets(models_manager: &ModelsManager) -> Vec<CollaborationModeMask> {`

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
- `workdocjcl/spec/06_UI/TUI.md`
