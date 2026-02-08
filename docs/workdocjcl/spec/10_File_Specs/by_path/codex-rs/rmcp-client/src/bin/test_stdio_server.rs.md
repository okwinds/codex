# `codex-rs/rmcp-client/src/bin/test_stdio_server.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `16516`
- sha256: `725d8a4eef900aa3a4da252806f8abbcff0961e1022596df1edc5ed934d514a1`
- generated_utc: `2026-02-08T10:45:38Z`

## Purpose (Why)
Source file implementing exported/public items listed below.

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/bin/test_stdio_server.rs` (read)
- env: `MCP_TEST_IMAGE_DATA_URL`

### Outputs / Side Effects
- writes to stdout/stderr

## Public Surface (auto)
- `pub fn stdio() -> (tokio::io::Stdin, tokio::io::Stdout) {`

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:1` `use std::borrow::Cow;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:2` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:3` `use std::sync::Arc;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:5` `use rmcp::ErrorData as McpError;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:6` `use rmcp::ServiceExt;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:7` `use rmcp::handler::server::ServerHandler;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:8` `use rmcp::model::CallToolRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:9` `use rmcp::model::CallToolResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:10` `use rmcp::model::JsonObject;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:11` `use rmcp::model::ListResourceTemplatesResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:12` `use rmcp::model::ListResourcesResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:13` `use rmcp::model::ListToolsResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:14` `use rmcp::model::PaginatedRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:15` `use rmcp::model::RawResource;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:16` `use rmcp::model::RawResourceTemplate;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:17` `use rmcp::model::ReadResourceRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:18` `use rmcp::model::ReadResourceResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:19` `use rmcp::model::Resource;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:20` `use rmcp::model::ResourceContents;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:21` `use rmcp::model::ResourceTemplate;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:22` `use rmcp::model::ServerCapabilities;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:23` `use rmcp::model::ServerInfo;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:24` `use rmcp::model::Tool;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:25` `use serde::Deserialize;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:26` `use serde_json::json;`
- `use` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:27` `use tokio::task;`
- `struct` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:30` `struct TestToolServer {`
- `const` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:36` `const MEMO_URI: &str = "memo://codex/example-note";`
- `const` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:37` `const MEMO_CONTENT: &str = "This is a sample MCP resource served by the rmcp test server.";`
- `const` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:38` `const SMALL_PNG_BASE64: &str = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGP4z8DwHwAFAAH/iZk9HQAAAABJRU5ErkJggg==";`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:40` `pub fn stdio() -> (tokio::io::Stdin, tokio::io::Stdout) {`
- `impl` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:44` `impl TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:45` `fn new() -> Self {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:60` `fn echo_tool() -> Tool {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:80` `fn image_tool() -> Tool {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:114` `fn image_scenario_tool() -> Tool {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:151` `fn memo_resource() -> Resource {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:165` `fn memo_template() -> ResourceTemplate {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:178` `fn memo_text() -> &'static str {`
- `struct` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:184` `struct EchoArgs {`
- `enum` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:197` `enum ImageScenario {`
- `struct` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:208` `struct ImageScenarioArgs {`
- `impl` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:216` `impl ServerHandler for TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:217` `fn get_info(&self) -> ServerInfo {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:228` `fn list_tools(`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:243` `fn list_resources(`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:258` `async fn list_resource_templates(`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:270` `async fn read_resource(`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:292` `async fn call_tool(`
- `impl` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:358` `impl TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:375` `fn image_scenario_result(args: ImageScenarioArgs) -> Result<CallToolResult, McpError> {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:434` `fn parse_data_url(url: &str) -> Option<(String, String)> {`
- `fn` `codex-rs/rmcp-client/src/bin/test_stdio_server.rs:442` `async fn main() -> Result<(), Box<dyn std::error::Error>> {`

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
- `use rmcp::model::ListResourceTemplatesResult;`
- `use rmcp::model::ListResourcesResult;`
- `use rmcp::model::ListToolsResult;`
- `use rmcp::model::PaginatedRequestParam;`
- `use rmcp::model::RawResource;`
- `use rmcp::model::RawResourceTemplate;`
- `use rmcp::model::ReadResourceRequestParam;`
- `use rmcp::model::ReadResourceResult;`
- `use rmcp::model::Resource;`
- `use rmcp::model::ResourceContents;`
- `use rmcp::model::ResourceTemplate;`
### Referenced env vars
- `MCP_TEST_IMAGE_DATA_URL`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
