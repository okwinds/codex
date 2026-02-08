# `codex-rs/core/tests/suite/client_websockets.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `10254`
- sha256: `f2201f284acac4b82c70f04f250e7d7b101bb81d494321a1194d2aa75bec3919`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/tests/suite/client_websockets.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::AuthManager;`
- `use codex_core::CodexAuth;`
- `use codex_core::ContentItem;`
- `use codex_core::ModelClient;`
- `use codex_core::ModelClientSession;`
- `use codex_core::ModelProviderInfo;`
- `use codex_core::Prompt;`
- `use codex_core::ResponseEvent;`
- `use codex_core::ResponseItem;`
- `use codex_core::TransportManager;`
- `use codex_core::WireApi;`
- `use codex_core::features::Feature;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_core::protocol::SessionSource;`
- `use codex_otel::OtelManager;`
- `use codex_otel::metrics::MetricsClient;`
- `use codex_otel::metrics::MetricsConfig;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::config_types::ReasoningSummary;`
- `use core_test_support::load_default_config_for_test;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/00_Overview/ARCHITECTURE.md`
