# `codex-rs/exec-server/tests/common/lib.rs`

## Identity
- kind: `test`
- ext: `.rs`
- size_bytes: `5922`
- sha256: `dce4f2f920846c024b6f89d7e00ee6198bc80e95fa73f112f72c6ca673f1ca27`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Test or snapshot file used for automated verification.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/tests/common/lib.rs` (read)

### Outputs / Side Effects
- none (file is declarative: doc/config/test/asset)

## Public Surface (auto)
- `pub struct InteractiveClient {`

## Definitions (auto, per-file)
- (not extracted)

## Dependencies (auto sample)
### Imports / Includes
- `use codex_core::MCP_SANDBOX_STATE_METHOD;`
- `use codex_core::SandboxState;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_utils_cargo_bin::find_resource;`
- `use rmcp::ClientHandler;`
- `use rmcp::ErrorData as McpError;`
- `use rmcp::RoleClient;`
- `use rmcp::Service;`
- `use rmcp::model::ClientCapabilities;`
- `use rmcp::model::ClientInfo;`
- `use rmcp::model::ClientRequest;`
- `use rmcp::model::CreateElicitationRequestParam;`
- `use rmcp::model::CreateElicitationResult;`
- `use rmcp::model::CustomRequest;`
- `use rmcp::model::ElicitationAction;`
- `use rmcp::model::ServerResult;`
- `use rmcp::service::RunningService;`
- `use rmcp::transport::ConfigureCommandExt;`
- `use rmcp::transport::TokioChildProcess;`
- `use serde_json::json;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- (none detected)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
