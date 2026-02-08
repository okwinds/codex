# `codex-rs/core/tests/suite/list_models.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `19417`
- sha256: `ce40c27fa3c1ea575aa157db049ee41734be07d169067665719cbb9c7e3b9396`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/list_models.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_core::CodexAuth;`
- `use codex_core::ThreadManager;`
- `use codex_core::built_in_model_providers;`
- `use codex_core::models_manager::manager::RefreshStrategy;`
- `use codex_protocol::openai_models::ModelPreset;`
- `use codex_protocol::openai_models::ModelUpgrade;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use codex_protocol::openai_models::default_input_modalities;`
- `use core_test_support::load_default_config_for_test;`
- `use indoc::indoc;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::HashMap;`
- `use tempfile::tempdir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
