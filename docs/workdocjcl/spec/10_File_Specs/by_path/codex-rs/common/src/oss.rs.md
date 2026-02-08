# `codex-rs/common/src/oss.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `2019`
- sha256: `0dcbf1c3fc392568c3d877f8fe52ecaf93140cede3eababadda97d89de032c8a`
- generated_utc: `2026-02-08T10:45:25Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/common/src/oss.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn get_default_model_for_oss_provider(provider_id: &str) -> Option<&'static str> {`

## Definitions (auto, per-file)
- `use` `codex-rs/common/src/oss.rs:3` `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use` `codex-rs/common/src/oss.rs:4` `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use` `codex-rs/common/src/oss.rs:5` `use codex_core::config::Config;`
- `fn` `codex-rs/common/src/oss.rs:8` `pub fn get_default_model_for_oss_provider(provider_id: &str) -> Option<&'static str> {`
- `fn` `codex-rs/common/src/oss.rs:17` `pub async fn ensure_oss_provider_ready(`
- `use` `codex-rs/common/src/oss.rs:42` `use super::*;`
- `fn` `codex-rs/common/src/oss.rs:45` `fn test_get_default_model_for_provider_lmstudio() {`
- `fn` `codex-rs/common/src/oss.rs:51` `fn test_get_default_model_for_provider_ollama() {`
- `fn` `codex-rs/common/src/oss.rs:57` `fn test_get_default_model_for_provider_unknown() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use codex_core::config::Config;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
