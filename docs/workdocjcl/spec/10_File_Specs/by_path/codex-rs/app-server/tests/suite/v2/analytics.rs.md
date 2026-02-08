# `codex-rs/app-server/tests/suite/v2/analytics.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2084`
- sha256: `85a372b9aed85ae2cd039fa13260206247ef4912003b1fd97f2a6dcf2c841b2e`
- generated_utc: `2026-02-08T10:45:15Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server/tests/suite/v2/analytics.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Result;`
- `use codex_core::config::ConfigBuilder;`
- `use codex_core::config::types::OtelExporterKind;`
- `use codex_core::config::types::OtelHttpProtocol;`
- `use pretty_assertions::assert_eq;`
- `use std::collections::HashMap;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
