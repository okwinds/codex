# `codex-rs/core/tests/chat_completions_sse.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `14837`
- sha256: `959dd78a6c6c849eb7a5c97ae89a1bc38a0419fc61501bd48eb4be2d97f07c04`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/chat_completions_sse.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use assert_matches::assert_matches;`
- `use codex_core::AuthManager;`
- `use std::sync::Arc;`
- `use tracing_test::traced_test;`
- `use codex_core::CodexAuth;`
- `use codex_core::ContentItem;`
- `use codex_core::ModelClient;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::Prompt;`
- `use codex_core::ResponseEvent;`
- `use codex_core::ResponseItem;`
- `use codex_core::TransportManager;`
- `use codex_core::WireApi;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::models::ReasoningItemContent;`
- `use codex_protocol::protocol::SessionSource;`
- `use core_test_support::load_default_config_for_test;`
- `use core_test_support::skip_if_no_network;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
