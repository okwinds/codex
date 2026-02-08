# `codex-rs/exec-server/src/posix/mcp.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `9210`
- sha256: `bf50ea0efea5fc0500e2f7bae88235f858a5fc0de1269984d3ff9685264c1353`
- generated_utc: `2026-02-08T10:45:36Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/exec-server/src/posix/mcp.rs` (read)

### Outputs / Side Effects
- spawns subprocesses

## Public Surface (auto)
- `pub struct ExecParams {`
- `pub struct ExecResult {`
- `pub struct ExecTool {`
- `pub fn new(`
- `pub struct CodexSandboxStateUpdateMethod;`

## Definitions (auto, per-file)
- `use` `codex-rs/exec-server/src/posix/mcp.rs:1` `use std::path::PathBuf;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:2` `use std::sync::Arc;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:3` `use std::time::Duration;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:5` `use anyhow::Context as _;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:6` `use anyhow::Result;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:7` `use codex_core::MCP_SANDBOX_STATE_CAPABILITY;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:8` `use codex_core::MCP_SANDBOX_STATE_METHOD;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:9` `use codex_core::SandboxState;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:10` `use codex_core::protocol::SandboxPolicy;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:11` `use codex_execpolicy::Policy;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:12` `use rmcp::ErrorData as McpError;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:13` `use rmcp::RoleServer;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:14` `use rmcp::ServerHandler;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:15` `use rmcp::ServiceExt;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:16` `use rmcp::handler::server::router::tool::ToolRouter;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:17` `use rmcp::handler::server::wrapper::Parameters;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:18` `use rmcp::model::CustomRequest;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:19` `use rmcp::model::CustomResult;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:20` `use rmcp::model::*;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:21` `use rmcp::schemars;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:22` `use rmcp::service::RequestContext;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:23` `use rmcp::service::RunningService;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:24` `use rmcp::tool;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:25` `use rmcp::tool_handler;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:26` `use rmcp::tool_router;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:27` `use rmcp::transport::stdio;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:28` `use serde_json::json;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:29` `use tokio::sync::RwLock;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:31` `use crate::posix::escalate_server::EscalateServer;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:32` `use crate::posix::escalate_server::{self};`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:33` `use crate::posix::mcp_escalation_policy::McpEscalationPolicy;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:34` `use crate::posix::stopwatch::Stopwatch;`
- `const` `codex-rs/exec-server/src/posix/mcp.rs:37` `const CODEX_BASH_PATH_ENV_VAR: &str = "CODEX_BASH_PATH";`
- `const` `codex-rs/exec-server/src/posix/mcp.rs:39` `const SANDBOX_STATE_CAPABILITY_VERSION: &str = "1.0.0";`
- `struct` `codex-rs/exec-server/src/posix/mcp.rs:48` `pub struct ExecParams {`
- `struct` `codex-rs/exec-server/src/posix/mcp.rs:60` `pub struct ExecResult {`
- `impl` `codex-rs/exec-server/src/posix/mcp.rs:67` `impl From<escalate_server::ExecResult> for ExecResult {`
- `fn` `codex-rs/exec-server/src/posix/mcp.rs:68` `fn from(result: escalate_server::ExecResult) -> Self {`
- `struct` `codex-rs/exec-server/src/posix/mcp.rs:79` `pub struct ExecTool {`
- `impl` `codex-rs/exec-server/src/posix/mcp.rs:89` `impl ExecTool {`
- `fn` `codex-rs/exec-server/src/posix/mcp.rs:90` `pub fn new(`
- `fn` `codex-rs/exec-server/src/posix/mcp.rs:108` `async fn shell(`
- `struct` `codex-rs/exec-server/src/posix/mcp.rs:153` `pub struct CodexSandboxStateUpdateMethod;`
- `impl` `codex-rs/exec-server/src/posix/mcp.rs:155` `impl rmcp::model::ConstString for CodexSandboxStateUpdateMethod {`
- `const` `codex-rs/exec-server/src/posix/mcp.rs:156` `const VALUE: &'static str = MCP_SANDBOX_STATE_METHOD;`
- `impl` `codex-rs/exec-server/src/posix/mcp.rs:160` `impl ServerHandler for ExecTool {`
- `fn` `codex-rs/exec-server/src/posix/mcp.rs:161` `fn get_info(&self) -> ServerInfo {`
- `fn` `codex-rs/exec-server/src/posix/mcp.rs:186` `async fn initialize(`
- `fn` `codex-rs/exec-server/src/posix/mcp.rs:194` `async fn on_custom_request(`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:236` `use super::*;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:237` `use pretty_assertions::assert_eq;`
- `use` `codex-rs/exec-server/src/posix/mcp.rs:238` `use serde_json::json;`
- `fn` `codex-rs/exec-server/src/posix/mcp.rs:244` `fn exec_params_json_schema_matches_expected() {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::path::PathBuf;`
- `use std::sync::Arc;`
- `use std::time::Duration;`
- `use anyhow::Context as _;`
- `use anyhow::Result;`
- `use codex_core::MCP_SANDBOX_STATE_CAPABILITY;`
- `use codex_core::MCP_SANDBOX_STATE_METHOD;`
- `use codex_core::SandboxState;`
- `use codex_core::protocol::SandboxPolicy;`
- `use codex_execpolicy::Policy;`
- `use rmcp::ErrorData as McpError;`
- `use rmcp::RoleServer;`
- `use rmcp::ServerHandler;`
- `use rmcp::ServiceExt;`
- `use rmcp::handler::server::router::tool::ToolRouter;`
- `use rmcp::handler::server::wrapper::Parameters;`
- `use rmcp::model::CustomRequest;`
- `use rmcp::model::CustomResult;`
- `use rmcp::model::*;`
- `use rmcp::schemars;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- has retry/timeout/backoff logic
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
