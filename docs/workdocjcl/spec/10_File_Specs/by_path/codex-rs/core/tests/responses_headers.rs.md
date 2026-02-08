# `codex-rs/core/tests/responses_headers.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `15057`
- sha256: `15bbaf7cc3cd8b45cc14119e57e37d928e8501b732f7069d743bcc38a7431137`
- generated_utc: `2026-02-08T10:45:34Z`

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
- `use codex_core::AuthManager;`
- `use codex_core::CodexAuth;`
- `use codex_core::ContentItem;`
- `use codex_core::ModelClient;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::Prompt;`
- `use codex_core::ResponseEvent;`
- `use codex_core::ResponseItem;`
- `use codex_core::WireApi;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_otel::OtelManager;`
- `use codex_otel::TelemetryAuthMode;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use codex_protocol::protocol::SessionSource;`
- `use codex_protocol::protocol::SubAgentSource;`
- `use core_test_support::load_default_config_for_test;`
- `use core_test_support::responses;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
