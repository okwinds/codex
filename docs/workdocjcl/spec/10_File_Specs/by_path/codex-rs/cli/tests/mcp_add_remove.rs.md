# `codex-rs/cli/tests/mcp_add_remove.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `6571`
- sha256: `2276f582e5d96a7588615638d241b116a860bffe148667571157e762000657f7`
- generated_utc: `2026-02-03T16:08:28Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/cli/tests/mcp_add_remove.rs` (read)

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
- `use codex_core::config::load_global_mcp_servers;`
- `use codex_core::config::types::McpServerTransportConfig;`
- `use predicates::str::contains;`
- `use pretty_assertions::assert_eq;`
- `use tempfile::TempDir;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- `workdocjcl/spec/03_API/CLI.md`
