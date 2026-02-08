# `codex-rs/core/tests/suite/models_cache_ttl.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `12212`
- sha256: `b97fe53002e93f68c93acb9a16918d0ecf15c38f311a89e151d2059b41d2e6da`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/models_cache_ttl.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::sync::Arc;`
- `use anyhow::Result;`
- `use chrono::DateTime;`
- `use chrono::TimeZone;`
- `use chrono::Utc;`
- `use codex_core::CodexAuth;`
- `use codex_core::features::Feature;`
- `use codex_core::models_manager::manager::RefreshStrategy;`
- `use codex_core::protocol::EventMsg;`
- `use codex_core::protocol::Op;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::openai_models::ConfigShellToolType;`
- `use codex_protocol::openai_models::ModelInfo;`
- `use codex_protocol::openai_models::ModelVisibility;`
- `use codex_protocol::openai_models::ModelsResponse;`
- `use codex_protocol::openai_models::ReasoningEffort;`
- `use codex_protocol::openai_models::ReasoningEffortPreset;`
- `use codex_protocol::openai_models::TruncationPolicyConfig;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
