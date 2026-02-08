# `codex-rs/app-server-protocol/tests/schema_fixtures.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `3533`
- sha256: `a9baa0bc6206c3b6e383d81c7b5028d84f934d8e5ad8fb5159ea81fbe85adc01`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/app-server-protocol/tests/schema_fixtures.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use anyhow::Context;`
- `use anyhow::Result;`
- `use codex_app_server_protocol::read_schema_fixture_tree;`
- `use codex_app_server_protocol::write_schema_fixtures;`
- `use similar::TextDiff;`
- `use std::path::Path;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
