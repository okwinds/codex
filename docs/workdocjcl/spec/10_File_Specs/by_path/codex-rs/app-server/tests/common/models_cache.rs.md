# `codex-rs/app-server/tests/common/models_cache.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3652`
- sha256: `371ad1957650cd38ccb2d38a74d7f7ce4154c93125e9ea731dd1a87206eedae4`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/common/models_cache.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub fn write_models_cache(codex_home: &Path) -> std::io::Result<()> {`
- `pub fn write_models_cache_with_models(`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use chrono::DateTime;`
- `use chrono::Utc;`
- `use codex_core::models_manager::model_presets::all_model_presets;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelPreset;`
- `use codex_protocol::openai_models::ModelVisibility;`
- `use codex_protocol::openai_models::TruncationPolicyConfig;`
- `use codex_protocol::openai_models::default_input_modalities;`
- `use serde_json::json;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
