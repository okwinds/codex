# `codex-rs/cli/tests/mcp_list.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5404`
- sha256: `0c88f56a7e5d0ca7a29b5cebbd4b5ed5225422a90905e251476395b0d087724b`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/tests/mcp_list.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use anyhow::Result;`
- `use codex_core::config::edit::ConfigEditsBuilder;`
- `use codex_core::config::load_global_mcp_servers;`
- `use codex_core::config::types::McpServerTransportConfig;`
- `use predicates::prelude::PredicateBooleanExt;`
- `use predicates::str::contains;`
- `use pretty_assertions::assert_eq;`
- `use serde_json::Value as JsonValue;`
- `use serde_json::json;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/03_API/CLI.md`
