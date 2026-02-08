# `codex-rs/mcp-server/tests/common/mcp_process.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `12796`
- sha256: `dbc45694d12aa29413a291f7e13d6218fc595a447ec17a70b0e456a43348420b`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/mcp-server/tests/common/mcp_process.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct McpProcess {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use std::process::Stdio;`
- `use std::sync::atomic::AtomicI64;`
- `use std::sync::atomic::Ordering;`
- `use tokio::io::AsyncBufReadExt;`
- `use tokio::io::AsyncWriteExt;`
- `use tokio::io::BufReader;`
- `use tokio::process::Child;`
- `use tokio::process::ChildStdin;`
- `use tokio::process::ChildStdout;`
- `use anyhow::Context;`
- `use codex_mcp_server::CodexToolCallParam;`
- `use pretty_assertions::assert_eq;`
- `use rmcp::model::CallToolRequestParam;`
- `use rmcp::model::ClientCapabilities;`
- `use rmcp::model::CustomNotification;`
- `use rmcp::model::CustomRequest;`
- `use rmcp::model::ElicitationCapability;`
- `use rmcp::model::Implementation;`
- `use rmcp::model::InitializeRequestParam;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
