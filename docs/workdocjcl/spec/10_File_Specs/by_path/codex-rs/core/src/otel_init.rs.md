# `codex-rs/core/src/otel_init.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `3523`
- sha256: `e5543be0a4e0a0bc2515206f226bcc5f0efad19b9458827c2ca40bda53d344b7`
- generated_utc: `2026-02-08T10:45:33Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/core/src/otel_init.rs` (read)

### Outputs / Side Effects
- (no obvious side effects detected by heuristic)

## Public Surface (auto)
- `pub fn build_provider(`
- `pub fn codex_export_filter(meta: &tracing::Metadata<'_>) -> bool {`

## Definitions (auto, per-file)
- `use` `codex-rs/core/src/otel_init.rs:1` `use crate::config::Config;`
- `use` `codex-rs/core/src/otel_init.rs:2` `use crate::config::types::OtelExporterKind as Kind;`
- `use` `codex-rs/core/src/otel_init.rs:3` `use crate::config::types::OtelHttpProtocol as Protocol;`
- `use` `codex-rs/core/src/otel_init.rs:4` `use crate::default_client::originator;`
- `use` `codex-rs/core/src/otel_init.rs:5` `use crate::features::Feature;`
- `use` `codex-rs/core/src/otel_init.rs:6` `use codex_otel::config::OtelExporter;`
- `use` `codex-rs/core/src/otel_init.rs:7` `use codex_otel::config::OtelHttpProtocol;`
- `use` `codex-rs/core/src/otel_init.rs:8` `use codex_otel::config::OtelSettings;`
- `use` `codex-rs/core/src/otel_init.rs:9` `use codex_otel::config::OtelTlsConfig as OtelTlsSettings;`
- `use` `codex-rs/core/src/otel_init.rs:10` `use codex_otel::otel_provider::OtelProvider;`
- `use` `codex-rs/core/src/otel_init.rs:11` `use std::error::Error;`
- `fn` `codex-rs/core/src/otel_init.rs:16` `pub fn build_provider(`
- `fn` `codex-rs/core/src/otel_init.rs:97` `pub fn codex_export_filter(meta: &tracing::Metadata<'_>) -> bool {`

## Dependencies (auto sample)
### Imports / Includes
- `use crate::config::Config;`
- `use crate::config::types::OtelExporterKind as Kind;`
- `use crate::config::types::OtelHttpProtocol as Protocol;`
- `use crate::default_client::originator;`
- `use crate::features::Feature;`
- `use codex_otel::config::OtelExporter;`
- `use codex_otel::config::OtelHttpProtocol;`
- `use codex_otel::config::OtelSettings;`
- `use codex_otel::config::OtelTlsConfig as OtelTlsSettings;`
- `use codex_otel::otel_provider::OtelProvider;`
- `use std::error::Error;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- `docs/workdocjcl/spec/00_Overview/ARCHITECTURE.md`
