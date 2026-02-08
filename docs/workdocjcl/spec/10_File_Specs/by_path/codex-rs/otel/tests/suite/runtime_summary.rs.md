# `codex-rs/otel/tests/suite/runtime_summary.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3006`
- sha256: `51e939e07ea8faa778cc0b0f6a7860d655ea2faedce2a5677796d48b93a26b9a`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/otel/tests/suite/runtime_summary.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_app_server_protocol::AuthMode;`
- `use codex_otel::OtelManager;`
- `use codex_otel::RuntimeMetricTotals;`
- `use codex_otel::RuntimeMetricsSummary;`
- `use codex_otel::metrics::MetricsClient;`
- `use codex_otel::metrics::MetricsConfig;`
- `use codex_otel::metrics::Result;`
- `use codex_protocol::ThreadId;`
- `use codex_protocol::protocol::SessionSource;`
- `use eventsource_stream::Event as StreamEvent;`
- `use opentelemetry_sdk::metrics::InMemoryMetricExporter;`
- `use pretty_assertions::assert_eq;`
- `use std::time::Duration;`
- `use tokio_tungstenite::tungstenite::Message;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
