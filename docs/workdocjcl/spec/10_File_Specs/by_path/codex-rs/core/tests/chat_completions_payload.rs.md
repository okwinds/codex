# `codex-rs/core/tests/chat_completions_payload.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `10036`
- sha256: `9d261ed94eb6f78dc50170ec1f2eb2c14ea6d2600627b770d883243491e867b4`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/chat_completions_payload.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::sync::Arc;`
- `use codex_app_server_protocol::AuthMode;`
- `use codex_core::ContentItem;`
- `use codex_core::LocalShellAction;`
- `use codex_core::LocalShellExecAction;`
- `use codex_core::LocalShellStatus;`
- `use codex_core::ModelClient;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::Prompt;`
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
- `use futures::StreamExt;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
