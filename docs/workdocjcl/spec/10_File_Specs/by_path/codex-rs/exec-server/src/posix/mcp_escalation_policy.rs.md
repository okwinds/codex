# `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `5191`
- sha256: `5047d77a14897479f26ee715418757bd7a334a036224b72f25ef0c823616b4bb`
- generated_utc: `2026-02-03T16:08:29Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:1` `use std::path::Path;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:3` `use codex_core::sandboxing::SandboxPermissions;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:4` `use codex_execpolicy::Policy;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:5` `use rmcp::ErrorData as McpError;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:6` `use rmcp::RoleServer;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:7` `use rmcp::model::CreateElicitationRequestParam;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:8` `use rmcp::model::CreateElicitationResult;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:9` `use rmcp::model::ElicitationAction;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:10` `use rmcp::model::ElicitationSchema;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:11` `use rmcp::service::RequestContext;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:13` `use crate::posix::escalate_protocol::EscalateAction;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:14` `use crate::posix::escalation_policy::EscalationPolicy;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:15` `use crate::posix::stopwatch::Stopwatch;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:16` `use std::sync::Arc;`
- `use` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:17` `use tokio::sync::RwLock;`
- `impl` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:40` `impl McpEscalationPolicy {`
- `fn` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:55` `async fn prompt(`
- `impl` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:100` `impl EscalationPolicy for McpEscalationPolicy {`
- `fn` `codex-rs/exec-server/src/posix/mcp_escalation_policy.rs:101` `async fn determine_action(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::Path;`
- `use codex_core::sandboxing::SandboxPermissions;`
- `use codex_execpolicy::Policy;`
- `use rmcp::ErrorData as McpError;`
- `use rmcp::RoleServer;`
- `use rmcp::model::CreateElicitationRequestParam;`
- `use rmcp::model::CreateElicitationResult;`
- `use rmcp::model::ElicitationAction;`
- `use rmcp::model::ElicitationSchema;`
- `use rmcp::service::RequestContext;`
- `use crate::posix::escalate_protocol::EscalateAction;`
- `use crate::posix::escalation_policy::EscalationPolicy;`
- `use crate::posix::stopwatch::Stopwatch;`
- `use std::sync::Arc;`
- `use tokio::sync::RwLock;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
