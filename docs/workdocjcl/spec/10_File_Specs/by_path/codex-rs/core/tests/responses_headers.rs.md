# `codex-rs/core/tests/responses_headers.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `19273`
- sha256: `a71f91caadffca75a257244d016c1e3d0b1a046f69a73dbfd8d571c96e03eab8`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/responses_headers.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::process::Command;`
- `use std::sync::Arc;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_core::AuthManager;`
- `use codex_core::CodexAuth;`
- `use codex_core::ContentItem;`
- `use codex_core::ModelClient;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::Prompt;`
- `use codex_core::ResponseEvent;`
- `use codex_core::ResponseItem;`
- `use codex_core::TransportManager;`
- `use codex_core::WEB_SEARCH_ELIGIBLE_HEADER;`
- `use codex_core::WireApi;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_otel::OtelManager;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::config_types::WebSearchMode;`
- `use codex_protocol::protocol::SessionSource;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
