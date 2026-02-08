# `codex-rs/common/src/oss.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3304`
- sha256: `118239c17571c3ac438410cd6dff4723b1161af98dc9e0a3c37d588c21f27692`
- generated_utc: `2026-02-03T16:08:29Z`

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
- `use` `codex-rs/common/src/oss.rs:4` `use codex_core::OLLAMA_CHAT_PROVIDER_ID;`
- `use` `codex-rs/common/src/oss.rs:5` `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use` `codex-rs/common/src/oss.rs:6` `use codex_core::WireApi;`
- `use` `codex-rs/common/src/oss.rs:7` `use codex_core::config::Config;`
- `use` `codex-rs/common/src/oss.rs:8` `use codex_core::protocol::DeprecationNoticeEvent;`
- `use` `codex-rs/common/src/oss.rs:9` `use std::io;`
- `fn` `codex-rs/common/src/oss.rs:12` `pub fn get_default_model_for_oss_provider(provider_id: &str) -> Option<&'static str> {`
- `fn` `codex-rs/common/src/oss.rs:21` `pub async fn ollama_chat_deprecation_notice(`
- `fn` `codex-rs/common/src/oss.rs:51` `pub async fn ensure_oss_provider_ready(`
- `use` `codex-rs/common/src/oss.rs:75` `use super::*;`
- `fn` `codex-rs/common/src/oss.rs:78` `fn test_get_default_model_for_provider_lmstudio() {`
- `fn` `codex-rs/common/src/oss.rs:84` `fn test_get_default_model_for_provider_ollama() {`
- `fn` `codex-rs/common/src/oss.rs:90` `fn test_get_default_model_for_provider_unknown() {`

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::LMSTUDIO_OSS_PROVIDER_ID;`
- `use codex_core::OLLAMA_CHAT_PROVIDER_ID;`
- `use codex_core::OLLAMA_OSS_PROVIDER_ID;`
- `use codex_core::WireApi;`
- `use codex_core::config::Config;`
- `use codex_core::protocol::DeprecationNoticeEvent;`
- `use std::io;`
- `use super::*;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
