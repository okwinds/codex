# `codex-rs/exec-server/tests/suite/list_tools.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `2791`
- sha256: `895a3c7abe33fce93bae653029f105cc504f29e63824f69e852320b233ea9ef0`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/tests/suite/list_tools.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::borrow::Cow;`
- `use std::fs;`
- `use std::sync::Arc;`
- `use anyhow::Result;`
- `use exec_server_test_support::create_transport;`
- `use pretty_assertions::assert_eq;`
- `use rmcp::ServiceExt;`
- `use rmcp::model::Tool;`
- `use rmcp::model::object;`
- `use serde_json::json;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
