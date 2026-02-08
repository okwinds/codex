# `codex-rs/rmcp-client/tests/resources.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `4333`
- sha256: `c8705376c877ea1fa7b66050a3da46ee48afe30c0ae2ae86cb303f9009ea31e4`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/tests/resources.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use std::ffi::OsString;`
- `use std::path::PathBuf;`
- `use std::time::Duration;`
- `use codex_rmcp_client::ElicitationAction;`
- `use codex_rmcp_client::ElicitationResponse;`
- `use codex_rmcp_client::RmcpClient;`
- `use codex_utils_cargo_bin::CargoBinError;`
- `use futures::FutureExt as _;`
- `use rmcp::model::AnnotateAble;`
- `use rmcp::model::ClientCapabilities;`
- `use rmcp::model::ElicitationCapability;`
- `use rmcp::model::Implementation;`
- `use rmcp::model::InitializeRequestParam;`
- `use rmcp::model::ListResourceTemplatesResult;`
- `use rmcp::model::ProtocolVersion;`
- `use rmcp::model::ReadResourceRequestParam;`
- `use rmcp::model::ResourceContents;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
