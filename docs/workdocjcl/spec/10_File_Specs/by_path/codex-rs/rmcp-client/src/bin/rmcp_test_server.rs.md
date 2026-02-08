# `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `4428`
- sha256: `a5729afab26fe313d983ea1dd7cf27dd29b40fa25abef4605afd729132fd8241`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs` (read)

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn stdio() -> (tokio::io::Stdin, tokio::io::Stdout) {`

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:1` `use std::borrow::Cow;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:2` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:5` `use rmcp::ErrorData as McpError;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:6` `use rmcp::ServiceExt;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:7` `use rmcp::handler::server::ServerHandler;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:8` `use rmcp::model::CallToolRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:9` `use rmcp::model::CallToolResult;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:10` `use rmcp::model::JsonObject;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:11` `use rmcp::model::ListToolsResult;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:12` `use rmcp::model::PaginatedRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:13` `use rmcp::model::ServerCapabilities;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:14` `use rmcp::model::ServerInfo;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:15` `use rmcp::model::Tool;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:16` `use serde::Deserialize;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:17` `use serde_json::json;`
- `use` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:18` `use tokio::task;`
- `struct` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:21` `struct TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:24` `pub fn stdio() -> (tokio::io::Stdin, tokio::io::Stdout) {`
- `impl` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:27` `impl TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:28` `fn new() -> Self {`
- `fn` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:35` `fn echo_tool() -> Tool {`
- `struct` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:57` `struct EchoArgs {`
- `impl` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:63` `impl ServerHandler for TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:64` `fn get_info(&self) -> ServerInfo {`
- `fn` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:74` `fn list_tools(`
- `fn` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:89` `async fn call_tool(`
- `fn` `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs:131` `async fn main() -> Result<(), Box<dyn std::error::Error>> {`

## Dependencies (auto sample)
### Imports / Includes
- `use std::borrow::Cow;`
- `use std::collections::HashMap;`
- `use std::sync::Arc;`
- `use rmcp::ErrorData as McpError;`
- `use rmcp::ServiceExt;`
- `use rmcp::handler::server::ServerHandler;`
- `use rmcp::model::CallToolRequestParam;`
- `use rmcp::model::CallToolResult;`
- `use rmcp::model::JsonObject;`
- `use rmcp::model::ListToolsResult;`
- `use rmcp::model::PaginatedRequestParam;`
- `use rmcp::model::ServerCapabilities;`
- `use rmcp::model::ServerInfo;`
- `use rmcp::model::Tool;`
- `use serde::Deserialize;`
- `use serde_json::json;`
- `use tokio::task;`
### Referenced env vars
- (none detected)

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
