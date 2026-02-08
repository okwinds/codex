# `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs`

## Identity
- kind: `source`
- ext: `.rs`
- size_bytes: `10853`
- sha256: `943aacb2e010929ce332e1a84917cdba53062da4a4b9879c051978feb6b271c6`
- generated_utc: `2026-02-03T16:08:30Z`

## Purpose (Why)
Source file (no public surface detected by heuristic).

## Interfaces (Inputs/Outputs)
### Inputs
- filesystem: `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs` (read)
- env: `BIND_ADDR`, `MCP_EXPECT_BEARER`, `MCP_STREAMABLE_HTTP_BIND_ADDR`

### Outputs / Side Effects
- performs network I/O
- writes to stdout/stderr

## Public Surface (auto)
- (none detected)

## Definitions (auto, per-file)
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:1` `use std::borrow::Cow;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:2` `use std::collections::HashMap;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:3` `use std::io::ErrorKind;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:4` `use std::net::SocketAddr;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:5` `use std::sync::Arc;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:7` `use axum::Router;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:8` `use axum::body::Body;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:9` `use axum::extract::State;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:10` `use axum::http::Request;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:11` `use axum::http::StatusCode;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:12` `use axum::http::header::AUTHORIZATION;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:13` `use axum::http::header::CONTENT_TYPE;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:14` `use axum::middleware;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:15` `use axum::middleware::Next;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:16` `use axum::response::Response;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:17` `use axum::routing::get;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:18` `use rmcp::ErrorData as McpError;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:19` `use rmcp::handler::server::ServerHandler;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:20` `use rmcp::model::CallToolRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:21` `use rmcp::model::CallToolResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:22` `use rmcp::model::JsonObject;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:23` `use rmcp::model::ListResourceTemplatesResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:24` `use rmcp::model::ListResourcesResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:25` `use rmcp::model::ListToolsResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:26` `use rmcp::model::PaginatedRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:27` `use rmcp::model::RawResource;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:28` `use rmcp::model::RawResourceTemplate;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:29` `use rmcp::model::ReadResourceRequestParam;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:30` `use rmcp::model::ReadResourceResult;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:31` `use rmcp::model::Resource;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:32` `use rmcp::model::ResourceContents;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:33` `use rmcp::model::ResourceTemplate;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:34` `use rmcp::model::ServerCapabilities;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:35` `use rmcp::model::ServerInfo;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:36` `use rmcp::model::Tool;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:37` `use rmcp::transport::StreamableHttpServerConfig;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:38` `use rmcp::transport::StreamableHttpService;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:39` `use rmcp::transport::streamable_http_server::session::local::LocalSessionManager;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:40` `use serde::Deserialize;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:41` `use serde_json::json;`
- `use` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:42` `use tokio::task;`
- `struct` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:45` `struct TestToolServer {`
- `const` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:51` `const MEMO_URI: &str = "memo://codex/example-note";`
- `const` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:52` `const MEMO_CONTENT: &str = "This is a sample MCP resource served by the rmcp test server.";`
- `impl` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:54` `impl TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:55` `fn new() -> Self {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:66` `fn echo_tool() -> Tool {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:86` `fn memo_resource() -> Resource {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:100` `fn memo_template() -> ResourceTemplate {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:113` `fn memo_text() -> &'static str {`
- `struct` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:119` `struct EchoArgs {`
- `impl` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:125` `impl ServerHandler for TestToolServer {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:126` `fn get_info(&self) -> ServerInfo {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:137` `fn list_tools(`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:152` `fn list_resources(`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:167` `async fn list_resource_templates(`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:179` `async fn read_resource(`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:201` `async fn call_tool(`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:242` `fn parse_bind_addr() -> Result<SocketAddr, Box<dyn std::error::Error>> {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:251` `async fn main() -> Result<(), Box<dyn std::error::Error>> {`
- `fn` `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs:307` `async fn require_bearer(`

## Dependencies (auto sample)
### Imports / Includes
- `use std::borrow::Cow;`
- `use std::collections::HashMap;`
- `use std::io::ErrorKind;`
- `use std::net::SocketAddr;`
- `use std::sync::Arc;`
- `use axum::Router;`
- `use axum::body::Body;`
- `use axum::extract::State;`
- `use axum::http::Request;`
- `use axum::http::StatusCode;`
- `use axum::http::header::AUTHORIZATION;`
- `use axum::http::header::CONTENT_TYPE;`
- `use axum::middleware;`
- `use axum::middleware::Next;`
- `use axum::response::Response;`
- `use axum::routing::get;`
- `use rmcp::ErrorData as McpError;`
- `use rmcp::handler::server::ServerHandler;`
- `use rmcp::model::CallToolRequestParam;`
- `use rmcp::model::CallToolResult;`
### Referenced env vars
- `BIND_ADDR`
- `MCP_EXPECT_BEARER`
- `MCP_STREAMABLE_HTTP_BIND_ADDR`

## Error Handling / Edge Cases
- returns structured errors (Result/ErrorKind)
- uses Rust panic/expect/unwrap-style failure paths

## Spec Links
- (none; see `09_Verification/CODE_TO_SPEC_MAP.md`)
