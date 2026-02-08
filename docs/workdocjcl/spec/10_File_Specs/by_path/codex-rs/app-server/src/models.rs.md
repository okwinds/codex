# `codex-rs/app-server/src/models.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `1579`
- sha256: `05622e252ae67c233c9f9f97457f69f797c7a7975361790d046c14e120dae00c`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/src/models.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/app-server/src/models.rs:1` `use std::sync::Arc;`
- `use` `codex-rs/app-server/src/models.rs:3` `use codex_app_server_protocol::Model;`
- `use` `codex-rs/app-server/src/models.rs:4` `use codex_app_server_protocol::ReasoningEffortOption;`
- `use` `codex-rs/app-server/src/models.rs:5` `use codex_core::ThreadManager;`
- `use` `codex-rs/app-server/src/models.rs:6` `use codex_core::config::Config;`
- `use` `codex-rs/app-server/src/models.rs:7` `use codex_core::models_manager::manager::RefreshStrategy;`
- `use` `codex-rs/app-server/src/models.rs:8` `use codex_protocol::openai_models::ModelPreset;`
- `use` `codex-rs/app-server/src/models.rs:9` `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `fn` `codex-rs/app-server/src/models.rs:11` `pub async fn supported_models(thread_manager: Arc<ThreadManager>, config: &Config) -> Vec<Model> {`
- `fn` `codex-rs/app-server/src/models.rs:21` `fn model_from_preset(preset: ModelPreset) -> Model {`
- `fn` `codex-rs/app-server/src/models.rs:37` `fn reasoning_efforts_from_preset(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use codex_app_server_protocol::Model;`
- `use codex_app_server_protocol::ReasoningEffortOption;`
- `use codex_core::ThreadManager;`
- `use codex_core::config::Config;`
- `use codex_core::models_manager::manager::RefreshStrategy;`
- `use codex_protocol::openai_models::ModelPreset;`
- `use codex_protocol::openai_models::ReasoningEffortPreset;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (no obvious error-handling patterns detected by heuristic)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
