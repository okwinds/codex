# `codex-rs/core/tests/suite/client_websockets.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `25663`
- sha256: `5b65797cb4bbeb6e9394372b9642c8ad4e806f0e395ba789e480d545b10d1a08`
- generated_utc: `2026-02-08T10:45:35Z`

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
- `use codex_core::WireApi;`
- `use codex_core::X_RESPONSESAPI_INCLUDE_TIMING_METRICS_HEADER;`
- `use codex_core::features::Feature;`
- `use codex_core::models_manager::manager::ModelsManager;`
- `use codex_core::protocol::SessionSource;`
- `use codex_otel::OtelManager;`
- `use codex_otel::TelemetryAuthMode;`
- `use codex_otel::metrics::MetricsClient;`
- `use codex_otel::metrics::MetricsConfig;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::account::PlanType;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
